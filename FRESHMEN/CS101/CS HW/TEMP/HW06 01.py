# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:47:34 2018

@author: RickyLi
"""

def polyeval(coefs,x):
    value = 0
    for coef in coefs:
        value = value + coef * (x ** (coefs.index(coef)))
    return value

print(polyeval( [ 0,1,0,-2,1 ],-1 ))