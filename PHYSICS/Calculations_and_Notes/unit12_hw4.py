import numpy as np

mc = 485
vc = [18,0]  #m/s toward east
mt = 1297
vt = [0,-10] #toward south

Pc_0 = mc*vc[0]
print(Pc_0)

Pt_0 = mt*(-vt[1])
print(Pt_0)

vx = (Pc_0 + 0)/(mc + mt)
vy = (mt*vt[1] + 0)/(mc + mt)
vf = (vx*vx+vy*vy)**0.5
angle = np.arctan(abs(vy/vx))/(2*np.pi)*360
print(angle)
print(vf)

Pf = (mc+mt)*vf
print(Pf)

print(0.5*(mc+mt)*vf*vf - 0.5*mc*vc[0]*vc[0] - 0.5*mt*vt[1]*vt[1])