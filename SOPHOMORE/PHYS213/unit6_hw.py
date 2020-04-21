# %%
from math import exp
m = 3e-26
T = 300
h = 5e3
g = 9.81
k = 1.38e-23
ratio = exp(-m*g*h/k/T)
print(ratio)