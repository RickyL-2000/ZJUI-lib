# %%
'''hw1'''
# Q1
print(1/2**12)

# %%
# Q2
print(8*9*11/2**12)

# %%
print(11*3*4*7/2**12)

# %%
'''hw2'''
b = 4e-4
print((4*b+2)/6)

# %%
'''hw3'''
m_b = 0.1
m_t = 1
v_i = 5

# Q1
v_f = m_b*v_i/(m_b + m_t)
KE_f = 0.5 * (m_b + m_t) * v_f**2
print(KE_f)

# %%
# Q2
KE_i = 0.5 * m_b * v_i**2
print(KE_i - KE_f)

# %%
# Q3
print((KE_i - KE_f) / 300)

# %%
'''hw4'''
# Q1
h = 0.6
m = 0.5
g = 9.81
U = m*g*h
print(U)

# %%
T = 0.6
c_V = 100 * U / m / 0.6
print(c_V)

# %%
