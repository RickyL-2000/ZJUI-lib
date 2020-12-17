from scipy.optimize import fsolve
import numpy as np
m1 = 5.7
v = 1.8
v1 = 0.7

def f(x): #x = [m2, v2]
    return np.array( 
        [ 
            m1*v - m1*v1 - x[0]*x[1],
            0.5*m1*v*v - 0.5*m1*v1*v1 - 0.5*x[0]*x[1]*x[1]
        ]
    )

[m2,v2] = fsolve(f, [1,1])

print([m2,v2])