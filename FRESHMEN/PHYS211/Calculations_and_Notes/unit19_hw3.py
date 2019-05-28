# Notice!!!! The equation:
###### f = μN ######
# only represents the MAXIMUM static friction, 
# not necessarily the actual value of the static friction. 

# so we have:
### mgsinθ - f = ma
### fr = 2/5 * mr^2 * alpha
### a = alpha * r

import numpy as np 

m = 8
r = 0.19
theta = 30/180*np.pi
g = 9.81

f = m*g*np.sin(theta)*2/7
print(f)