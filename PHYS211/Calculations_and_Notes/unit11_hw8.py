from math import sin, cos, pi, atan, tan
q = 1.6e-19
m = 1.67e-27
D = 0.79
vx = 2.4e5
vy = 1.8e5

# Q1
v = (vx * vx + vy * vy) ** 0.5
print(v)

# Q2
theta = atan(vy / vx)
R = D / sin(theta)
print(R)

# Q3
h = R - D / tan(theta)
print(h)

# Q4
# F = qvB
# R = mv/qB
B = -m * v / q / R
print(B)
