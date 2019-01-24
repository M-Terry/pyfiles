# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:15:50 2019

@author: James
"""

"""Return an approximation to the definite integral of f from a to b
using the trapezoidal rule with n intervals."""
import numpy as np

def Trapezoidal(f, a, b, n):
    h = (b-a) / float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    return s * h