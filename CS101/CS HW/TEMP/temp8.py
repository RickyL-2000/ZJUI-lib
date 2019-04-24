# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:09:59 2018

@author: RickyLi
"""
import numpy as np
def mc_pi(n):
    xy = np.random.random((n,2))*2-1
    d = (xy[:,0]**2 + xy[:,1]**2)**0.5 - 1
    d = np.maximum(d,0)
    return d
print(mc_pi(10))