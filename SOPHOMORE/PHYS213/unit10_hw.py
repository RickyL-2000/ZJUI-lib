# %%
"""hw1"""
from math import log, exp
T_1 = 283
C_1 = 9e-4
T_2 = 293
k = 1.381e-23
delta = 2.208e-20
p = C_1 / exp(-delta / k / T_1)
C_2 = p * exp(-delta / k / T_2)
print(C_2)

# %%
"""hw2"""
n = 20
NA = 6.022e23
N = n * NA
T = 300
V_i = 0.01
V_f = 0.02
# Q1
b = 1e-28
delta_mu = T * ((k * log(V_i - b * N) - N*k*b/(V_i - b*N)) - (k * log(V_f - b * N) - N*k*b/(V_f - b*N)))
print(delta_mu)

# %% Q2
delta_mu = T * k * log(V_i / V_f)
print(delta_mu)

# %% Q3
a = 9e-50
# k = 1.38e-23
delta_mu = 2*a*N/V_i + T*(k*log(V_i-b*N) - N*k*b/(V_i-b*N)) - 2*a*N/V_f - T*(k*log(V_f-b*N) - N*k*b/(V_f-b*N))
print(delta_mu)

# %%
"""hw3"""
k = 1.38e-23
delta = 1.424 * 1.602e-19   # eV
N = 1e20
T = 280.15
ratio = exp(-delta / 2 / k / T)
print(-delta / k / T)
print(ratio)
print(ratio * N)

# %% Q2
print(N - ratio*N)

