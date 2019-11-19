R1 = R2 = 54
R3 = 66
R4 = 108
L = 245e-3
V = 12
from math import exp

# Q1
I4_0 = V/(R1+R3+R4)
print(I4_0)

# Q2
R23 = R2*R3/(R2+R3)
I4_inf = V/(R1+R23+R4)
print(I4_inf)

# Q3
IL_inf = V*R23/(R1+R23+R4)/R2
print(IL_inf)

# Q4
I0 = IL_inf
R = R2+R3
t = 5.9e-3
I = I0*exp(-R*t/L)
print(I)    # the direction is inversed

# Q5
IL_max_closed = V*R3/(R1+R3+R4)
print(IL_max_closed)

# Q6
IL_max_open = I0*(R2+R3)
print(IL_max_open)