lam1 = 4.7e-4   # ! miuC / cm   Pay very attention!
pi = 3.1415
epsilon = 8.85e-12

# Q1
a = 0.069
# E*2*pi*r*L = Q/epsilon
# E = lam/epsilon/2/pi/r
ExP = lam1 / epsilon / 2 /pi/ a
print(ExP)

# Q3
h = 0.094
Phi = lam1*h/epsilon
print(Phi)

# Q4
lam2 = -14.1e-4
x = 0.0345
ExP2 = ExP + lam2/epsilon/2/pi/(a-x)
print(ExP2)

# Q5
Phi2 = (lam1+lam2)*h/epsilon
print(Phi2)

# Q6
Exp3 = lam1/epsilon/2/pi/(1.5*a) + lam2/epsilon/2/pi/(0.5*a)
print(Exp3)

