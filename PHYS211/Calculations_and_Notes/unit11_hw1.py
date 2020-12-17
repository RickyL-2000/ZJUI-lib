R = 4.8
V = 5

# Q1
I = V / R
print(I)

# Q2
# C = Q/V
Q = 19.5e-6
C = Q/V
print(C*1e6)

# Q3
C = 7.2e-6
R1 = 3
R2 = 5.5
R3 = 1.5
I = 0.38

V = I*R1    # ?
print(V)

# Q4
I = V/(R1+R2+R3)
print(I)

# Q5
V23 = I*R2 + I*R3
Q = C*V23
print(Q)
