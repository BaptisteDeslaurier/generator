#!/usr/bin/python3

def additionAbsolute(a,b):
	'''
	>>> additionAbsolute(2,3)
	5
	>>> additionAbsolute(2,-3)
	5
	'''
	
	return a + b

#print(additionAbsolute(2,3))

import doctest
doctest.testmod()
