f1 = 9.8
x2 = 73.62
f2 = 24.7
x0 = 12.7
y0 = 8.1

# Q1
x1 = x0*f1/(x0 - f1)
print(x1)

# Q2
y1 = - x1/x0*y0
print(y1)

# Q3
x1_ = x2 - x1
x3 = x1_*f2/(x1_ - f2)
print(x3+x2)

# Q4
y3 = - x3/x1_*y1
print(y3)