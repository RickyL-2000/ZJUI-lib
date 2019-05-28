R1 = 0.23
R2 = 0.11
v1 = 0.81
pi = 3.141593

rate = v1*pi*R1*R1
print('rate =', rate)

v2 = rate/(pi*R2*R2)
print('v2 =' ,v2)

t = 139/rate/60 #minutes
print('t =', t)

# Q4
# P1 + 0.5*rho*v1*v1 = 
P1 = 243120
rho = 1000
P2 = P1 + 0.5*rho*v1*v1 - 0.5*rho*v2*v2
print('P2 =', P2)