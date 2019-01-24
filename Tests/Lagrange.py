"""
Created on Tue Jan 24 16:30:00 2019

@author: Matthew Terry
"""	
# Calculate coefficients of Lagrange Functions
def lagrange_coef(x,y):
	d = []
	c = [0]*len(x)
	for k in range(len(x)):
		d.append(1)
		for i in range(len(x)):
			if i != k:
				d[k] = d[k]*(x[k]-x[i])
			c[k] = (y[k]/d[k])
	return c

# Evaluate Lagrange interpolation polynomial at x=t
def lagrange_eval(t,x,c):
	p = []
	
	for i in range(len(t)):
		p.append(0)
		N = []
		N = [1]*len(x)
		for j in range(len(x)):
			#pdb.set_trace()
			for k in range(len(x)):
				if j != k:
					N[j] = float(N[j])*(float(t[i]) - float(x[k]))
			p[i] = float(p[i])+float(N[j])*float(c[j])
	return p


#x=[0, .5, 1, 1.5, 2]
#y=[0, .19, .26, .29, .31]

x=[0, .1, .4, .5, .6, .9, 1, 1.1, 1.4, 1.5, 1.6, 1.9, 2]
y=[0, .06, .17, .19, .21, .25, .26, .27, .29, .29, .3, .31, .31]

xi = [i/100.0 for i in range(0, 201, 1)]
cia=lagrange_coef(x,y)
yia=lagrange_eval(xi,x,cia)
print yia
