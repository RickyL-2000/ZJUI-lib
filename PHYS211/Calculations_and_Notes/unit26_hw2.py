from numpy import sin, cos, pi
m = 0.93
L = 6.7
A = 0.21
t = 0.496
f = 0.42
mu = m/L

# Q1
v = L/t
print('v =', v)

# Q2
w = f*2*pi
k = w/v
T = w*w/k/k*mu
print('T =', T)

P = 2*pi/w
v_a = 4*A/P
print('v_a =', v_a)

# Q4
lam = v*P
print('lam =', lam)

# Q6
mu2 = mu/2
print('mu2 =', mu2)

T2 = T*2
v2 = (T2/mu2)**0.5
t2 = 2*L/v2
print('t2 =', t2)

# Q8
# v = lam/P = lam*f
lam2 = v2/f
print('lam2 =', lam2)