# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:32:02 2019

@author: RickyLi
"""

from scipy.optimize import fsolve

def f(x):
    return x + 2 - 3/x

x = fsolve(f,[-1])

print(x)