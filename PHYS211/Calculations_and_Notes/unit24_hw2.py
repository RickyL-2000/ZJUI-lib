from numpy import pi, sin, cos
import numpy as np 
from scipy.optimize import fsolve
m = 5
v0 = 2
x0 = -0.33
k = 61.2
w = (k/m)**0.5
# x = Dsin(wt + phi)
# v = Dwcos(wt + phi)
# w = (k/m)**0.5

def f(x):  #x[0] = D, x[1] = phi
    return np.array(
        [
            x0 - x[0]*sin(x[1]), 
            v0 - x[0]*w*cos(x[1])
        ]
    )

[D, phi] = fsolve(f, [1,-1])
print(D,phi)

def g(t): 
    return D*sin(w*t + phi)

t = fsolve(g, [0])[0]

print(t)