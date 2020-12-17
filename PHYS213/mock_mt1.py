# %%
"""Ex2"""
m = 0.5
T_i = 273.15
C_l = 333500
C_v = 4184
# Q1
del_S = C_l * m / T_i
print(del_S)

# %%
from math import log
T_f = T_i + 20
del_S = C_v * m * log(T_f / T_i)
print(del_S)

# %% Q3
Q = C_l * m + C_v * m * (T_f - T_i)
print(Q)

# %%
"""Ex3"""
V = 3e2
n_o = 1000
n_h = 9e3
T_i = 20 + 273.15
R = 8.314
# Q1
p = (n_h + n_o) * R * T_i / V
print(p / 101325)

# %% Q2
T_f = 30 + 273.15
Q = 2.5 * n_o * R * (T_f - T_i) + 1.5 * n_h * R * (T_f - T_i)
print(Q)

# %%
"""Ex4"""
from math import exp
h = 1000
m_0 = 4.65e-26
g = 9.8
k = 1.38e-23
# Q1
T = 250
r = exp(-m_0 * g * 0.5 * h / k / T)
print(r)

# %%
"""Ex5"""
E = 1.6e-21
T = 250
z = 1 + 2 * exp(-E / k / T)
U = 2 * exp(-E/k/T)/z * E
print(U)

# %%
"""Ex6"""
n = 3
T = 290
V_i = 2
V_f = 1
W_on = n * R * T * log(V_i / V_f)
print(W_on)

# %%
"""Ex7"""
V = 2
N_h = 3e23
N_n = 6e23
M_h = 4
M_n = 28
ratio = (M_n / M_h)**0.5
print(ratio)

# %%
"""Ex8"""
m = 500
M = 107
Q = 300
n = m / M
del_T = Q / (6 / 2 * n * R)
print(del_T)

# %%
"""Ex9"""
a = 0.3
