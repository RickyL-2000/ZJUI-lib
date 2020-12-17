lam = 5.4e-2
Bx = 3.9e-6
By = 3.3e-6
c = 3e8
epsilon = 8.85e-12
from math import pi
mu0 = 4*pi*1e-7

# Q1
f = c/lam
print(f/1e9)

# Q2
B0 = (Bx*Bx + By*By)**0.5
E0 = B0*c
I = 0.5*c*epsilon*E0*E0
print(I)

# Q3
S = -c*B0*B0/mu0
print(S)

# Q4
Ex = By*c
print(Ex)
