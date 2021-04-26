# %%
from collections import Counter
import numpy as np

# %%
a = {'a', 'b', 'c'}
b = Counter(a)

# %%
print(b*3)

# %%
b['a'] = 2
print(b)

# %%
y = [1,2,2,3]
y = np.array(y)
y[y==2]

# %%
np.argwhere(y==2)[0, 0]

# %%
a = np.array([True, True, False, True])
b = np.array([True, False, False, True])
print(a == b)

# %%
print(sum(a & b))

# %%
