# %%
"""hw1"""
from math import log
C = 1.7
T_c = T_out = 273.15
T_h = T_in = 293.15
# Q1
W_by = C * (T_h * log(T_h / T_c) - T_h + T_c)
print(W_by)

# %% Q2
T_c = 263.15
T_h = 283.15
W_by = C * (T_h * log(T_h / T_c) - T_h + T_c)
print(W_by)

# %%
"""hw2"""
n_A = 1
n_B = 2
V = 1
b = 2e-4
V_A = (n_A * V + n_B * b * n_A) / (n_A + n_B)
print(V_A)

# %%
"""hw3"""
T = 280
V_A = 2
n = 1.2
V_B = 3.5
R = 8.314
W_m = n * R * T * log((V_A + V_B) / V_A)
print(W_m)