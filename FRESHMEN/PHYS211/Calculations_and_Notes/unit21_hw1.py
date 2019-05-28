w0 = 6.4
r = 0.39
I = 0.220545
d = 0.32
wt = 3.2

# Q2 
# I = 0.5*m*r*r
md = 2*I/r/r
print('md =', md) 

L = I*w0
print('L =', L)

# Q5
# L_i = L_f
# I*w0 = It*wt
It = I*w0/wt
print('It =', It)

# Q6
# It = I + mc*d*d
mc = (It - I)/d/d
print('mc =', mc)