# %%
import matplotlib.pyplot as plt
import numpy as np
import pickle

# %%
X_min, X_max = 0, 1
Y_min, Y_max = 0, 0.5
x_min, x_max = 0.3, 0.7
y_min, y_max = 0.2, 0.3

V_outer, V_inner = 0, 1
delta_x, delta_y = 0.01, 0.01

# %%
####################### part 1 ########################
N = 10000
m = int((Y_max-Y_min)/delta_y+1)
n = int((X_max-X_min)/delta_x+1)
V = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
            V[i, j] = V_inner

V_old = np.copy(V)
for _ in range(N):
    for i in range(1, m-1):
        for j in range(1, n-1):
            if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
                continue
            V[i, j] = ( (V_old[i+1, j] + V_old[i-1, j])/delta_x**2 + (V_old[i, j+1] + V_old[i, j-1])/delta_y**2 ) / (2/delta_x**2 + 2/delta_y**2)
    V_old = np.copy(V)

# %%
# save
with open('V.txt', 'wb') as f:
    pickle.dump(V, f)

# %%
# load
# with open('V.txt', 'rb') as f:
#     V = pickle.load(f)

# %%
plt.imshow(V)
# plt.xticks(np.linspace(X_min, X_max, n+1))
# plt.yticks(np.linspace(Y_min, Y_max, m+1))
plt.xticks([])
plt.yticks([])
plt.title('V Plot for $N_{iter}$ = 10000')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

# %%
####################### part 2 ########################
E = np.zeros((m, n))
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
        E[i, j] = (u*u + v*v)**0.5
        Ex[i, j] = u
        Ey[i, j] = v

# %%
plt.imshow(E)
plt.xticks([])
plt.yticks([])
plt.title('E')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

# %%
maxE = np.max(E)
maxi, maxj = np.where(abs(E - maxE) <= 0.1)
maxx = maxj * delta_x
maxy = Y_max - maxi * delta_y
max_xy = np.append(maxx, maxy).reshape(2, -1).T
print("Points where E is at its maxima:")
print(max_xy)

# %%
####################### part 3 ########################
x = np.linspace(X_min, X_max, n)
y = np.linspace(Y_min, Y_max, m)
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, V)
plt.quiver(X, Y, Ex, -Ey)

# %%
####################### part 4 ########################
def error(V, V_bm):
    # return ((V - V_bm)*(V - V_bm)).mean() / (V_bm * V_bm).mean()
    return np.linalg.norm(V-V_bm) / np.linalg.norm(V_bm)

def iter_sync(V, V_bm, N, m, n):
    V_old = np.copy(V)
    err = []
    for _ in range(N):
        for i in range(1, m-1):
            for j in range(1, n-1):
                if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
                    continue
                V[i, j] = ( (V_old[i+1, j] + V_old[i-1, j])/delta_x**2 + (V_old[i, j+1] + V_old[i, j-1])/delta_y**2 ) / (2/delta_x**2 + 2/delta_y**2)
        V_old = np.copy(V)
        err.append(error(V, V_bm))
    return err

def iter_nonsync(V, V_bm, N, m, n):
    err = []
    for _ in range(N):
        for i in range(1, m-1):
            for j in range(1, n-1):
                if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
                    continue
                V[i, j] = ( (V[i+1, j] + V[i-1, j])/delta_x**2 + (V[i, j+1] + V[i, j-1])/delta_y**2 ) / (2/delta_x**2 + 2/delta_y**2)
        err.append(error(V, V_bm))
    return err

# %%
N = 10000
m = int((Y_max-Y_min)/delta_y+1)
n = int((X_max-X_min)/delta_x+1)
V_sync = np.zeros((m, n))
V_nonsync = np.zeros((m, n))
V_old = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
            V_sync[i, j] = V_inner
            V_nonsync[i, j] = V_inner
            V_old[i, j] = V_inner

# sync
err_sync = []
for _ in range(N):
    for i in range(1, m-1):
        for j in range(1, n-1):
            if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
                continue
            V_sync[i, j] = ( (V_old[i+1, j] + V_old[i-1, j])/delta_x**2 + (V_old[i, j+1] + V_old[i, j-1])/delta_y**2 ) / (2/delta_x**2 + 2/delta_y**2)
    V_old = np.copy(V_sync)
    err_sync.append(np.linalg.norm(V-V_sync) / np.linalg.norm(V))

# nonsync
err_nonsync = []
for _ in range(N):
    for i in range(1, m-1):
        for j in range(1, n-1):
            if (y_min <= Y_max - i * delta_y <= y_max) and (x_min <= j * delta_x <= x_max):
                continue
            V_nonsync[i, j] = ( (V_nonsync[i+1, j] + V_nonsync[i-1, j])/delta_x**2 + (V_nonsync[i, j+1] + V_nonsync[i, j-1])/delta_y**2 ) / (2/delta_x**2 + 2/delta_y**2)
    err_nonsync.append(np.linalg.norm(V-V_nonsync) / np.linalg.norm(V))

# %%
plt.semilogy(err_sync, label='error_sync')
plt.semilogy(err_nonsync, label='error_nonsync')
plt.legend()
plt.title('Relative Error of Sync/nonsync Iteration')
plt.show()

# %%
