import numpy as np 
from scipy.optimize import fsolve

m1 = 117
v1 = 4.1
m2 = 98
v2 = -3.2

v_cm = (m1*v1 + m2*v2)/(m1+m2)
print(v_cm)

v12 = v_cm - (v1 - v_cm)
v22 = v_cm - (v2 - v_cm)
print(v1-v_cm)
print(v12)
print(v22)

v3 = (m1*v1 + m2*v2)/(m1+m2)
print(v3)