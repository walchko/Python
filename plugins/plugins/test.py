#!/usr/bin/env python
#
# Kevin J. Walchko
# 22 Sept 2014
#

class PluginInterface:
	def __init__(self):
		print '[+] PluginInterface init()'
		
	def cb(self):
		print '[-] Plugin not setup yet'


class Plugin(PluginInterface):
    def __init__(self):
    	PluginInterface.__init__(self)
        print "plugin Test: constructor"

#    def cb(self):
#        print "plugin Test: callback"