import numpy as np 

m = 11.4
R = 0.39
t = 16.3
w = 27
alpha = w/t
print('alpha = ', alpha)
d = 0.5*alpha*t*t
print('d = ', d)
mi = 0.5*m*R*R
print('mi = ', mi)
E = 0.5*mi*w*w
print('E =', E)
print('tang a =', R*alpha)
print('radial a =', w*w*R/4)
print('speed =',w*R/2)
print('distance =', 2*np.pi*R*d/2/np.pi)