# %%
'''hw1'''
from math import exp
m = 3e-26
T = 300
h = 5e3
g = 9.81
k = 1.3806e-23
ratio = exp(-m*g*h/k/T)
print(ratio)

# %%
'''hw2'''
# Q1
N = 6.022e23
eps = 2.07e-21
T = 200
U = N * eps / (exp(eps/k/T) + 1)
print(U)

# %% Q2
C = N*eps*eps/k*exp(eps/k/T)/T/T/(exp(eps/k/T) + 1)**2
print(C)

# %% Q3
T = 250
C = N*eps*eps/k*exp(eps/k/T)/T/T/(exp(eps/k/T) + 1)**2
print(C)

# %% Q4
T = 20
C = N*eps*eps/k*exp(eps/k/T)/T/T/(exp(eps/k/T) + 1)**2
print(C)

# %%
'''hw3'''
# Q1
from math import log
f = 1.7e12
h = 6.626e-34
eps = h * f
T = eps / k / log(2)
print(T)

# %% Q2
T  = 0.1*T
P1_over_P0 = exp(-eps/k/T)
print(P1_over_P0)

# %% Q3
P2_over_P1 = exp(-eps/k/T)
print(P2_over_P1)

# %% Q4
E_bar = eps / (exp(eps/k/T) - 1)
print(E_bar/k/T)

# %%
'''hw4'''
# Q1
E = 10.2*1.6022e-19
T = 5900
Z = 1 + 4 * exp(-E / k / T)
P = 3 * exp(-E / k / T) / Z
print(P)

# %% Q2
T = 4300
Z = 1 + 4 * exp(-E / k / T)
P = 3 * exp(-E / k / T) / Z
print(P)
