C1 = 4e-6
C2 = 5.5e-6
C3 = 3e-6
C4 = 3.5e-5

# Q1
C23 = C2+C3
print(C23)

# Q2
V23 = 7.6
Q23 = C23*V23
print(Q23)

# Q3
V2 = V23
print(V2)

# Q4
C = 1/(1/C1 + 1/C23 + 1/C4)
Q1 = Q23
print(Q1)