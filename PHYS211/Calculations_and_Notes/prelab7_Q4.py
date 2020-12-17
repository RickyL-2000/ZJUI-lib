from numpy import pi
m = 0.108
d = 0.24
r = d/2
w0 = 550/60*2*pi

I = 0.5*m*r*r + 0.5*m*r*r*0.5
print('I =', I)

# (b)
# tau = I*alpha
# w*w - 0 = 2*alpha*theta

tau = w0*w0*I/2/(pi/2)
print(tau)