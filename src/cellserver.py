#!/usr/bin/python

import sys
import pika
import zmq

context = zmq.Conext()
socket_cell = context.socket(zmq.REP)

client_list = []

#Define c_move handler
def cmove_handler ():

#Define s_put, s_move, s_del
s_put = "sput"
s_move = "smove"
s_del = "sdel"

#temporary tcp location
socket_cell.bind("tcp://127.0.0.1:5000")

##########Init##########
#Connect to RabbitMQ


##########Loop##########
# Receive c_move and correct data according to c_move
while True:
    message = socket_cell.recv()
    if (msg = "cmove")
        print "Receive", msg

    #Broadcasting - s_put, s_move, s_del - list division
    socket_cell.send(s_put)
    socket_cell.send(s_move)
    socket_cell.send(s_del)

