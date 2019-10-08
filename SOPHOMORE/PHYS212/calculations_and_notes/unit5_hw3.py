k = 9e9
q2 = 0.8e-6
q1 = -0.4e-6
d1 = 0.061

# Q1
# V = k*Q/r
d2 = 0.024
delPE = k*q2*q1/d2 - k*q2*q1/d1
print(delPE)

# Q2
q3 = 0.4e-6
q4 = q3
a = 0.014
delPE2 = k*q3*q1/(a*a+d2*d2)**0.5*2 - k*q3*q1/(a*a+d1*d1)**0.5*2
print(delPE2)

# Q3
PE3 = k*q1*q3/(a*a+d2*d2)**0.5+k*q1*q4/(a*a+d2*d2)**0.5+k*q3*q4/(2*a)
print(PE3)

# Q4
q5 = -q4
PE4 = k*q1*q3/(a*a+d2*d2)**0.5+k*q1*q5/(a*a+d2*d2)**0.5+k*q3*q5/(2*a)
print(PE4)

# Q5
q6 = 0.8e-6
d = d1+d2
PE5_P = k*q2*q1/d1 + k*q2*q6/(d1+d2) + k*q1*q6/d2
PE5_R = k*q2*q1/d2 + k*q2*q6/(d1+d2) + k*q1*q6/(d2+d1-d2)
print(PE5_R - PE5_P)