from numpy import pi
m = 6.4
R = 0.39
r = 1.29
f = 18.7
w = f*2*pi
g = 9.81

# Omega = tau/L
tau = m*g*r
L = 0.5*m*R*R*w
print('L =', L)
print('tau =', tau)

Omega = tau/L
T = 2*pi/Omega
print('T =', T)