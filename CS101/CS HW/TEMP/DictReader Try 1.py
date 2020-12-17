# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:44:43 2018

@author: RickyLi
"""

from csv import DictReader
reader = DictReader(open('C:\\Users\\RickyLi\\Desktop\\autos.csv'))
print(list(reader))