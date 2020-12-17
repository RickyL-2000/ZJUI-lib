C1 = 2.4e-6
C5 = C1
C2 = 3.5e-6
C3 = 7.9e-6
C4 = 2.6e-6
V = 12

# Q1
C23 = 1/(1/C2 + 1/C3)
Cab = C23 + C4
print(Cab)

# Q2
Cac = 1/(1/C1 + 1/Cab)
print(Cac)

# Q3
Ctotal = 1/(1/C5 + 1/Cac)
Qtotal = Ctotal*V
Q5 = Qtotal
print(Q5)

# Q4
Vab = Qtotal / Cab
Qab = C23*Vab
Q2 = Qab
print(Q2)

# Q5
Q1 = Qtotal
print(Q1)

# Q6
V4 = Vab
print(V4)