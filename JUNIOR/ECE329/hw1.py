# %%
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# %%
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax = plt.axes(projection='3d')

charges = np.array([[0, 0, -1],
                    [0, 0, 1]])
points = np.array([[0, 0, 0],
                  [0, 0, 2],
                  [0, -1, 0]])
ax.scatter(charges[:, 0], charges[:, 1], charges[:, 2], c='b', s=60)
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', s=60)

E1 = np.array([0, 0, -3])
E2 = np.array([0, 0, 7/9])
E3 = np.array([0, 2**0.5/4, -3*2**0.5/4])

ax.quiver(*points[0], *(points[0] + E1), arrow_length_ratio=0.1)
ax.quiver(*points[1], *(points[1] + E2), arrow_length_ratio=0.1)
ax.quiver(*points[2], *(points[2] + E3), arrow_length_ratio=0.1)

ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 4)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# %%
data = np.random.randint(0, 255, size=[3, 3, 3])
print(data)
print(data[0][:2])
print(data[1][:2])

