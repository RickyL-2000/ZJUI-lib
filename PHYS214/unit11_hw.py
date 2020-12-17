# %%
'''hw1'''
from math import e, pi
a0 = 0.053e-9
phi0 = 0.32
delV = 0.01**3

# Q1
print(phi0*phi0 * delV)

# %%
# Q2
delV = (0.01*a0)**3
phi = ((pi*a0**3)**(-0.5)/e)
print(phi**2*delV)

# %%
# Q3
print(0.01**3/pi/e**4)

# %%
'''hw2'''
# Q2
E0 = -13.6
print(E0/9)
print(E0/4)
print(E0)

# %%
'''hw3'''
E = 1.505/4/4*4 + 1.505/4 + 1.505/4*4
E = 1.505/4/4 + 1.505/4 + 1.505/4*4
print(E)

# %%
'''hw4'''
print(e**3/64)

# %%
'''hw5'''
# Q2
print(1/32/pi/e)

# %%
'''hw6'''
# Q3
mu_e = 9.28e-24
B = 0.9
E = -mu_e * B / (1.6e-19)
print(E)

# %%
E = abs(2 * E)
print(E)
lamb = 1240 / E
print(E / (4.14e-15))

# %%
'''quiz'''