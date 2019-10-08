import math
a = 0.024
rho = 49e-6     # C/m^3
b = 0.185
c = 0.215
lam = -0.54e-6  # C/m
pi = 3.1415
epsilon = 8.85e-12

# Q1
d = 0.49
EyR = lam/(2*pi*epsilon*d) + rho*pi*a*a/(2*pi*epsilon*d)
print(EyR)

# Q2
# 积分
lamin = rho*pi*a*a
VP_minus_VR = (lam+lamin)/(2*pi*epsilon)*(math.log(d)-math.log(2**0.5*d))
print(VP_minus_VR)

# Q3
Vc_minus_Va = lamin/(2*pi*epsilon)*(math.log(a)-math.log(b))
print(Vc_minus_Va)

# Q4
# rho > 0

# Q5
# rho_p
# rho_p*pi*a*a + lam = 0
rho_p = -lam/pi/a/a
print(rho_p)