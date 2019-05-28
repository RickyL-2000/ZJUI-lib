m1 = 9.8
R = 0.18
w = 32
m2 = 3.9
l = 2*R

Id = 0.5*m1*R*R
Ir = m2*l*l/12
Li = Id*w
print('Li =', Li)

Ei = 0.5*Id*w*w
print('Ei =', Ei)

# Q3 Li = Lf = (Id + Ir)*wf
wf = Li/(Id + Ir)
print('wf =', wf)

Lf = Li

Ef = 0.5*(Id + Ir)*wf*wf
print('Ef =', Ef)

alpha = wf/5.7
# tq = I*alpha
tq = Ir*alpha
print('tq =', tq)