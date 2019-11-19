Lab = 39e-2
Lbc = 64e-2
I = 0.262
B = 0.85

# Q1
Fac_x = -I*Lbc*B
print(Fac_x)

# Q2
Fac_y = I*Lab*B
print(Fac_y)

# Q3
# 左图应该是势能最小的情况，右图是最大情况
# 从0积分到180, 即 2muB*(-cos(180)+cos0)
mu = I*0.5*Lab*Lbc
delU = 2*mu*B
print(delU)

# Q4
# 和 Q3一样