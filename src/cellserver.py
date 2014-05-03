#!/usr/bin/python

import sys
import pika
import zmq
import time

#make server by using zmq.REP and zmp.REQ

#Echo server example
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    # Do some 'work'
    time.sleep(1)

    # Send reply back to client
    socket.send("world")

#Publish server example
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    zipcode = 1
    temperature = 1
    relhumidity = 1

    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))


##########Init##########
# MQ connection, creation of world
########################


##########Loop##########
# Receive c_move and correct data according to c_move
# Broadcasting - s_put, s_move, s_del - list division
########################
