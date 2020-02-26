# %%
from math import sin, cos, pi

# %%
A1 = A2 = 1
f = 1


# %%
# Q5
phi = 15
A_sum = 2*A1*cos(phi/2/180*pi)
print(A_sum)

# %%
# Q11
A1 = 0.5
A_sum = (A1*A1 + A2*A2 + 2*A1*A2*cos(phi/180*pi))**0.5
print(A_sum)

# %%
