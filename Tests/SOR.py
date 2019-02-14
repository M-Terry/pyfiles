# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:38:00 2019

@author: James
"""
import numpy as np
from numpy import linalg
from copy import copy

def SOR(A,b,x0,w,tol,maxIter):
#    Solution of the system of linear equations 
#    Ax=b
#    using SOR iterative algorithm
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
    C = -copy(A)
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
            x[j] = (1 - w) * xold[j] + w * (C[j,:] * x + r[j])
        if linalg.norm(xold-x) <= tol:
            print 'SOR method converged'
            return x
        print i, np.transpose(x)
        i = i + 1
    print 'SOR method did not converge'
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
#x1 = SOR(A,b,x0,0.5,tol,maxIter)
#x2 = SOR(A,b,x0,1.2,tol,maxIter)
#x3 = SOR(A,b,x0,1.4,tol,maxIter)
#x4 = SOR(A,b,x0,1.8,tol,maxIter)
#print '\n',x1,'\n'
#print x2,'\n'
#print x3,'\n'
#print x4,'\n'