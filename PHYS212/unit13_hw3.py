from math import pi, cos
B = 1.8
d = 0.2
N = 12
I = 0.85
g = 9.81

theta = pi/6
mu = N*I*d*d
tau = mu*B*cos(theta)
# tau = r x F = d/2 * Mg * cos(theta)
M = tau / (d/2) / g / cos(theta)
print(M)