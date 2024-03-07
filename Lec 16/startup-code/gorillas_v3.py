"""
Gorillas game Version 3

"""
import numpy as np
import matplotlib.pyplot as plt

N = 11
BW = 12
stageX = []
stageY = []
splatX = [] # x coordinate of points where banana hist a building
splatY = [] # y coordinate of points where banana hist a building



## Main function that implements the high-level program flow
def main():
    createStage()
    playerIndicies = getPlayerIndicies()
    plotStage(playerIndicies)
    plt.show()
   
    winner = ''
    play = True
    while play:
        
        for playerNum in range(2):
            (angle, velocity) = getThrowParameters(playerNum)
            (trajectoryX, trajectoryY, splatBuildingIndex) = calcTrajectory(
                playerNum, playerIndicies[playerNum], angle, velocity)

            plotStage(playerIndicies)
            plotTrajectory(trajectoryX, trajectoryY)
            plt.show()
        
            if splatBuildingIndex == playerIndicies[1]:
                winner = 'Player ' + str(playerNum + 1)
                play = False
                break # breaks the for loop

    
    # Done playing
    # ============
    if not winner == '':
        print(winner, 'Won! Game Over ...')
    
    print('Thank you for playing.')
    

# ===============================================

## CREATE STAGE: creates the x and y coordinates of the stage that represents
#  the buildings  
def createStage():
    global stageX
    global stageY
    
    stageX = np.arange(0, N) * BW #Positions (m).
    stageY = (1 + np.random.random(stageX.shape) * N) * N/2

# ===============================================

## GET PLAYER INDICIES: returns randomly selected buildings indicies for players.
def getPlayerIndicies():
    # First player on a building in the first half of the stage and the second
    # player on the second half of the stage. Skip the first and last buildings
    index1 = np.random.randint(1, N//2)
    index2 = np.random.randint(N//2, N-2)
    return (index1, index2)  
    
# ===============================================

## PLOTSTAGE: plots the buildings and places the players on top of them.
#  Also plots where the bananas hit buildings if splatX, splatY contains data
#  Note that we do not call plt.show() here because we want to plot the
#  trajectory of a throw on this same plot.
def plotStage(playerIndicies):
    plt.bar(stageX, stageY, width=BW*0.9)
    plt.axis([0, max(stageX), 0, np.round(N**2)])
    plt.plot(stageX[playerIndicies[0]], stageY[playerIndicies[0]]+4, '*g', markersize=15)
    plt.plot(stageX[playerIndicies[1]], stageY[playerIndicies[1]]+4, '*b', markersize=15)  
    if len(splatX) > 0:
        plt.plot(splatX, splatY, "*r")
        
# ===============================================
    
## PLOTTRAJECTORY: plots the trajectory of a throw.
def plotTrajectory(trajectoryX, trajectoryY):
    plt.plot(trajectoryX, trajectoryY, 'r')


# ===============================================

## GET THROW PARAMETERS: obtains the angle and velocity of throw for a given 
#  player as user inputs and returns them. Angle is obtained in degrees as an
#  acute andgle but returns its value in radians measured from the standard
#  horizontal axix and measured in counter-clockwise 
def getThrowParameters(playerNumber):
    print()
    if playerNumber == 0: # giving first turn to the first player
        print("Player 1 (facing east)")
        angle = float(input("    Angle (degrees): "))
    else: # giving the second turn to the second player
        print("Player 2 (facing west)")
        angle = 180 - float(input("    Angle (degrees): "))    
    
    angle = np.radians(angle)
    velocity = float(input("    Velocity (m/s): ")) 
    
    return (angle, velocity)

# ===============================================

## CALC TRAJECTOR: Calculates the trajectory of a throw for a given player
#  for a given angle and velocity
def calcTrajectory(playerNumber, playerBuildingIndex, a, v):
    global splatX
    global splatY
    
    t = np.arange(0, 1000, 0.1) # time (s)
    g = 9.81
    
    x = v *  np.cos(a) * t
    y = v * np.sin(a) * t - 0.5 * g * t**2
    
    x = stageX[playerBuildingIndex] + x
    y = stageY[playerBuildingIndex] + 4 + y
    
    
    #Stop the banana when it splats on a building
    #
    # calculate the closest building index for every
    # x value
    buildingIndex = -1
    splatBuildingIndex = -1
    for i in range(1, len(x)):
        
        # We want to limit the trajectoty within the
        # range of x values in stageX
        if x[i] < stageX[0] or x[i] > stageX[N-1]:
            break
        
        buildingIndex = int(np.round(x[i]/BW))
        if y[i] < stageY[buildingIndex]:
            # Hits the building
            splatX.append(x[i])
            splatY.append(y[i])
            splatBuildingIndex = buildingIndex
            break # breaks the for loop
            
    # we do not need any trajectory beyond the 
    # the current ''th posiiton
    x = x[0:i+1]
    y = y[0:i+1]
    
    return (x, y, splatBuildingIndex)
    
# ===============================================

## Calls the main function to start the program
main()
