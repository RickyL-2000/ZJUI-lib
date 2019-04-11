import numpy as np 
m = 4.2
R = 0.119
v = 8.1
miu = 0.27
g = 9.81

f = miu*m*g 
I = m*R*R*2/5
alpha = f*R/I
print(alpha)

a = f/m
print(a)

t = v/(alpha*R+a)
print(t)

x = v*t - 0.5*a*t*t
print(x)

vt = v - a*t
print(vt)

w = alpha*t
Er = 0.5*I*w*w 
Et = 0.5*m*vt*vt 
print(Er,Et)