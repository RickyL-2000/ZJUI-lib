L = 24e-3
C = 40e-6
f = 310
E = 120
Im = 1.4
from math import sin, cos, pi, asin

omega = 2*pi*f
XL = omega*L
XC = 1/omega/C

print(XL, XC)

phi = asin((XL-XC)*Im/E)
print(phi*180/pi)