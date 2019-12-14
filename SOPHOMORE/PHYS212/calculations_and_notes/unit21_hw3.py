Em = 24
omega = 185
Im = 0.98
C = 122e-6
from math import sin, cos, pi, tan

# Q1
R = Em / Im
L = 1/omega**2/C
print(L*1e3)

# Q2
VC = Im/omega/C
Umax_C = 0.5*C*VC*VC
print(Umax_C)

# Q3
T = 2*pi/omega
P = 0.5*Im*Em
del_U = T*P
print(del_U)

# Q4
Q = (L/R/R/C)**0.5
print(Q)

# Q5
print(R)

# Q6
