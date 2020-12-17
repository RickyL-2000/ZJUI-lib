# %%
"""hw1"""

# %%
"""hw2"""
L = 0.5
E1 = 1.505/4/L/L
del_E = E1*4*4 - E1*3*3
E_g = del_E/8
print(E_g)


# %%
"""hw3"""

L = 10
lam = 640.15
E1 = 1.505/4/L/L
print(E1)
del_E = 1240/lam
print(del_E)
n = 0.5*(del_E/5/E1 + 5)    # 不要用int()估计！这不是四舍五入！
print(n)
E_f = E1*(n-5)*(n-5)
print(E_f)

# %%
"""hw4"""
L = 0.12

lam1 = L*2
print(lam1)
E1 = 1.505/4/L/L
print(E1)

lam2 = L * 2 / 3
print(lam2)
E3 = E1 * 3 * 3
print(E3)

lam3 = L / 2
print(lam3)
E4 = E1*4*4
print(E4)

lam4 = L / 3
print(lam4)
E6 = E1*6*6
print(E6)

N = (2/L)**0.5
print(N)

# %%
"""hw5"""
L = 0.8
lam = 1.965

# %%
# Q4
Ke = 1.505/lam/lam
print(Ke)

# %%
# Q6
Ke = 1.505/4/L/L
print(Ke)

# %%
"""quiz"""
L = 5

# %%
# Q2
E1 = 1.505/4/L/L
E3 = E1*3*3
print(E3)

# %%
# Q4
print(1/211)

# %%
