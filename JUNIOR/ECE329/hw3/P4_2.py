# %%
from scipy import integrate
import numpy as np
# from math import cos, sin, pi
from numpy import cos, sin, pi
import matplotlib.pyplot as plt
epsilon = 8.854e-12

# %%
def V_i(theta, x, y, z, Qi):
    return Qi / ((x - cos(theta))**2 + (y - sin(theta))**2 + z**2)**0.5

# %%
################# x-y plane #################
n = 1000
h = 0.01
x = np.linspace(-5, 5, int(5/h) + 1)
y = np.linspace(-5, 5, int(5/h) + 1)
theta = np.linspace(0, 2*pi, n + 1)
V = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
for i in range(int(5/h)+1):
    if i % 10 == 0:
        print("i = {}".format(i))
    for j in range(int(5/h)+1):
        if x[i]**2 + y[j]**2 <= 1:
            continue
        for phi in theta:
            V[i][j] -= V_i(phi, x[i], y[j], 0, 1/n)
        V[i, j] /= 4*pi*epsilon

# %%
import threading
import time
def main_threaded(V, theta, x, y, n, h, max_threads=32):

    width = int(5/h) + 1
    idx_queue = [idx for idx in range(width*width - 1, -1, -1)]

    def process_queue():
        while True:
            try:
                idx = idx_queue.pop()
            except IndexError:
                break

            if idx % 1000 == 0:
                print(idx)

            for phi in theta:
                i = idx // width
                j = idx % width
                V[i][j] -= V_i(phi, x[i], y[j], 0, 1/n)
            V[i, j] /= 4*pi*epsilon
    
    threads = []
    while threads or idx_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < max_threads and idx_queue:
            thread = threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        time.sleep(1)
            
# %%
n = 1000
h = 0.01
x = np.linspace(-5, 5, int(5/h) + 1)
y = np.linspace(-5, 5, int(5/h) + 1)
theta = np.linspace(0, 2*pi, n + 1)
V_xy = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
main_threaded(V_xy, theta, x, y, n, h)

# %%
plt.contour(x, y, V_xy, 100)

# %%
################# x-z plane #################
def xz_threaded(V, theta, x, z, n, h, max_threads=32):

    width = int(5/h) + 1
    idx_queue = [idx for idx in range(width*width - 1, -1, -1)]

    def process_queue():
        while True:
            try:
                idx = idx_queue.pop()
            except IndexError:
                break

            if idx % 1000 == 0:
                print(idx)

            for phi in theta:
                i = idx // width
                j = idx % width
                V[i][j] -= V_i(phi, x[i], 0, z[j], 1/n)
            V[i, j] /= 4*pi*epsilon
    
    threads = []
    while threads or idx_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < max_threads and idx_queue:
            thread = threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        time.sleep(1)
            
# %%
n = 1000
h = 0.01
x = np.linspace(-5, 5, int(5/h) + 1)
z = np.linspace(-5, 5, int(5/h) + 1)
theta = np.linspace(0, 2*pi, n + 1)
V_xz = np.zeros(shape=(int(5/h)+1, int(5/h)+1))
main_threaded(V_xz, theta, x, z, n, h)
