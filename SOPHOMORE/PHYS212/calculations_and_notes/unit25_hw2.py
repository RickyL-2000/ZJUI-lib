from math import sin, asin, cos, acos, pi, atan, tan
phi1 = 39.5/180*pi
h = 0.12
d = 32.9e-2

# Q1
phi2 = atan(h/(d - h*tan(pi/3)))
print(phi2/pi*180)

# Q2
n = sin(pi/3 - phi1) / sin(pi/3 - phi2)
print(n)

# Q3
phi3 = acos(n*cos(phi2))
print(phi3/pi*180)

# Q4
phi2 = acos(1/n)
phi1 = pi/3 - asin(n*sin(pi/3 - phi2))
print(phi1/pi*180)

# Q6
n = 1.42
phi1 = 60/180*pi
phi2 = phi1
phi3 = acos(n*cos(phi2))
print(phi3/pi*180)