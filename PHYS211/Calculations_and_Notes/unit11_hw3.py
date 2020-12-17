R1 = R2 = 49
R3 = 118
R4 = 128
C = 57e-6
V = 24

# Q1
I1_0 = V/(R1+R4)
print(I1_0)

# Q2
I1_t = V/(R1+R2+R3+R4)
print(I1_t)

# Q3
Qt = C*(I1_t*(R2+R3))
print(Qt*1e6)

# Q4
R5 = 118
R235 = (R2+R3)*R5/(R2+R3+R5)
I1_0 = V/(R1+R235+R4)
print(I1_0)
