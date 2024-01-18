"""
Created on Wed Jan 11 19:32:41 2023

@author: ranaweer
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style


# Calculating a projectile motion under gravity


"""
A bullet shot to the sky leaves the gun at an initial velocity u = 500 meters 
per second at an angle theta = 75 degrees to the horizontal. Assuming there
is no air resistance, the height "h" of the bullet in the projectile can be 
calculated at agiven time "t" (in seconds, since the shot is triggered) by the 
following equation.

    h = u sin(theta) t - (1/2) g t^2 
        where g is the gravitational constant and t^2 denotes t-square
        
Plot the h vs t projectile for a period of time from 0 to 75 seconds in
1-second increments.

Emperically adjust the time range until you get the graph showing the full
projectile approximately.

Show the plot title, axis labels, grid, etc.
"""

u = 500
theta = 77
t = np.arange(0, 100)
g = 9.81
h = u * np.sin(np.radians(theta)) * t - (1/2) * g * t ** 2

# Plot height vs time; specify the colour of the graph and the legend label
plt.plot(t, h, color="r", label="height")

# Set the x-axis label
plt.xlabel('Time')

# Set the y-axis label
plt.ylabel('Height')

# Turn the grid on and set the grid-lines color to cyan
plt.grid(visible = True, color="c")

# Display the legend
plt.legend()


