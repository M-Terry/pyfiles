# Calculate coefficients of Lagrange Functions
def lagrange_coef(x,y):
	d = [1]*len(x)
	c = [0]*len(x)
	for k in range(len(x)):
		for i in range(len(x)):
			if i != k:
				d[k] = float(d[k])*(float(x[k])-float(x[i]))
			c[k] = (float(y[k])/float(d[k]))
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

""" Example from interp_demo.m """
from scipy import interpolate
import matplotlib.pyplot as plt
#x=[0, .5, 1, 1.5, 2]
#y=[0, .19, .26, .29, .31]
x=[0, .1, .4, .5, .6, .9, 1, 1.1, 1.4, 1.5, 1.6, 1.9, 2]
y=[0, .06, .17, .19, .21, .25, .26, .27, .29, .29, .3, .31, .31]

xi = [i/100.0 for i in range(0, 201, 1)]
cia=lagrange_coef(x,y)
yia=lagrange_eval(xi,x,cia)
#print yia
yic=interpolate.interp1d(x,y,kind = 'linear',);
yid=interpolate.interp1d(x,y,kind = 'cubic');

figure = plt.figure()
plt.plot(x,y,'b*', label = 'points')
plt.plot(xi,yia,'r', label = 'Lagrange')
plt.plot(xi,yic(xi),'g', label = 'linear')
plt.plot(xi,yid(xi),'k', label = 'cubic spline')

plt.xlabel('x')
plt.ylabel('y')
plt.title('plot ')
plt.legend()
