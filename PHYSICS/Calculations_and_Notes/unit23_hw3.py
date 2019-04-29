from numpy import pi, sin, cos
m = 7.1
k1 = 29
k2 = 50
D = 0.23

#Q1
F = k1*D + k2*D
print('F =', F)

#Q2 
# F = k1*x + k2*x = k*x
k = k1 + k2
print('k =', k)

#Q3
w = (k/m)**0.5
T = 2*pi/w
print('T =', T)

v_m = w*D
print('v_m =', v_m)

a_m = w*w*D
print('a_m =', a_m)

# Q7
# X(t) = -D cos(wt)
x = -D*cos(w*1.3)
print('x =', x)

# Q8
# v(t) = D sin(wt)
# a(t) = D cos(wt)
a = D*cos(w*1.3)
F = m*a
print('F =', F)

# Q9
E_total = 0.5*m*v_m*v_m
print('E_total =', E_total)
