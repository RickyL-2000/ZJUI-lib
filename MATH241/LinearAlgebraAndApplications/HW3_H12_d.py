import numpy as np

# ax = b
a = np.array([[2, 0, 1j],
              [1, -3, -1j],
              [1j, 1, 1]])

b = np.array([[1j],
              [2j],
              [1+1j]])

c = np.linalg.solve(a, b)
print(c)