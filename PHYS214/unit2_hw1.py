# %%
d = 0.01e-3
L = 3
lamb = 500e-9

del_y = lamb / d * L

from math import sin

a = 2*lamb*((16*del_y)**2+L*L)**0.5/16/del_y

print(a*1e3)

# emmmm this is wrong...

# %%
## CORRECTION
a = 2/15*d
print(a*1e3)

# %%
