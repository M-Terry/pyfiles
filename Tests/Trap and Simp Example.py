# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 21:12:02 2019

@author: James
"""
import numpy as np
import sympy as sy
from Trapezoidal_Tests import Trapezoidal1,Trapezoidal2,Trapezoidal3,Trapezoidal4,Trapezoidal5,Trapezoidal6
from Simpson_Tests import Simpson1,Simpson2,Simpson3
#from pyfiles import trap,simp
x = sy.symbols('x')

func = lambda t: np.exp(-(np.float64(t)**np.float64(2.0)))
a = np.float64(0.0)
b = np.float64(2.0)
n = 3000
Ans1 = (np.float64(2.0)/np.sqrt(np.pi)) * Trapezoidal1(func,a,b,n)
Ans2 = (np.float64(2.0)/np.sqrt(np.pi)) * Trapezoidal2(func,a,b,n)
Ans3 = (np.float64(2.0)/np.sqrt(np.pi)) * Trapezoidal3(func,a,b,n)
Ans4 = (np.float64(2.0)/np.sqrt(np.pi)) * Trapezoidal4(func,a,b,n)
Ans5 = (np.float64(2.0)/np.sqrt(np.pi)) * Trapezoidal5(func,a,b,n)
Ans6 = (np.float64(2.0)/np.sqrt(np.pi)) * Trapezoidal6(func,a,b,n)
print 'Trapezoidal1: ',Ans1
print 'Trapezoidal2: ',Ans2
print 'Trapezoidal3: ',Ans3
print 'Trapezoidal4: ',Ans4
print 'Trapezoidal5: ',Ans5
print 'Trapezoidal6: ',Ans5,'\n'
print 'trap1 comparison: ',0.995322265018953-Ans1
print 'trap2 comparison: ',0.995322265018953-Ans2
print 'trap3 comparison: ',0.995322265018953-Ans3
print 'trap4 comparison: ',0.995322265018953-Ans4
print 'trap5 comparison: ',0.995322265018953-Ans5
print 'trap6 comparison: ',0.995322265018953-Ans6,'\n'

Simp1 = (np.float64(2.0)/np.sqrt(np.pi)) * Simpson1(func,a,b,n)
Simp2 = (np.float64(2.0)/np.sqrt(np.pi)) * Simpson2(func,a,b,n)
Simp3 = (np.float64(2.0)/np.sqrt(np.pi)) * Simpson3(func,a,b,n)
print 'Simpson1: ',Simp1
print 'Simpson2: ',Simp2
print 'Simpson3: ',Simp3,'\n'
print 'Simp1 comparison: ',0.995322265018953-Simp1
print 'Simp2 comparison: ',0.995322265018953-Simp2
print 'Simp3 comparison: ',0.995322265018953-Simp3

"""This section was for testing out Matt Terry's code to check 
for similarities"""
#Ans3 = trap('math.exp(-(x**2.0))',0.0,2.0,1000)
#Ans4 = simp('math.exp(-(x**2.0))',0.0,2.0,1000)
#print 'Other trap: ',Ans3
#print 'Other simp: ',Ans4,'\n'
#print 'other trap comparison: ',0.995322265018953-Ans3
#print 'other simp comparison: ',0.995322265018953-Ans4