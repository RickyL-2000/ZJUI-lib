x3 = 46.1
f1 = -12.8
x2 = 21
x0 = 29.8
y0 = 23

# Q1
x1 = x0*f1/(x0 - f1)
print(x1)

# Q2
y1 = -x1/x0*y0
print(y1)

# Q3
x1_ = x2 - x1
f2 = (x3 - x2)*x1_/(x3 - x2 + x1_)
print(f2)

# Q4
y3 = -(x3-x2)/x1_*y1
print(y3)