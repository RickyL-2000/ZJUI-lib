R1 = 44
R5 = R1
R2 = 148
R3 = 118
R4 = 78
V = 12

# Q1
# this problem is wierd, what about R1 and R5?
R23 = R2 + R3
Rab = R23 * R4 / (R23 + R4)
print(Rab)

# Q2
Rac = Rab + R1
print(Rac)

# Q3
I5 = V / (Rac + R5)
print(I5)

# Q4
Vab = V * Rab / (Rac + R5)
I2 = Vab / (R2 + R3)
print(I2)

# Q5
I1 = I5
print(I1)

# Q6
V4 = Vab
print(V4)
