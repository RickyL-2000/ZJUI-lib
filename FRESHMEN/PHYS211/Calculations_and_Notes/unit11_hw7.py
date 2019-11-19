from math import sin, cos
m = 4.9e-8
B = 3.9
R = 0.92
T = 577e-6 * 4
pi = 3.1415926535

# Q1
# R = mv/qB
# qvB = m 4pi^2 * R / T^2 = m v^2 / R
# v^2 / R = 4pi^2 * R / T^2
v = (4 * pi * pi * R / T / T * R) ** 0.5
print(v)

# Q2
# careful!!!! there is a negative sign!!!
t1 = 192.2e-6
F = m * v * v / R
theta = t1 / T * 4 * pi / 2
Fx = -F * cos(theta)
print(Fx)

# Q3
Fy = -F * sin(theta)
print(Fy)

# Q4
# F = qvB
q = -F / v / B
print(q*1e6)

# Q5
# R = mv/qB
