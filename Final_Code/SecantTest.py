# -*- coding: utf-8 -*-
"""
Created on Sun Feb 03 15:32:08 2019

@author: MTerry
"""

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)


def Secant(f,a,b,tol,iterate):
    x = []
    y = []
    x.append(a)
    x.append(b)
    y.append(float(feval(f,[x[0]])))
    y.append(float(feval(f,[x[1]])))
    for i in range(1,iterate):
        x.append(x[i]-y[i]*(x[i]-x[i-1])/(y[i]-y[i-1]))
        y.append(float(feval(f,[x[i+1]])))
        if abs(x[i+1]-x[i]) < tol:
            print 'Secant method has converged'
            break;
        if y[i] == 0:
            print 'exact zero found'
            break;
        count = i
    if count >= iterate:
        print 'zero not found to desired tolerance'
    return x[-1], y[-1]

# example
    
x,y = Secant('x**2 - 2',1,3,0.02,20)
print x
print y