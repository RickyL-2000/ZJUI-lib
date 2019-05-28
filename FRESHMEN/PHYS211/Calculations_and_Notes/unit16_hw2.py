import numpy as np 

m = 9.35
R = 1.44
F = 305
ag = 32

tq3 = F*np.cos(32/180*np.pi)*R
print(tq3)

I = 0.5*m*R*R 
alpha = 66.737/I
print(alpha)

t = 1.6
w = alpha*t
E = 0.5*I*w*w
print(E) 