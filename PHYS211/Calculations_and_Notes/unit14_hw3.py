import numpy as np 

M = 17.4
m1 = 4.9
m2 = 5.1
m3 = M - m1 - m2
ag1 = 21/180*np.pi 
ag2 = 26/180*np.pi
v1 = 25.9
v2 = 21.4
print(m3)

vx = (m1*v1*np.cos(ag1) - m2*v2*np.sin(ag2))/m3
vy = (m2*v2*np.cos(ag2) - m1*v1*np.sin(ag1))/m3
print(vx)
print(vy)

v3 = (vx*vx+vy*vy)**0.5
Ek = 0.5*m1*v1*v1 + 0.5*m2*v2*v2 + 0.5*m3*v3*v3

print(Ek)