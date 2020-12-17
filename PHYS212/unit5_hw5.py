a = 0.055       # solid insulating sphere
rho = -109e-6   # C/m^3
b = 0.105       # uncharged spherical conducting shell
c = 0.125
pi = 3.1415
k = 9e9

# Q1
Q = rho*(4/3*pi*a*a*a)
d = 0.3
ExP = k*rho*(4/3*pi*a*a*a)/d/d
print(ExP)

# Q2
Vb = k*Q/c
print(Vb)

# Q3
Va_minus_b = k*Q*(1/a-1/b)
Va = Va_minus_b + Vb
print(Va)

# Q4
print(-Va_minus_b)

# Q5
Q_shell = 0.0337e-6
Vb = k*(Q+Q_shell)/c
Va_minus_b = k*Q*(1/a-1/b)
Va = Va_minus_b + Vb
print(Va)