#!/usr/bin/env python
#
# Kevin J. Walchko 13 Oct 2014
# 

import time
import json
from mqttclass import *


def vel_callback(client, userdata, msg):
	print msg.topic, msg.payload

def main():
	sub_topics = [('vel',0)]
	callbacks = [vel_callback]
	
	p = PubSubJSON(sub_topics,callbacks)
	p.start()
	ref = 0.1
	while True:
		data = {'x': ref, 'y':2.0*ref}
		ref += 0.25
		p.publish('cmd',data)
		p.publish('sensor',data)
		time.sleep(.1)
	p.stop()

if __name__ == "__main__":
	main()