R1 = 440
L1 = 220e-3
L2 = 122e-3
C = 196e-6
V = 12
from math import cos, pi

# Q1
I1_0 = I2_0 = V/R1
UL1_0 = 0.5*L1*I1_0*I1_0
print(UL1_0)

# Q2
omega = 1/((L1+L2)*C)**0.5
print(omega)

# Q3
# Uc = 0.5*C*V*V
# UL12 = 0.5*(L1+L2)*(V/R1)**2
# Qm = (2*(Uc+UL12)*C)**0.5
# the above is wrong!
Qm = V/R1/omega
print(Qm*1e6)

# Q4
t1 = 3.85e-3
Q_t1 = Qm*cos(omega*t1+pi/2)
print(Q_t1*1e6)

# Q5
T = 2*pi/omega
t2 = T/4
print(t2*1e3)

# Q6
U = 0.5*Qm*Qm/C
print(U)