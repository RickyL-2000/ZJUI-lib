b = 0.37
h = 0.54
R = 1.9
T = 1.3
B = 1.9
from math import sin, cos, pi

A = 0.5*b*h
# Q1
omega = 2*pi/T
print(omega)

# Q2
Emax = omega*B*0.5*b*h
Imax = Emax/R
print(Imax)

# Q3
t1 = 0.4875
Phi1 = 0.5*b*h*B*cos(omega*t1)
print(Phi1)

# Q4
I1 = omega*B*A*sin(omega*t1)/R
print(I1)