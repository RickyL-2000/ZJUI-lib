# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from .analysis import analyse

base_dir = os.getcwd() + "/SOPHOMORE/MATH286/lab"

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def euler_explicit(f, a, b, t0, y0, h):
    """
    Explicit Euler Method
    :param f: the f function
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: step length
    :return: list of numerical results of t and y
    """
    assert a <= t0 <= b
    t_list, y_list = [], []
    ti, yi = t0, y0
    t_temp, y_temp = [], []
    for _ in range(round((t0 - a)/h)):
        y_ = yi - h * f(ti, yi)
        t_temp.append(ti-h), y_temp.append(y_)
        ti, yi = ti-h, y_

    if t_temp and y_temp:
        t_temp.reverse(), y_temp.reverse()
        t_list.extend(t_temp), y_list.extend(y_temp)

    t_list.append(t0), y_list.append(y0)

    ti, yi = t0, y0
    # while ti+h <= b:
    for _ in range(round((b - ti)/h)):
        y_ = yi + h * f(ti, yi)
        t_list.append(ti+h), y_list.append(y_)
        ti, yi = ti+h, y_

    return t_list, y_list

# %%
def euler_implicit(f, a, b, t0, y0, h, threshold=1e-4, epochs=100):
    """
    Implicit (backward) Euler Method
    :param f: the f function
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: step length
    :param threshold: the threshold to control the iteration
    :param epochs: the maximum number of epochs used to control the iteration
    :return: list of numerical results of t and y
    """
    assert a <= t0 <= b
    t_list, y_list = [], []
    ti, yi = t0, y0
    t_temp, y_temp = [], []
    for _ in range(round((t0 - a)/h)):
        y_ = yi - h * f(ti, yi)
        epoch = 0
        while True:
            epoch += 1
            y__ = yi - h * f(ti-h, y_)
            if abs(y__ - y_) < threshold or epoch > epochs:
                break
            y_ = y__
        t_temp.append(ti-h), y_temp.append(y_)
        ti, yi = ti-h, y_

    if t_temp and y_temp:
        t_temp.reverse(), y_temp.reverse()
        t_list.extend(t_temp), y_list.extend(y_temp)

    t_list.append(t0), y_list.append(y0)

    ti, yi = t0, y0
    for _ in range(round((b - ti) / h)):
        y_ = yi + h * f(ti, yi)
        epoch = 0
        while True:
            epoch += 1
            y__ = yi + h * f(ti + h, y_)
            if abs(y__ - y_) < threshold or epoch > epochs:
                break
            y_ = y__
        t_list.append(ti + h), y_list.append(y_)
        ti, yi = ti + h, y_

    return t_list, y_list

# %%
def euler_trapezium(f, a, b, t0, y0, h, threshold=1e-4, epochs=50):
    """
    Implicit (backward) Euler Method
    :param f: the f function
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: step length
    :param threshold: the threshold to control the iteration
    :param epochs: the maximum number of epochs used to control the iteration
    :return: list of numerical results of t and y
    """
    assert a <= t0 <= b
    t_list, y_list = [], []
    ti, yi = t0, y0
    t_temp, y_temp = [], []
    for _ in range(round((t0 - a) / h)):
        y_ = yi - h * f(ti, yi)
        epoch = 0
        while True:
            epoch += 1
            y__ = yi - 0.5 * h * (f(ti, yi) + f(ti - h, y_))
            if abs(y__ - y_) < threshold or epoch > epochs:
                break
            y_ = y__
        t_temp.append(ti - h), y_temp.append(y_)
        ti, yi = ti - h, y_

    if t_temp and y_temp:
        t_temp.reverse(), y_temp.reverse()
        t_list.extend(t_temp), y_list.extend(y_temp)

    t_list.append(t0), y_list.append(y0)

    ti, yi = t0, y0
    for _ in range(round((b - ti) / h)):
        y_ = yi + h * f(ti, yi)
        epoch = 0
        while True:
            epoch += 1
            y__ = yi + 0.5 * h * (f(ti, yi) + f(ti + h, y_))
            if abs(y__ - y_) < threshold or epoch > epochs:
                break
            y_ = y__
        t_list.append(ti + h), y_list.append(y_)
        ti, yi = ti + h, y_

    return t_list, y_list

# %%
def euler_improved(f, a, b, t0, y0, h):
    assert a <= t0 <= b
    t_list, y_list = [], []
    ti, yi = t0, y0
    t_temp, y_temp = [], []
    for _ in range(round((t0 - a)/h)):
        y_ = yi - h * f(ti, yi)
        y_ = yi - 0.5 * h * (f(ti, yi) + f(ti-h, y_))
        t_temp.append(ti-h), y_temp.append(y_)
        ti, yi = ti-h, y_
    if t_temp and y_temp:
        t_temp.reverse(), y_temp.reverse()
        t_list.extend(t_temp), y_list.extend(y_temp)

    t_list.append(t0), y_list.append(y0)

    ti, yi = t0, y0
    for _ in range(round((b - ti)/h)):
        y_ = yi + h * f(ti, yi)
        y_ = yi + 0.5 * h * (f(ti, yi) + f(ti+h, y_))
        t_list.append(ti+h), y_list.append(y_)
        ti, yi = ti+h, y_

    return t_list, y_list

# %%
# pd.set_option('display.max_rows', None)
if __name__ == '__main__':
    pass

# %%
# 确定 f1 的区间
a1 = -3.0
b1 = 1.0
h1 = (0.01, 0.005, 0.001)
df1_1 = analyse(f1, euler_explicit, a1, b1, 0, 1, h=h1)
df1_2 = analyse(f1, euler_implicit, a1, b1, 0, 1, h=h1)
df1_3 = analyse(f1, euler_trapezium, a1, b1, 0, 1, h=h1)
df1_4 = analyse(f1, euler_improved, a1, b1, 0, 1, h=h1)

# %%
df1_1.to_csv(base_dir + "/data/ivp1_euler_explicit.csv", index=False)
df1_2.to_csv(base_dir + "/data/ivp1_euler_implicit.csv", index=False)
df1_3.to_csv(base_dir + "/data/ivp1_euler_trapezium.csv", index=False)
df1_4.to_csv(base_dir + "/data/ivp1_euler_improved.csv", index=False)

# %%
# 确定 f2 的区间
a2 = -100.0
b2 = 5.0
h2 = (0.01, 0.005, 0.001)
df2_1 = analyse(f2, euler_explicit, a2, b2, 0, 1, h=h2)
df2_2 = analyse(f2, euler_implicit, a2, b2, 0, 1, h=h2)
df2_3 = analyse(f2, euler_trapezium, a2, b2, 0, 1, h=h2)
df2_4 = analyse(f2, euler_improved, a2, b2, 0, 1, h=h2)

# %%
df2_1.to_csv(base_dir + "/data/ivp2_euler_explicit.csv", index=False)
df2_2.to_csv(base_dir + "/data/ivp2_euler_implicit.csv", index=False)
df2_3.to_csv(base_dir + "/data/ivp2_euler_trapezium.csv", index=False)
df2_4.to_csv(base_dir + "/data/ivp2_euler_improved.csv", index=False)
