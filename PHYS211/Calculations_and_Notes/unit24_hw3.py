L = 1
m = 2.5
d = 0.17
g = 9.81
from numpy import pi
# tau = -I alpha
# alpha = - tau/I
# tau = (L - d)/L*mg*(L-d)/2*theta - d/L*mg*d/2*theta
# = ((L-d)**2/2/L - d**2/2/L)*mg*theta
# = (L**2 - 2*L*d)/2/L*mg*theta

I = m*L*L/12 + m*(L/2-d)**2

w = ((L**2 - 2*L*d)/2/L*m*g/I)**0.5

T = 2*pi/w
print(T)