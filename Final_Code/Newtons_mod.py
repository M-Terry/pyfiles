import math
import numpy as np

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)

def Newtons_Zero(self, dself, ddself, a, b, tol, iter):
	#Input: Function (string), 1st of Function (string), 2nd Derivative of Function (string), [a,b] - bounds containing zero, tolerance, max # iterations
	#Output: Array of iteration values
	x = [(a+b)/2]
	y = [feval(self, [x[0]])]
	y_pr = [feval(dself, [x[0]])]
	y_prpr = [feval(ddself,[x[0]])]
	for i in range(1, iter + 1, 1):
		x.append(x[i-1]-((y[i-1]*y_pr[i-1])/((y_pr[i-1]**2)-(y[i-1]*y_prpr[i-1]))))
		y.append(feval(self,[x[i]]))
		if np.abs(x[i]-x[i-1]) < tol:
			break
		y_pr.append(feval(dself,[x[i]]))
		y_prpr.append(feval(ddself,[x[i]]))
		iteration=i
	return print(x)

#test
func = 'x**2-2'
dfunc = '2*x'
ddfunc = '2'
Newtons_Zero(func, dfunc, ddfunc, 0, 4, .0001, 400)
