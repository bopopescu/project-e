#!/usr/bin/python
import socket
import sys
import pika

##########Init : MQ connection, creation of world(Oh...)#############3

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8000)
print


#loop : receive c-move and correct data according to c-move
#       broad casting - s_put, s_move, s_del - list division


PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
