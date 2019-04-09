from scipy.optimize import fsolve
m1 = 3.5
v1 = 6.3
m2 = 1.7
d = 1.85
g = 9.81

v = (m1*v1 + 0)/(m1+m2)

def f(miu):
    return -miu*(m1+m2)*g*d + 0.5*(m1+m2)*v*v

miu = fsolve(f, 0)

print(miu)