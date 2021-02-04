# %%
import math
from math import pi

def cos(angle):
    return math.cos(math.radians(angle))

def sin(angle):
    return math.sin(math.radians(angle))

def acos(val):
    return math.degrees(math.acos(val))

def asin(val):
    return math.degrees(math.asin(val))

# %%
def get_beta(L, H, Delta):
    L *= pi / 180
    H *= pi / 180
    Delta *= pi / 180
    sinBeta = cos(L) * cos(H) * cos(Delta) + sin(L) * sin(Delta)
    return asin(sinBeta) * 180 / pi

def get_phi(L, H, Delta, beta):
    L *= pi / 180
    H *= pi / 180
    Delta *= pi / 180
    beta *= pi / 180
    cosphi = (sin(Delta) * cos(L) - cos(Delta) * sin(L) * cos(H)) / cos(beta)
    return acos(cosphi) * 180 / pi

def get_gamma(phi, Phi):
    return abs(phi - Phi)

def get_theta(beta, gamma, alpha):
    beta *= pi / 180
    gamma *= pi / 180
    alpha *= pi / 180
    costheta = cos(beta) * cos(gamma) * sin(alpha) + sin(beta) * cos(alpha)
    return acos(costheta) * 180 / pi

# %%
beta = get_beta(30.5, -22.15, 23.45)
print(get_beta(30.5, -22.15, 23.45))

# %%
phi = get_phi(30.5, 22.15, 23.45, beta)
print(get_phi(30.5, 22.15, 23.45, beta))

# %%
gamma = get_gamma(phi, 90)
print(gamma)

# %%
theta = get_theta(beta, get_gamma(phi, 90), 90)
print(theta)

# %%
import matplotlib.pyplot plt

