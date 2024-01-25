"""
Updated on Jan 25, 2024

@author: ranaweer
"""
import numpy as np
import matplotlib.pyplot as plt

# SETTING UP THE STAGE
maxNumFloors = 10
numBuildings = 10
floorHeight = 4 # m
buildingSeparation = 10 # m
stageX = np.arange(0, numBuildings*buildingSeparation, buildingSeparation)
stageY = floorHeight * (1 + np.trunc(np.random.random(stageX.shape) * maxNumFloors))


# PLACING 2 PLAYERS
# For now, place two players on the second and the second-last building
# TODO: place the players on random building indices where the
# player should be placed in the left (west) half of the stage and
# the second player should be in the right (east) half of the stage.
# Don't put the both players on the same building. 
index = [1, numBuildings-2]


# Now, plot the stage with the players. 
plt.bar(stageX, stageY, width=buildingSeparation*0.9)
plt.axis([0, max(stageX), 0, 2*maxNumFloors*floorHeight])
plt.plot(stageX[index], stageY[index]+3, '*r', markersize=20)
plt.show()

# Player 1 throwing a banana
player1X = stageX[index[0]]
player1Y = stageY[index[0]]
a = float(input("Enter the angle for the player facing east: "))
v = float(input("Enter the velocity for the player facing east: "))

# Convert the angle into radians. Calculate the trajectory of the
# throw over a 5 second (tmax) period in steps of 0.1 seconds
tmax = 5
g = 9.81 # gravity
aRadians = np.radians(a)
t = np.arange(0, tmax, 0.1)
x = v *  np.cos(aRadians) * t
y= v * np.sin(aRadians) * t - 0.5 * g * t**2

# shift the origin of the projectile to the 
# first player's coordinates 
x = x + player1X;
y = y + player1Y;

# Now, plot the stage, the two players and the projectile of the 
# first player's throw. Note: we cannot just only plot the 
# projectile because we closed the plot using plt.show()
# previously; if we do so, the projectile will be drown on the plot
# without the stage or the player.
plt.plot(x, y, 'r')
plt.show()


# Player 2 throwing a banana
player2X = stageX[index[1]]
player2Y = stageY[index[1]]
a = float(input("Enter the angle for the player facing west: "))
v = float(input("Enter the velocity for the player facing west: "))

# We must subtract the angle from 180 degrees to get the angle
# from the right-end side of the x-axis
a = 180-a

# Convert the angle into radians. Calculate the trajectory of the
# throw over a time interval as same as previously
aRadians = np.radians(a)
x = v *  np.cos(aRadians) * t
y= v * np.sin(aRadians) * t - 0.5 * g * t**2

# shift the origin of the projectile to the 
# second player's coordinates 
x = x + player2X;
y = y + player2Y;

# Now, once again plot the stage, two players, and the 
# new projectile all over again

