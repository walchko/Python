#!/usr/bin/env python


import json
import yaml

"""
Simple read/write json/yaml class
"""
class Doc:
	# could eventually switch between json and yaml
	
	doc_yaml = 0
	doc_json = 1
	
	def __init__(self,type=doc_yaml):
		self.type = type
	
	# maybe determine from filename??	
	def read(self,filename):
		if self.type == doc_yaml:
			d = self.yaml_read(filename)
		else
			d = self.json_read(filename)
		
		return d
		
	def yaml_read(self,filename):
		f = open(filename,'r')
		file = yaml.safe_load(f)
		f.close()
		return file
		
	def yaml_write(self,filename,data):
		f = open(filename,'w')
		yaml.dump(data,f)
		f.close()
		
	def json_read(self,filename):
		f = open(filename,'r')
		file = json.load(f)
		f.close()
		return file
		
	def json_write(self,filename,data):
		f = open(filename,'w')
		json.dump(data,f)
		f.close()

def main():
	import pprint as pp
	j = Doc()
	
	# Json
	print ' --- JSON ---'
	data = j.json_read('test.json')
	data['kevin'] = 'is cool'
	pp.pprint(data)
	j.json_write('out.json',data)
	
	# Yaml
	print '\n--- Yaml ---'
	data = j.yaml_read('test.yaml')
	data['kevin'] = 'cool cat'
	pp.pprint(data)
	j.yaml_write('out.yaml',data)

if __name__ == '__main__':
    main()

