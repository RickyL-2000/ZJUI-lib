mu = 2.4e-4
L = 0.97
T = 98.4

# Q1
# v = (T/mu)**0.5
v = (T/mu)**0.5
print('v =', v)

# Q2
# f0 = v/(2L)
f0 = v/(2*L)
print('f0 =', f0)

f1 = f0*L/(L - 0.153)
print('f1 =', f1)