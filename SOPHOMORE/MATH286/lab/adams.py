# %%
import pandas as pd
import numpy as np
import os

base_dir = os.getcwd()

# %%
def f1(t, y):
    return y*y + t*y + t*t

def f2(t, y):
    return y*y*y + t*y*y + t*t*y + t*t*t

# %%
def lin_multistep(f, a, b, t0, y0, h, alpha=(1, 0, 0), beta=(0, 23/12, -4/3, 5/12)):
    # NOTE: The check of the parameters are too sophisticated so just skip it
    pass

# %%
def adams_bashforth():
    pass

# %%
def adams_monlton():
    pass

# %%
def simpson():
    pass

# %%
def hamming():
    pass
