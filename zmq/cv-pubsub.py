#!/usr/bin/env python
#
# Kevin J. Walchko 25 Oct 2014
# 

import sys
import time
import json
from zmqclass import *
import datetime as dt
import cv2


def pub():
	p = PubBase64()
	camera = cv2.VideoCapture(0)
	try:
		while True:
			ret, frame = camera.read()
			jpeg = cv2.imencode('.jpg',frame)[1]
			p.pub('image',jpeg)
			print '[*] frame: %d k   jpeg: %d k'%(frame.size/1000,len(jpeg)/1000)
			#time.sleep(0.1)
			
	except KeyboardInterrupt:
		pass

def sub():
	sub_topics = ['image']
	
	p = SubBase64(sub_topics)
	
	try:
		while True:
			topic,msg = p.recv()
			
			if not msg:
				pass
			elif 'image' in msg:
				im = msg['image']
				buf = cv2.imdecode(im,1)
				cv2.imshow('image',buf)
				cv2.waitKey(10)
	
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