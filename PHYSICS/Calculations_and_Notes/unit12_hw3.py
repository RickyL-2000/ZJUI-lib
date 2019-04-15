from scipy.optimize import fsolve
m1 = 670
v1 = 8.9
vf = 5.3

def f(m2):
    return m1*v1 - (m1 + m2)*vf
m2 = fsolve(f,100)

delta_k = 0.5*(m1+m2)*vf**2 - 0.5*m1*v1**2

v2 = -6.4
vt = (m1*v1 + m2*v2)/(m1+m2)
P1_f = m1*vt

print(m2)
print(delta_k)
print(vt)
print(P1_f)