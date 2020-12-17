Q = 4.7e-6
a = 0.069
pi = 3.1415
k = 9e9

# Q1
lam = Q/(0.25*pi*2*a)
print(lam)

# Q2
lam_rad = 2*Q/pi
Ex = 2*k*Q/(a*a*pi)
print(Ex)

# Q3
Ey = Ex
print(Ey)

# Q4
E = k*Q/a/a
print(Ex*2**0.5)
print(E)

#Q5
print(2*Ex)