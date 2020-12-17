# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Tuple
from SOPHOMORE.MATH286.lab.euler import euler_explicit, euler_implicit, euler_improved, euler_trapezium
from SOPHOMORE.MATH286.lab.runge_kutta import runge_kutta_3rd, runge_kutta_4th
from SOPHOMORE.MATH286.lab.adams import adams_monlton, adams_bashforth, simpson, hamming
import time
from memory_profiler import profile

base_dir = os.getcwd()

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def analyse_step_len(f, method, a, b, t0, y0, *h, **params):
    """
    analyse the affect of step length on accuracy

    :param f: the f function of the IVP
    :param method: the numerical method
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: a list of step lengths to be analysed, h=(0.01, 0.005, 0.001)
    :param params: the params for the certain numerical method
    :return: pd.DataFrame() whose columns are results of different step length
    """
    if not h:
        h = (0.01, 0.005, 0.001)

    df = pd.DataFrame()
    space = h[-1]
    df['t'] = np.linspace(a, b, round((b - a) / space) + 1)
    for i in range(len(h)):
        df['y with h=' + str(h[i])] = np.nan
        t, y = method(f, a, b, t0, y0, h[i], **params)
        # df['y with h=' + str(h[i])] = [y[j] for j in range(0, len(y), round(space / h[i]))]
        l = [np.nan] * len(df)
        for j in range(0, len(y)):
            # df['y with h=' + str(h[i])].loc[round(j * h[i] / space)] = y[j]
            l[round(j * h[i] / space)] = y[j]
        df['y with h=' + str(h[i])] = l

    return df

# %%
def analyse_time(f, method, a, b, t0, y0, h, epochs=10, **params) -> float:
    """
    :param method: the method to calc the time
    :param epochs: how many iterations
    :param params: the params for 'method'
    :return: the average time computing the method (in microseconds)
    """
    assert epochs > 0
    t_start = time.time() * 1000
    for _ in range(epochs):
        t, y = method(f, a, b, t0, y0, h, **params)
    t_end = time.time() * 1000
    return (t_end - t_start) / epochs

# %%
@profile(precision=6)
def analyse_memory(f, method, a, b, t0, y0, h, **params):
    t, y = method(f, a, b, t0, y0, h, **params)


