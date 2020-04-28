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
