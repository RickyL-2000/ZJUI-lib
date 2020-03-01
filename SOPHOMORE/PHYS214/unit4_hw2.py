# %%
from math import asin, pi
lamb1 = 1500e-9
lamb2 = 1510e-9
# d = (2e-3 - 900*200e-9)/900
d = 1/450/1000

del_s = 0.5e-3
theta1 = asin(lamb1/d)
theta2 = asin(lamb2/d)
R = del_s/(theta2-theta1)

print(R*1e2)

# 我吐了！！！原来是d算错了！！！

# %%
## cosine
print((1-lamb1**2/d**2)**0.5)

# %%
