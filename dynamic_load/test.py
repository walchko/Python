#!/usr/bin/env python

import re
import os
import importlib

def load_plugins():
	path = os.getcwd() # get current path
	pysearchre = re.compile('.py$', re.IGNORECASE) # build a filter
	pluginfiles = filter(pysearchre.search,os.listdir(path+'/module')) # apply filter to get script names
	form_module = lambda fp: fp.split('.')[0] # make another filter to strip off extensions
	plugins = map(form_module, pluginfiles) # apply filter
	modules = []
	for plugin in plugins:
		if not plugin.startswith('__'): # weed out __init__.py
			modules.append(importlib.import_module('module.'+plugin)) # import module.primatives
			print 'module.'+plugin
	return modules
    
m = load_plugins()
print m

# what value is having __init__.py, i don't use it???
# problem is I don't know what I am calling with m[0]???
a=m[0].Circle(3.0)
print a.name,'radius:',a.x,'area:',a.area()

b=m[0].Square(3.0)
print b.name,'size:',b.x,'area:',b.area()

print getattr(m[0],'__name__').split('.')[1] # primatives
print getattr(m[1],'__name__').split('.')[1] # stuff

