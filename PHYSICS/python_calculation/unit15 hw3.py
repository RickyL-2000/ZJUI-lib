import numpy as np 

m = 18
R = 0.7
w = 33*2*np.pi 
t = 9.8

mi = 0.5*m*R*R
print('mi =', mi)

a_ag = w/t 
print('a_ag =', a_ag)

ag = w*w/2/a_ag
print('ag =', ag)

W0 = 0.5*mi*w*w 
print('W0 =', W0)

