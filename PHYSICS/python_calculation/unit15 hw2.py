import numpy as np 

m = 11.4
R = 0.39
t = 16.3
w = 27
a = w/t
print('a = ', a)
d = 0.5*a*t*t
print('d = ', d)
mi = 0.5*m*R*R
print('mi = ', mi)
E = 0.5*mi*w*w
print('E =', E)
print('tang a =', R*a)
print('speed =',w*R/2)
print('distance =', 2*R*np.sin(69.75/180*np.pi))