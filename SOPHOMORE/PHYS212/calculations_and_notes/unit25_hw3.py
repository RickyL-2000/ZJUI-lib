x2 = 53.1
x1 = 31.2       # left
y1 = 6.26
n = 1.39

# Q1
f = x1*x2/(x1 + x2)
print(f)

# Q2
M = -x2/x1
y2 = M*y1
print(y2)

# Q3
R = (n-1)*f
print(R)

# Q4
x1_new = 9.8    #left
x2_new = f*x1_new/(x1_new-f)
print(x2_new)