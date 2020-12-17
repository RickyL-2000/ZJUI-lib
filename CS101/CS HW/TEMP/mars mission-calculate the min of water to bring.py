# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:30:11 2018

@author: RickyLi
"""
waters = []
for day in range(10,150):
    waters.append((day,16*day*0.925**(-730/day)))
waters.sort(key = lambda x:x[1])
print(waters[0])

