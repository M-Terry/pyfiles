# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:27:10 2019

@author: James
"""

# find integral of f using composite Simpson rule
# n must be even
# the input for func must be a function, an example is provided below:
#f = lambda x: np.sqrt(1 + 4.0*(x**2))
import numpy as np
from scipy import integrate

def Simpson1(func,a,b,n):
    """This was the original attempt to translate MATLAB code to 
    Python code, this is also the least accurate."""
    if type(a) == np.float64:
        if type(b) == np.float64:
            if type(n) == int:
                h = (b - a) / np.float64(n)
                S = np.float64(func(a))
                for i in range(1,n-1,2):
                    x = a + np.float64(h) * np.float64(i)
                    S += np.float64(4.0) * np.float64(func(np.float64(x)))
                
                for i in range(2,n-2,2):
                    x = a + np.float64(h) * np.float64(i)
                    S += np.float64(2.0) * np.float64(func(np.float64(x)))
                
                S += np.float64(func(b))
                I = np.float64(h) * np.float64(S) / np.float64(3.0)
                return np.float64(I)
            else:
                print 'n must be an integer'
        else:
            print 'b must be float64'
    else:
        print 'a must be float64'
        
def Simpson2(f,a,b,n):
    x = np.linspace(a, b, n + 1)
    return integrate.simps(f(x), x)

def Simpson3(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,n/2 + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,n/2):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)