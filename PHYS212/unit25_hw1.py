n2 = 1.2
from math import sin, cos, pi, asin
theta_in = 75/180*pi

# sin(theta_in)/sin(theta1) = n2
theta1 = asin(sin(theta_in)/n2)
print(theta1/pi*180)

critical_angle = asin(1/n2)
print(critical_angle/pi*180)

theta2 = theta1 - pi/4
theta3 = asin(n2*sin(theta2))
theta_out = theta3 + pi/4
print(theta_out/pi*180)