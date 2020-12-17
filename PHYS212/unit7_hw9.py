import math
a = 2.6e-2
lami = -0.31e-6  # C/m
b = 0.108
c = 0.148
lamo = 0.31e-6  # C/m
epsl = 8.85e-12
pi = 3.1415

# Q1
d = 5.9e-2
ExP = lami/(2*pi*epsl*d)
print(ExP)

# Q2
Vc_minus_Va = lami/(2*pi*epsl)*math.log(a/b)
print(Vc_minus_Va)

# Q3
C = lamo*1/Vc_minus_Va
print(C)

# Q5
lamo_new = lamo*2
print(lamo_new)