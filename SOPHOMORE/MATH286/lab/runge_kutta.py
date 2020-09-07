# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Tuple

base_dir = os.getcwd() + "/SOPHOMORE/MATH286/lab"
# base_dir = os.getcwd()

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def equal(a, b):
    return abs(a - b) < 0.0000001

# %%
def analyse_step_len(f, method, a, b, t0, y0, h=(0.01, 0.005, 0.001)):
    df = pd.DataFrame()
    space = h[0]
    df['t'] = np.linspace(a, b, round((b - a) / space) + 1)
    for i in range(len(h)):
        t, y = method(f, a, b, t0, y0, h[i])
        df['y with h='+str(h[i])] = [y[j] for j in range(0, len(y), round(space / h[i]))]

    return df

# %%
def runge_kutta_3rd(f, a, b, t0, y0, h, **params) -> Tuple[np.ndarray, np.ndarray]:
    """
    3-order-Runge Kutta method
    :param f: the f function
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: step length
    :param params: params to be determined, should contain 'alpha' and 'beta' tuples.
                   default: kwargs['alpha'] = (1/6, 2/3, 1/6);
                            kwargs['beta'] = (1/2, 1/2, 1.0, -1.0, 2.0)
    :return: list of numerical results of t and y
    """
    assert a <= t0 <= b

    if 'alpha' in params:
        alpha = params['alpha']
    else:
        alpha = (1/6, 2/3, 1/6)
    if 'beta' in params:
        beta = params['beta']
    else:
        beta = (1/2, 1/2, 1.0, -1.0, 2.0)

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
    for _ in range(round((b - t0)/h)):
        k1 = h * f(ti, yi)
        k2 = h * f(ti + beta[0] * h, yi + beta[1] * k1)
        k3 = h * f(ti + beta[2] * h, yi + beta[3] * k1 + beta[4] * k2)
        y_ = yi + alpha[0] * k1 + alpha[1] * k2 + alpha[2] * k3
        t_list.append(ti+h)
        y_list.append(y_)
        ti, yi = ti + h, y_

    return np.array(t_list), np.array(y_list)

# %%
def runge_kutta_4th(f, a, b, t0, y0, h, **params) -> Tuple[np.ndarray, np.ndarray]:
    """
    4-order-Runge Kutta method

    :param f: the f function
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: step length
    :param params: params to be determined, should contain 'alpha' and 'beta' tuples.
                   default: kwargs['alpha'] = (1/6, 1/3, 1/3, 1/6);
                            kwargs['beta'] = (1/2, 1/2, 1/2, 0, 1/2, 1, 0, 0, 1)
    :return: list of numerical results of t and y
    """
    # NOTE: The check of the parameters are too sophisticated so just skip it

    if 'alpha' in params:
        alpha = params['alpha']
    else:
        alpha = (1/6, 1/3, 1/3, 1/6)
    if 'beta' in params:
        beta = params['beta']
    else:
        beta = (1/2, 1/2, 1/2, 0, 1/2, 1, 0, 0, 1)

    t_list, y_list = [], []
    ti, yi = t0, y0
    t_temp, y_temp = [], []
    for _ in range(round((t0 - a) / h)):
        k1 = h * f(ti, yi)
        k2 = h * f(ti - beta[0] * h, yi - beta[1] * k1)
        k3 = h * f(ti - beta[2] * h, yi - beta[3] * k1 - beta[4] * k2)
        k4 = h * f(ti - beta[5] * h, yi - beta[6] * k1 - beta[7] * k2 - beta[8] * k3)
        y_ = yi - alpha[0] * k1 - alpha[1] * k2 - alpha[2] * k3 - alpha[3] * k4
        t_temp.append(ti - h)
        y_temp.append(y_)
        ti, yi = ti - h, y_
    if t_temp and y_temp:
        t_temp.reverse(), y_temp.reverse()
        t_list.extend(t_temp), y_list.extend(y_temp)

    t_list.append(t0), y_list.append(y0)

    ti, yi = t0, y0
    for _ in range(round((b - t0) / h)):
        k1 = h * f(ti, yi)
        k2 = h * f(ti + beta[0] * h, yi + beta[1] * k1)
        k3 = h * f(ti + beta[2] * h, yi + beta[3] * k1 + beta[4] * k2)
        k4 = h * f(ti + beta[5] * h, yi + beta[6] * k1 + beta[7] * k2 + beta[8] * k3)
        y_ = yi + alpha[0] * k1 + alpha[1] * k2 + alpha[2] * k3 + alpha[3] * k4
        t_list.append(ti + h)
        y_list.append(y_)
        ti, yi = ti + h, y_

    return np.array(t_list), np.array(y_list)


# %%
if __name__ == "__main__":
    a, b = -3, 1
    params = {
        'alpha': (1 / 6, 2 / 3, 1 / 6),
        'beta': (1 / 2, 1 / 2, 1.0, -1.0, 2.0)
    }
    t, y = runge_kutta_3rd(f1, a, b, 0, 1, 0.001, **params)

    # %%
    a1 = -3.0
    b1 = 1.0
    h1 = (0.01, 0.005, 0.001)
    df1_1 = analyse_step_len(f1, runge_kutta_3rd, a1, b1, 0, 1, h=h1)
    df1_2 = analyse_step_len(f1, runge_kutta_4th, a1, b1, 0, 1, h=h1)

    # %%
    df1_1.to_csv(base_dir + "/data/ivp1_runge_kutta_3rd.csv", index=False)
    df1_2.to_csv(base_dir + "/data/ivp1_runge_kutta_4th.csv", index=False)

    # %%
    a2 = -50.0
    b2 = 1.0
    h2 = (0.01, 0.005, 0.001)
    df2_1 = analyse_step_len(f2, runge_kutta_3rd, a2, b2, 0, 1, h=h2)
    df2_2 = analyse_step_len(f2, runge_kutta_4th, a2, b2, 0, 1, h=h2)

    # %%
    df2_1.to_csv(base_dir + "/data/ivp2_runge_kutta_3rd.csv", index=False)
    df2_2.to_csv(base_dir + "/data/ivp2_runge_kutta_4th.csv", index=False)

# %%
################ 以下试水专用 ##################
# a, b = -3, 1
# params = {
#     'alpha': (1/6, 2/3, 1/6),
#     'beta': (1/2, 1/2, 1.0, -1.0, 2.0)
# }
# t, y = runge_kutta_3rd(f1, a, b, 0, 1, 0.001, **params)
