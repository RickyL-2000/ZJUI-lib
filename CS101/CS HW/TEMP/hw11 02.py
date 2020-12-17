# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:19:03 2018

@author: RickyLi
"""
import numpy as np
import matplotlib.pyplot as plt
def dist( angle,m_prop ):

# Reference code from HW10
# 0.  Place your necessary imports here.  You may find it useful to be able to plot when debugging and visualizing your result.


# 1.  Create a 1D vector named `t` and 2D arrays named `vx`, `vy`, `x`, and `y` to hold the state variables, of size 90 x 1001.
    t = np.linspace(0,10,1001)
    vx = np.zeros([1001])
    vy = np.zeros([1001])
    x = np.zeros([1001])
    y = np.zeros([1001])

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

    for j in range(1,1001):  # loop over each time step
#        # check that the location isn't below the ground; if so, adjust as specified above
#        #print("i=", i, " j=" ,j, " y=", y[i][j-1])
        if y[j-1] <= 0.0:
            #print("Negative when i=", i, "j=" ,j)
            vx[j] = vy[j] = vx[j-1] = vy[j-1] = y[j] = y[j-1] = 0.0
            x[j-1] = x[j-2]
            x[j] = x[j-1]
            continue
            
#        # calculate the acceleration including drag (for both x and y, x shown)
        v = np.sqrt( vx[ j-1 ]**2 + vy[ j-1 ]**2 )
        ax = -( 0.5*rho*C*A/m_prop ) * v**2 * ( vx[ j-1 ] / v )
        ay = -( 0.5*rho*C*A/m_prop ) * v**2 * ( vy[ j-1 ] / v )  
        
#        # calculate the change in position at time `ts` using the current velocities (`vx[ i ][ j ]`) and the previous positions (`x[ i ][ j-1 ]`).  This is slightly different from the previous example you solved in an earlier homework.
        vy[j] = vy[j-1] + (ay+g)*dt
        vx[j] = vx[j-1] + ax*dt
            
        x[j] = x[j-1] + vx[j]*dt
        y[j] = y[j-1] + vy[j]*dt
        
    plt.plot(x,y,'k-')
    plt.xlim(0,150)
    plt.ylim(0,100)
    plt.show()
    return x[-2]

## 6.  The purpose of these calculations was to show which angle yielded the furthest distance.  Find this out and store the result in a variable named `best_angle`.
#maxRow = x.max(1)
#best_angle = maxRow.argmax() + 1
for i in range(1,91):
    dist(i,0.1)