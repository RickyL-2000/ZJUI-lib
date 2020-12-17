from math import pi, sin, cos, acos
theta1 = 60/180*pi
theta2 = 130/180*pi

cos_theta2_minus_theta3 = (0.02*2/(cos(theta2-theta1))**2)**0.5
theta2_minus_theta3 = acos(cos_theta2_minus_theta3)
theta3 = theta2 - theta2_minus_theta3
print(theta3/pi*180)