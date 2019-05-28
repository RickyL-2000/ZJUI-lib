# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:32:37 2018

@author: RickyLi
"""

import matplotlib.pyplot as plt
import numpy as np
A = np.random.uniform(100,size=(1,1000))
B = np.random.uniform(100,size=(1000,))
plt.plot(A,'bo')
plt.plot(B,'ro')
