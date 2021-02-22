# %%
import numpy as np

# %%
arr = np.array([1, 2, 3, 4, 5, 6])
sample = np.random.choice(arr, 3, replace=False)
print(sample)
sample[1] = -1
print(sample)
print(arr)

# %%
print(np.argmin(arr))
print(type(np.argmin(arr)))

# %%
arr = np.array([1, 2, 3, 4, 5, 6])
idx = np.random.choice(np.arange(len(arr)), 3, replace=False)
sample = arr[idx]
print(idx)
print(sample)
sample[1] = -1
print(arr)
print(sample)
# 所以 arr[idx] 这一步会 copy 一个新的 array ？

# %%
arr = np.array([[1,2,3],[4,5,6]])
print(arr.reshape(-1))
