# %%
import matplotlib.pyplot as plt
import numpy as np
import pickle

# %%
X_min, X_max = 0, 1
Y_min, Y_max = 0, 0.5

delta_x, delta_y = 0.01, 0.01

# %$
N = 10000
m = int((Y_max-Y_min)/delta_y+1)
n = int((X_max-X_min)/delta_x+1)
V = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        if (0.3 <= j * delta_x <= 0.4) and (0.2 <= Y_max - i * delta_y <= 0.3):
            V[i, j] = 1.0
        if (0.6 <= j * delta_x <= 0.7) and (0.2 <= Y_max - i * delta_y <= 0.3):
            V[i, j] = -1.0

V_old = np.copy(V)
for _ in range(N):
    for i in range(1, m-1):
        for j in range(1, n-1):
            if ((0.3 <= j * delta_x <= 0.4) or (0.6 <= j * delta_x <= 0.7)) and (0.2 <= Y_max - i * delta_y <= 0.3):
                continue
            V[i, j] = ( (V_old[i+1, j] + V_old[i-1, j])/delta_x**2 + (V_old[i, j+1] + V_old[i, j-1])/delta_y**2 ) / (2/delta_x**2 + 2/delta_y**2)
    V_old = np.copy(V)

# %%
Ex = np.zeros((m, n))
Ey = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        if i == 0:
            v = - (V[i, j] - V[i+1, j]) / delta_y
        if i == m-1:
            v = - (V[i-1, j] - V[i, j]) / delta_y
        if j == 0:
            u = - (V[i, j+1] - V[i, j]) / delta_x
        if j == n-1:
            u = - (V[i, j] - V[i, j-1]) / delta_x
        if i != 0 and i != m-1 and j != 0 and j != n-1:
            u = - (V[i, j+1] - V[i, j-1]) / 2 / delta_x
            v = - (V[i-1, j] - V[i+1, j]) / 2 / delta_y
        Ex[i, j] = u
        Ey[i, j] = v


# %%
# save
with open('V2.txt', 'wb') as f:
    pickle.dump(V, f)

# %%
x = np.linspace(X_min, X_max, n)
y = np.linspace(Y_min, Y_max, m)
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, V)
plt.quiver(X, Y, Ex, -Ey)
plt.show()