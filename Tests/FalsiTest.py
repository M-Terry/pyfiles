# -*- coding: utf-8 -*-
"""
Created on Sun Feb 03 15:02:36 2019

@author: MTerry
"""
def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)


def Falsi(f,aa,bb,tol,iterate):
    a = []
    b = []
    ya = []
    yb = []
    a.append(float(aa))
    b.append(float(bb))
    ya.append(float(feval(f,a)))
    yb.append(float(feval(f,b)))
    if ya[0]*yb[0] > 0.0:
        print 'Funtion has the same sign at end points'
        return False
    x = []
    y = []
    count = 0
    for i in range(iterate):
        x.append(b[i]-yb[i]*(b[i]-a[i])/(yb[i]-ya[i]))
        y.append(float(feval(f,[x[i]])))
        if y[i] == 0.0:
            print 'exact zero found'
            break;
        elif y[i]*ya[i] < 0:
            a.append(a[i])
            ya.append(ya[i])
            b.append(x[i])
            yb.append(y[i])
        else:
            a.append(x[i])
            ya.append(y[i])
            b.append(b[i])
            yb.append(yb[i])
        if i>1 and abs(x[i]-x[i-1]) < tol:
            print 'Falsi method has converged'
            break;
        count = i
    if count > max:
        print 'zeros not found to disired tolerance'
    n = len(x)
    k = [g for g in range(n)]
   # out = [k' a(1:n)' b(1:n)' x'  y'];
    return x[count], y

x,y = Falsi('x**2 - 2',1,3,0.02,20)
print x
print y

