from numpy import arctan, pi
L = 2.9
m = 22
miu = 0.49
g = 9.81

#Q2
# N1 = mg
# f = miu*mg
# N2 = f = miu*mg
# mg*L/2*cos(theta) = N2*
# so: 2*miu*tan(theta) = 1

theta = arctan(1/2/miu)/pi*180
print(theta)

#Q3
M = 62
N1 = m*g+M*g
print(N1)

theta = arctan((0.5*m+M)/miu/(m+M))/pi*180
print(theta)