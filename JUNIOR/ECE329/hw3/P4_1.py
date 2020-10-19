# %%
from scipy import integrate
import numpy as np
# from math import cos, sin, pi
from numpy import cos, sin, pi

# %%
def f_x(theta, x, y):
    return (x - cos(theta)) / ((x - cos(theta))**2 + (y - sin(theta))**2)**(3/2)

def f_y(theta, x, y):
    return (y - sin(theta)) / ((x - cos(theta))**2 + (y - sin(theta))**2)**(3/2)

# %%
h = 0.01
x = np.linspace(-5, 5, int(5/h) + 1)
y = np.linspace(-5, 5, int(5/h) + 1)
E_x = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
E_y = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
for i in range(int(5/h)+1):
    for j in range(int(5/h)+1):
        ff_x = lambda theta: f_x(theta, x[i], y[j])
        ff_y = lambda theta: f_y(theta, x[i], y[j])
        E_x[i, j] = integrate.quad(ff_x, 0, 2*pi)[0]
        E_y[i, j] = integrate.quad(ff_y, 0, 2*pi)[0]

# %%
h = 0.1
x = np.linspace(-5, 5, int(5/h) + 1)
y = np.linspace(-5, 5, int(5/h) + 1)
P_x = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
P_y = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
for i in range(int(5/h)+1):
    for j in range(int(5/h)+1):
        print("i = {}, j = {}".format(i, j))
        P_x = integrate.tplquad(
            f_x, 
            0, 
            2*pi, 
            lambda u: 0,
            lambda u: x[i],
            lambda u,v: 0,
            lambda u,v: y[j]
        )