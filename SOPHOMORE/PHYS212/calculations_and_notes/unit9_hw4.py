V = 12
R1 = 49
R2 = 158
R3 = 108
R4 = 128
# Rx
I4 = 0

# Q1
I1 = V / (R1 + R3)
print(I1)

# Q2
# R1/R2 = R3/Rx
Rx = R3 * R2 / R1
I2 = V / (R2 + Rx)
V2 = I2 * R2
print(V2)

# Q3
print(I2)

# Q4
print(Rx)

# Q5
V1 = I1 * R1
print(V1)