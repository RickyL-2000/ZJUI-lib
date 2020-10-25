# %%
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import scipy as sp
import scipy.stats as st
import pickle as pkl
import csv as csv

# %%
p = 0.3
st.bernoulli.rvs(p)

# %%
array = np.arange(20)
y = list(array[array % 2 == 0])
print(y)

# or #

y = list(filter(lambda x: x % 2 == 0, array))
print(y)

# %%
print(type(st.bernoulli(p)))
x = st.bernoulli(p)
print(x.rvs())

# %%
st.binom.pmf()

# %%
p = 0.014
n = 8 * 40 * 60
lamb = n * p
print(st.binom(n, p).rvs())
# %%
d = {}
d['a'] += 1
d