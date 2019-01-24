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