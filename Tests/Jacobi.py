# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:30:52 2019

@author: James
"""
import numpy as np
from numpy import linalg
from copy import copy

def Jacobi(A,b,x0,tol,maxIter):
#    Solution of the system of linear equations
#    Ax=b
#    using iterative Jacobi algorithm
#    Inputs:
#    A coefficient matrix (n-by-n)
#    b right-hand side (n-by-1)
#    x0 initial solution (n-by-1)
#    tol stop if norm of change in x<tol.
#    maxIter maximum number of iterations
#    Outputs:
#    x solution vector (n-by-1)
    [n,m] = np.shape(A)
    d = np.zeros((n,1))
    xold = copy(x0)
    C = -copy(A)
    for i in range(0,n):
        C[i,i] = 0
    for i in range(0,n):
        C[i,:] = C[i,:] / A[i,i]
    for i in range(0,n):
        d[i,0] = b[i] / A[i,i]
    i = 1
    print '   i         x1         x2         x3   ......'
    while (i <= maxIter):
        xnew = C * xold + d
        if linalg.norm(xnew - xold) <= tol:
            x = xnew
            print 'Jacobi method converged'
            return
        else:
            xold = xnew
        print i,    xnew
        i = i + 1
    print 'Jacobi method did not converge'
    print 'Results after maximum number of iterations: '
    x = xnew
    print x
    
    
""" Example """
A = np.matrix([[4.0,1.0,0.0],
               [1.0,3.0,-1.0],
               [1.0,0.0,2.0]])
    
b = np.transpose(np.matrix([3.0,-4.0,5.0]))

x0 = np.transpose(np.matrix([0.0,0.0,0.0]))
maxIter = 10
tol = 1E-8

x = Jacobi(A,b,x0,tol,maxIter)
print x