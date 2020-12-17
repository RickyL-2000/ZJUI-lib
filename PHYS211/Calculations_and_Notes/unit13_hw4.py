import numpy as np 
from scipy.optimize import fsolve

m = 1.59
v = 2.91
a1 = 37/360*2*np.pi
a2 = 53/180*np.pi 

def f(x): #x = [v1,v2]
    return np.array( 
        [
            m*x[0]*np.sin(a1) - m*x[1]*np.sin(a2),
            m*v - m*x[0]*np.cos(a1) - m*x[1]*np.cos(a2)
        ]
    )

[v1,v2] = fsolve(f,[1,1])

print(v1)
print(v2)
print(m*v)
print(0.5*m*v*v)