#!/usr/bin/env python
#
# Kevin J. Walchko 13 Oct 2014
#
# see https://pypi.python.org/pypi/paho-mqtt#publishing for more info

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json

class PubSub:
	def __init__(self,topic,host='localhost',port=9000,keep_alive=60):		
		self.mqttc = mqtt.Client()
	
		# functions
		self.mqttc.on_connect = self.on_connect 
		self.topic = topic
		
		err = self.mqttc.connect(host, port,keep_alive)
		
		if err != 0:
			print '[-] Error, could not connect'
			
		ps = self.mqttc.socket().getsockname()	# this computer
		brk = self.mqttc.socket().getpeername() # broker
		print '[+] %s:%d connected to broker %s:%d'%(ps[0],ps[1],brk[0],brk[1])
	
	def __del__(self):
		self.stop()
		
	def start(self):
		self.mqttc.loop_start()
		
	def stop(self):
		print '[<] Shutting down'
		self.mqttc.loop_stop()
		self.mqttc.disconnect()
		
	def on_connect(self,mqttc, userdata, flags, rc):
		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
		self.mqttc.subscribe(self.topic)
		#print("rc: "+str(rc)+str(userdata)+str(flags))
			
	def publish(self,msg):
		self.mqttc.publish(self.topic,msg)
		

class Sub(PubSub):
	def __init__(self,topic,callback,host='localhost',port=9000):	
		PubSub.__init__(self,topic,host,port)
		self.mqttc.on_message = callback
		self.mqttc.will_set(self.topic,'exit_sub')

class Pub(PubSub):
	def __init__(self,topic,host='localhost',port=9000):	
		PubSub.__init__(self,topic,host,port)	
		self.mqttc.will_set(self.topic,'exit_pub')

class SubJSON(PubSub):
	def __init__(self,topic,callback,host='localhost',port=9000):	
		PubSub.__init__(self,topic,host,port)
		self.cb = callback
		self.mqttc.will_set(self.topic,'exit_sub')
		
		self.mqttc.on_message = self.on_message
		
	def on_message(self,client, userdata, message):
		# unpack the message to a dict()
		m = json.loads(message.payload)
		message.payload = m
		
		# now call the user defined cb
		self.cb(client, userdata, message)
		
class PubJSON(Pub):
	def __init__(self,topic,host='localhost',port=9000):	
		Pub.__init__(self,topic,host,port)	
		
	"""
	remember to unpack json: decoded = json.loads(data_string)
	"""
	def publish(self,msg):
		msg = json.dumps(msg)
		self.mqttc.publish(self.topic,msg)

if __name__ == "__main__":
	pass