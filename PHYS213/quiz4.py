# %% b
from math import log
n = 0.2
V_i = 0.8e-3
T_i = 300
V_f = 1e-3
R = 8.314

T_f = T_i * V_f**(-2/3) / V_i**(-2/3)
print(T_f)

# %% c
del_U = 1.5 * n * R * (T_i - T_f)
print(del_U)

# %%
del_S = 1.5 * n * R * log(T_i / T_f) - del_U / 300
print(del_S)

