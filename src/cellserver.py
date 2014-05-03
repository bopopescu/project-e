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




##########Init##########
# MQ connection, creation of world
########################


##########Loop##########
# Receive c_move and correct data according to c_move
# Broadcasting - s_put, s_move, s_del - list division
########################
