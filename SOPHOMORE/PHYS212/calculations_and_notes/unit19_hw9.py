Em = 120
omega = 740
R = 72
C = 593e-6
from math import pi, sin, cos, tan
phi = 44/180*pi

# Q1
t1 = phi/omega
print(t1)

# Q2
Z = R/cos(phi)
print(Z)

# Q3
XL_minus_XC = R*tan(phi)
XC = 1/omega/C
L = (XL_minus_XC + XC)/omega
print(L*1e3)

# Q4
Im = Em/Z
XL = omega*L
VLm = Im*XL
print(VLm)

# Q5
VL = VLm*cos(phi)
print(VL)