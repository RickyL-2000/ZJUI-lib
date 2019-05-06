from numpy import pi, sin, cos 
m = 2.2
L = 2.41
theta = 8.4/180*pi
g = 9.81

w = (g/L)**0.5
T = 2*pi/w
print('T =', T)

Fx = m*g*sin(theta)
print('Fx =', Fx)

# Q3
# x(t) = D*cos(wt)
# v(t) = -D*w*sin(wt)
omega_m = theta*w
v_m = omega_m*L
print('v_m =', v_m)

theta_t = theta*cos(w*3.64)
print('theta_t =', theta_t/pi*180)

# Q5
# a(t) = -D*w*w*cos(wt)
alpha_m = theta*w*w
a_m = alpha_m*L
print('a_m =', a_m)

# Q6
a_r = v_m**2/L
print('a_r =', a_r)