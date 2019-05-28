# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:55:08 2018

@author: RickyLi
"""
import numpy as np
def factors( n ):
    fs = []
    n = int(n)    
    for i in range(2,n):
        if n % i == 0.0:
            fs.append(i)
            #print(i)
    return fs
        

def fraction( n ):
    n_str = str( n )
    decimal_part = n_str[ n_str.find( '.' )+1: ]
    # 1. Multiply by ten repeatedly.
    numer = n * 10 ** len(decimal_part)
    denom = float(10 ** len(decimal_part))

    # 2. Find factors.
    numer_factors = factors(numer)
    denom_factors = factors(denom)
    max = []
    # factor = 1
    for f in numer_factors:# ??? find greatest common factor of both numerator and denominator
        if f in denom_factors:
            max.append(f)
    f = np.max(max)                
    numer = numer/f
    denom = denom/f
    #denom_factors.remove(f)# ??? divide both by GCF before returning them
    return ( numer,denom )

print(fraction(88))