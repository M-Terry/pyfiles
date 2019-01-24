def lagrange_coef(x,y):
	d = [1]*len(x)
	c = [0]*len(x)
	for k in range(len(x)):
		for i in range(len(x)):
			if i != k:
				d[k] = float(d[k])*(float(x[k])-float(x[i]))
			c[k] = (float(y[k])/float(d[k]))
	return c
	