# %%
import pandas as pd
import numpy as np
import os
from typing import Tuple, List
from SOPHOMORE.MATH286.lab.euler import euler_trapezium, euler_improved, euler_implicit, euler_explicit
from SOPHOMORE.MATH286.lab.runge_kutta import runge_kutta_4th, runge_kutta_3rd

base_dir = os.getcwd()

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def analyse(f, method, a, b, t0, y0, h=(0.01, 0.005, 0.001)):
    pass

# %%
def lin_multistep(f, a, b, t0, y0, h, **kwargs) -> Tuple[np.ndarray, np.ndarray]:
    """
    The general linear multi-step method

    :param f: the f function
    :param a: left bound
    :param b: right bound
    :param t0: initial t
    :param y0: initial y
    :param h: the step length (**can be negative to predict the left part**)
    :param kwargs: params to be determined.
                    default:
                    k: number of steps, k=3;
                    alpha: the first set of params, alpha=(1, 0, 0);
                    beta: the second set of params, beta=(0, 23/12, -4/3, 5/12);
                    pre_method: the method to predict the points within the k steps, pre_method=runge_kutta_4th;
                    threshold: the threshold to control the iteration of implicit part, threshold=1e-4;
                    epochs: the upper bound of the epochs to iter to control the iteration of implicit part, epochs=100;
    :return: list of numerical results of t and y
    """

    def __update(t_list: List, y_list: List, f_list: List, f, h: float, k: int, alpha: Tuple, beta: Tuple,
                 threshold=1e-6, epochs=100) -> float:
        """
        Choose to whether update the y_{i+1} explicitly or implicitly

        :param t_list: the current t_i sequence (the t_{i+1} is to be predicted) (can be reversed to predict the left part)
        :param y_list: the current y_i sequence (the y_{i+1} is to be predicted) (can be reversed to predict the left part)
        :param h: the step length (**can be negative to predict the left part**)
        :param threshold: the threshold to control the iteration of implicit part
        :param epochs: the upper bound of the epochs to iter to control the iteration of implicit part
        :return: the new numerical result of y_{i+1}
        """
        if beta[0] == 0:
            # explicit
            return sum([alpha[i] * y_list[-i - 1] for i in range(k)]) + \
                   h * sum([beta[i+1] * f_list[-i - 1] for i in range(k)])
        else:
            # implicit
            epoch = 0
            y_ = sum([alpha[i] * y_list[-i - 1] for i in range(k)]) + \
                h * sum([beta[i + 1] * f_list[-i - 1] for i in range(k)])
            f_ = f(t_list[-1] + h, y_)
            while True:
                epoch += 1
                y__ = sum([alpha[i] * y_list[-i - 1] for i in range(k)]) + \
                    h * (beta[0] * f_ + sum([beta[i+1] * f_list[-i - 1] for i in range(k)]))
                f__ = f(t_list[-1] + h, y__)
                if abs(y__ - y_) < threshold or epoch > epochs:
                    break
                y_ = y__
                f_ = f__
            return y_

    # NOTE: The check of the parameters are too sophisticated so just skip it

    if 'k' in kwargs:
        k = kwargs['k']
        assert k > 0
    else:
        k = 3
    if 'alpha' in kwargs:
        alpha = kwargs['alpha']
        assert len(alpha) == k
    else:
        alpha = (1, 0, 0)
    if 'beta' in kwargs:
        beta = kwargs['beta']
        assert len(beta) == k+1
    else:
        beta = (0, 23/12, -4/3, 5/12)
    if 'pre_method' in kwargs:
        pre_method = kwargs['pre_method']
    else:
        pre_method = runge_kutta_4th
    if 'threshold' in kwargs:
        threshold = kwargs['threshold']
    else:
        threshold = 1e-6
    if 'epochs' in kwargs:
        epochs = kwargs['epochs']
    else:
        epochs = 100

    assert alpha and beta
    assert len(alpha) == k and len(beta) == k+1

    ############ left ############
    t_left, y_left = pre_method(f, max(t0 - (k-1) * h, a), t0, t0, y0, h)
    t_left = t_left.tolist()
    y_left = y_left.tolist()
    f_left = [f(ti, yi) for ti, yi in zip(t_left, y_left)]
    t_list, y_list, f_list = t_left, y_left, f_left     # with t0 included

    if round((t0 - a) / h + 1) > k:
        # have to multi-step
        t_temp, y_temp, f_temp = t_left[::-1], y_left[::-1], f_left[::-1]   # reverse the list to grow left-wards
        ti, yi = t_temp[-1], y_temp[-1]
        for _ in range(round((t0 - a) / h + 1 - k)):
            y_ = __update(t_temp, y_temp, f_temp, f, -h, k, alpha, beta, threshold, epochs)    # -h indicates left
            f_ = f(ti-h, y_)
            t_temp.append(ti-h)
            y_temp.append(y_)
            f_temp.append(f_)
            ti, yi = ti-h, y_
        t_list, y_list, f_list = t_temp[::-1], y_temp[::-1], f_temp[::-1]    # reverse, with t0 included

    ############ right ############
    if len(t_list) < k:
        # the left part is not enough for multi-step
        t_temp, y_temp = pre_method(f, t0, min(b, t0 + (k - len(t_list)) * h), t0, y0, h)   # with t0 included
        f_temp = [f(ti, yi) for ti, yi in zip(t_temp, y_temp)]
        t_list, y_list, f_list = t_list.extend(t_temp[1:]), y_list.extend(y_temp[1:]), f_list.extend(f_temp[1:])
    ti, yi = t_list[-1], y_list[-1]
    for _ in range(round((b - ti) / h)):
        # y_ = sum([alpha[i] * y_list[-i-1] for i in range(k)]) + \
        #          h * sum([beta[i+1] * f_list[-i-1] for i in range(k)])
        y_ = __update(t_list, y_list, f_list, f, h, k, alpha, beta, threshold, epochs)  # positive h indicates right
        f_ = f(ti+h, y_)
        t_list.append(ti+h)
        y_list.append(y_)
        f_list.append(f_)
        ti, yi = ti+h, y_

    return np.array(t_list), np.array(y_list)


# %%
def adams_bashforth(f, a, b, t0, y0, h, **kwargs) -> Tuple[np.ndarray, np.ndarray]:

    if 'threshold' in kwargs:
        threshold = kwargs['threshold']
    else:
        threshold = 1e-4
    if 'epochs' in kwargs:
        epochs = kwargs['epochs']
    else:
        epochs = 100

    k = 4
    alpha = (1, 0, 0, 0)
    beta = (0, 55 / 24, -59 / 24, 37 / 24, -9 / 24)

    params = {
        'k': k,
        'alpha': alpha,
        'beta': beta,
        'threshold': threshold,
        'epochs': epochs,
    }
    return lin_multistep(f, a, b, t0, y0, h, **params)

# %%
def adams_monlton(f, a, b, t0, y0, h, **kwargs) -> Tuple[np.ndarray, np.ndarray]:

    if 'threshold' in kwargs:
        threshold = kwargs['threshold']
    else:
        threshold = 1e-10
    if 'epochs' in kwargs:
        epochs = kwargs['epochs']
    else:
        epochs = 100

    k = 3
    alpha = (1, 0, 0)
    beta = (9/24, 19/24, -5/24, 1/24)

    params = {
        'k': k,
        'alpha': alpha,
        'beta': beta,
        'threshold': threshold,
        'epochs': epochs,
    }
    return lin_multistep(f, a, b, t0, y0, h, **params)

# %%
def simpson(f, a, b, t0, y0, h, **kwargs) -> Tuple[np.ndarray, np.ndarray]:
    if 'threshold' in kwargs:
        threshold = kwargs['threshold']
    else:
        threshold = 1e-4
    if 'epochs' in kwargs:
        epochs = kwargs['epochs']
    else:
        epochs = 100

    k = 3
    alpha = (0, 1, 0)
    beta = (1/3, 4/3, 1/3, 0)

    params = {
        'k': k,
        'alpha': alpha,
        'beta': beta,
        'threshold': threshold,
        'epochs': epochs,
    }
    return lin_multistep(f, a, b, t0, y0, h, **params)

# %%
def hamming(f, a, b, t0, y0, h, **kwargs) -> Tuple[np.ndarray, np.ndarray]:
    if 'threshold' in kwargs:
        threshold = kwargs['threshold']
    else:
        threshold = 1e-4
    if 'epochs' in kwargs:
        epochs = kwargs['epochs']
    else:
        epochs = 100

    k = 3
    alpha = (9/8, 0, -1/8)
    beta = (3/8, 3/4, -3/8, 0)

    params = {
        'k': k,
        'alpha': alpha,
        'beta': beta,
        'threshold': threshold,
        'epochs': epochs,
    }
    return lin_multistep(f, a, b, t0, y0, h, **params)
