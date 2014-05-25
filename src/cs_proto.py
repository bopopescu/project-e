#!/usr/bin/python

import sys
import pika

# data members
client_list = array.array()

# methods

# generate messages and publish.
def cmove_handler (message):
    #data members
    cmove_id = ""
    cmove_x = ""
    cmove_y = ""
    cmove_gw = ""

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
    while temp != ",":
        cmove_y = cmove_y + temp
        i++
    i++
    temp = message[i]
    while temp != ")":
        cmove_gw = cmov_gw + temp

    #check wheter client in list or not
    //if client is in list then delete it.

    #add to client list
    client_data = [cmove_id, cmove_x, cmove_y]
    client_list = array.append(client_data)

    #Generate s_put, s_move, s_del
    s_put = 'sput(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ',' + cmove_gw + ')'
    s_move = 'smove(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ',' + cmove_gw + ')'
    s_del = 'sdel(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ',' + cmove_gw + ')'

    #publish message to gateway by using cmove_gw
    channel_pub.basic_publish(exchange = '', routing_key = 'GW_N', body = s_put)
    channel_pub.basic_publish(exchange = '', routing_key = 'GW_N', body = s_move)
    channel_pub.basic_publish(exchange = '', routing_key = 'GW_N', body = s_del)

# Init : MQ connection, ZK connection
connection = pika.BlockingConnection(pika.ConnectionParameters('TBD')
channel_pub = connection.channel()
channel_pub.queue_declare(queue = 'GW_N')

connection = pika.BlockingConnection(pika.ConnectionParameters('TBD')
channel_sub = connection.channel()
channel_sub.queue.declare(queue = 'ALL')

# Loop : processing protocol
while True:
    #subscribe message
    msg = socket_cell.recv()
    #Receive c_move
    if msg[0:4] = "cmove":
        print "Receive", msg
        cmove_handler(msg)


