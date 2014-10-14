#!/usr/bin/env python
#
# Kevin J. Walchko 13 Oct 2014
# 

import time
import json
from mqttclass import *


def sensor_callback(client, userdata, msg):
	print msg.topic, msg.payload

def cmd_callback(client, userdata, msg):
	print msg.topic, msg.payload

def main():
	sub_topics = [('sensor',0),('cmd',0)]
	callbacks = [sensor_callback,cmd_callback]
	
	p = PubSubJSON(sub_topics,callbacks)
	p.start()
	ref = 0.1
	while True:
		data = {'x': ref, 'y':2.0*ref}
		ref += 0.25
		p.publish('vel',data)
		time.sleep(.1)
	p.stop()

if __name__ == "__main__":
	main()