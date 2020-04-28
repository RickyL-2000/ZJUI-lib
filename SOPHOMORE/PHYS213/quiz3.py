# %%
# a
from math import exp
k = 1.38e23
E_2 = 2e-22
E_1 = 1.5e-22
E_0 = 0
T = 300
z = exp(-E_2/k/T) + exp(-E_1/k/T) + 1
E_avr = exp(-E_2/k/T) * E_2 / z + exp(-E_1/k/T) * E_1 / z
print(z)
print(E_avr)

# %% d
from math import log
T = 5 / 1.38 / log(2)
print(T)