R1 = 120
R2 = 330
R3 = 240
L = 1.6e-3
V = 9
from math import log

V0 = V*R2/(R1+R2)
R = R3 + R1*R2/(R1+R2)
t0 = -L/R*log(0.37)
print(t0)