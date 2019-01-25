from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
""" 3D Plotting Example"""
x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
z = [0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
     0.0, 0.0047, 0.0374, 0.1263, 0.2994, 0.5848,
     0.0, 0.0059, 0.0472, 0.1592, 0.3772, 0.7368,
     0.0, 0.0067, 0.0540, 0.1822, 0.4318, 0.8434,
     0.0, 0.0074, 0.0594, 0.2005, 0.4753, 0.9283,
     0.0, 0.0080, 0.0640, 0.2160, 0.5120, 1.0000]
zz = interpolate.interp2d(x,y,z)
xx = np.linspace(0,1,11)
yy = xx
from mpl_toolkits import mplot3d
figure = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(xx,yy,zz(xx,yy),101)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

func = lambda x,y: x**(1.0/3.0) * y**3.0
figure = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(xx,yy,zz(xx,yy) - func(xx,yy),101)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()