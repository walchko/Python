#!/usr/bin/env python

import numpy as np
#import Base

class Stuff:
	def __init__(self,a):
		self.x = a
		
	def test(self):
		return self.x

	

if __name__ == '__main__':
	s = Stuff(5.0)
	print 'Stuff: ',s.test



