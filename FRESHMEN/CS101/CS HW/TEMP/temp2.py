# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:25:03 2018

@author: RickyLi
"""
import numpy
myarray = numpy.array( [[1,2,3,1],[4,5,6,1],[7,8,9,1]] )
print(myarray[:,1])
print(myarray[:][1])
print(myarray[1,:])
print(myarray[1][:])
print(myarray[0:2,0:2])
print(myarray[:])
print(myarray[1])