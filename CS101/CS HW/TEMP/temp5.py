# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 10:39:55 2018

@author: RickyLi
"""
import matplotlib.pyplot as plt
import numpy as np
t = np.array(np.linspace(0,4500,5001),dtype=np.float64) #t/s
dt = 4500/5000
y = np.array(np.zeros((5001,)),dtype=np.float64)
v = np.array(np.zeros((5001,)),dtype=np.float64)
y[0] = 250000.0     #h/m
v[0] = 0.0      #v/m/s
g = -8.87                  #up+
bounces = 0
for i in range(1,5001):
    if y[i-1] + v[i-1]*dt + 0.5*g*dt*dt > 0:
        v[i] = v[i-1] + g*dt
        y[i] = y[i-1] + v[i-1]*dt + 0.5*g*dt*dt
    else:
        y[i] = 0
        v[i] = -0.9*(v[i-1] + g*dt)
        bounces += 1
plt.plot(t,y,'k-')
plt.xlabel('time')
plt.ylabel('height')
plt.xlim(0,5001)
plt.ylim(0,250000.0)
plt.plot(t,v,'k-')
plt.xlabel('time')
plt.ylabel('velocity')
plt.xlim(0,5001)
print(bounces)