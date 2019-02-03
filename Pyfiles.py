# Created by Matthew Terry and James Faunda

import numpy as np
import math
from scipy import integrate
from scipy.interpolate import interp1d

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)
		
class PyFiles(object):
	'''
	Class of all the functions needed in Aerodynamic simulation
	'''
	def __init__(self):
		pass

	# find integral of f using trapezoidal rule
	# n must be even
	def trapezoidal(self, f, a, b, n):
		'''
		INPUT: function in strings in terms of x, lower bound, upper bound, itereation
		OUTPUT: Integral
		'''
		h = (b-a) / float(n)
		s = 0.5*(feval(f,[a]) + feval(f,[b]))
		for i in range(1,n,1):
			s = s + feval(f,[a + i*h])
		return s * h

	# find integral of f using composite Simpson rule
	# n must be even
	def simpson(self,f,a,b,n):
		'''
		INPUT: function in strings in terms of x, lower bound, upper bound, itereation
		OUTPUT: Integral
		'''
		x = np.linspace(a, b, n + 1)
		return integrate.simps(feval(f,[x]), x)

	# find integral of function f on [a,b]
	# using Gaussian quadrature at k(k=2,...5)points
	def guass_quad(self,f,a,b,k):
		'''
		INPUT: function in strings in terms of x, lower bound, upper bound, iterations
		OUTPUT: single int gaussian
		'''
		if k < 2 or k > 5:
			raise Exception("k value must be in between 2 and 5")
			return False

		t=[[-0.5773502692, -0.7745966692, -0.8611363116, -0.9061798459],
			[0.5773502692,  0.0000000000, -0.3399810436, -0.5384693101],
			[0.0,           0.7745966692,  0.3399810436,  0.0000000000],
			[0.0,           0.0,           0.8611363116, 0.5384693101],
			[0.0,           0.0,           0.0,           0.9061798459]]
		
		c=[[1.0,         0.5555555556,  0.3478548451,  0.2369268850],
			[1.0,         0.8888888889,  0.6521451549,  0.4786286705],
			[0.0,         0.5555555556,  0.6521451549,  0.5688888889],
			[0.0,         0.0,           0.3478548451,  0.4786286705],
			[0.0,         0.0,           0.0,           0.2369268850]]
		x = []
		for i in range(k):
			x.append(.5*((b-a)*t[i][k-2]+b+a))

		y = []
		for i in x:
			y.append(feval(f,[i]))

		cc = []
		for i in range(k):
			cc.append(c[i][k-2])

		cc = np.asmatrix(cc)
		cd = cc.getH()
		it = y*cd
		I = it*(b-a)/2
		return  np.squeeze(np.asarray(I))

	def erf2(self):
		return 0.995322265018953

	# Calculate coefficients of Lagrange Functions
	def lagrange_coef(self,x,y):
		d = [1]*len(x)
		c = [0]*len(x)
		for k in range(len(x)):
			for i in range(len(x)):
				if i != k:
					d[k] = float(d[k])*(float(x[k])-float(x[i]))
				c[k] = (float(y[k])/float(d[k]))
		return c

	# Evaluate Lagrange interpolation polynomial at x=t
	def lagrange_eval(self,t,x,c):
		p = []
		
		for i in range(len(t)):
			p.append(0)
			N = []
			N = [1]*len(x)
			for j in range(len(x)):
				for k in range(len(x)):
					if j != k:
						N[j] = float(N[j])*(float(t[i]) - float(x[k]))
				p[i] = float(p[i])+float(N[j])*float(c[j])
		return p

	def bisect(fun,a,b,tol,maxIter):
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

	def falsi(f,aa,bb,tol,iterate):
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
		if count >= iterate:
			print 'zeros not found to disired tolerance'
		n = len(x)
		k = [g for g in range(n)]
		# out = [k' a(1:n)' b(1:n)' x'  y'];
		return x[count], y

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


