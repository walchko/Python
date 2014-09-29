#!/usr/bin/env python

import numpy as np

# Base class does nothing
class Base:
	def __init__(self, name='none'):
		self.x = 0
		self.y = 0
		self.name = name
		
	"""
	square uses this
	"""
	def area(self):
		return self.x*self.y

# Simple shape, inherits the area function
class Square(Base):
	def __init__(self,x):
		Base.__init__(self,'Square')
		self.x = x
		self.y = x

# Redefines the area function for a circle
class Circle(Base):
	def __init__(self,x):
		Base.__init__(self,'Circle')
		self.x = x
		self.y = 0
	"""
	this over rides the base class
	"""
	def area(self):
		return self.x*self.x*np.pi

def main():
	s = Square(5.0)
	print s.name + ' ' + str(s.area())
	
	c = Circle(1.0)
	print c.name + ' ' + str(c.area())
	

if __name__ == '__main__':
    main()

