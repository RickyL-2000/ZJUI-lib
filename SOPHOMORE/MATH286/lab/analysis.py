# %%
import numpy as np
import pandas as pd

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
