# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# constants
pi = np.pi
lamb = 4 # m
T = 10 # s

omega = 2*pi/T
beta = 2*pi/lamb

vp = omega / beta

Z_C = 50
d = lamb / 4
R_S = 100
R_L = 25
V_0 = 1
R = 0
G = 0

L = Z_C / vp
C = 1 / Z_C / vp

# %%
def v_in(t):
    return 0.5 * V_0 * np.sin(omega * t)

# %%
def FDTD(del_z, del_t):
    z_steps = int(d / del_z + 1)
    t_steps = int(10 * T / del_t + 1)

    v_zt = np.zeros((t_steps, z_steps))
    i_zt = np.zeros((t_steps, z_steps))
    # v_n_i corresponds to i_(n+1/2)_(i+1/2)

    for n in range(1, t_steps):
        v_zt[n, 0] = v_in(n * del_t)

        for i in range(1, z_steps):
            v_zt[n, i] = ((C / del_t - G / 2) * v_zt[n-1, i] - 
                            1 / del_z * (i_zt[n-1, i] - i_zt[n-1, i-1])) / (C / del_t + G / 2)

        for i in range(z_steps-1):
            i_zt[n, i] = ((L / del_t - R / 2) * i_zt[n-1, i] - 
                            1 / del_z * (v_zt[n, i+1] - v_zt[n, i])) / (L / del_t + R / 2)

        i_zt[n, z_steps-1] = v_zt[n, z_steps-1] / R_L

    return v_zt, i_zt

# %%
"""2.1"""
del_z = lamb / 20 / 2
del_t = del_z / vp / 2
v_zt, i_zt = FDTD(del_z, del_t)
t = np.linspace(0, 10*T, int(10 * T / del_t + 1))
plt.plot(t, v_zt[:, 0], 'b', label="v_in")
plt.plot(t, v_zt[:, -1], 'y', label="v_L")
plt.plot(t, i_zt[:, -2] * 50, 'r', label="i_L*50")
plt.legend()
plt.title("")
plt.show()

# %%
# analytical & comparison
"""2.2"""
V_L = lambda t: -3/8*np.cos(omega*t) + 1/8*np.cos(omega*t)
I_L = lambda t: -3/8*np.cos(omega*t) - 1/8*np.cos(omega*t)
plt.plot(t, V_L(t), 'b', label="v_L analytical")
plt.plot(t, v_zt[:, -1], 'y', label="v_L numerical")
plt.plot(t, I_L(t), 'g', label="i_L*50 analytical")
plt.plot(t, i_zt[:, -2] * 50, 'r', label="i_L*50 numerical")
plt.legend()
plt.title("")
plt.show()

# %%
"""2.3"""
V_L_lumped = lambda t: np.sin(omega * t) / 5
I_L_lumped = lambda t: np.sin(omega * t) / 125
plt.plot(t, V_L_lumped(t), 'b', label="v_L_lumped")
plt.plot(t, v_zt[:, -1], 'y', label="v_L numerical")
plt.plot(t, I_L_lumped(t)*50, 'g', label="i_L_lumped*50")
plt.plot(t, i_zt[:, -2] * 50, 'r', label="i_L*50 numerical")
plt.legend()
plt.title("compare with lumped circuit theory")
plt.show()

# %%
"""3"""
def V_analytical(z, t):
    return -3 / 8 * np.cos(omega * t - beta * z) + 1 / 8 * np.cos(omega * t + beta * z)

def I_analytical(z, t):
    return -3 / 400 * np.cos(omega * t - beta * z) - 1 / 400 * np.cos(omega * t + beta * z)

# %%
dz = lamb / 20 / 2
dt = del_z / vp / 2
z_steps = int(d / dz + 1)
t_steps = int(10 * T / dt + 1)
v_zt, i_zt = FDTD(dz, dt)

# %%
# t = T / 8
z = np.linspace(-d, 0, int(d / dz + 1))
plt.plot(z, V_analytical(z, T/8), 'b', label="V analytical")
plt.plot(z, v_zt[int((t_steps-1)/80), :], 'g', label="V numerical")
plt.plot(z, I_analytical(z, T/8)*50, 'y', label="I*50 analytical")
plt.plot(z, i_zt[int((t_steps-1)/80), :]*50, 'r', label="I*50 numerical")
plt.legend()
plt.title("t = T / 8")
plt.show()

# %%
# t = T / 4
z = np.linspace(-d, 0, int(d / dz + 1))
plt.plot(z, V_analytical(z, T/4), 'b', label="V analytical")
plt.plot(z, v_zt[int((t_steps-1)/40), :], 'g', label="V numerical")
plt.plot(z, I_analytical(z, T/4)*50, 'y', label="I*50 analytical")
plt.plot(z, i_zt[int((t_steps-1)/40), :]*50, 'r', label="I*50 numerical")
plt.legend()
plt.title("t = T / 4")
plt.show()

# %%
# t = T * 3 / 8
z = np.linspace(-d, 0, int(d / dz + 1))
plt.plot(z, V_analytical(z, T*3/8), 'b', label="V analytical")
plt.plot(z, v_zt[int((t_steps-1)*3/80), :], 'g', label="V numerical")
plt.plot(z, I_analytical(z, T*3/8)*50, 'y', label="I*50 analytical")
plt.plot(z, i_zt[int((t_steps-1)*3/80), :]*50, 'r', label="I*50 numerical")
plt.legend()
plt.title("t = T * 3 / 8")
plt.show()

# %%
# t = T / 2
z = np.linspace(-d, 0, int(d / dz + 1))
plt.plot(z, V_analytical(z, T/2), 'b', label="V analytical")
plt.plot(z, v_zt[int((t_steps-1)/20), :], 'g', label="V numerical")
plt.plot(z, I_analytical(z, T/2)*50, 'y', label="I*50 analytical")
plt.plot(z, i_zt[int((t_steps-1)/20), :]*50, 'r', label="I*50 numerical")
plt.legend()
plt.title("t = T / 2")
plt.show()

# %%
# t = T
z = np.linspace(-d, 0, int(d / dz + 1))
plt.plot(z, V_analytical(z, T), 'b', label="V analytical")
plt.plot(z, v_zt[int((t_steps-1)/10)-1, :], 'g', label="V numerical")
plt.plot(z, I_analytical(z, T)*50, 'y', label="I*50 analytical")
plt.plot(z, i_zt[int((t_steps-1)/10)-1, :]*50, 'r', label="I*50 numerical")
plt.legend()
plt.title("t = T")
plt.show()

# %%
# t = 10T
z = np.linspace(-d, 0, int(d / dz + 1))
plt.plot(z, V_analytical(z, 10*T), 'b', label="V analytical")
plt.plot(z, v_zt[-1, :], 'g', label="V numerical")
plt.plot(z, I_analytical(z, 10*T)*50, 'y', label="I*50 analytical")
plt.plot(z, i_zt[-1, :]*50, 'r', label="I*50 numerical")
plt.legend()
plt.title("t = 10T")
plt.show()
# %%
