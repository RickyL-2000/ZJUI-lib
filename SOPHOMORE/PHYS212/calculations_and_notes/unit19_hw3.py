C1 = 526e-6
C2 = 95e-6
L = 296e-3
IL0 = 138e-3
from math import cos, pi

# Q1
C = C1*C2/(C1+C2)
omega0 = 1/(L*C)**0.5
print(omega0)

# Q2
t1 = 17.9e-3
Qm = IL0/omega0
Q1_t1 = Qm*cos(omega0*t1+pi/2)
print(Q1_t1)

# Q3
Vbc = Qm*cos(omega0*t1+pi/2)/C
print(Vbc)

# Q4
print(Qm)