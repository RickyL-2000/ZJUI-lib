lam = 0.3
I = 45
c = 3e8
from math import pi, cos
mu0 = 4*pi*1e-7

B0 = (2*I*mu0/c)**0.5
omega = 2*pi*c/lam
t = 1.5e-9

B = B0*cos(-omega*t)
print(B)