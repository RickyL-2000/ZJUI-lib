# %%
"""hw1"""
T_h = 48 + 273.15
T_c = -16 + 273.15
Q_h = 530
# Q1
e = 1 - T_c / T_h
Q_c = Q_h - e*Q_h
print(Q_c)

# %% Q2
W_by = Q_h - Q_c
print(W_by)


# %% Q3
limit = 1 - T_c / T_h
print(limit)


# %%
"""hw2"""
# Q1
p = 100000
T = 300
V_i = 0.01
V_f = 0.032


# %%
"""hw3"""
T_h = 400 + 273.15
T_c = 30 + 273.15
e_r = 0.25
e_i = 1 - T_c / T_h
print(e_i)
ratio = 1 / (e_i / e_r - 1)
print(ratio)


# %%
T_c = 300
T_h = 340
C_v = 33
