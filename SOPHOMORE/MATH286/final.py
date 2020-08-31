# %%
import numpy as np

A = np.mat([[1, -2, -2],
            [-4, -1, 2],
            [0, 0, -3]])
print(np.linalg.eig(A))