rho_c = 713
rho_w = 1025
L1 = 0.2
r1 = 0.05
L2 = 0.1
r2 = 0.1

# rho*g*V = m*g
# rho*V = m

#1
# rho_w*pi*r1*r1*(L1-h1) = rho_c*pi*r1*r1*L1
# rho_w*(L1-h1) = rho_c*L1
# h1 = (rho_w*L1-rho_c*L1)/rho_w
h1 = (rho_w - rho_c)/rho_w*L1
h2 = (rho_w - rho_c)/rho_w*L2
print(h2/h1)