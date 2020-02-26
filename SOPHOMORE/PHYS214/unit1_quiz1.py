# %%
from math import sin, cos, pi

# %%
v = 330
f = 125
I = 6

# %%
# Q1
lamb = v/f
phi = (2*2**0.5 - 2)*2*pi/lamb
print(phi)

# %%
# Q2
print((6**0.5 + 6**0.5)**2)


# %%
phi = 2.4
A = I**0.5
A_ = 2*A*cos(phi/2)
I_ = A_**2
print(I_)

# %%
