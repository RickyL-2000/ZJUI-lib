a = 0.02
I1 = 1.2
b = 0.04
c = 0.06
I2 = 2.4
from math import pi
mu0 = 4*pi*1e-7
r = 0.05

B1 = mu0*I1/(2*pi*r)
B2 = mu0*I2/(2*pi*r) * (r*r-b*b)/(c*c-b*b)

B = B1 - B2

Bx = -B/2
print(Bx)