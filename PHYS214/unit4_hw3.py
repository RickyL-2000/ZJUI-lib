# %%
lamb = 248e-9
D_b = 1e-2
D_f = 1.3e-2
f = 0.625e-2

# %%
# Q1
from math import asin
theta = 1.22*lamb / D_b
# 这个精度居然还可以估算...
w = 2*theta*f
print(w*1e9)

# %%
# Q2
print(w/2*1e9)

# %%
lamb = 157e-9
theta = 1.22*lamb / D_b
# 这个精度居然还可以估算...
w = 2*theta*f
print(w/2*1e9)

# %%
# 189.1-119.7125
print((1/119.7125-1/189.1)/(1/119.7125))

# %%
#Q4
w1 = 2*f*asin(248e-9/D_b)
w2 = 2*f*asin(157e-9/D_b)
print((w1/w2)**2)

# %%
#Q5
lamb = 248e-9/1.33
theta = 1.22*lamb / D_b
# 这个精度居然还可以估算...
w = 2*theta*f
print(w/2*1e9)

# %%
