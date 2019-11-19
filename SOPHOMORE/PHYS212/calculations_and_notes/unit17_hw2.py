I1 = 3.4
t1 = 12
I4 = -3.4
t4 = 31
t3 = 24
W = 0.22
L = 0.64
d = 0.54
from math import pi, log
mu0 = 4*pi*1e-7

t2 = t3 + I1*(t4-t3)/I4

# Q1
Phi = mu0*I1*W*log(1+L/d)/2/pi
print(Phi)

# Q2
E1 = -Phi/I1*I1/t1  # counter-clockwise
print(E1)

# Q3
print("t2 =", t2)

# Q5
E4 = Phi/I1*(-I4)/(t4-t3)
print(E4)