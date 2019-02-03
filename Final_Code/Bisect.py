# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:47:53 2019

@author: James
"""
import numpy as np
from feval import feval
def Bisect(fun,a,b,tol,maxIter):
    """
          Input and output variables
     fun       string containing name of function
     [a,b]     interval containing zero
     tol       allowable tolerance in computed zero
     maxIter   maximum number of iterations
     x         vector of approximations to zero
     y         vector of function values, fun(x)
    
    """
    A = np.empty([1,maxIter])
    B = np.empty([1,maxIter])
    x = np.empty([1,maxIter])
    y = np.empty([1,maxIter])
    ya = np.empty([1,maxIter])
    yb = np.empty([1,maxIter])
    A[0,0] = a
    B[0,0] = b
    ya[0,0] = feval(fun,[A[0,0]])
    yb[0,0] = feval(fun,[B[0,0]])
    if ya[0,0] * yb[0,0] > 0.0:
        print 'Function has same sign at end points'
        return
    
    for i in range(0,maxIter-1):
        x[0,i] = (A[0,i] + B[0,i]) / 2
        y[0,i] = feval(fun,[x[0,i]])
        if (x[0,i] - A[0,i]) < tol:
            print 'Bisection method has converged'
            break
        elif y[0,i] == 0.0:
            print 'exact zero found'
            break
        elif y[0,i] * ya[0,i] < 0:
            A[0,i+1] = A[0,i]
            ya[0,i+1] = ya[0,i]
            B[0,i+1] = x[0,i]
            yb[0,i+1] = y[0,i]
        else:
            A[0,i+1] = x[0,i]
            ya[0,i+1] = y[0,i]
            B[0,i+1] = B[0,i]
            yb[0,i+1] = yb[0,i]
        
        iteration = i
    
    if (iteration >= maxIter):
        print 'zero not found to desired tolerance'
    
    n = i+1
    k = np.linspace(1,n,n)
    out = np.zeros((n,5))
    for i in range(n):
        out[i,0] = k[i]
        out[i,1] = A[0,i]
        out[i,2] = B[0,i]
        out[i,3] = x[0,i]
        out[i,4] = y[0,i]
    np.set_printoptions(precision = 16)
    print '  step        a         b          x          y'
    print out
    return out

""" Example """
f = '(x ** 2) - 7'
Q = Bisect(f,1.0,10.0,10E-15,1000)