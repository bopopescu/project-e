#!/usr/bin/python

import sys
import pika
import zmq
from kazoo.client import KazooClient
from kazoo.client import KazooState

#Init : ZMQ connection, RabbitMQ connection, ZK Connection
#ZMQ connection
context = zmq.Conext()
socket_cell = context.socket(zmq.REP)
#temporary tcp location
socket_cell.bint("tcp://127.0.0.1:2492")
#temporary client arry. we will use hashtable later
client_list = array.array()

#connection to zookeeper
connect_cnt = 0
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
def my_listener(state):
    #register somewhere that the session was lost
    if state == KazooState.LOST:
        zk.delete("cellservers/node", recursive = True)
    #Handle being disconnected from Zookeeper
    elif state == KazzoState.SUSPENDED:
        zk.delete("/cellservers/node", recursive = True)
    #Handle being connected/reconnected to Zookeeper
    else:
        zk.ensure_path("/cellservers")
        zk.create("/cellservers/node", connect_cnt)

zk.add_listener(my_listener)

#connection to RabbitMQ
connection_send = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel_send = connection_send.channel()
channel_send.queue_declare(queue = 'send_to_MQ')

connection_receive = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel_receive = connection_receive.channel()
channel_receive.queue_declare(queue = 'receive_from_MQ')

#Define c_move handler
#save client list. reply message(change to broadcasting later).
def cmove_handler (message):
    #divide message
    temp = message[6]
    i = 6
    while temp != ",":
        cmove_id = cmove_id + temp
        i++
    i++
    temp = message[i]
    while temp != ",":
        cmove_x = cmove_x + temp
        i++
    i++
    temp = message[i]
    while temp = != ")":
        cmove_y = cmove_y + temp
        i++

    #check wheter client in list or not

    #save client list
    client_data = [cmove_id, cmove_x, cmove_y]
    client_list = array.append(client_data)
    #Broadcasting - s_put, s_move, s_del - list division
    s_put = 'sput(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ')'
    s_move = 'smove(' + cmove_id + ',' + comve_x + ',' + cmove_y + ')'
    s_del = 'sdel(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ')'

    #RabbitMQ and ZMQ which one should I use???
    #Send message to RabbitMQ
    channel_send.basic_publish(exchange = '', routing_key = 'MQ', body = s_put)
    channel_send.basic_publish(exchange = '', routing_key = 'MQ', body = s_move)
    channel_send.basic_publish(exchange = '', routing_key = 'MQ', body = s_del)

    #Send message by using ZMQ
    socket_cell.send(s_put)
    socket_cell.send(s_move)
    socket_cell.send(s_del)

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

#Receive messages from RabbitMQ
channel_receive.basic_consume(callback, queue = 'receive_from_MQ', no_ack = True)
channel_receive.start_consuming()

#Loop : Receive c_move, run cmove_handler
while True:
    msg = socket_cell.recv()
    #Receive c_move
    if msg[0:4] = "cmove":
        print "Receive", msg
        cmove_handler(mgs)

#close the RabbitMQ connection
connection_send.close()
