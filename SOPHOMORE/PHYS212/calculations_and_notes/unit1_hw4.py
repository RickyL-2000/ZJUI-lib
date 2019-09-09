Q1 = 4.9e-6 # miu C
Q2 = -3.1e-6
q = -3.8e-6
a = 0.21 # cm
b = 0.20 # cm
k = 9*10^9

# Q1
F2_x = k*Q2*q/(a*a+b*b) * a / (a*a+b*b)**0.5
print(F2_x)

# Q2
F2_y = k*Q2*q/(a*a+b*b) * b / (a*a+b*b)**0.5
print(F2_y)

# Q3
F1 = k*Q1*q/a/a
F_net_x = F2_x + F1
print(F_net_x)

# Q4
F_net_y = F2_y
print(F_net_y)

# Q5
F_net = (F_net_x**2 + F_net_y**2)**0.5
print(F_net)