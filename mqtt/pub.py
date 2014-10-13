#!/usr/bin/env python
#
# Kevin J. Walchko 13 Oct 2014
# 

import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
from mqttclass import *

def main():
	p = PubJSON('sensor')
	p.start()
	ref = 0.1
	while True:
		data = {'x': ref, 'y':2.0*ref}
		ref += 0.25
		p.publish(data)
		time.sleep(.1)
	p.stop()

if __name__ == "__main__":
	main()