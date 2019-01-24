# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:15:50 2019

@author: James
"""

"""Return an approximation to the definite integral of f from a to b
using the trapezoidal rule with n intervals."""
import numpy as np

def Trapezoidal1(func,a,b,n):
    """This was the original attempt to translate MATLAB code to 
    Python code, this is also the least accurate."""
    if type(a) == np.float64:
        if type(b) == np.float64:
            if type(n) == int:
                h = (b - a) / n
                S = func(a)
                for i in range(1,n-1):
                    x = a + h * i
                    S += 2.0 * func(x)
                S += func(b)
                I = h * S / 2.0
                return np.float64(I)
            else:
                print 'n must be an integer'
        else:
            print 'b must be float64'
    else:
        print 'a must be float64'

def Trapezoidal2(f, a, b, n):
    h = (b-a) / float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    return s * h

def Trapezoidal3(f, a, b, n):
    h = (b - a) / n
    s = (f(a) + f(b))
    i = 1
    while i < n: 
        s += 2 * f(a + i * h) 
        i += 1
    return ((h / 2) * s) 

def Trapezoidal4(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    return np.trapz(f(x), x)

def Trapezoidal5(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    s = y[0] + 2.0 * sum(y[1:n]) + y[n]
    h = float(b - a) / n
    return s * h / 2.0

def Trapezoidal6(f, a, b, n):
    h = (b-a) / float(n)
    area = (f(a) + f(b))/2.0
    for i in xrange(1, n):
        x = a + i*h;
        area = area + f(x)
    area = area*h
    return area