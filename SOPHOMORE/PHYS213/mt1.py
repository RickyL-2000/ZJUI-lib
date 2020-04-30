# %% Q1
print(4.9 * 3 / 2)


# %% Q3
V = 1e-3
n = 4
T = 20 + 273.15
R = 8.314
p = n * R * T / V
print(p / 101325)

# %% Q4
Q = 2.5 * 1 * R * 10 + 1.5 * 3 * R * 10
print(Q)

# %% Q5
alpha = 3e-4
del_T = 100
Q = alpha / 4 * del_T**4
print(Q)

# %% Q7
V = 0.1
p_i = 2 * 101325
T_i = 300
Q = 2.5 * p_i * V / T_i * 4
print(Q)

# %% Q8
N = 2.4e24
T = 250
p = 1.5 * 101325
k = 1.38e-23
V_i = N * k * T / p
print(V_i * 1000)

# %% Q9
from math import log
print(log(3))

# %% Q10
m = 3000
M = 207.2
Q = 3 * m / M * R * 1
print(Q)

# %% Q11
print(2 / (4 / 5 + 1))

# %% 12
T0 = 273.15
del_S_1 = log((75 + T0)/(50 + T0)) + log((75 + T0)/(100 + T0))
print(del_S_1)
del_S_2 = log((30 + T0)/(50 + T0)) + log((30 + T0)/(10 + T0))
print(del_S_2)

# %% 13
V = 0.5e-3
m = 400
T = 300
M = 187
p = m * R * T / M / V
print(p / 101325)

# %% Q14
m = 1000
T_i = 300
del_h = 1.5
M = 27
g = 9.8
Q = 1 * g * del_h
del_T = Q / 3 / (m / M) / R
print(del_T)

# %% Q15
from math import exp
E = 1.01e-20
T = 245
ratio = exp(-3 * E / k / T)
print(ratio)

# %% Q17
print(k * log(4))

# %% 21
m = 4.65e-26
h = 500
T = 300
p_b = 1.2e5
g = 9.8
print(-m * g * h / k / T)
print(exp(-m * g * h / k / T) * p_b)

