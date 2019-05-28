from scipy.optimize import fsolve
import numpy as np 

R = 4*1.6e15 /1.7
print(R)

def f(v):
    return np.array(
        [
            90*v[0] - 145*v[1],
            90*v[0]*v[0] + 145*v[1]*v[1] - R/(1e26) 
        ]
    )

v = fsolve(f, [-2,2])
print(v)
