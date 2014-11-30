#!/usr/bin/env python
#
# by Kevin J. Walchko 

from yapsy.IPlugin import IPlugin

class SimplePlugin(IPlugin):
	def __init__(self):
		IPlugin.__init__(self)
		print 'hobo'
		
	def avtivate(self):
		IPlugin.activate(self)
		return
		
	def print_name(self):
		print "This is plugin 1"