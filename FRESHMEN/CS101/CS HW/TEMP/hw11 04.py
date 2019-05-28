# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:01:31 2018

@author: RickyLi
"""

def find_coins(weight):
    import itertools
    value = {0.125:0,0.25:1,0.5:2,1:3,1.5:4,2:5,4:6,7:7}
    solution = []
    for i in range(1,13):
        for set in list(itertools.combinations_with_replacement (list(value.keys()),i)):
            keys = []
            if sum(set) == weight:
                for v in set:
                    keys.append(value[v])
                solution.append(keys)
    return solution