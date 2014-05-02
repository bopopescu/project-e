#!/usr/bin/python

#Init : MQ connection, creation of world(Oh...)
    
#loop : receive c-move and correct data according to c-move
#       broad casting - s_put, s_move, s_del - list division

import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
