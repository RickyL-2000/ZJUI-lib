from math import exp
R1 = R2 = 24
R3 = 73
R4 = 158
C = 81e-6
V = 12

# Q1
R23 = R2*R3/(R2+R3)
I4_0 = V/(R1+R23+R4)
print(I4_0)

# Q2
I4_t = V/(R1+R3+R4)
V3 = I4_t*R3
Qt = C*V3
print(Qt*1e6)

# Q3
t = 606e-6
R = R2 + R3
Qt = Qt*exp(-t/R/C)
print(Qt*1e6)

# Q4
Im_closed = I4_0*(R2*R3/(R2+R3))/R2
print(Im_closed)

# Q5
Im_open = -V3/(R2+R3)
print(Im_open)
