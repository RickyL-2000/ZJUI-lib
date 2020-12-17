mu = 3.4e-4
f = 69
L = 0.57
g = 9.81

#Q1 and *Q5* NOTE! just CHANGE THE VALUES!
lam = 2*L
print('lam =', lam)

#Q2
v = f*lam
print('v =', v)

T = v*v*mu
print('T =' ,T)

print('m =', T/g)