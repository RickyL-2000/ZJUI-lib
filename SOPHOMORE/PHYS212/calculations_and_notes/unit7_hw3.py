C0 = 20e-9
V = 12
kap = 2.6
epsl = 8.85e-12

# C = Q/V
# C = epsl*A*kap/d
# Qi = C*V = epsl*A/d*V
# Qf = epsl*0.5*A/d*V + epsl*0.5*A*kap/d*V
# Qf = epsl*0.5*A/d*V*(1+kap)
# Qf/Qi = 0.5*(1+kap)

Qi = C0*V
Qf = 0.5*(1+kap)*Qi
print(Qf)