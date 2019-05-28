from numpy import pi, sin, cos
from scipy.optimize import fsolve
m = 7.4
x = 0.23
v = 3.9
g = 9.81

# mg = kx
k = m*g/x
print('k =', k)

w = (k/m)**0.5
f = w/pi/2
print('f =', f)

T = 1/f
print(T)
# positive down
# x(t) = -Asin(wt)
# v(t) = -wAcos(wt)
# a(t) = wwAsin(wt)
# mgA - 0.5*k*((A+x)**2 - x*x) = -0.5*m*v*v

def F(A):
    return m*g*A - 0.5*k*((A+x)**2 - x*x) + 0.5*m*v*v
A = fsolve(F, [1])
print(A)

vt = -w*A*cos(w*0.42)
print('vt =', vt)

a_m = w*w*A
print('a_m =', a_m)

at = w*w*A*sin(w*0.42)
Fnet = m*at
print('Fnet =', Fnet)