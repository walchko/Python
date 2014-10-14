#!/usr/bin/env python
#
# Kevin J. Walchko 13 Oct 2014
#
# see https://pypi.python.org/pypi/paho-mqtt#publishing for more info

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json

"""

MQTTMessage. This is a class with members topic, payload, qos, retain.

todo: 
- add logging
- Base64 for image storage
"""
class PubSub:
	"""
	"""
	def __init__(self,topics,callbacks,host='localhost',port=9000,keep_alive=60):		
		self.mqttc = mqtt.Client()
	
		# functions
		self.mqttc.on_connect = self.on_connect 
		self.mqttc.on_message = self.on_message
		self.topics = topics
		
		try:
			err = self.mqttc.connect(host, port,keep_alive)
			ps = self.mqttc.socket().getsockname()	# this computer
			brk = self.mqttc.socket().getpeername() # broker
			print '[+] %s:%d connected to broker %s:%d'%(ps[0],ps[1],brk[0],brk[1])
			
			if len(topics) != len(callbacks):
				raise Exception('Error: len(topics) != len(callbacks)')
			
			cb_dict={}
			
			if len(self.topics) > 0:
				for i,j in zip(topics,callbacks):
					#self.mqttc.message_callback_add(i[0],j)
					cb_dict[i[0]]=j
				
			self.cb = cb_dict
				
 		except Exception,e:
 			print '[-] Error, %s to %s:%d'%(str(e),host,port)
 			#raise
	
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
		if len(self.topics) > 0:
			self.mqttc.subscribe(self.topics)
			
	def publish(self,topic,msg):
		self.mqttc.publish(topic,msg)
		
	def on_message(self,client, userdata, msg):
		f=self.cb[msg.topic]
		f(client, userdata, msg)
		
"""
dumps - encode
loads - decode
"""
class PubSubJSON(PubSub):
	
	def __init__(self,topic,callback,host='localhost',port=9000):	
		PubSub.__init__(self,topic,callback,host,port)
		#self.mqttc.on_connect = self.on_connect 
		self.mqttc.on_message = self.on_message
	
	def publish(self,topic,msg):
		jmsg = json.dumps(msg)
		self.mqttc.publish(topic,jmsg)
		
	def on_message(self,client, userdata, msg):
		#print msg.topic, msg.payload
		f=self.cb[msg.topic]
		jmsg = msg
		jmsg.payload = json.loads(msg.payload)
		f(client, userdata, jmsg)

"""
"""
class PubSubBase64(PubSub):
	def __init__(self,topic,callback,host='localhost',port=9000):	
		PubSub.__init__(self,topic,callback,host,port)
		self.mqttc.on_message = self.on_message
	
	def publish(self,topic,msg):
		jmsg = json.dumps(msg)
		self.mqttc.publish(topic,jmsg)
		
	def on_message(self,client, userdata, msg):
		#print msg.topic, msg.payload
		f=self.cb[msg.topic]
		jmsg = msg
		jmsg.payload = json.loads(msg.payload)
		f(client, userdata, jmsg)

if __name__ == "__main__":
	pass