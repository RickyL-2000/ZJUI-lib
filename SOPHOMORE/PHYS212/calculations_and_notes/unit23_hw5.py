I0 = 348
from math import pi, cos, acos, sin
theta1 = 79/180*pi

# Q1
I_mid = I0/2
print(I_mid)

# Q2
I_final = I_mid*(cos(theta1))**2
print(I_final)

# Q3
ratio = sin(theta1)*(I_final/I0)**0.5
print(ratio)

# Q4
I_final_new = I0*(sin(theta1))**2*(cos(theta1))**2
print(I_final_new)