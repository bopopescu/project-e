#!/usr/bin/python
import zmq
import pika
from kazoo.client import KazooClient
from kazoo.client import KazooState
#Init : Protocol Handler, MQ Connection, ZK Connection
#MQ Connection
context=zmq.Context()
connect_cnt=0
socket_client=context.socket(zmq.REP)
#socket_cell=context.socket(zmq.REQ)

#RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare( queue = 'MQ' )

#temporary tcp location
socket_client.bind("tcp://127.0.0.1:5000")
#socket_cell.connect("tcp://127.0.0.1:2492")

#connection to zookeeper
zk=KazooClient(hosts='127.0.0.1:2181')
zk.start()
def my_listener(state):	
	if state==KazooState.LOST:
		zk.delete("gateways/node",recursive=True)
	#Register somewhere that the session was lost
	elif state==KazooState.SUSPENDED:
		zk.delete("/gateways/node",recursive=True)
	#Handle being disconnected from Zookeeper
	else:
		zk.ensure_path("/gateways")
		zk.create("/gateways/node", connect_cnt)
	#Handle being connected/reconnected to Zookeeper

zk.add_listener(my_listener)

#loop1 : Connection Accept, receive messages from clients -> send to MQ
#while True...?True...? I don't know. @_@

while True:
	msg=socket_client.recv()
#when client is connected to socket, send msg "connected"
	if (msg=="connected"):#connect count++
		connect_cnt=connect_cnt+1
		zk.set("/gateways/node",connect_cnt)
#when client cut connection, send msg "cut"
	elif (msg=="cut"):#connect count--
		connect_cnt=connect_cnt-1
		zk.set("/gateways/node",connect_cnt)
#when client's msg starts with 'cmove', send it to rabbitmq
	elif (str.startswith('cmove')):
		#socket_cell.send(msg)
		channel.basic_publish(exchange='',
				      routing_key = 'MQ',
				      body = msg)

#receive messages from MQ -> send to clients
#	msg_cell=socket_cell.recv()
def callback(ch, method, properties, body):
	print "Received %r" % (body, )

channel.basic_consume(callback,
		      queue = 'MQ',
		      no_ack = True)
channel.start_consuming()
#Maybe we need to filter msg_cell. But how?...
#	socket_client.send(msg_cell)

#closing RabbitMQ. But when...?
#connection.close()
