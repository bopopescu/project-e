#!/usr/bin/python

  import zmq
  import time

  context = zmq.Context()

  # Socket
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://localhost:5555")

  # Send request
  while True:
    print("Sending request %s" % request)
    socket.send("Request")
    # Get reply
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
    time.sleep(10)
