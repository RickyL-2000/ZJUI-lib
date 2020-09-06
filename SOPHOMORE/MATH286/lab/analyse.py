# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Tuple
from .euler import euler_explicit, euler_implicit, euler_improved, euler_trapezium
from .runge_kutta import runge_kutta_3rd, runge_kutta_4th
from .adams import adams_monlton, adams_bashforth, simpson, hamming

base_dir = os.getcwd()

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def analyse_step_len(f, method, a, b, t0, y0, *h, **params):
    if not h:
        h = (0.01, 0.005, 0.001)

    df = pd.DataFrame()
    space = h[0]
    df['t'] = np.linspace(a, b, round((b - a) / space) + 1)
    for i in range(len(h)):
        t, y = method(f, a, b, t0, y0, h[i], **params)
        df['y with h=' + str(h[i])] = [y[j] for j in range(0, len(y), round(space / h[i]))]

    return df

# %%
def analyse_time(f, method, a, b, t0, y0, h, **params, epochs=10):
    df = pd.DataFrame()
    pass
