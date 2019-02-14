# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:42:42 2019

@author: James
"""
import numpy as np

def Thomas(a,d,b,r):
#    solve Ax=b, where A is a tridiadonal matrix
#    Input
#    a upper diagonal of matrix A,a(n)=0.
#    d diagonal of matrix A
#    b lower diagonal of matrix A, b(1)=0
#    r right-hand side of equation
    n = len(d)
    x = np.matrix(np.zeros((n,1)))
    a[0] = a[0] / d[0]
    r[0] = r[0] / d[0]
    for i in range(1,n-1):
        denom = d[i] - b[i] * a[i-1]
        if (denom == 0):
            print 'zero in denominator'
            break
        a[i] = a[i] / denom
        r[i] = (r[i] - b[i] * r[i-1]) / denom
    r[n-1] = (r[n-1] - b[n-1] * r[n-2]) / (d[n-1] - b[n-1] * a[n-2])
    x[n-1] = r[n-1]
    for i in range(n-1,0,-1):
        x[i-1] = r[i-1] - a[i-1] * x[i]
    return x
        
""" Example """        
#a = np.transpose(np.matrix([1.0,-1.0,0]))
#    
#d = np.transpose(np.matrix([4.0,3.0,4.0]))
#
#b = np.transpose(np.matrix([0.0,1.0,-1.0]))
#r = np.transpose(np.matrix([3.0,4.0,5.0]))
#
#x = Thomas(a,d,b,r)