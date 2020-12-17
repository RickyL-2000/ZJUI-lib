# %%
'''hw1'''
# Q1
Ti = 15 + 273.15
Vi = 0.0042
Vf = 1.08 * Vi
Tf = Ti * Vf / Vi
print(Tf - 273.15)

# %%
# Q2
p = 101.3e3
Wby = p * (Vf - Vi)
print(Wby)

# %%
'''hw2'''
# Q1
n_i = 2.5
T_i = 310
V_i = 0.5
k = 8.31
p = n_i * k * T_i / V_i
print(p)

# %%
# Q2
p_2 = 15464.04
V_f = n_i * k * T_i / p_2
print(V_f)

# %%
# Q3
from math import log
W_on = -n_i * k * T_i * log(V_f / V_i)
print(W_on)

# %%
'''hw3'''
# Q1
b = 8e-4
n = 30.2
V = 1
p = 101300
T = p*(V - n*b) / n / k
print(T)


# %%
# Q2
b = 8e-4
n = 1.5
p = 101300
T = 350
V = (n*k*T + p*n*b) / p
print(V)

# %%
