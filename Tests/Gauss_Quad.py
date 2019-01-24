# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:27:02 2019

@author: James
"""

from scipy import integrate
import numpy as np

def Gauss_Quad(f,a,b,k):
    return integrate.fixed_quad(f,a,b,n = k)[0]


"""Test"""
f = lambda x: np.sqrt(1.0 + (1.0 / np.cos(x))**4.0)

Ans = Gauss_Quad(f,0.0,(np.pi/4.0),2)
print 1.273910135067533 - Ans