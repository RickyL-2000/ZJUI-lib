# %%
'''hw1'''
p = 101300
V_0 = 0.5e-3
T_0 = 303.15
del_T = 10
del_V = V_0 / T_0 * del_T

W = p * del_V
print(-W)

# %%
"""hw2"""
R = 8.314
M_al = 27
M_cu = 63.5
m_al = 200
m_cu = 500
T_al = 76.85 + 273.15
T_cu = 26.85 + 273.15
T_f = (m_al / M_al * T_al + m_cu / M_cu * T_cu) / (m_al / M_al + m_cu / M_cu)
print(T_f - 273.15)


# %%
'''hw3'''
M = 28
p = 2 * 101325
rho = 1.8   # g / L
v = (3 * p / rho)**0.5
print(v)

# %%
"""hw4"""
k = 1.381e-23
N = 1e4
N_n = 2500
N_a = 7500
M_n = 28
M_a = 40
U_t = 5e-17
T = U_t / (2.5 * N_n * k + 1.5 * N_a * k)
print(T)