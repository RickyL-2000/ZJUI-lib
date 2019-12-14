Em = 120
omega = 231
L = 335e-3
Pavg = 72
from math import pi, sin, cos, tan
phi = 59/180*pi

# Q1
Im = 2*Pavg/Em/cos(phi)
print(Im)

# Q2
VR = Em*cos(phi)
R = VR/Im
print(R)

R = Em*cos(phi)/Im

# Q3
# the CPU is bullshit!
C = 1/(Em*sin(phi)/Im + omega*L)/omega
print(C*1e6)
XL = omega*L
Z = Em/Im
C = 1/omega/(XL + (Z*Z - (Em*cos(phi)/Im)**2)**0.5)
print(C*1e6)

C = 1/(omega*(omega*L - ((Em/Im)**2 - R*R)**0.5))
print(C)

# Q5
Im = Em/R
P = 0.5*Im*Em
print(P)