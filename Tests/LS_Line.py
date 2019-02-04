# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:20:58 2019

@author: James
"""

def LS_Line(x,y):
    m = len(x)
    x = x[:]
    y = y[:]    # Convert to column form if necessary
    sx = sum(x)
    sy = sum(y)
    sxx = sum(x*x)
    sxy = sum(x*y)
    c = m * sxx - sx**2   # Solve using Cramer's rule
    a = (m * sxy - sx * sy) / c
    b = (sxx * sy - sxy * sx) / c
    table = [x,  y,  (a*x+b),  (y-(a*x+b))]
    print '[x  y  (a*x+b)  (y-(a*x+b))'
    print table
    err = sum(table[3][:]**2)
    s = [a,b]
    return s