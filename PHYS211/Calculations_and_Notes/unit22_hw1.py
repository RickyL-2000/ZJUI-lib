R = 1.99
I = 214
w0 = 1.46
m = 53
v = 4.4

Lmi = I*w0
print('Lmi =', Lmi)

Lpi = m*v*R
print('Lpi =', Lpi)

# Q4 Lmi + Lpi = Lf = (I + Ip)*wf
wf = (Lmi + Lpi)/(I + m*R*R)
print('wf =', wf)

F = m*wf*wf*R
print('F =', F)

v = wf*R
print('v =', v)