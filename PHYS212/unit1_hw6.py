q = -2e-6
Q = 4e-6
d = 0.12
k = 9e9

from scipy.optimize import fsolve

# k*q/x**2 + k*Q/(d-x)**2 = 0

def f(x):
    return q/x**2 - Q/(d-x)**2

x = fsolve(f, -1)
print(0.12/(2**0.5 + 1))