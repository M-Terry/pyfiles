# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:41:18 2019

@author: James
"""
import numpy as np
from copy import copy
def Gauss_Elim(A,b):
#    Solve Ax=b using Gaussian elimination without pivoting
#    Inputs:
#    A is the n-by-n coefficient matrix
#    b is the n-by-k right-hand-side matrix
#    Outputs:
#    x is the n-by-k solution matrix
    [n,k1] = np.shape(A)
    a = copy(A)
    [n1,k] = np.shape(b)
    B = copy(b)
    x = np.zeros((n,k))
    for i in range(1,n,1):
        m = -a[i:n,i-1] / a[i-1,i-1]
        a[i:n,:] = a[i:n,:] + m * a[i-1,:]
        B[i:n,:] = B[i:n,:] + m * B[i-1,:]
    x[n-1,:] = B[n-1,:] / a[n-1,n-1]
    for i in range((n - 1),0,-1):
        x[i-1,:] = (B[i-1,:] - a[i-1,i:n] * x[i:n,:]) / a[i-1,i-1]
    
    return x

""" Example """
A = np.matrix([[4.0,1.0,0.0],
               [1.0,3.0,-1.0],
               [1.0,0.0,2.0]])
    
b = np.transpose(np.matrix([3.0,-4.0,5.0]))
Ans = Gauss_Elim(A,b)
print Ans