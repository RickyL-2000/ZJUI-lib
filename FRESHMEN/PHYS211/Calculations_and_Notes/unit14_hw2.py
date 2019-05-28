import numpy as np 

m = 0.254
angle = 27/180*np.pi
v1 = [18.8*np.cos(angle),-18.8*np.sin(angle)]
t = 0.062

p = m*18.8
print(p)

v2 = [-18.8*np.cos(angle),-18.8*np.sin(angle)]
deltav = ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)**0.5
deltap = -m*deltav
print(deltap)

F = deltap/t
print(F)

#Q4
I2 = m*(-11.8-18.8)
print(I2)

t = abs(I2)/F
print(t)

Ek = 0.5*m*11.8*11.8 - 0.5*m*18.8*18.8
print(Ek)