epsilon = 8.85e-12
sigm1 = 0.71e-6
sigm2 = -0.12e-6     # C/m^2
c = 0.22
a = 0.09
b = 0.13

# Q1
# E = sigm/(2*epsilon)
x_P = 0.045
ExP = sigm1/(2*epsilon) - sigm2/(2*epsilon)
print(ExP)

# Q2
# sigm1 - sigm2 + sigma - sigmb = 0
# ! 这个地方a处和b处的电场应该都视作向导体内部的
sigma = (sigm1 - sigm2)/2
print(sigma)

# Q4
x_S = 0.175
VS_minus_b = (sigm1-sigm2)/2/epsilon*(b - x_S)
Va_minus_P = (sigm1-sigm2)/2/epsilon*(x_P - a)
VS_minus_P = VS_minus_b + Va_minus_P
print(VS_minus_P)

# Q5
x_T = 0.265
ExT = (sigm1+sigm2)/2/epsilon
print(ExT)