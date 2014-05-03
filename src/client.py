#!/usr/bin/python

  import zmq
  import time
  import random

  context = zmq.Context()

  # Socket
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://127.0.0.1:5000")
  socket.send("connected");

  # Send request
  while True:
    request="cmove(%d,%d)" %(x_temp,y_temp);
    print("Sending request %s" % request)
	x_temp=random.randint(0,2**16)
	y_temp=random.randint(0,2**16)
    socket.send(request);
    # Get reply
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
    time.sleep(10)
