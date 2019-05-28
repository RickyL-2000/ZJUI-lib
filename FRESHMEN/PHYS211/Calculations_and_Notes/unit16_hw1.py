import numpy as np 

mr = 7.35
L = 5.76
ms = 36.75
R = 1.44

I1 = mr*L*L/3 + 2*ms*R*R/5 + ms*(L+R)**2
print('I =', I1)

F = 410
alpha1 = F*0.5*L/I1
print('alpha1 =', alpha1)

I2 = mr*L*L/12 + 2*ms*R*R/5 + ms*(0.5*R)**2 + mr*(2*R+0.5*R)**2
print('I2 =', I2)

I3 = mr*L*L/12 + 2*ms*R*R/5 + ms*R*R + mr*(4*R)**2
print('I3 =', I3)