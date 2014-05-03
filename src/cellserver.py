#!/usr/bin/python

import sys
import pika
import zmq

context = zmq.Conext()
socket_cell = context.socket(zmq.REP)

client_list = []

#Define c_move handler
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

    #save client list
    client_data = [cmove_id, cmove_x, cmove_y]
    client_list = 
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
        cmove_handler(mgs)
