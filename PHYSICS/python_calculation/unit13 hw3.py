from scipy.optimize import fsolve
import numpy as np 

m1 = 3.2
v = 2.1
m2 = 4.3

def f(x):  #x = [v1,v2]
    return np.array( 
        [
            m1*v - m1*x[0] - m2*x[1],
            0.5*m1*v*v - 0.5*m1*x[0]*x[0] - 0.5*m2*x[1]*x[1]
        ]
    )

x = fsolve(f, [-1,1])

v_cm = (m1*x[0]+m2*x[1])/(m1+m2)
vf = x[0] - v_cm
print(vf)
print(v_cm)
print(x[0])
print(x[1])