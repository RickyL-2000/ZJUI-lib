A = 0.2207
Vb = 6
d = 0.55e-2
epsl = 8.85e-12

# Q1
C = epsl*A/d
print(C)

# Q2
Q = C*Vb
print(Q)

# Q3
kap = 2.9
C1 = epsl*A/(0.5*d)
C2 = epsl*A*kap/(0.5*d)
Q = Vb*C1*C2/(C1+C2)
print(Q)

# Q4
# U = 0.5*Q*V
U = 0.5*Q*Vb
print(U)

# Q5
C = epsl*A/d
V = Q/C
print(V)