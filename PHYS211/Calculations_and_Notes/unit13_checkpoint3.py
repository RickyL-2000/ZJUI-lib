import numpy as np 
from scipy.optimize import fsolve
m1 = 1
m2 = 2
v1 = 2
v2 = -1
def f(v):
    return np.array( 
        [
            m1*v1 + m2*v2 - m1*v[0] - m2*v[1],
            0.5*m1*(v1*v1-v[0]*v[0]) + 0.5*m2*(v2*v2-v[1]*v[1])
        ]
    )

v = fsolve(f,[-1,1])
print(v)