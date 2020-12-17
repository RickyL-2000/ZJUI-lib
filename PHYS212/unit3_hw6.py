k = 9e9
q1 = -5.2e-6
a = 0.022   # inner radius
b = 0.043   # outer radius
q2 = 1.2e-6 # conductive
pi = 3.1415

# Q1
d = 0.074
ExP = k*(q1+q2)/d/d
print(ExP)

# Q4
d2 = 0.011
EyR = k*q1/d2/d2
print(EyR)

# Q5
rho_b = (q1+q2)/(4*pi*b*b)
print(rho_b)

# Q6
rho_a = -q1/(4*pi*a*a)
print(rho_a)

# Q7


# Q8
r = 0.011
q2 = 1.2e-6