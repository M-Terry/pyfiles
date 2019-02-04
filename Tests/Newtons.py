# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:23:22 2019

@author: James
"""
from feval import feval
import numpy as np

def Newtons(fun,fun_pr,a,b,tol,maxIter):
    x = []
    y = []
    y_pr = []
    x.append(((a+b)/2.0))
    y.append(feval(fun,[x[0]]))
    y_pr.append(feval(fun_pr,[x[0]]))
    for i in range(1,maxIter):
        x.append(x[i - 1] - y[i - 1] / y_pr[i - 1])
        y.append(feval(fun,[x[i]]))
        if abs(x[i] - x[i - 1]) < tol:
            print 'Newton method has converged'
            break
        y_pr.append(feval(fun_pr,[x[i]]))
        iteration = i
    if (iteration >= maxIter):
        print 'zero not found to desired tolerance'
    n = len(x)
    k = np.linspace(1,n,n)
    out = np.zeros((n,3))
    for i in range(n):
        out[i,0] = k[i]
        out[i,1] = x[i]
        out[i,2] = y[i]
    np.set_printoptions(precision = 16)
#    print '  step        a         b          x          y'
#    print out
    return [n,out[n - 1,1],out[n - 1,2]]

""" Example """
#func = 'x**2-7'
#dfunc = '2*x'
#Ans = Newtons(func,dfunc,1,10,10E-16,100)