from numpy import sin, pi
f = 40
A = 0.25
mu = 0.02
T = 20.48

# y(x,t) = Asin(kx-vt)
# 0 = A*sin(0)
v = (T/mu)**0.5
# v = lam*f
lam = v/f
k = 2*pi/lam
y = A*sin(k*0.5-v*0)
print('y =', y)