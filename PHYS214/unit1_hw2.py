
# %% Q1
# from scipy.optimize import fsolve
from math import sin, cos, pi

# def f(theta):
#     return [(sin(theta)-theta)/sin(theta)-0.05]

# theta0 = [6]
# result = fsolve(f, theta0)
# print(result)

# %% Q2
minval = 999
for theta in range(90, 0, -1):
    if minval > abs(abs(0.5*(theta/180*pi)**2 + cos(theta/180*pi)-1)/abs(cos(theta/180*pi)) - 0.01):
        minval = abs(abs(0.5*(theta/180*pi)**2 + cos(theta/180*pi)-1)/abs(cos(theta/180*pi)) - 0.01)
        angle = theta
print(angle)
# it's 14!!! how to get it?

# %%
print(sin(90))

# %%
