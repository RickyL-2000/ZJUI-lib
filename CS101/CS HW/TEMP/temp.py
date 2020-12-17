# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:46:52 2018

@author: RickyLi
"""

import numpy.random as npr
import timeit
def mc_pi( n ):
    xy = npr.rand( n,2 ) * 2 - 1
    n_circle = 0
    for pair in xy:
        if ( pair[0]**2+pair[1]**2 )**0.5 < 1.0:
            n_circle += 1
    estimate = n_circle / n * 4.0
    return estimate

def series_pi( n ):
    result = 0
    for k in range( 1,n ):
        term = ( ( -1 ) ** ( k+1 ) ) / ( 2 * k - 1 )
        result += term
    return result*4
%timeit  mc_pi( 1e5 )
%timeit  series_pi( int(1e5) )