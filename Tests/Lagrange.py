# Calculate coefficients of Lagrange Functions
def lagrange_coef(x,y):
	d = []
	for k in range(len(x)):
		d.append(1)
		for i in range(len(x)):
			if i != k:
				d[k] = d[k]*(x[k]-x[i])
			c.append(y[k]/d[k])

# Evaluate Lagrange interpolation polynomial at x=t
def langrange_Eval(t,x,c):
	p = []
	N = []
	for i in range(len(t)):
		p.append(0)
		for j in range(len(t)):
			N.append(1)
			for k in range(len(t)):
			if j != k:
				N[j] = N[j]*(t[i] - x[k]);
			p[i] = p[i]+N[j]*c[j]


