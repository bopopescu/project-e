#!/usr/bin/python

import sys
import pika

# data members
client_list = array.array() # list for client
cell_size = [0, 0, 65536, 65536] # area of cell server. In this case, AA will be (0,0), BB will be (65536,65536).

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
    #case 1 : c_move가 셀 서버 내부를 가리키고, client_list에 해당 클라이언트가 없는 경우
    #client_list에 넣어준다.
    #case 2 : c_move가 셀 서버 내부를 가리키고, client_list에 해당 클라이언트가 있는 경우
    #기존의 클라이언트를 제거한 후 client_list에 넣어준다.
    #case 3 : c_move가 셀 서버 외부를 가리키면 해당 메시지를 무시하고 함수를 종료시킨다.
    if x >= cell_size[0] && x <= cell_size[1] && y >= cell_size[2] && y <= cell_size[3]:
        if cmove_id가 client_list에 있다면 :
            #case 1
            client_data = [cmove_id, cmove_x, cmove_y]
            client_list = array.append(client_data)
        else :
            #case 2
            client_list에서 cmove_id 제거
            client_data = [cmove_id, cmove_x, cmove_y]
            client_list = array.append(client_data)
    else:
        #case 3
        return

    #Generate s_put, s_move, s_del
    #P, M, D가 시야 범위 내의 클라이언트 리스트들을 가지고 있도록 메시지를 만들어준다.
    #지금은 예시로 메시지를 생성해준 것이다.
    s_put = 'sput(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ',' + cmove_gw + ')'
    s_move = 'smove(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ',' + cmove_gw + ')'
    s_del = 'sdel(' + cmove_id + ',' + cmove_x + ',' + cmove_y + ',' + cmove_gw + ')'

    #publish message to gateway by using cmove_gw
    channel_pub.basic_publish(exchange = '', routing_key = 'GW_N', body = s_put)
    channel_pub.basic_publish(exchange = '', routing_key = 'GW_N', body = s_move)
    channel_pub.basic_publish(exchange = '', routing_key = 'GW_N', body = s_del)

# Init : MQ connection, ZK connection
# GW_N 큐를 만들어준다.
connection = pika.BlockingConnection(pika.ConnectionParameters('TBD')
channel_pub = connection.channel()
channel_pub.queue_declare(queue = 'GW_N')

# ALL 큐를 만들어준다.
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
        # c_move가 오면 cmove_handler를  통해 P,M,D 메시지를 pub 해준다.
        cmove_handler(msg)


