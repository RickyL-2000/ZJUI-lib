m = 0.75
v = 2.5
M = 2
L = 0.9

# m*v*L = I_t*w = (M*L*L/3 + m*L*L)*w
w = m*v*L/(M*L*L/3 + m*L*L)
Ei = 0.5*m*v*v
Ef = 0.5*(M*L*L/3 + m*L*L)*w*w

fraction = (Ei - Ef)/Ei
print(fraction)