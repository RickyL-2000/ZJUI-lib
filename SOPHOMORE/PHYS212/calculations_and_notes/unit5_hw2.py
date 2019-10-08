import math
epsilon = 8.85e-12
pi = 3.1415


# Q1
g = 2.3
h = 7
deltaV = (-3/2*7*7) - (-3/2*2.3*2.3)
print(deltaV)

# Q3
lam = 2.8e-6
# Ex = lam/(2*pi*epsilon*x)
c = 3
d = 7
V3 = lam/(2*pi*epsilon) * (math.log(7)-math.log(3))
print(V3)

# Q4
sigm = 1.1e-6
V4 = sigm/(2*epsilon)*(0.2-1.9)
print(V4)

