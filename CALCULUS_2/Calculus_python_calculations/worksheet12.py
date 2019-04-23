import math
#Q1 (b)
sum = 0
for n in range(0,7):
    sum += (-1)**n/math.factorial(n)
print(sum)

#Q3 (b)
a2 = 2*2**0.5/9801 * 4*3*2*(1103+26390)/(396**4)
a1 = 2*2**0.5/9801 * 1103
pi1 = 1/a1
pi2 = 1/(a1+a2)
print(pi1)
print(pi2)