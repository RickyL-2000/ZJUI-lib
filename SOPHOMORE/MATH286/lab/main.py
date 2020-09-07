# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Tuple
import scipy.signal as signal
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
# t1, y1 = df1_truth['Var1'].values, df1_truth['Var2'].values
# t2, y2 = df2_truth['Var1'].values, df2_truth['Var2'].values

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
""" 2.1 errors of different methods compare with each other """
# %%
h_hat = 0.001
h = 0.0001
a1, b1 = -2.0, 0.81
a2, b2 = -14.0, 0.42

t_1_1, y_1_1 = euler_explicit(f1, a1, b1, 0, 1, h)
t_1_1 = [t_1_1[i] for i in range(0, len(t_1_1), round(h_hat / h))]
y_1_1 = [y_1_1[i] for i in range(0, len(y_1_1), round(h_hat / h))]
t_1_2, y_1_2 = euler_implicit(f1, a1, b1, 0, 1, h)
t_1_2 = [t_1_2[i] for i in range(0, len(t_1_2), round(h_hat / h))]
y_1_2 = [y_1_2[i] for i in range(0, len(y_1_2), round(h_hat / h))]
t_1_3, y_1_3 = euler_trapezium(f1, a1, b1, 0, 1, h)
t_1_3 = [t_1_3[i] for i in range(0, len(t_1_3), round(h_hat / h))]
y_1_3 = [y_1_3[i] for i in range(0, len(y_1_3), round(h_hat / h))]
t_1_4, y_1_4 = euler_improved(f1, a1, b1, 0, 1, h)
t_1_4 = [t_1_4[i] for i in range(0, len(t_1_4), round(h_hat / h))]
y_1_4 = [y_1_4[i] for i in range(0, len(y_1_4), round(h_hat / h))]
t_1_5, y_1_5 = runge_kutta_3rd(f1, a1, b1, 0, 1, h)
t_1_5 = [t_1_5[i] for i in range(0, len(t_1_5), round(h_hat / h))]
y_1_5 = [y_1_5[i] for i in range(0, len(y_1_5), round(h_hat / h))]
t_1_6, y_1_6 = runge_kutta_4th(f1, a1, b1, 0, 1, h)
t_1_6 = [t_1_6[i] for i in range(0, len(t_1_6), round(h_hat / h))]
y_1_6 = [y_1_6[i] for i in range(0, len(y_1_6), round(h_hat / h))]
t_1_7, y_1_7 = adams_monlton(f1, a1, b1, 0, 1, h)
t_1_7 = [t_1_7[i] for i in range(0, len(t_1_7), round(h_hat / h))]
y_1_7 = [y_1_7[i] for i in range(0, len(y_1_7), round(h_hat / h))]
t_1_8, y_1_8 = adams_bashforth(f1, a1, b1, 0, 1, h)
t_1_8 = [t_1_8[i] for i in range(0, len(t_1_8), round(h_hat / h))]
y_1_8 = [y_1_8[i] for i in range(0, len(y_1_8), round(h_hat / h))]

t_2_1, y_2_1 = euler_explicit(f2, a2, b2, 0, 1, h)
t_2_1 = [t_2_1[i] for i in range(0, len(t_2_1), round(h_hat / h))]
y_2_1 = [y_2_1[i] for i in range(0, len(y_2_1), round(h_hat / h))]
t_2_2, y_2_2 = euler_implicit(f2, a2, b2, 0, 1, h)
t_2_2 = [t_2_2[i] for i in range(0, len(t_2_2), round(h_hat / h))]
y_2_2 = [y_2_2[i] for i in range(0, len(y_2_2), round(h_hat / h))]
t_2_3, y_2_3 = euler_trapezium(f2, a2, b2, 0, 1, h)
t_2_3 = [t_2_3[i] for i in range(0, len(t_2_3), round(h_hat / h))]
y_2_3 = [y_2_3[i] for i in range(0, len(y_2_3), round(h_hat / h))]
t_2_4, y_2_4 = euler_improved(f2, a2, b2, 0, 1, h)
t_2_4 = [t_2_4[i] for i in range(0, len(t_2_4), round(h_hat / h))]
y_2_4 = [y_2_4[i] for i in range(0, len(y_2_4), round(h_hat / h))]
t_2_5, y_2_5 = runge_kutta_3rd(f2, a2, b2, 0, 1, h)
t_2_5 = [t_2_5[i] for i in range(0, len(t_2_5), round(h_hat / h))]
y_2_5 = [y_2_5[i] for i in range(0, len(y_2_5), round(h_hat / h))]
t_2_6, y_2_6 = runge_kutta_4th(f2, a2, b2, 0, 1, h)
t_2_6 = [t_2_6[i] for i in range(0, len(t_2_6), round(h_hat / h))]
y_2_6 = [y_2_6[i] for i in range(0, len(y_2_6), round(h_hat / h))]
t_2_7, y_2_7 = adams_monlton(f2, a2, b2, 0, 1, h)
t_2_7 = [t_2_7[i] for i in range(0, len(t_2_7), round(h_hat / h))]
y_2_7 = [y_2_7[i] for i in range(0, len(y_2_7), round(h_hat / h))]
t_2_8, y_2_8 = adams_bashforth(f2, a2, b2, 0, 1, h)
t_2_8 = [t_2_8[i] for i in range(0, len(t_2_8), round(h_hat / h))]
y_2_8 = [y_2_8[i] for i in range(0, len(y_2_8), round(h_hat / h))]

# %%
df1 = df1_truth[(df1_truth['Var1'] >= a1) & (df1_truth['Var1'] <= b1)]
df2 = df2_truth[(df2_truth['Var1'] >= a2) & (df2_truth['Var1'] <= b2)]
t1, y1 = df1['Var1'].values, df1['Var2'].values
t2, y2 = df2['Var1'].values, df2['Var2'].values

# %%
e_1_1 = np.power((abs(y_1_1 - y1)), 1/3)
e_1_2 = np.power((abs(y_1_2 - y1)), 1/3)
e_1_3 = np.power((abs(y_1_3 - y1)), 1/3)
e_1_4 = np.power((abs(y_1_4 - y1)), 1/3)
e_1_5 = np.power((abs(y_1_5 - y1)), 1/3)
e_1_6 = np.power((abs(y_1_6 - y1)), 1/3)
e_1_7 = np.power((abs(y_1_7 - y1)), 1/3)
e_1_8 = np.power((abs(y_1_8 - y1)), 1/3)

e_2_1 = np.power(signal.medfilt(abs(y_2_1 - y2), 101), 1/3)
e_2_2 = np.power(signal.medfilt(abs(y_2_2 - y2), 101), 1/3)
e_2_3 = np.power(signal.medfilt(abs(y_2_3 - y2), 101), 1/3)
e_2_4 = np.power(signal.medfilt(abs(y_2_4 - y2), 101), 1/3)
e_2_5 = np.power(signal.medfilt(abs(y_2_5 - y2), 101), 1/3)
e_2_6 = np.power(signal.medfilt(abs(y_2_6 - y2), 101), 1/3)
e_2_7 = np.power(signal.medfilt(abs(y_2_7 - y2), 101), 1/3)
e_2_8 = np.power(signal.medfilt(abs(y_2_8 - y2), 101), 1/3)

# %%
plt.title("Processed Error = (y_hat - y)^(1/3) with h = 0.0001")
plt.plot(t_1_1, e_1_1, 'b', label='euler_explicit')
# plt.plot(t_1_2, e_1_2, 'g', label='euler_implicit')
# plt.plot(t_1_3, e_1_3, 'y', label='euler_trapezium')
plt.plot(t_1_4, e_1_4, 'c', label='euler_improved')
# plt.plot(t_1_5, e_1_5, 'w', label='runge_kutta_3rd')
plt.plot(t_1_6, e_1_6, 'r', label='runge_kutta_4th')
plt.plot(t_1_7, e_1_7, 'k', label='adams_monlton')
plt.plot(t_1_8, e_1_8, 'm', label='adams_bashforth')
plt.legend()
plt.show()

# NOTE: the graphs of rk4 and adams_bf are approximately overlapped

# %%
plt.plot(t_1_6, e_1_6, 'r', label='runge_kutta_4th')
plt.legend()
plt.show()

# %%
plt.title("Processed Error = (y_hat - y)^(1/3) with h = 0.0001")
plt.plot(t_2_1, e_2_1, 'b', label='euler_explicit')
# plt.plot(t_2_2, e_2_2, 'g', label='euler_implicit')
# plt.plot(t_2_3, e_2_3, 'y', label='euler_trapezium')
plt.plot(t_2_4, e_2_4, 'c', label='euler_improved')
# plt.plot(t_2_5, e_2_5, 'w', label='runge_kutta_3rd')
plt.plot(t_2_6, e_2_6, 'r', label='runge_kutta_4th')
plt.plot(t_2_7, e_2_7, 'k', label='adams_monlton')
plt.plot(t_2_8, e_2_8, 'm', label='adams_bashforth')
plt.legend()
plt.show()

# %%
""" 2.2 the error of different h """

