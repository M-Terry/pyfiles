# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:31:42 2019

@author: James
"""

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)