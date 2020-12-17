from math import pi
H = 0.29
W = 0.75
I2 = 0.207
L = 0.27
I1 = 0.793
mu0 = 4*pi*1e-7

# B = mu0*I/2/pi/R

# Q1
Bad = mu0*I1/2/pi/L
Fad_x = I2*H*Bad
print(Fad_x)

# Q2
Bbc = mu0*I1/2/pi/(L+W)
Fbc_x = I2*H*Bbc
print(-Fbc_x)

# Q3
# 0

# Q4
F1 = Fad_x - Fbc_x # right
# I3
# Fbc3 = I2*H*mu0*I3/(2*pi*2*L)      # right
# Fad3 = I2*H*mu0*I3/(2*pi*(2*L+W))  # left
# Fbc3 - Fad3 = F1
# I2*H*mu0*I3/(2*pi*2*L) - I2*H*mu0*I3/(2*pi*(2*L+W)) = F1
# I3*(I2*H*mu0/(2*pi*2*L) - I2*H*mu0/(2*pi*(2*L+W))) = F1
I3 = F1 / (I2*H*mu0/(2*pi*2*L) - I2*H*mu0/(2*pi*(2*L+W)))
print(I3)