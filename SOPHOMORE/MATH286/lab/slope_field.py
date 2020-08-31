# %%
import numpy as np
from sympy import Function
from sympy.abc import t
from sympy import *
import matplotlib.pyplot as plt

# %%
tdomain = np.linspace(-3, 3, 30)
ydomain = np.linspace(-3, 3, 30)

y = Function('y')
formula1 = y(t)*y(t) + t*y(t) + t*t
formula2 = y(t)*y(t)*y(t) + t*y(t)*y(t) + t*t*y(t) + t*t*t



# %%
def plotSlopeField(tdomain,ydomain,formula,points = []):
    # initialize figure
    fig = plt.figure(num=1)
    # create grid
    T,Y = np.meshgrid(tdomain,ydomain )
    # calculate direction vectors
    U = 1
    V = np.array([[formula.subs({y(t): yval, t: tval}) for tval in tdomain] for yval in ydomain],dtype = 'float')
    N = np.sqrt(U**2+V**2)
    U2, V2 = U/N, V/N
    # make the plot
    plt.quiver( T,Y,U2, V2)
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y$")
    plt.axhline(0,0,1,linewidth = 2, color = 'black')
    plt.axvline(0,0,1,linewidth = 2, color = 'black')
    return fig

# %%
sample = plotSlopeField(tdomain, ydomain, formula1, [])
sample.show()

# %%
sample = plotSlopeField(tdomain, ydomain, formula2, [])
sample.show()