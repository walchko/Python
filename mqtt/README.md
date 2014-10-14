# MQTT

A very simple publish/subscribe framework using [MQTT](https://pypi.python.org/pypi/paho-mqtt#publishing) and [Mosquito](http://mosquitto.org). Basically there is one class that is capable of publishing or subscribing to topics. All you need to do is:

	
	import time
	import json
	from mqttclass import *

	def sensor_callback(client, userdata, msg):
		decode = json.loads(msg.payload)
		print msg.topic, decode

	def cmd_callback(client, userdata, msg):
		decode = json.loads(msg.payload)
		print msg.topic, decode

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

Create an array of topics to subscribe to as tuples, where `(topic,QoS)` and an array of callbacks. Note the number of topics must equal the number of callbacks and they must all be unique. Then create an instance of `PubSub` or `PubSubJSON`. You don't have to identify the published topics up front.

## Requirements

You will need the python bindings and the server, you can install them with:

    sudo pip install paho-mqtt
    
    brew update
    brew install mosquitto

## Examples

First you will need to start the server:

    [kevin@Tardis topic]$ mosquitto -p 9000 -v

where `-p` is the port to use and `-v` is for verbose. Change as you see fit.    

See `pubsub.py` and `pubsub2.py` for examples of how to use them.