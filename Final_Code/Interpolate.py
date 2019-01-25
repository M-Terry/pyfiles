# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:08:08 2019

@author: James
"""

from scipy import interpolate

def interp1d(x,y,xi,kind):
    func = interpolate.interp1d(x,y,kind);
    yi = func(xi)
    return yi

def interp2d(x,y,z,xx,yy):
    func = interpolate.interp2d(x,y,z)
    zz = func(xx,yy)
    return zz

""" kind : str
Specifies the kind of interpolation as a string (‘linear’, ‘nearest’, ‘zero’,
 ‘slinear’, ‘quadratic’, ‘cubic’, ‘previous’, ‘next’, where ‘zero’, ‘slinear’,
 ‘quadratic’ and ‘cubic’ refer to a spline interpolation of zeroth, first,
 second or third order; ‘previous’ and ‘next’ simply return the previous or
 next value of the point) or as an integer specifying the order of the spline
 interpolator to use. Default is ‘linear’. """

""" Example """
#import matplotlib.pyplot as plt
#import numpy as np
#x=[0, .1, .4, .5, .6, .9, 1, 1.1, 1.4, 1.5, 1.6, 1.9, 2]
#y=[0, .06, .17, .19, .21, .25, .26, .27, .29, .29, .3, .31, .31]
#
#xi = [i/100.0 for i in range(0, 201, 1)]
#
#yic = interp1d(x,y,xi,'linear');
#yid = interp1d(x,y,xi,'cubic');
#
#figure = plt.figure()
#plt.plot(xi,yic,'g', label = 'linear')
#plt.plot(xi,yid,'k', label = 'cubic spline')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('plot ')
#plt.legend()
#
#""" 3D Plotting Example"""
#x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
#y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
#z = [0.0,    0.0,    0.0,    0.0,    0.0,    0.0,
#     0.0, 0.0047, 0.0374, 0.1263, 0.2994, 0.5848,
#     0.0, 0.0059, 0.0472, 0.1592, 0.3772, 0.7368,
#     0.0, 0.0067, 0.0540, 0.1822, 0.4318, 0.8434,
#     0.0, 0.0074, 0.0594, 0.2005, 0.4753, 0.9283,
#     0.0, 0.0080, 0.0640, 0.2160, 0.5120, 1.0000]
#
#xx = np.linspace(0,1,11)
#yy = xx
#zz = interp2d(x,y,z,xx,yy)
#from mpl_toolkits import mplot3d
#figure = plt.figure()
#ax = plt.axes(projection='3d')
#ax.contour3D(xx,yy,zz,101)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#
#func = lambda x,y: x**(1.0/3.0) * y**3.0
#figure = plt.figure()
#ax = plt.axes(projection = '3d')
#ax.contour3D(xx,yy,(zz - func(xx,yy)),10)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')