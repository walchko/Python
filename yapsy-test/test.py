#!/usr/bin/env python
#
# by Kevin J. Walchko 

from yapsy.PluginManager import PluginManager
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('yapsy').setLevel(logging.DEBUG)

if __name__ == '__main__':
	pm = PluginManager()
	pm.setPluginPlaces(['plugins'])
	pm.collectPlugins()
	
	for p in pm.getAllPlugins():
		p.plugin_object.print_name()