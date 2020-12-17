# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:24:31 2018

@author: RickyLi
"""

def method1(N,K):    #first multipy all the 2s, then plus 1s. 
    for n in range(0,K):
        if 
    if K%(2**n) == 0:
        return n
    elif K%(2**n) <= (2**(n+1) - 2**n)/2:
        return n + K%(2**n)
    else:
        return n+1 + (2**(n+1) - 2**n)/2 - K%(2**n)-1
print(method1(2,16))