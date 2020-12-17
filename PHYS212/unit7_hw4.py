A = 3704e-4 # m^2
Vb = 6
d = 0.59e-2
epsl = 8.85e-12

# Q1
C = epsl*A/d
Q = C*Vb
print(Q)

# Q2
U = 0.5*Q*Vb
print(U)

# Q3
d = 2*d
C = epsl*A/d
V = Q/C
U = 0.5*Q*V
print(U)

# Q4
E = V/d
print(E)

# Q5
print(V, Vb)
