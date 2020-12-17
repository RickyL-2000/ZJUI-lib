x0 = 4.4e-2
n = 1300
I1 = 3.7 # nega z
I2 = 4.4 # posi z
from math import pi
mu0 = 4*pi*1e-7

# Q2
B1 = 0.5*mu0*n*I1
B2 = 0.5*mu0*n*I2
xP = 2.2e-2
ByP = -B1-B2
print(ByP)

# Q3
xR = 6.6e-2
ByR = -B2 + B1
print(ByR)

# Q4
ab = 13.9e-2
cd = ab
ad = 4.9e-2
bc = 7.9e-2
H = 13.8e-2
print(mu0*n*H*I1)

# Q5
xS = 6.6e-2

# Q6
B = B1 + B2 # down
integral = -B*H
print(integral)