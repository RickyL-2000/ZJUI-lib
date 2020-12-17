from math import pi
mu0 = 4*pi*1e-7

# Q5
n1 = 1600
I1 = 3.4
n2 = 1300
I2 = 2.5
B1 = 0.5*mu0*n1*I1
B2 = 0.5*mu0*n2*I2

B = B1+B2
print(B)