Em = 120
omega = 893
R = 94
L = 70e-3
C = 10.5e-6
from math import sin, cos, pi, atan

# Q1
XL = omega*L
XC = 1/omega/C
Z = (R*R+(XL-XC)**2)**0.5
print(Z)

# Q2
Im = Em/Z
print(Im)

# Q3
phi = atan((XC-XL)/R)
print(phi*180/pi)

# Q4
t1 = (pi-pi/2-phi)/omega
print(t1)

# Q5
VC = Im*XC*cos(phi)
print(VC)