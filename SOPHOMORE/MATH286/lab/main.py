# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Tuple
from SOPHOMORE.MATH286.lab.euler import euler_explicit, \
                                        euler_implicit, \
                                        euler_improved, \
                                        euler_trapezium
from SOPHOMORE.MATH286.lab.runge_kutta import runge_kutta_3rd, \
                                              runge_kutta_4th
from SOPHOMORE.MATH286.lab.adams import adams_monlton, \
                                        adams_bashforth, \
                                        simpson, \
                                        hamming
from SOPHOMORE.MATH286.lab.analysis import analyse_step_len, \
                                           analyse_time, \
                                           analyse_memory

# if run in ipython
base_dir = os.getcwd() + '/SOPHOMORE/MATH286/lab'

# %%
a1, b1 = -2.5, 1.0
a2, b2 = -50.0, 0.5

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
if __name__ == "__main__":
    pass

# %%
""" 1. step-length analysis """
# %%
for i in range(1, 3):
    if i == 1:
        h1 = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)
        f = f1
        a, b = a1, b1
    else:
        h1 = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)
        f = f2
        a, b = a2, b2
    df1_1 = analyse_step_len(f, euler_explicit, a, b, 0, 1, *h1)
    df1_2 = analyse_step_len(f, euler_implicit, a, b, 0, 1, *h1)
    df1_3 = analyse_step_len(f, euler_trapezium, a, b, 0, 1, *h1)
    df1_4 = analyse_step_len(f, euler_improved, a, b, 0, 1, *h1)
    df1_5 = analyse_step_len(f, runge_kutta_3rd, a, b, 0, 1, *h1)
    df1_6 = analyse_step_len(f, runge_kutta_4th, a, b, 0, 1, *h1)
    df1_7 = analyse_step_len(f, adams_monlton, a, b, 0, 1, *h1)
    df1_8 = analyse_step_len(f, adams_bashforth, a, b, 0, 1, *h1)

    df1_1.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_explicit.csv'.format(i), index=False)
    df1_2.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_implicit.csv'.format(i), index=False)
    df1_3.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_trapezium.csv'.format(i), index=False)
    df1_4.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_improved.csv'.format(i), index=False)
    df1_5.to_csv(base_dir + '/data/step_length_analysis/ivp{}_runge_kutta_3rd.csv'.format(i), index=False)
    df1_6.to_csv(base_dir + '/data/step_length_analysis/ivp{}_runge_kutta_4th.csv'.format(i), index=False)
    df1_7.to_csv(base_dir + '/data/step_length_analysis/ivp{}_adams_monlton.csv'.format(i), index=False)
    df1_8.to_csv(base_dir + '/data/step_length_analysis/ivp{}_adams_bashforth.csv'.format(i), index=False)

# %%
