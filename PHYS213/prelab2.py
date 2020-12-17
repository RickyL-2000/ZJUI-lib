# %% Q1
M_cu = 63.6
M_al = 27
C_al = 900

# %% Q2
del_T = 10 * 60 / (C_al * 0.025**3 * 2700)
T_i = 20 + 273.15
print(del_T)
print(T_i + del_T - 273.15)

# %% 3.a
from math import pi
T_h = 0.2 / pi / (2e-3)**2 / 235 + 20
print(T_h)

# %% 3.b
T_h = 0.2 / pi / (2e-3)**2 / 401 + 20
print(T_h)

# %% 3.c
k_cu = 401
k_al = 235
r = 2e-3
l = 0.2
T_j = k_al * 50 / (k_al + k_cu)
print(T_j)
H = k_cu * T_j / l * pi * r**2
print(H)
