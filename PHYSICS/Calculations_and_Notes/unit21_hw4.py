mp = 78
R = 1.59
md = 199
w = 1.5
r = 0.53

Id = 0.5*md*R*R
Ii = Id + mp*R*R
print('Ii =', Ii)
If = Id + mp*r*r
print('If =', If)

# Q3
Li = Ii*w
# Li = Lf = If*wf
wf = Li/If
print('wf =', wf)
Ei = 0.5*Ii*w*w
Ef = 0.5*If*wf*wf
delta = Ef - Ei
print('delta =', delta)

a = wf*wf*r
print('a =', a)
