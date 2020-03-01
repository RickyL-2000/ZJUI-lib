# %%
lamb_r = 700e-9
lamb_b = 400e-9

# %%
# Q1
from math import sin, pi
theta = pi/3
d = 2*lamb_r/sin(theta)
print(0.01/d)

# %%
# Q6
print(3*lamb_r/d)
# greater than 1, impossible

# %%
# Q8
l1 = 588.995e-9
l2 = 589.592e-9
N = 0.02/d
print(1/2/N-(l2-l1)/l2)

# %%
