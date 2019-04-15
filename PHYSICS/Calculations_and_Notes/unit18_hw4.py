import numpy as np 

mh = 2.8
rh = 0.17
md = 1.8
rd = 0.08
ms = 3.6
rs = 0.2
g = 9.81

a = mh*g/(mh + 7*ms/5 + md/2)
T1 = mh*(g-a)
T2 = 7/5*ms*a
alpha_d = a/rd
alpha_s = a/rs

print('Tension between disk and sphere T2 =', T2)
print('Tension between disk and hook T1 =', T1)
print('a =', a)
print('alpha_d =', alpha_d)
print('alpha_s =', alpha_s)