from math import atan, pi
L = 340e-3
C = 25e-6
R = 280
Em = 120

VL = 60.6
VC = -10.1
VR = Em - VC - VL

print(VR)

omega = (VL / (L * C * abs(VC)))**0.5
XL = omega*L
XC = 1/omega/C
# theta = atan((VL - abs(VC))/VR)
theta = atan((XL-XC)/R)

print(omega)
print(theta)
print((VL - abs(VC))/VR)

t_imax = theta/omega
print(t_imax)