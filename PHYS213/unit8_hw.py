# %%
"""hw1"""
T_h = 48 + 273.15
T_c = -16 + 273.15
# Q1
W_on = 900
Q_h = W_on / (1 - T_c / T_h)
Q_c = Q_h - W_on
print(Q_c)

# %% Q2
print(Q_h)

# %% Q3
K = Q_c / W_on
print(K)

# %%
"""hw2"""
b = 5e-29
n = 3
T = 300
V = 0.001
R = 8.314
N_A = 6.022e23
# Q1
p_i = n * k * T / (V - n*N_A*b)
print(p_i)

# %% Q2
V_f = 0.002
p_f = n * R * T / (V_f - n*N_A*b)
print(p_f)

# %% Q3
from math import log
N = n * N_A
W = n*R*T*log((V_f - N*b)/(V - N*b))
print(log((V_f - N*b)/(V - N*b)))
print(N*k*T)
print(W)

# %%
"""hw3"""
m = 96  # g
p = 101325
T = 373.15
M = 18
C = 2260
# Q1
Q = C * m
print(Q)

# %% Q2
V_f = m / M * R * T / p
W = p * V_f
print(W)

# %% Q3
del_U = Q - W
print(del_U)

# %%
"""hw4"""
from math import log
V_i = 1e-3
M = 0.04
p = 1e4
T = 22 + 273.15
k = 1.38e-23
# Q1
N_over_V = p / k / T
print(N_over_V)

# %% Q2
print(T)

# %% Q3
N = N_over_V * V_i
V_f = 3e-3
p_f = N * k * T / V_f
print(p_f)

# %% Q4
W_by = N * k * T * log(V_f / V_i)
print(W_by)
