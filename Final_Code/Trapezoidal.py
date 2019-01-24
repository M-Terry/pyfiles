# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:15:50 2019

@author: James
"""

"""Return an approximation to the definite integral of f from a to b
using the trapezoidal rule with n intervals."""
import numpy as np

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)

def Trapezoidal(f, a, b, n):
    h = (b-a) / float(n)
    s = 0.5*(feval(f,[a]) + feval(f,[b]))
    for i in range(1,n,1):
        s = s + feval(f,[a + i*h])
    return s * h

# example
ss = 'np.exp(-(np.float64(x)**np.float64(2.0)))'
I2 = Trapezoidal(ss,0,1.5,500)
print I

