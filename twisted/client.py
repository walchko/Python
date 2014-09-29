#!/usr/bin/env python

import socket
import sys

HOST, PORT = "localhost", 9000

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and send data
sock.connect((HOST, PORT))

while True:
	data = raw_input('--> ')
	
	if data == 'q':
		break
	
	sock.send(data + "\n")
	
	# Receive data from the server and shut down
	received = sock.recv(1024)
	
	print "Sent:     %s" % data
	print "Received: %s" % received
	
sock.close()