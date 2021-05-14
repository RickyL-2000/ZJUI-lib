# %%
import numpy as np

# %%
centroids = np.array([[3, 3], [6, 2], [8, 5]])
X = np.array([[3, 3], [6, 2], [8, 5]])

i = 2
print(np.argmin(np.sum((centroids - X[i])**2, axis=1).squeeze()))
print(np.sum((centroids - X[i])**2, axis=1))

# %%
X = np.array([1,0,0,0,1,1,1,0,0,0,1,0])
Y = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(X == 1)
print(Y[X == 1])

# %%
