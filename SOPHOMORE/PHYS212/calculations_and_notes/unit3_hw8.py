from math import cos, sin
lam1 = 8.9e-6
a = 0.021
b = 0.042
rho = -656e-6
pi = 3.1415
epsilon = 8.85e-12

# Q1
lam2 = rho*(pi*b*b-pi*a*a)
print(lam2)

# Q2

# Q3
d = 0.078
EyP = (lam1+lam2)/2/pi/d/epsilon
print(EyP)

# Q4
d = 0.0105
ExR = lam1/2/pi/d/epsilon * cos(pi/6)
print(ExR)

# Q5
EyR = lam1/2/pi/d/epsilon * sin(pi/6)
print(EyR)

# Q7
lam1 = 17.8e-6
