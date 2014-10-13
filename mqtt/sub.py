#!/usr/bin/env python

import paho.mqtt.client as mqtt
from mqttclass import *
import time


global cnt
cnt = 0

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	global cnt
	print(msg.topic+' '+str(cnt)+" "+str(msg.payload))
	cnt += 1

s = SubJSON('sensor',on_message)
s.start()

while True:
	time.sleep(1)
	pass