from numpy import pi, sin, cos
mu = 0.148
# y(x,t) = 0.17sin(2.3x + 17.1t)
# f = w/2pi
# lam = 2pi/k
# v = f*lam
# T/mu = w^2/k^2
k = 2.3
w = 17.1
A = 0.17
P = 2*pi/w
# Q5
T = mu*w*w/k/k
print('T =', T)

# v(x,t) = A*w*cos(kx + wt)
v = A*w*cos(k*3.2+w*0.44)
print('v =', v)

# a(x,t) = -A*w*wsin(kx + wt)
a = -A*w*w*sin(k*3.2 + w*0.44)
print('a =', a)

v_a = 4*A/P
print('v_a =', v_a)