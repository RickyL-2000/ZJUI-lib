# %%
'''hw1'''
from math import factorial
# Q1
print(factorial(5)/factorial(3)/factorial(2))

# %%
# Q2
U = 5
N = 3
total = factorial(U+N-1)/factorial(N-1)/factorial(U)
print(total)

# %%
# Q3
num = factorial(U+N-2)/factorial(N-2)/factorial(U)
p = num / total
print(p)

# %%
# Q4
num = 2
print(num / total)

# %%
'''hw2'''
from math import exp
# Q2
k = 1.38e-23
epsl = 1e-20
T = 320
ratio = exp(-2*epsl/k/T)
print(ratio)

# %%
'''hw3'''
r = exp(-2)
p_B = 2*r / (1 + 2*r + 3*r*r)
print(p_B)

# %%
'''hw4'''
mu = 9.3e-24
# Q1
ratio = 0.62 / (1 - 0.62)
print(ratio)

# %%
# Q2
from math import log
T = 273.15 + 24
del_E = k*T*log(ratio)
print(del_E)

# %%
B = del_E / 2 / mu
print(B)

# %%
'''hw5'''
# Q1
T = 300
E1 = 0.1 * 1.6e-19
n1 = exp(-E1/k/T)
# print(-0.1/k/T)
# print(n1)
print(2*n1 / (2*n1 + 1))

# %% Q3
T = -E1 / k / log(0.5)
print(T)