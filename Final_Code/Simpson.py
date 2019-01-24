# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:27:10 2019

@author: James
"""

# find integral of f using composite Simpson rule
# n must be even
# the input for func must be a function, an example is provided below:
#f = lambda x: np.sqrt(1 + 4.0*(x**2))
import numpy as np
from scipy import integrate
 
def Simpson(f,a,b,n):
    x = np.linspace(a, b, n + 1)
    return integrate.simps(f(x), x)