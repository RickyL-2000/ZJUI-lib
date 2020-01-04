x2 = -37.8
y2 = 2.5
f = -54.8

# Q1
x1 = x2*f/(x2 - f)
print(-x1)

# Q2
y1 = -x1/x2*y2
print(y1)

# Q3
f_c = 30.77
x3 = 79.2   # neg
x1_ = x1 - x3
x4 = x1_*f_c/(x1_ - f_c)
print(x4-x3)

# Q4
x4_ = -x4 + x3
x5 = x4_*f/(x4_ - f)
print(x5)