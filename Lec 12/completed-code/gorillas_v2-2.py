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
plt.bar(stageX, stageY, width=buildingSeparation*0.8)
plt.axis([0, max(stageX), 0, 2*maxNumFloors*floorHeight])
plt.plot(stageX[index], stageY[index]+3, '*r', markersize=20)
plt.show()

g = 9.81 # gravity
tmax = 10 # time
t = np.arange(0, tmax, 0.1)
play = True
while play:
    
    for playerNumber in range(0,2):
        
        if playerNumber == 0:
            activePlayerIndex = index[0]
            opponentIndex = index[1]
            a = float(input("Enter the angle for the player facing east: "))
        else:
            activePlayerIndex = index[1]
            opponentIndex = index[0]
            a = 180 - float(input("Enter the angle for the player facing west: "))
                

        v = float(input("Enter the velocity: "))

        # Player 1 throwing a banana
        playerX = stageX[activePlayerIndex]
        playerY = stageY[activePlayerIndex]

    
        # Convert the angle into radians. Calculate the trajectory of the
        aRadians = np.radians(a)
    
        x = v *  np.cos(aRadians) * t
        y = v * np.sin(aRadians) * t - 0.5 * g * t**2
    
        # shift the origin of the projectile to the 
        # first player's coordinates 
        x = x + playerX;
        y = y + playerY;
    
        
        # Now, plot the stage, the two players and the projectile of the 
        # first player's throw. Note: we cannot just only plot the 
        # projectile because we closed the plot using plt.show()
        # previously; if we do so, the projectile will be drown on the plot
        # without the stage or the player.
        plt.bar(stageX, stageY, width=buildingSeparation*0.8)
        plt.axis([0, max(stageX), 0, 2*maxNumFloors*floorHeight])
        plt.plot(stageX[index], stageY[index]+3, '*r', markersize=20)
        plt.plot(x, y, 'r')
        plt.show()
    

print('Game Over')
