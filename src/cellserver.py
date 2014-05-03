#!/usr/bin/python

import sys
import pika
import zmq

context = zmq.Conext()
socket_cell = context.socket(zmq.REP)

client_list = []

#Define c_move handler
def cmove_handler (message):
    #save client list
    #Broadcasting - s_put, s_move, s_del - list division


#temporary tcp location
socket_cell.bind("tcp://127.0.0.1:5000")

##########Init##########
#Connect to RabbitMQ


##########Loop##########
while True:
    msg = socket_cell.recv()
    #Receive c_move
    if msg[0:4] = "cmove":
        print "Receive", msg
        #save data and broadcasting
        cmove_handler(msg)
