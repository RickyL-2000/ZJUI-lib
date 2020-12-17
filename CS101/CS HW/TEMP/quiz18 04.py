# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:19:46 2018

@author: RickyLi
"""
import math
def dfdx( f,x,h=1e-3 ):
    return ( f( x+h ) - f( x ) ) / h

def newton( f,x0,tol=1e-3 ):
    d = abs( 0 - f( x0 ) )
    while d > tol:
        x0 = x0 - f( x0 ) / dfdx( f,x0 )
        d = abs( 0 - f( x0 ) )
    return ( x0,f( x0 ) )
def f(x): 
    return x*x*x - 3*x + math.cos(x) + 2
print(newton(f,0))