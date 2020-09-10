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
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pass

# %%
""" 0. load the ground truth """
# df1_truth = pd.read_csv(base_dir + '/data/ivp1_ground_truth.csv')
# df2_truth = pd.read_csv(base_dir + '/data/ivp2_ground_truth.csv')
df1_truth = pd.read_csv(base_dir + '/data/ivp1_ground_truth_h5.csv')
df2_truth = pd.read_csv(base_dir + '/data/ivp2_ground_truth_h5.csv')
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
h_hat = 0.00001   # the step length of the ground truth
h1 = 0.01
h2 = 0.01
a1, b1 = -2.0, 0.81
# a2, b2 = -14.0, 0.42
a2, b2 = -5.0, 0.42

t_1_list = []
y_1_list = []
e_1_list = []

t_2_list = []
y_2_list = []
e_2_list = []

methods = [euler_explicit, euler_implicit, euler_trapezium, euler_improved,
           runge_kutta_3rd, runge_kutta_4th,
           adams_monlton, adams_bashforth]

# %%
df1 = df1_truth[(df1_truth['Var1'] >= a1) & (df1_truth['Var1'] <= b1)]
df2 = df2_truth[(df2_truth['Var1'] >= a2) & (df2_truth['Var1'] <= b2)]
t1, y1 = df1['Var1'].values, df1['Var2'].values
t2, y2 = df2['Var1'].values, df2['Var2'].values

# %%
# ivp1
for i, method in enumerate(methods):
    if h1 <= h_hat:
        t_list, y_list = method(f1, a1, b1, 0, 1, h1)
        t_list = np.array([t_list[j] for j in range(0, len(t_list), round(h_hat / h1))])
        y_list = np.array([y_list[j] for j in range(0, len(y_list), round(h_hat / h1))])
        t_1_list.append(t_list)
        y_1_list.append(y_list)

        e_list = np.power(abs(y_list - y1), 1 / 3)
        e_1_list.append(e_list)
    else:
        t_list, y_list = method(f1, a1, b1, 0, 1, h1)
        t_1_list.append(t_list)
        y_1_list.append(y_list)

        y1_tmp = np.array([y1[j] for j in range(0, len(y1), round(h1 / h_hat))])
        e_list = np.power(abs(y_list - y1_tmp), 1 / 3)
        e_1_list.append(e_list)

# %%
# ivp2
for i, method in enumerate(methods):
    if h2 <= h_hat:
        t_list, y_list = method(f2, a2, b2, 0, 1, h2)
        t_list = np.array([t_list[j] for j in range(0, len(t_list), round(h_hat / h2))])
        y_list = np.array([y_list[j] for j in range(0, len(y_list), round(h_hat / h2))])
        t_2_list.append(t_list)
        y_2_list.append(y_list)

        e_list = np.power(signal.medfilt(abs(y_2_list[i] - y2), 101), 1 / 4)
        e_2_list.append(e_list)
    else:
        t_list, y_list = method(f2, a2, b2, 0, 1, h2)
        t_2_list.append(t_list)
        y_2_list.append(y_list)

        y2_tmp = np.array([y2[j] for j in range(0, len(y2), round(h2 / h_hat))])
        e_list = np.power(abs(y_list - y2_tmp), 1 / 4)
        e_2_list.append(e_list)

# %%
# IVP1 error
plt.title("IVP1 Processed Error = (y_hat - y)^(1/3) with h = {}".format(h1))
plt.plot(t_1_list[0], e_1_list[0], 'b', label='euler_explicit')
## plt.plot(t_1_list[1], e_1_list[1], 'g', label='euler_implicit')
## plt.plot(t_1_list[2], e_1_list[2], 'y', label='euler_trapezium')
plt.plot(t_1_list[3], e_1_list[3], 'c', label='euler_improved')
## plt.plot(t_1_list[4], e_1_list[4], 'w', label='runge_kutta_3rd')
plt.plot(t_1_list[5], e_1_list[5], 'r', label='runge_kutta_4th')
plt.plot(t_1_list[6], e_1_list[6], 'k', label='adams_monlton')
plt.plot(t_1_list[7], e_1_list[7], 'm', label='adams_bashforth')
plt.legend()
plt.show()

# NOTE: the graphs of rk4 and adams_bf are approximately overlapped

# %%
# IVP2 error
plt.title("IVP2 Processed Error = (y_hat - y)^(1/4) with h = {}".format(h2))
plt.plot(t_2_list[0], e_2_list[0], 'b', label='euler_explicit')
## plt.plot(t_2_list[1], e_2_list[1], 'g', label='euler_implicit')
## plt.plot(t_2_list[2], e_2_list[2], 'y', label='euler_trapezium')
plt.plot(t_2_list[3], e_2_list[3], 'c', label='euler_improved')
## plt.plot(t_2_list[4], e_2_list[4], 'w', label='runge_kutta_3rd')
plt.plot(t_2_list[5], e_2_list[5], 'r', label='runge_kutta_4th')
plt.plot(t_2_list[6], e_2_list[6], 'k', label='adams_monlton')
plt.plot(t_2_list[7], e_2_list[7], 'm', label='adams_bashforth')
plt.legend()
plt.show()

# %%
""" the average error """
# %%
h_hat = 0.00001   # the step length of the ground truth
h1 = 0.001
h2 = 0.001
a1, b1 = -2.12, 0.858
# a2, b2 = -14.0, 0.42
a2, b2 = -10.0, 0.439

t_1_list = []
y_1_list = []
e_1_list = []

t_2_list = []
y_2_list = []
e_2_list = []

methods = [euler_explicit, euler_implicit, euler_trapezium, euler_improved,
           runge_kutta_3rd, runge_kutta_4th,
           adams_monlton, adams_bashforth]

# %%
df1 = df1_truth[(df1_truth['Var1'] >= a1) & (df1_truth['Var1'] <= b1)]
df2 = df2_truth[(df2_truth['Var1'] >= a2) & (df2_truth['Var1'] <= b2)]
t1, y1 = df1['Var1'].values, df1['Var2'].values
t2, y2 = df2['Var1'].values, df2['Var2'].values

# %%
# ivp1
for i, method in enumerate(methods):
    if h1 <= h_hat:
        t_list, y_list = method(f1, a1, b1, 0, 1, h1)
        # t_list = np.array([t_list[j] for j in range(0, len(t_list), round(h_hat / h1))])
        y_list = np.array([y_list[j] for j in range(0, len(y_list), round(h_hat / h1))])
        # t_1_list.append(t_list)
        # y_1_list.append(y_list)

        e_list = abs(y_list - y1)
        e_1_list.append(e_list)
    else:
        t_list, y_list = method(f1, a1, b1, 0, 1, h1)
        # t_1_list.append(t_list)
        y_1_list.append(y_list)

        y1_tmp = np.array([y1[j] for j in range(0, len(y1), round(h1 / h_hat))])
        e_list = abs(y_list - y1_tmp)
        e_1_list.append(e_list)

# %%
avg_e_1_list = [e_list.mean() for e_list in e_1_list]
print(avg_e_1_list)

# %%
# ivp2
for i, method in enumerate(methods):
    if h2 <= h_hat:
        t_list, y_list = method(f2, a2, b2, 0, 1, h2)
        # t_list = np.array([t_list[j] for j in range(0, len(t_list), round(h_hat / h2))])
        y_list = np.array([y_list[j] for j in range(0, len(y_list), round(h_hat / h2))])
        # t_2_list.append(t_list)
        # y_2_list.append(y_list)

        e_list = abs(y_2_list[i] - y2)
        e_2_list.append(e_list)
    else:
        t_list, y_list = method(f2, a2, b2, 0, 1, h2)
        # t_2_list.append(t_list)
        y_2_list.append(y_list)

        y2_tmp = np.array([y2[j] for j in range(0, len(y2), round(h2 / h_hat))])
        e_list = abs(y_list - y2_tmp)
        e_2_list.append(e_list)

# %%
avg_e_2_list = [e_list.mean() for e_list in e_2_list]
print(avg_e_2_list)

# %%
""" 2.3 error vs h """
h_hat = 0.00001   # the step length of the ground truth
methods = [euler_explicit, euler_improved, runge_kutta_4th, adams_monlton]
a1, b1 = -2.0, 0.81
a2, b2 = -5.0, 0.42
h1 = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)
h2 = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)

mh_t_1_list = []
mh_y_1_list = []
mh_e_1_list = []

mh_t_2_list = []
mh_y_2_list = []
mh_e_2_list = []

# %%
df1 = df1_truth[(df1_truth['Var1'] >= a1) & (df1_truth['Var1'] <= b1)]
df2 = df2_truth[(df2_truth['Var1'] >= a2) & (df2_truth['Var1'] <= b2)]
t1, y1 = df1['Var1'].values, df1['Var2'].values
t2, y2 = df2['Var1'].values, df2['Var2'].values

# %%
# ivp1
for method in methods:
    h_t_1_list = []
    h_y_1_list = []
    h_e_1_list = []
    for h in h1:
        if h <= h_hat:
            t_list, y_list = method(f1, a1, b1, 0, 1, h)
            t_list = np.array([t_list[j] for j in range(0, len(t_list), round(h_hat / h))])
            y_list = np.array([y_list[j] for j in range(0, len(y_list), round(h_hat / h))])
            h_t_1_list.append(t_list)
            h_y_1_list.append(y_list)

            e_list = np.power(abs(y_list - y1), 1 / 5)
            h_e_1_list.append(e_list)
        else:
            t_list, y_list = method(f1, a1, b1, 0, 1, h)
            h_t_1_list.append(t_list)
            h_y_1_list.append(y_list)

            y1_tmp = np.array([y1[j] for j in range(0, len(y1), round(h / h_hat))])
            e_list = np.power(abs(y_list - y1_tmp), 1 / 5)
            h_e_1_list.append(e_list)
    mh_t_1_list.append(h_t_1_list)
    mh_y_1_list.append(h_y_1_list)
    mh_e_1_list.append(h_e_1_list)

# %%
# ivp2
for method in methods:
    h_t_2_list = []
    h_y_2_list = []
    h_e_2_list = []
    for h in h1:
        if h <= h_hat:
            t_list, y_list = method(f2, a2, b2, 0, 1, h)
            t_list = np.array([t_list[j] for j in range(0, len(t_list), round(h_hat / h))])
            y_list = np.array([y_list[j] for j in range(0, len(y_list), round(h_hat / h))])
            h_t_2_list.append(t_list)
            h_y_2_list.append(y_list)

            e_list = np.power(abs(y_list - y2), 1 / 5)
            h_e_2_list.append(e_list)
        else:
            t_list, y_list = method(f2, a2, b2, 0, 1, h)
            h_t_2_list.append(t_list)
            h_y_2_list.append(y_list)

            y2_tmp = np.array([y2[j] for j in range(0, len(y2), round(h / h_hat))])
            e_list = np.power(abs(y_list - y2_tmp), 1 / 5)
            h_e_2_list.append(e_list)
    mh_t_2_list.append(h_t_2_list)
    mh_y_2_list.append(h_y_2_list)
    mh_e_2_list.append(h_e_2_list)

# %%
# ivp1 error vs h
plt.title("IVP1 Processed Error = (y_hat - y)^(1/5) of Explicit Euler Method")
plt.plot(mh_t_1_list[0][0], mh_e_1_list[0][0], 'b', label='h = {}'.format(h1[0]))
plt.plot(mh_t_1_list[0][1], mh_e_1_list[0][1], 'c', label='h = {}'.format(h1[1]))
plt.plot(mh_t_1_list[0][2], mh_e_1_list[0][2], 'r', label='h = {}'.format(h1[2]))
plt.plot(mh_t_1_list[0][3], mh_e_1_list[0][3], 'k', label='h = {}'.format(h1[3]))
plt.plot(mh_t_1_list[0][4], mh_e_1_list[0][4], 'm', label='h = {}'.format(h1[4]))
plt.legend()
plt.show()

# %%
plt.title("IVP1 Processed Error = (y_hat - y)^(1/5) of Improved Euler Method")
plt.plot(mh_t_1_list[1][0], mh_e_1_list[1][0], 'b', label='h = {}'.format(h1[0]))
plt.plot(mh_t_1_list[1][1], mh_e_1_list[1][1], 'c', label='h = {}'.format(h1[1]))
plt.plot(mh_t_1_list[1][2], mh_e_1_list[1][2], 'r', label='h = {}'.format(h1[2]))
plt.plot(mh_t_1_list[1][3], mh_e_1_list[1][3], 'k', label='h = {}'.format(h1[3]))
plt.plot(mh_t_1_list[1][4], mh_e_1_list[1][4], 'm', label='h = {}'.format(h1[4]))
plt.legend()
plt.show()

# %%
plt.title("IVP1 Processed Error = (y_hat - y)^(1/5) of Runge-Kutta 4th Method")
plt.plot(mh_t_1_list[2][0], mh_e_1_list[2][0], 'b', label='h = {}'.format(h1[0]))
plt.plot(mh_t_1_list[2][1], mh_e_1_list[2][1], 'c', label='h = {}'.format(h1[1]))
plt.plot(mh_t_1_list[2][2], mh_e_1_list[2][2], 'r', label='h = {}'.format(h1[2]))
plt.plot(mh_t_1_list[2][3], mh_e_1_list[2][3], 'k', label='h = {}'.format(h1[3]))
plt.plot(mh_t_1_list[2][4], mh_e_1_list[2][4], 'm', label='h = {}'.format(h1[4]))
plt.legend()
plt.show()

# %%
plt.title("IVP1 Processed Error = (y_hat - y)^(1/5) of Adams-Monlton Method")
plt.plot(mh_t_1_list[3][0], mh_e_1_list[3][0], 'b', label='h = {}'.format(h1[0]))
plt.plot(mh_t_1_list[3][1], mh_e_1_list[3][1], 'c', label='h = {}'.format(h1[1]))
plt.plot(mh_t_1_list[3][2], mh_e_1_list[3][2], 'r', label='h = {}'.format(h1[2]))
plt.plot(mh_t_1_list[3][3], mh_e_1_list[3][3], 'k', label='h = {}'.format(h1[3]))
plt.plot(mh_t_1_list[3][4], mh_e_1_list[3][4], 'm', label='h = {}'.format(h1[4]))
plt.legend()
plt.show()

# %%
# ivp2 error vs h
plt.title("IVP2 Processed Error = (y_hat - y)^(1/5) of Explicit Euler Method")
plt.plot(mh_t_2_list[0][0], mh_e_2_list[0][0], 'b', label='h = {}'.format(h2[0]))
plt.plot(mh_t_2_list[0][1], mh_e_2_list[0][1], 'c', label='h = {}'.format(h2[1]))
plt.plot(mh_t_2_list[0][2], mh_e_2_list[0][2], 'r', label='h = {}'.format(h2[2]))
plt.plot(mh_t_2_list[0][3], mh_e_2_list[0][3], 'k', label='h = {}'.format(h2[3]))
plt.plot(mh_t_2_list[0][4], mh_e_2_list[0][4], 'm', label='h = {}'.format(h2[4]))
plt.legend()
plt.show()

# %%
plt.title("IVP2 Processed Error = (y_hat - y)^(1/5) of Improved Euler Method")
plt.plot(mh_t_2_list[1][0], mh_e_2_list[1][0], 'b', label='h = {}'.format(h2[0]))
plt.plot(mh_t_2_list[1][1], mh_e_2_list[1][1], 'c', label='h = {}'.format(h2[1]))
plt.plot(mh_t_2_list[1][2], mh_e_2_list[1][2], 'r', label='h = {}'.format(h2[2]))
plt.plot(mh_t_2_list[1][3], mh_e_2_list[1][3], 'k', label='h = {}'.format(h2[3]))
plt.plot(mh_t_2_list[1][4], mh_e_2_list[1][4], 'm', label='h = {}'.format(h2[4]))
plt.legend()
plt.show()

# %%
plt.title("IVP2 Processed Error = (y_hat - y)^(1/5) of Runge-Kutta 4th Method")
plt.plot(mh_t_2_list[2][0], mh_e_2_list[2][0], 'b', label='h = {}'.format(h2[0]))
plt.plot(mh_t_2_list[2][1], mh_e_2_list[2][1], 'c', label='h = {}'.format(h2[1]))
plt.plot(mh_t_2_list[2][2], mh_e_2_list[2][2], 'r', label='h = {}'.format(h2[2]))
plt.plot(mh_t_2_list[2][3], mh_e_2_list[2][3], 'k', label='h = {}'.format(h2[3]))
plt.plot(mh_t_2_list[2][4], mh_e_2_list[2][4], 'm', label='h = {}'.format(h2[4]))
plt.legend()
plt.show()

# %%
plt.title("IVP2 Processed Error = (y_hat - y)^(1/5) of Adams-Monlton Method")
plt.plot(mh_t_2_list[3][0], mh_e_2_list[3][0], 'b', label='h = {}'.format(h2[0]))
plt.plot(mh_t_2_list[3][1], mh_e_2_list[3][1], 'c', label='h = {}'.format(h2[1]))
plt.plot(mh_t_2_list[3][2], mh_e_2_list[3][2], 'r', label='h = {}'.format(h2[2]))
plt.plot(mh_t_2_list[3][3], mh_e_2_list[3][3], 'k', label='h = {}'.format(h2[3]))
plt.plot(mh_t_2_list[3][4], mh_e_2_list[3][4], 'm', label='h = {}'.format(h2[4]))
plt.legend()
plt.show()

# %%
""" 3. time consuming analysis """
a1, b1 = -2.5, 1.0
a2, b2 = -20.0, 0.5
methods = [euler_explicit, euler_implicit, euler_trapezium, euler_improved,
           runge_kutta_3rd, runge_kutta_4th,
           adams_monlton, adams_bashforth]
columns = ["h",
           "euler_explicit", "euler_implicit", "euler_trapezium", "euler_improved",
           "runge_kutta_3rd", "runge_kutta_4th",
           "adams_monlton", "adams_bashforth"]
h_list = (0.01, 0.005, 0.001, 0.0005, 0.0002, 0.0001)

df_time_1 = pd.DataFrame(columns=columns)
df_time_1['h'] = h_list
for i, method in enumerate(methods):
    tm_list = []
    for h in h_list:
        tm = analyse_time(f1, method, a1, b1, 0, 1, h)
        tm_list.append(tm)
    df_time_1[columns[i+1]] = tm_list

df_time_1.to_csv(base_dir + '/data/time_analysis/ivp1_time_analysis.csv', index=False, float_format="%.8f")

df_time_2 = pd.DataFrame(columns=columns)
df_time_2['h'] = h_list
for i, method in enumerate(methods):
    tm_list = []
    for h in h_list:
        tm = analyse_time(f2, method, a2, b2, 0, 1, h)
        tm_list.append(tm)
    df_time_2[columns[i+1]] = tm_list

df_time_2.to_csv(base_dir + '/data/time_analysis/ivp2_time_analysis.csv', index=False, float_format="%.8f")


# %%
""" try try water """
fig = plt.figure()
ax = plt.axes(projection='3d')
plt.title("z = y^3 + t*y^2 + t^2*y + t^3")
ax.set_xlabel('t')
ax.set_ylabel('y')

tt = np.arange(-20, 20, 0.1)
yy = np.arange(-20, 20, 0.1)
T, Y = np.meshgrid(tt, yy)
Z = Y*Y*Y + T*Y*Y + T*T*Y + T*T*T

ax.plot_surface(T, Y, Z, cmap='rainbow')
plt.show()
