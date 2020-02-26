# %%
from math import pi, sin, cos

# %%
lamb = 475e-9
x1 = 0.7
x2 = 1.5
I0 = 0.5
y1 = 2e-3
y2 = 1e-3


# %%
# Q1
p1 = (y1*y1 + x2*x2)**0.5 + (y1*y1 + x1**2)**0.5
p2 = (y2*y2 + x2*x2)**0.5 + (y2**2 + x1**2)**0.5
phi = 2*pi*(p1-p2)/lamb
del_p = p1-p2
## p1 比 p2 滞后 phi
phi = phi % (2*pi)
A = I0**0.5
A_1 = 2*A*cos(phi/2)
I = A_1**2
print(I)


# %%
# Q2
"""the same"""


# %%
# Q3
print(2*del_p*1e9/13)

# %%
# Q4
print(phi/2/pi)

# %%
