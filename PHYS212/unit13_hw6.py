from math import pi
d = 30e-2
dh = 26e-2
I1 = 2.2
I2 = 0.7
I3 = 8.4
mu0 = 4*pi*1e-7

# B = mu0*I/2/pi/R

# Q1
B1_0_0 = mu0*I1/2/pi/(d/2) # down
B2_0_0 = mu0*I2/2/pi/(d/2) # down
B3_0_0 = mu0*I3/2/pi/(dh) # right

Bx_0_0 = B3_0_0
print(Bx_0_0)

# Q2
By_0_0 = -B1_0_0-B2_0_0
print(By_0_0)

# Q3
B3_1 = mu0*I3/2/pi/d
B3_1_x = B3_1*3**0.5/2  # right
B3_1_y = B3_1/2     # down
B2_1 = mu0*I2/2/pi/d    # down
L = 1
Fx_1 = -I1*L*(B3_1_y+B2_1)
print(Fx_1)

# Q4
Fy_1 = -I1*L*B3_1_x
print(Fy_1)

# Q5
B3_2 = mu0*I3/2/pi/d
B3_2_x = B3_2*3**0.5/2  # right
B3_2_y = B3_2/2     # up
B1_2 = mu0*I1/2/pi/d    # down

Fx_2 = -I2*L*(B3_2_y - B1_2)
print(Fx_2)

# Q6
# I4
