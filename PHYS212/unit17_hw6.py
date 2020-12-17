R1 = R2 = 49
R3 = 118
R4 = 128
L = 413e-3
V = 24

# Q1
I1_0 = V/(R1+R2+R3+R4)
print(I1_0)

# Q2
I1_inf = V/(R1+R4)
print(I1_inf)

# Q3
VL_0 = I1_0*(R2+R3)
print(VL_0)

# Q4
print(I1_inf)