V = 12
C1 = 3e-6
C2 = 2e-6
C3 = 2e-6
C4 = 1e-6
C5 = 4e-6

# Series:
# C = 1/(1/C1 + 1/C2 + ... + 1/Cn)
# V = V1 + ... + Vn
# Q = Q1 = Q2 = ... = Qn

# Parallel:
# C = C1 + C2 + ... Cn
# V = V1 = ... = Vn
# Q = Q1 + ... + Qn

C34 = 1/(1/C3 + 1/C4)
C2345 = C2 + C34 + C5
C12345 = 1/(1/C1 + 1/C2345)
Q1 = V*C12345
V34 = Q1/C2345
Q34 = C34*V34
V4 = Q34/C4
print(V4)
print(C12345)