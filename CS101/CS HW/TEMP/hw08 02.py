# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:55:59 2018

@author: RickyLi
"""

def midpointint(f,a,b,n):
    import numpy as np
    h = (b-a)/n
    df = np.zeros((n,))
    for i in range(0,int(n)):
        df[i] = f(a - 0.5*h + (i+1)*h)
    return h * np.sum(df)

def y(x):
    return 2*x
print(midpointint(y,2,4,1))
