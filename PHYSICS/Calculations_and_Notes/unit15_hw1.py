from scipy.integrate import quad
import numpy as np 

md = 3.3
R = 0.26
mr = 1.2
L = 0.74

mi_each_r = mr/L * quad(lambda x:x*x, 0, L)[0]
print(mi_each_r)

mi_d = 0.5*md*R*R
print(mi_d)

mi = 5*mi_each_r + mi_d
print(mi)

t = 3.3
a = 2*14*2*np.pi/t/t
print(a)

w = a*t 
print(w)

print(0.5*1.207*w*w)
print(w*2**0.5/2)
print((w-37.697188)/3.3)