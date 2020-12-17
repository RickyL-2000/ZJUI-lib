a = 4.4e-2
b = 7.3e-2
I2 = 5.3
I1 = 3.7
from math import pi
mu0 = 4*pi*1e-7

# Q1
d = 0.27
ByP = mu0*(I2-I1)/(2*pi*d)
print(ByP)

# Q2
integral = mu0*(I2-I1)/8
print(integral)

# Q3
rT = 5.2e-2
B1 = mu0*I1/(2*pi*rT)
B2 = mu0*I2/(2*pi*rT) * (rT*rT-a*a)/(b*b-a*a)
ByT = B1 - B2
print(ByT)

# Q4
