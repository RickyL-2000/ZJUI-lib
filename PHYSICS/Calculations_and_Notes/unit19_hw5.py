# Note:

import numpy as np 
from scipy.optimize import fsolve

mb = 6.8
ms = 17.9
L = 2.45
theta = 31.1/180*np.pi
g = 9.81

#Q1
def f1(T):
    return ms*g*L*np.cos(theta) + mb*g*L*0.5*np.cos(theta) - T*L*2/3*np.sin(theta)
T = fsolve(f1,[1])
print('T =', T)

#Q2
N1 = T
N2 = mb*g + ms*g 
F_N = (N1*N1 + N2*N2)**0.5
print('F_N =', F_N)

#Q3
T = 1013
def f3(ms):
    return ms*g*L*np.cos(theta) + mb*g*L*0.5*np.cos(theta) - T*L*2/3*np.sin(theta)
ms = fsolve(f3, [1])
print('ms =', ms)
