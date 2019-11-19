import numpy as np 

E = np.array([[1, 2, 3, 4],
              [5, 6, 7, 0],
              [8, 9, 0, 0],
              [10, 0, 0, 0]])

print(np.linalg.det(E))