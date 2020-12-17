# %%
"""hw1"""
L = 3e-9
x1 = 1e-9
x2 = 2e-9

P = 30/(L**5) * ((x2**5/5 - L*x2**4/2 + L*L*x2**3/3) - (x1**5/5 - L*x1**4/2 + L*L*x1**3/3))

print(P)

# %%
"""hw2"""
from math import sin, cos, pi
L = 0.5
E = 29.66
U0 = 50
K = 2*pi*((U0-E)/1.505)**0.5
C = 1.42
P = C*C/2/K

print(0.5 - P)

# %%
"""hw3"""

# Q2
print(0.469**2)

# %%
# Q3
print(0.656**2)

# %%
# Q4
print(0.592**2)

# %%
# Q5
print(0.469**2 + 0.656**2*4 + 0.592**2*9)

# %%
# %%
"""hw4"""

# Q1
L = 4
E1 = 1.505/4/L/L
print(E1)

# %%
# Q2
E2 = 4*E1
print(E2)

# %%
# Q3
h = 4.14e-15
f1 = E1/h
print(f1)

# %%
# Q4
f2 = E2/h
print(f2)

# %%
print(2*f1)

# %%
print(2*f2)

# %%
# Q7
print(1/(f2-f1))

# %%
"""hw5"""
from math import exp, log

# Q1
L = 0.61
U0 = 3
E = 2

G = 16*E/U0*(1-E/U0)
K = 2*pi*((U0-E)/1.505)**0.5
T = G*exp(-2*K*L)
print(T)

# %%
U1 = 2.8
G1 = 16*E/U1*(1-E/U1)
K1 = 2*pi*((U1-E)/1.505)**0.5
T1 = G1*exp(-2*K1*L)
print(T1/T)

# %%
# Q3
print(log(10)/2/K)

# %%
"""hw6"""

lam = 420
del_t = 80e-12  #ps
c = 3e8

# %%
# Q2
P = 6.626e-34 / (420e-9)
del_x = del_t*c
print(del_t*c)

# %%
# Q3
print(lam*1e-9 / 2/ pi / del_x)

# %%
del_p = 6.626e-34/2/pi/del_x
del_lam = 6.626e-34/P/P*del_p
print(del_lam*1e9)

# %%
"""quiz"""
# Q1
L = 3.5
print(L*5/6)

# %%
# Q2
print(L*3/5)

# %%
# Q3
del_x = 0.007
print(2/L*del_x)

# %%
