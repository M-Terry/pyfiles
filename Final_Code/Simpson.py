# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:27:10 2019

@author: James
"""

# find integral of f using composite Simpson rule
# n must be even
import numpy as np
from scipy import integrate

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)

def Simpson(f,a,b,n):
    x = np.linspace(a, b, n + 1)
    return integrate.simps(feval(f,[x]), x)

# example
ss = 'np.exp(-(np.float64(x)**np.float64(2.0)))'
I = Simpson(ss,0,1,5)
print I