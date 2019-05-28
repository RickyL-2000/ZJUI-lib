rhoa = 1.28
rhoh = 0.18
R = 5.3
mb = 129.0
Vb = 0.057
mp = 71.0
Vp = 0.077
g = 9.81
pi = 3.1415926535

V = 4/3*pi*R*R*R
print('V =', V)

# Q2
F1 = (mb + rhoh*V)*g
print('F1 =', F1)

#Q3
Fb1 = rhoa*g*(V+Vb)
print('Fb1 =', Fb1)

F4 = mp*g
print('F4 =', F4)

F5 = rhoa*g*Vp
print('F5 =', F5)

# Q6
# F1 + n*F4 = Fb1 + n*F5
n = (Fb1-F1)/(F4-F5)
print('n =', n)