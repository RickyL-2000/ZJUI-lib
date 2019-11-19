I1 = 3.4
d = 0.44
v = 0.18
W = 0.29
from math import pi
mu0 = 4*pi*1e-7

# Q1
E = v*mu0*I1*W/(2*pi*d)
print(E)

# Q2
t1 = 1.6
d = d - t1*v
E = v*mu0*I1*W/(2*pi*d)
print(E)

# Q3
L = 0.44
W = 0.29
v = 0.18
d = 0.44
R = 1.9
I = - v*mu0*I1*W/(2*pi*R) *(1/d - 1/(d+L))
print(I)

# Q5
I2 = 2*pi*R*I/(v*mu0*L*(1/(d+W) - 1/d))
print(I2)