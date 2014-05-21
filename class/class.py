#!/usr/bin/env python

import numpy as np

# Base class does nothing
class Base:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.name = 'None'
	def area(self):
		return self.x*self.y

# Simple shape, inherits the area function
class Square(Base):
	def __init__(self,x):
		self.x = x
		self.y = x
		self.name = 'Square'

# Redefines the area function for a circle
class Circle(Base):
	def __init__(self,x):
		self.x = x
		self.y = 0
		self.name = 'Circle'
	def area(self):
		return self.x*self.x*np.pi

def main():
	s = Square(5.0)
	print s.name + ' ' + str(s.area())
	
	c = Circle(1.0)
	print c.name + ' ' + str(c.area())
	

if __name__ == '__main__':
    main()

