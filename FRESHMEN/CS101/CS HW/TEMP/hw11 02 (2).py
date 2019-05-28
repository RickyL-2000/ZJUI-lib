# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:07:59 2018

@author: RickyLi
"""

import numpy as np
import matplotlib.pyplot as plt
def dist( angle,m_prop ):

# Reference code from HW10
# 0.  Place your necessary imports here.  You may find it useful to be able to plot when debugging and visualizing your result.


# 1.  Create a 1D vector named `t` and 2D arrays named `vx`, `vy`, `x`, and `y` to hold the state variables, of size 90 x 1001.
    t = np.linspace(0,10,1001)
    vx = np.zeros([1001,])
    vy = np.zeros([1001,])
    x = np.zeros([1001,])
    y = np.zeros([1001,])

# 2.  Store the angles from 1 to 90 degrees as radians in a variable called `radians`. Use this to initialize the state variables for `vx` and `vy`.


# 3.  Define properties like gravity, Callista's surface area, and Callista's mass, and any other parameters you may need as they come up.
    A = 0.8  # m^2
    g = -9.8  # m/s^2
    initial_height = 5
    initial_velocity = 1500*(m_prop/65)**0.45
    C = 1.4
    rho = 1.225
    dt = 0.01

## 4.  At this point, you should have defined `t`, `x`, `y`, `vx`, `vy`, `radians`, and the properties you need.  Now, initialize the starting condition in each array:

    y[ 0 ]  = initial_height
    vx[ 0 ] = initial_velocity * np.cos( angle * 2*np.pi/360 )
    vy[ 0 ] = initial_velocity * np.sin( angle * 2*np.pi/360 )  # (see "Angles" above)
    
## 5.  Now you are ready to begin the simulation proper.  You will need two loops, one over every angle, and one over every time step for that angle's launch.

    for j in range(0, 1001):  # loop over each time step
        # Check that the location isn't below the ground; if so, adjust as specified in the question above.
        if j == 0:
            continue
        # calculate the acceleration including drag (for both x and y, x shown)
        v = np.sqrt( vx[ j-1 ]**2 + vy[ j-1 ]**2 )
        ax = -( 0.5*rho*C*A/m_prop ) * v**2 * ( vx[ j-1 ] / v )
        ay = -( 0.5*rho*C*A/m_prop ) * v**2 * ( vy[ j-1 ] / v )
        vx[j] = vx[j-1] + ax*dt 
        vy[j] = vy[j-1] + (ay+g)*dt
        #x[i,j] = x[i,j-1] + vx[i,j-1]*dt + 0.5*ax*dt*dt
        #y[i,j] = y[i,j-1] + vy[i,j-1]*dt + 0.5*(ay+g)*dt*dt
        x[j] = x[j-1] + vx[j]*dt
        y[j] = y[j-1] + vy[j]*dt
        

        # calculate the change in position at time `t` using the current velocities (`vx[ i ][ j ]`) and the previous positions (`x[ i ][ j-1 ]`).  This is slightly different from the question you have solved in an earlier homework.

# 6.  The purpose of these calculations was to show which angle yielded the farthest distance.  Find this out and store the result in a variable named `best_angle`.
        if y[j] < 0:
            vx[j] = 0
            vy[j] = 0
            y[j] = 0
            break
    for k in range(j+1, 1001):
        x[k] = x[j]
        y[k] = 0
    
    plt.plot(x,y,'k-')
    plt.show()
    plt.xlim(0,150)
    plt.ylim(0,100)
    return x[-1]

## 6.  The purpose of these calculations was to show which angle yielded the furthest distance.  Find this out and store the result in a variable named `best_angle`.
#maxRow = x.max(1)
#best_angle = maxRow.argmax() + 1
#for i in range(1,91):
print(dist(30,0.1))
