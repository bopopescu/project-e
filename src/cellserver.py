#!/usr/bin/python

import sys
import pika

#Connect to RabbitMQ
connection_send = pika.BlockinConnection(pika.ConnectionParameters(host='locahost'))
channel_send = connection_send.channel()

connection_receive = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel_receive = connection.channel()

channel_send.queue_declare(queue='send')
channel_receive.queue_declare(queue='receive')

channel_send.basic_publish(exchange='', routing_key='send', body='Hello')
print " px[ Sent 'Hello World!'"

print "receive"

def callback(ch, method, properties, body):
    print "receive %r" % (body,)

channel_receive.basic_consume(callback, queue='receive', no_ack=True)

channel_receive.start_consuming()







connection_send.close()


##########Init##########
# MQ connection, creation of world
########################


##########Loop##########
# Receive c_move and correct data according to c_move
# Broadcasting - s_put, s_move, s_del - list division
########################
