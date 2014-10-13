#!/usr/bin/env python
#
# Kevin J. Walchko
# 22 Sept 2014
#

import os
import sys

path = "plugins/"
#plugins = {}
plugins = []

# Load plugins
sys.path.insert(0, path)
for f in os.listdir(path):
    fname, ext = os.path.splitext(f)
    if ext == '.py':
        mod = __import__(fname)
        #plugins[fname] = mod.Plugin()
        plugins.append( mod.Plugin() )
sys.path.pop(0)

# Callback
#for plugin in plugins.values():
#    plugin.cb()

for plugin in plugins:
	plugin.cb()