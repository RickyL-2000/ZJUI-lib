# Note!!! Be sure to use the *torque = F*R* when calculating the torsion constant!
from numpy import sin, cos, pi
m = 7
R = 0.67
F = 41
theta = pi/2

kappa = F*R/(pi/2)
print('kappa =', kappa)

torque = kappa*2*pi
print('torque =', torque)

# Q3
# I*alpha = - kappa*theta
I = 0.5*m*R*R
w = (kappa/I)**0.5
print('w =', w)
