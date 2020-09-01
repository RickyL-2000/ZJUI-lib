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
def analyse(f, method, a, b, t0, y0, h=(0.01, 0.005, 0.001)):
    """
    The main process to analyse a set of results with different step lengths
    :param f: the f function of the IVP
    :param method: the numerical method
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: a list of step lengths to be analysed
    :return: a DataFrame of numerical results
    """
    df = pd.DataFrame()
    space = h[0]
    df['t'] = np.linspace(a, b, round((b - a) / space) + 1)
    for i in range(len(h)):
        t, y = method(f, a, b, t0, y0, h[i])
        df['y with h='+str(h[i])] = [y[j] for j in range(0, len(y), round(space / h[i]))]

    return df

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
a1 = -3.0
b1 = 1.0
df1 = analyse(f1, euler_explicit, a1, b1, 0, 1, h=(0.01, 0.005, 0.001))

# %%
pd.set_option('display.max_rows', None)
print(df1)

# %%
# 确定 f2 的区间
a2 = -30.0
b2 = 5.0
df2 = analyse(f2, euler_explicit, a2, b2, 0, 1, h=(0.01, 0.005, 0.001))

# %%
print(df2)
