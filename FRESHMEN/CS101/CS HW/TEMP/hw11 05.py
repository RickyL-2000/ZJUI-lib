# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:41:38 2018

@author: RickyLi
"""
import numpy as np
import scipy.optimize
def f_r(x):
    return 20 + x*x - 0.1 * np.cos(2*np.pi*x)
xstar = float(scipy.optimize.minimize(f_r,0).x)
fstar = float(scipy.optimize.minimize(f_r,0).fun)
print(float(scipy.optimize.minimize(f_r,0).x))