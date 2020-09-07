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
""" 0. load the ground truth """
df1_truth = pd.read_csv(base_dir + '/data/ivp1_ground_truth.csv')
df2_truth = pd.read_csv(base_dir + '/data/ivp2_ground_truth.csv')
t1, y1 = df1_truth['Var1'].values, df1_truth['Var2'].values
t2, y2 = df2_truth['Var1'].values, df2_truth['Var2'].values

# %%
""" 1. step-length analysis """
# %%
for i in range(2, 3):
    if i == 1:
        h = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)
        f = f1
        a, b = a1, b1
    else:
        h = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)
        f = f2
        a, b = a2, b2
    df1_1 = analyse_step_len(f, euler_explicit, a, b, 0, 1, *h)
    df1_2 = analyse_step_len(f, euler_implicit, a, b, 0, 1, *h)
    df1_3 = analyse_step_len(f, euler_trapezium, a, b, 0, 1, *h)
    df1_4 = analyse_step_len(f, euler_improved, a, b, 0, 1, *h)
    df1_5 = analyse_step_len(f, runge_kutta_3rd, a, b, 0, 1, *h)
    df1_6 = analyse_step_len(f, runge_kutta_4th, a, b, 0, 1, *h)
    df1_7 = analyse_step_len(f, adams_monlton, a, b, 0, 1, *h)
    df1_8 = analyse_step_len(f, adams_bashforth, a, b, 0, 1, *h)

    df1_1.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_explicit.csv'.format(i), index=False, float_format="%.8f")
    df1_2.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_implicit.csv'.format(i), index=False, float_format="%.8f")
    df1_3.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_trapezium.csv'.format(i), index=False, float_format="%.8f")
    df1_4.to_csv(base_dir + '/data/step_length_analysis/ivp{}_euler_improved.csv'.format(i), index=False, float_format="%.8f")
    df1_5.to_csv(base_dir + '/data/step_length_analysis/ivp{}_runge_kutta_3rd.csv'.format(i), index=False, float_format="%.8f")
    df1_6.to_csv(base_dir + '/data/step_length_analysis/ivp{}_runge_kutta_4th.csv'.format(i), index=False, float_format="%.8f")
    df1_7.to_csv(base_dir + '/data/step_length_analysis/ivp{}_adams_monlton.csv'.format(i), index=False, float_format="%.8f")
    df1_8.to_csv(base_dir + '/data/step_length_analysis/ivp{}_adams_bashforth.csv'.format(i), index=False, float_format="%.8f")

# %%
""" 2. error analysis """
# %%
h = 0.001

t_1_1, y_1_1 = euler_explicit(f1, a1, b1, 0, 1, h)
t_1_2, y_1_2 = euler_implicit(f1, a1, b1, 0, 1, h)
t_1_3, y_1_3 = euler_trapezium(f1, a1, b1, 0, 1, h)
t_1_4, y_1_4 = euler_improved(f1, a1, b1, 0, 1, h)
t_1_5, y_1_5 = runge_kutta_3rd(f1, a1, b1, 0, 1, h)
t_1_6, y_1_6 = runge_kutta_4th(f1, a1, b1, 0, 1, h)
t_1_7, y_1_7 = adams_monlton(f1, a1, b1, 0, 1, h)
t_1_8, y_1_8 = adams_bashforth(f1, a1, b1, 0, 1, h)

t_2_1, y_2_1 = euler_explicit(f2, a2, b2, 0, 1, h)
t_2_2, y_2_2 = euler_implicit(f2, a2, b2, 0, 1, h)
t_2_3, y_2_3 = euler_trapezium(f2, a2, b2, 0, 1, h)
t_2_4, y_2_4 = euler_improved(f2, a2, b2, 0, 1, h)
t_2_5, y_2_5 = runge_kutta_3rd(f2, a2, b2, 0, 1, h)
t_2_6, y_2_6 = runge_kutta_4th(f2, a2, b2, 0, 1, h)
t_2_7, y_2_7 = adams_monlton(f2, a2, b2, 0, 1, h)
t_2_8, y_2_8 = adams_bashforth(f2, a2, b2, 0, 1, h)

