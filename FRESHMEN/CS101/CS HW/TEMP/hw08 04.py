# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:39:03 2018

@author: RickyLi
"""

def mc_pi(n):
    import numpy as np
    xy = np.random.random((n,2))*2-1
    d = (xy[:,0]**2+xy[:,1]**2)**0.5 - 1
    d = np.maximum(d,0)
    return 4*(n-np.count_nonzero(d))/n


def mc(n):
    import numpy as np
    xy = np.random.uniform(-1,1,size=(n,2))
    return np.sum(xy[:,1]**2 + xy[:,0]**2 <= 1.0)/n*4

print(mc(1000))