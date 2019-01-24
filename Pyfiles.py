# Created by Matthew Terry and James Faunda

import numpy as np
import math
from scipy import integrate

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
