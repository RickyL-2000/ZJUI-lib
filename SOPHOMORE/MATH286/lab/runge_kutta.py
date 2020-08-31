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

    t_list = []
    y_list = []
    ti = t0
    yi = y0
    t_temp = []
    y_temp = []
    if t0 > a:
        for _ in range(round((t0 - a)/h)):
            k1 = h * f(ti, yi)
            k2 = h * f(ti - beta[0]*h, yi - beta[1]*k1)
            k3 = h * f(ti - beta[2]*h, yi - beta[3]*k1 - beta[4]*k2)
            y_ = yi - alpha[0] * k1 - alpha[1] * k2 - alpha[2] * k3
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
    for _ in range(round((b - ti)/h)):
        k1 = h * f(ti, yi)
        k2 = h * f(ti + beta[0] * h, yi + beta[1] * k1)
        k3 = h * f(ti + beta[2] * h, yi + beta[3] * k1 + beta[4] * k2)
        y_ = yi + alpha[0] * k1 + alpha[1] * k2 + alpha[2] * k3
        t_list.append(ti+h)
        y_list.append(y_)

    return t_list, y_list

# %%
# 确定 f1 的区间
