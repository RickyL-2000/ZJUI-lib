from math import sin, cos, pi 

m = 1050
theta = 23/180*pi
g = 9.81
T = 3*m*g/5/sin(theta)

miu = (m*g - T*sin(theta))/T/cos(theta)
print(miu)