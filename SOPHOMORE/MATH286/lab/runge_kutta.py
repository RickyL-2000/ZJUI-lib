# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .analysis import analyse

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def equal(a, b):
    return abs(a - b) < 0.0000001

# %%
def runge_kutta_3rd(f, a, b, t0, y0, h, alpha=(1/6, 2/3, 1/6), beta=(1/2, 1/2, 1.0, -1.0, 2.0)):
    assert a <= t0 <= b
    assert equal(sum(alpha), 1.0)
    assert equal(beta[0] * alpha[1] + beta[2] * alpha[2], 0.5)
    assert equal(beta[2], beta[3] + beta[4])
    assert equal(beta[0], beta[1])
    assert equal(beta[0] * beta[0] * alpha[1] + beta[2] * beta[2] * alpha[2], 1/3)
    assert equal(beta[0] * beta[4] * alpha[2], 1/6)

    t_list, y_list = [], []
    ti, yi = t0, y0
    t_temp, y_temp = [], []
    for _ in range(round((t0 - a)/h)):
        k1 = h * f(ti, yi)
        k2 = h * f(ti - beta[0]*h, yi - beta[1]*k1)
        k3 = h * f(ti - beta[2]*h, yi - beta[3]*k1 - beta[4]*k2)
        y_ = yi - alpha[0] * k1 - alpha[1] * k2 - alpha[2] * k3
        t_temp.append(ti-h)
        y_temp.append(y_)
        ti, yi = ti-h, y_
    if t_temp and y_temp:
        t_temp.reverse(), y_temp.reverse()
        t_list.extend(t_temp), y_list.extend(y_temp)

    t_list.append(t0), y_list.append(y0)

    ti, yi = t0, y0
    for _ in range(round((b - ti)/h)):
        k1 = h * f(ti, yi)
        k2 = h * f(ti + beta[0] * h, yi + beta[1] * k1)
        k3 = h * f(ti + beta[2] * h, yi + beta[3] * k1 + beta[4] * k2)
        y_ = yi + alpha[0] * k1 + alpha[1] * k2 + alpha[2] * k3
        t_list.append(ti+h)
        y_list.append(y_)
        ti, yi = ti + h, y_

    return t_list, y_list

# %%
# 确定 f1 的区间
df1 = pd.DataFrame()
a1 = -1.0
b1 = 1.0
df1['t'] = np.linspace(a1, b1, int((b1 - a1) / 0.1 + 1))
t1_1, y1_1 = runge_kutta_3rd(f1, a1, b1, 0, 1, 0.1)
t1_2, y1_2 = runge_kutta_3rd(f1, a1, b1, 0, 1, 0.05)
t1_3, y1_3 = runge_kutta_3rd(f1, a1, b1, 0, 1, 0.01)
t1_4, y1_4 = runge_kutta_3rd(f1, a1, b1, 0, 1, 0.001)
df1['y with h=0.1'] = [y1_1[i] for i in range(0, len(y1_1), round(0.1 / 0.1))]
df1['y with h=0.05'] = [y1_2[i] for i in range(0, len(y1_2), round(0.1 / 0.05))]
df1['y with h=0.01'] = [y1_3[i] for i in range(0, len(y1_3), round(0.1 / 0.01))]
df1['y with h=0.001'] = [y1_4[i] for i in range(0, len(y1_4), round(0.1 / 0.001))]

# %%
plt.plot(t1_1, y1_1)
plt.show()
plt.plot(t1_2, y1_2)
plt.show()
plt.plot(t1_3, y1_3)
plt.show()
plt.plot(t1_4, y1_4)
plt.show()

# %%
print("runge_kutta_3rd h = 0.1: ", y1_1[-1])
print("runge_kutta_3rd h = 0.01: ", y1_2[-1])
print("runge_kutta_3rd h = 0.001: ", y1_3[-1])

# %%
print(df1)

# %%
