# %%
import numpy as np

# %%
def f(x):
    ret = np.copy(x)
    ret[0] = 1
    return ret

x = np.array([0,2,3])
y = f(x)
print(x)
print(y)
# %%
a = np.array([[-1,1],[1,-1]])
b = 1 * (a > 0.0)
print(b)

# %%
a = np.array([1,2])
a = a.reshape(2,1)
# %%
print(a)
print(b)
b = np.array([[2,3]])
a.dot(b)

# %%
a = np.array([[1,2,3,4],[4,5,6,7]])
b = np.array([[2,3,4], [3,4,5], [4,5,6], [5,6,7]])
print(a.shape)
print(a)
print(b.shape)
print(b)
c = a.dot(b)
print(c)
d = np.array([1,-1,1,-1])
c = a * d
print(c)

# %%
print(c)# %%
np.sum(c, axis=1)

# %%
