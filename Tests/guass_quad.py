import numpy as np
import math

def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)
# find integral of function f on [a,b]
# using Gaussian quadrature at k(k=2,...5)points
def guass_quad(f,a,b,k):
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
# test
I = guass_quad('math.exp(-x**2)',0,2,5)
print I