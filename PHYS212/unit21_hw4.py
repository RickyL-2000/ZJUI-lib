from math import sin, cos, pi
lam = 655e-9
B1 = 11.8e-6

# Q1
k = 2*pi/lam
print(k)

# Q2
z_max = pi/2/k
print(z_max*1e9)

# Q3
c = 3e8
E_max = 2**0.5*B1*c
print(E_max)

# Q4
Ey = E_max*2**0.5/2
print(Ey)

# Q5
omega = c*k
t_max = pi/2/omega
print(t_max)