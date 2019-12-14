I0 = 696
from math import cos, pi, acos
theta2 = 84/180*pi
theta3 = 22/180*pi
theta1 = pi/2

# Q1
I2 = 0.5*I0*(cos(theta1 - theta2))**2
print(I2)

# Q2
I3 = I2*(cos(theta2-theta3))**2
print(I3)

# Q3
I_final_new = 0.5*I0*(cos(theta1-theta3))**2*(cos(theta2-theta3))**2
print(I_final_new)

# Q3
I_final_RL = 0.5*I0*(cos(theta2-theta3))**2*(cos(theta1-theta3))**2
print(I_final_RL)

# Q4
I_final_RL_new = 0.5*I0*(cos(theta2-theta3))**2*(cos(theta3))**2
print(I_final_RL_new)
