from math import pi, sin, cos
H = 0.24
W = 0.79
B = 1.35
I = 0.238
theta = 22/180*pi

# Q1
mu = I*H*W
mux = -mu*sin(theta)
print(mux)

# Q2
muy = mu*cos(theta)
print(muy)

# Q3
tau = -mu*B*sin(theta)
print(tau)

# Q4
Fbc = I*H*B
print(Fbc)
