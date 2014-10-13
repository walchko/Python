# MQTT

A very simple publish/subscribe framework using [MQTT](https://pypi.python.org/pypi/paho-mqtt#publishing) and [Mosquito](http://mosquitto.org).

## Requirements

You will need the python bindings and the server, you can install them with:

    sudo pip install paho-mqtt
    
    brew update
    brew install mosquitto

## Examples

First you will need to start the server:

    [kevin@Tardis topic]$ mosquitto -p 9000 -v

where `-p` is the port to use and `-v` is for verbose. Change as you see fit.    

See `pub.py` and `sub.py` for examples of how to use them.