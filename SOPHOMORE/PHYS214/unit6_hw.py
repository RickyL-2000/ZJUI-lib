# %%
from math import sin, cos, tan, acos, asin, atan, pi
amu = 1.66e-27
c = 3e8
q_e = 1.6022e-19
eV = q_e
m_e = 5.11e5

# %%
"""hw1"""

# %%
E = 1.8488*eV
v = E/7/amu/c
t = 1e-3/v
print(t)

# %%
"""hw2"""
h = 4.14e-15 # eV

# %%
lamb = 200
phi = 4.08

E = 1240/lamb - phi
pc = (2*5.11e5*E)**0.5
print(1240/pc)

# %%
"""hw3"""
phi = 2.5
P = 1.1e-6
lamb = 240

# %%
# Q1
print(1240/lamb - phi)

# %%
# Q2
N = (P*lamb*1e-9/1.986e-25)
print(N)


# %%
# Q3
I_max = q_e*N
print(I_max)

# %%
# Q4
f_c = phi/4.14e-15
print(f_c)

# %%
"""hw4"""
E_e = 28e3

# %%
# Q1
print(E_e * eV)

# %%
# Q2
lamb = 1240/E_e
print(lamb)

# %%
f = c*1e9/lamb
print(f)

# %%
"""hw5"""
E = 0.035       # eV
m = 1.675e-27   # kg
mc2 = 939.6e6   # MeV

# %%
# Q1
# m_ = mc2 / (c*1e9)**2
pc = (2*mc2*E)**0.5
lamb = 1240/pc
print(lamb)

# %%
# Q3
E = 1240/lamb
print(E*1e-3)

# %%
# Q4
p_x_c = 1240/lamb
print(p_x_c/pc)

# %%
"""hw6"""
P = 100
lamb = 510

# %%
E = 1240/lamb
print(E)

# %%
# Q2
D = 3
n = 0.025*P/E/eV
N = n*1e-4/(4/3*pi*D**3)
print(N)

# %%
# Q3
lamb = 765
E = 1240/lamb
D = 3
n = 0.025*P/E/eV
N = n*1e-4/(4/3*pi*D**3)
print(N)

# %%
"""quiz"""
E = 25e3

# %%
# Q1
lamb = 1240/(2*5.11e5*E)**0.5
print(lamb)

# %%
# Q3
lamb_gamma = 1240/E
print(lamb_gamma)

# %%
# Q4