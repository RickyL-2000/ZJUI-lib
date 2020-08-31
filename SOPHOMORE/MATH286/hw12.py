# %%
import numpy as np

# %%
A = np.mat([[-1, 1, 0],
            [1, -2, 1],
            [0, 1, -1]])
print(A)
I = np.eye(3)
B = (A + I) * A * (A + 3 * I)
print(B)
print(A*A)

# %%
Phi = np.mat([[1, 1, 1],
              [1, 0, -2],
              [1, -1, 1]])
print(Phi.I)
print(np.linalg.det(Phi))