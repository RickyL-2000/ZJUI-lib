q1 = -2.1e-6
q2 = 6.3e-6
d = 6.9e-2
k = 9e9

# Q1
ExP = k*q1/(2*d**2)/2**0.5
print(ExP)

# Q2
EyP = ExP + k*q2/d**2
print(EyP)

# Q3
q3 = 2.7e-6
ExP = ExP + k*q3/d**2
print(ExP)

# Q4
q1 *= 2
q2 *= 2
q3 *= 2