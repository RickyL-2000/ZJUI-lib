# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:01:39 2018

@author: RickyLi
"""

# 0.  Place your necessary imports here.  You may find it useful to be able to plot when debugging and visualizing your result.
import numpy as np
import matplotlib.pyplot as plt
# 1.  Create a 1D vector named `t` and 2D arrays named `vx`, `vy`, `x`, and `y` to hold the state variables, of size 90 x 1001.
t = np.linspace(0,10,1001)
vx = np.zeros((90,1001))
vy = np.zeros((90,1001))
x = np.zeros((90,1001))
y = np.zeros((90,1001))
# 2.  Store the angles from 1 to 90 degrees as radians in a variable called `radians`. Use this to initialize the state variables for `vx` and `vy`.
m = 90   # angles to fire at
angles = np .array(range(1,91,1))
radians = angles * 2*np.pi/360

# 3.  Define properties like gravity, Callista's surface area, and Callista's mass, and any other parameters you may need as they come up.
A = 0.8  # m^2
g = -9.8  # m/s^2  #check the sign according to your convention
mass = 65.0 #kg
C = 1.4
rho = 1.225
initial_velocity = 70.0 # m/s
initial_height = 5 # m
dt = 0.01 # s
# etc.  Note that I have used variables `initial_height`, `initial_velocity` and others below. Please check before you define your own variables

distance = 0
max = {}

# 4.  At this point, you should have defined `t`, `x`, `y`, `vx`, `vy`, `radians`, and the properties you need.  Now, initialize the starting condition in each array:
for i in range(m):
    y[ i ][ 0 ]  = initial_height
    vx[ i ][ 0 ] = initial_velocity * np.cos( radians[ i ] )
    vy[ i ][ 0 ] = initial_velocity * np.sin( radians[ i ] )# (see "Angles" above)

# 5.  Now you are ready to begin the simulation proper.  You will need two loops, one over every angle, and one over every time step for that angle's launch.
for i in range(m):  # loop over each angle
    for j in range(0, 1001):  # loop over each time step
        # Check that the location isn't below the ground; if so, adjust as specified in the question above.
        if j == 0:
            continue
        # calculate the acceleration including drag (for both x and y, x shown)
        v = np.sqrt( vx[ i,j-1 ]**2 + vy[ i,j-1 ]**2 )
        ax = -( 0.5*rho*C*A/mass ) * v**2 * ( vx[ i,j-1 ] / v )
        ay = -( 0.5*rho*C*A/mass ) * v**2 * ( vy[ i,j-1 ] / v )
        vx[i,j] = vx[i,j-1] + ax*dt 
        vy[i,j] = vy[i,j-1] + (ay+g)*dt
        #x[i,j] = x[i,j-1] + vx[i,j-1]*dt + 0.5*ax*dt*dt
        #y[i,j] = y[i,j-1] + vy[i,j-1]*dt + 0.5*(ay+g)*dt*dt
        x[i,j] = x[i,j-1] + vx[i,j]*dt
        y[i,j] = y[i,j-1] + vy[i,j]*dt
        

        # calculate the change in position at time `t` using the current velocities (`vx[ i ][ j ]`) and the previous positions (`x[ i ][ j-1 ]`).  This is slightly different from the question you have solved in an earlier homework.

# 6.  The purpose of these calculations was to show which angle yielded the farthest distance.  Find this out and store the result in a variable named `best_angle`.
        if y[i,j] < 0:
            vx[i,j] = 0
            vy[i,j] = 0
            y[i,j] = 0
            if x[i,j] >= distance:
                distance = x[i,j]
                max = {i+1:distance}
            break
    for k in range(j+1, 1001):
        x[i,k] = x[i,j]
        y[i,k] = 0
    plt.plot(x[i,:],y[i,:],'k-')
    # plt.show()
    plt.xlim(0,150)
    plt.ylim(0,105)

plt.show()

best_angle = list(max.keys())[0]
print(list(max.keys())[0])
print(x[33,:])