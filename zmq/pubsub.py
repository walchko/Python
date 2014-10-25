#!/usr/bin/env python
#
# Kevin J. Walchko 23 Oct 2014
# 

import sys
import time
import json
from zmqclass import *
import datetime as dt


def pub():
	p = Pub()
	ref = 0.1
	try:
		while True:
			data = {'x': ref, 'y':2.0*ref}
			ref += 0.25
			p.pub('vel',data)
			p.pub('pos',data)
			print 'sent data'
			time.sleep(0.1)
			
	except KeyboardInterrupt:
		pass

def sub():
	sub_topics = ['vel','pos']
	
	p = Sub(sub_topics)
	
	try:
		while True:
			topic,msg = p.recv()
			print topic,msg,dt.datetime.now()
	
	except KeyboardInterrupt:
		pass

def cli():
	print 'usage: pubsub.py "pub"|"sub" '
	sys.exit(1)

def main():
	if len(sys.argv) < 2:
		cli()
		
	func = sys.argv[1]
	if func == 'sub':
		sub()
	elif func == 'pub':
		pub()
	else:
		cli()
		

if __name__ == "__main__":
	main()