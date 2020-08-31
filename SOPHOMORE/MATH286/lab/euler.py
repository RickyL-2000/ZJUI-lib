# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def euler_explicit(f, a, b, t0, y0, h):
    assert a <= t0 <= b
    t_list = []
    y_list = []
    ti = t0
    yi = y0
    t_temp = []
    y_temp = []
    if t0 > a:
        # while ti-h >= a:
        for _ in range(round((t0 - a)/h)):
            y_ = yi - h * f(ti, yi)
            t_temp.append(ti-h)
            y_temp.append(y_)
            ti, yi = ti-h, y_
    if t_temp and y_temp:
        t_temp.reverse()
        y_temp.reverse()
        t_list.extend(t_temp)
        y_list.extend(y_temp)

    t_list.append(t0)
    y_list.append(y0)

    ti = t0
    yi = y0
    # while ti+h <= b:
    for _ in range(round((b - ti)/h)):
        y_ = yi + h * f(ti, yi)
        t_list.append(ti+h)
        y_list.append(y_)
        ti, yi = ti+h, y_

    return t_list, y_list

# %%
# 确定 f1 的区间
df1 = pd.DataFrame()
a1 = -1.0
b1 = 1.0
df1['t'] = np.linspace(a1, b1, int((b1 - a1) / 0.1 + 1))
t1_1, y1_1 = euler_explicit(f1, a1, b1, 0, 1, 0.1)
t1_2, y1_2 = euler_explicit(f1, a1, b1, 0, 1, 0.01)
t1_3, y1_3 = euler_explicit(f1, a1, b1, 0, 1, 0.001)
df1['y with h=0.1'] = [y1_1[i] for i in range(0, len(y1_1), round(0.1 / 0.1))]
df1['y with h=0.01'] = [y1_2[i] for i in range(0, len(y1_2), round(0.1 / 0.01))]
df1['y with h=0.001'] = [y1_3[i] for i in range(0, len(y1_3), round(0.1 / 0.001))]

# %%
plt.plot(t1_1, y1_1)
plt.show()
plt.plot(t1_2, y1_2)
plt.show()
plt.plot(t1_3, y1_3)
plt.show()

# %%
print("euler h = 0.1: ", y1_1[-1])
print("euler h = 0.01: ", y1_2[-1])
print("euler h = 0.001: ", y1_3[-1])

# %%
print(df1)

# %%
# 确定 f2 的区间
df2 = pd.DataFrame()
a2 = -1.0
b2 = 1.0
df2['t'] = np.linspace(a2, b2, int((b2 - a2) / 0.1 + 1))
t2_1, y2_1 = euler_explicit(f2, a2, b2, 0, 1, 0.1)
t2_2, y2_2 = euler_explicit(f2, a2, b2, 0, 1, 0.01)
t2_3, y2_3 = euler_explicit(f2, a2, b2, 0, 1, 0.001)
df2['y with h=0.1'] = [y2_1[i] for i in range(0, len(y2_1), round(0.1 / 0.1))]
df2['y with h=0.01'] = [y2_2[i] for i in range(0, len(y2_2), round(0.1 / 0.01))]
df2['y with h=0.001'] = [y2_3[i] for i in range(0, len(y2_3), round(0.1 / 0.001))]

# %%
plt.plot(t2_1, y2_1)
plt.show()
plt.plot(t2_2, y2_2)
plt.show()
plt.plot(t2_3, y2_3)
plt.show()

# %%
print("euler h = 0.1: ", y2_1[-1])
print("euler h = 0.01: ", y2_2[-1])
print("euler h = 0.001: ", y2_3[-1])

# %%
print(df2)
