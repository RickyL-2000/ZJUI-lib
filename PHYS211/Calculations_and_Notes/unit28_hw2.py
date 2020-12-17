h1 = 0.39
h2 = 0.14
h3 = 0.3
PA = 101300
rhow = 1000
g = 9.81

#Q1
# Be careful!!! To calculate the absolute pressure you have to add in atmospheric pressure.
p = rhow*g*h1+PA
print('p =', p)

#Q2
p2 = p - rhow*g*h2
print('p2 =', p2)

# Q3
# p2 = rhoo*g*h3+PA
rhoo = (p2 - PA)/g/h3
print('rhoo =', rhoo)

rhog = 1261
p4 = rhog*g*h3 + PA
print('p4 =', p4)

H = h1 + h2
# rhow*h1 = rhow*(H - h1) + rhog*h3
h1 = (rhow*H + rhog*h3)/(rhow + rhow)
h2 = H - h1
d = h1 - h2 - h3
print('d =', d)

p6 = rhow*g*h1 + PA
print('p6 =', p6)