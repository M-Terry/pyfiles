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
       s = [a,b] #a is slope, b is intercept
    return s

""" Example """
""" Problem 4 """
import matplotlib.pyplot  as plt
import numpy as np
from Bisect import Bisect
f = '(x**4) - 0.25'
BisectAns = Bisect(f,0.1,1,10E-16,1000)
root = np.sqrt(2) / 2
error = abs(root - BisectAns[1])
x = error[0:len(error)-1]
y = error[1:len(error)]
[slope,intercept]= LS_Line(x,y)
err_k = slope * x + intercept
fig = plt.figure()
plt.plot(error[1:len(error)],'*',err_k)
plt.xlabel('Iteration')
plt.ylabel('Err_k')
plt.title('Err_k Over Time')
