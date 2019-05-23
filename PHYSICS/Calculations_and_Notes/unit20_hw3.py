# A meterstick (L = 1 m) has a mass of m = 0.239 kg. Initially it hangs 
# from two short strings: one at the 25 cm mark and one at the 75 cm mark. 
from scipy.optimize import fsolve
m = 0.239
L = 1
l = 0.25
g = 9.81
I = m*L*L/12 + m*(L/4)**2

#Q2
tau = 0.75*m*g*0.75/2 - 0.25*m*g*0.25/2
alpha = tau/I
print(alpha)

### Caution!!! Q3!!!
#######################################################################
### Use the right end as the pivot and                               ##
### then calculate the left tension                                  ##
### !!!Also!!!                                                       ##
### After changing the reference frame, the I should be changed.     ##
#######################################################################
#
# ↑↑↑ This is wrong!!! 
#
### Correct answer: Use the translative Newton's second law: F_net = m*a_CM
### Then substitude the a_CM and alpha.

##################### BUT WHY THE PREVIOUS IS WRONG?

T = m*g - m*alpha*L/4
print(T)

################ Q3 trial ########################

# Because the net acceleration points down? 
# T*0.75 - mg*0.5 = (m*L*L/12 + m*(L/4)**2)*alpha
T2 = ((m*L*L/12 + m*(L/4)**2)*alpha + m*g*0.5)/0.75
print('T2 =', T2)

### emmmmmmm it's stil wrong....

##################################################
#Q4
# angular kinetic mg*L/4 = 0.5*I*w*w
w = (m*g*L/2/I)**0.5
print(w)

#Q5
### Caution!!! Donnot forget the radial acceleration!
a = w*w*L/4
print(a)

#Q6
# T - mg = ma
T = m*g + m*a
print(T)