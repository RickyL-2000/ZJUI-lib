V = 12
R1 = R3 = 24
R4 = R5 = 138
R2 = 98
Vb = 11.46

R = R1 + R2 * (R3 + R4 + R5) / (R2 + R3 + R4 + R5)
R2345 = R2 * (R3 + R4 + R5) / (R2 + R3 + R4 + R5)

# Q1
I1 = Vb / (R1 + R2345)
print(1000 * I1)

# Q2
# V * R / (R+r) = Vb
r = V * R / Vb - R
print(r)

# Q3
V2 = Vb - I1 * R1
I3 = V2 / (R3 + R4 + R5)
print(1000 * I3)

# Q4
I2 = V2 / R2
P2 = V2 * I2
print(P2)

# Q5
print(V2)
