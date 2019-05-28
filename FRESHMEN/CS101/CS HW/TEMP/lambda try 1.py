# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:44:43 2018

@author: RickyLi
"""

def sortDictAsList( d ):
    items = list( d.items() )
    items.sort( key=lambda x:x[1] )
    return items
d = { 'a':2, 'b':1, 'c':-1, 'd':14 }
print(sortDictAsList( d ))