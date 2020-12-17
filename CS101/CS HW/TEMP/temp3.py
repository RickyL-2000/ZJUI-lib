# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:03:50 2018

@author: RickyLi
"""
import numpy
mysquare = numpy.array([[1,4,3],[2,5,6],[7,8,9]])
print(mysquare.T)
print(mysquare.tolist())
mysquare.sort()
print(mysquare)
T = mysquare.T
print(T)
print(numpy.linspace( 0,10,101 ))
t = mysquare.tolist()
print(t)