# %%
N = 8e3
lamb = 660e-9
w = 2e-2

# %%
# Q1
from math import asin, pi
d = w/N
theta = asin(lamb/d)
print(theta/pi*180)

# %%
# Q2
del_lamb = lamb/2/N
print(del_lamb*1e9)

# %%
lamb_b = 475e-9
lamb_r = 650e-9
D = 2e-3
a_b = 1.22*lamb_b/D
a_r = 1.22*lamb_r/D
d = 3
print(d/a_b)
print(d/a_r)

# %%
