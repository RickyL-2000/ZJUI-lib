# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
xx = np.linspace(-20, 20, 410)
yy = -xx*xx*xx
zz = [0.0] * len(xx)
plt.plot(xx, yy, 'k', xx, zz, 'k')
font = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 30
}
plt.xticks([])
plt.yticks([])
plt.xlabel('y', font)
plt.ylabel("y'", font)
# plt.annotate('-t', xy=(0, 10), xytext=(0, -20), xycoords=(0, 0), fontsize=30)
plt.show()
