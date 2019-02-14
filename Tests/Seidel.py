# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:31:54 2019

@author: James
"""
import numpy as np
from numpy import linalg
from copy import copy

def Seidel(A,b,x0,tol,maxIter):
#    Solution of the system of linear equations Ax=b
#    using Gauss-Seidel iterative algorithm
#    Inputs:
#    A coefficient matrix (n-by-n)
#    b right-hand side (n-by-1)
#    x0 initial solution (n-by-1)
#    tol stop if norm of change in x<tol.
#    maxIter maximum number of iterations
#    Outputs:
#    x solution vector (n-by-1)
    [n,m] = np.shape(A)
    r = np.zeros((n,1))
    x = copy(x0)
    C = -A
    for i in range(0,n):
        C[i,i] = 0
    for i in range(0,n):
        C[i,0:n] = C[i,0:n] / A[i,i]
    for i in range(0,n):
        r[i,0] = b[i] / A[i,i]
    i = 1
    print '   i         x1         x2         x3   ......'
    while (i <= maxIter):
        xold = copy(x) # Save solution from previous step
        for j in range(0,n):
            x[j] = C[j,:] * x + r[j]
        if linalg.norm(xold - x) <= tol:
            print 'Gauss-Seidel method converged'
            return x
        print i, np.transpose(x)
        i = i + 1
    print '\n','Gauss-Seidel method did not converge'
    print 'Results after maximum number of iterations: '
    print np.transpose(x)
    return x

""" Example """
#A = np.matrix([[4.0,1.0,0.0],
#               [1.0,3.0,-1.0],
#               [1.0,0.0,2.0]])
#    
#b = np.transpose(np.matrix([3.0,-4.0,5.0]))
#
#x0 = np.transpose(np.matrix([0.0,0.0,0.0]))
#maxIter = 10
#tol = 1E-8
#
#x = Seidel(A,b,x0,tol,maxIter)
#print x