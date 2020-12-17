sigm1 = -2.1e-6
a = 0.021
b = 0.042
sigm2 = 74e-6
epsilon = 8.85e-12

# Q1
# E = del/2/epsilon
ExP = (sigm1+sigm2) / 2 / epsilon
print(ExP)

# Q3    !!! pay attention!
ExR = (sigm1-sigm2)/2/epsilon
print(ExR)

# Q5
# sigma = (sigm2-sigm1)/2
# sigmb = (sigm2+sigm1)/2
sigmb = (sigm2+sigm1)/2
print(sigmb)

# Q7
sigma = (sigm2-sigm1)/2
print(sigma)