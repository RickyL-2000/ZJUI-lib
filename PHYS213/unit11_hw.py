# %%
"""hw3"""
p_i = 4e5
T = 300
NA = 6.022e23
k = 1.38e-23
# Q1
from math import log
p_f = 2e5
del_G = NA * 1 * k * T * log(p_f / p_i)
print(del_G)

# %% Q3
b = 2e-28
V_i = NA * k * T / p_i + NA * b
V_f = NA * k * T / p_f + NA * b
del_S = NA * k * (log(V_f - NA * b) - log(V_i - NA * b))
del_pV = NA * b * (p_f - p_i)
del_G = - T * del_S + del_pV
print(del_G)

# %% Q4
T = 304
p = 4448
