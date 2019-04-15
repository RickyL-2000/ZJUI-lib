import numpy as np 
from scipy.optimize import fsolve
m1 = 48
m2 = 125
L = 5
g = 9.81

#Q1
def f1(N):
    return np.array(
        [
            N[1]*L/3 + N[0]*L*2/3 - m1*g*L - m2*g*L/2,
            N[0]*L/3 + N[1]*L*2/3 - m2*g*L/2
        ]
    )
N = fsolve(f1,[1,1])
print('N1 =',N[0],'N2 =', N[1])

#Q2
def f2(m):
    return m2*g*(L/2 - L/3) - (m1+m)*g*L/3
m = fsolve(f2,[1])
print('m =',m[0])