"""
Gorillas game Version 4

"""
import numpy as np
import matplotlib.pyplot as plt
 

# CREATE STAGE: creates the x and y coordinates of the stage that represents
# the buildings
def createStage(n, bw):
    global stage
    
    x = np.arange(0, n) * bw #Positions (m).
    y = (1 + np.random.random(x.shape) * n) * n/2
    
    return {'x':x, 'y': y, 'bw': bw, 'splatX': [], 'splatY': []}

# ===============================================

## GET PLAYER INDICIES: returns randomly selected buildings indicies for players.
def getPlayerIndicies(n):
    # First player on a building in the first half of the stage and the second
    # player on the second half of the stage. Skip the first and last buildings
    index1 = np.random.randint(1, n//2)
    index2 = np.random.randint(n//2, n-2)
    return (index1, index2)  
    

# ===============================================

## PLOTSTAGE: plots the buildings and places the players on top of them.
#  Also plots where the bananas hit buildings if splatX, splatY contains data
#  Note that we do not call plt.show() here because we want to plot the
#  trajectory of a throw on this same plot.
def plotStage(stage):
    sx = stage['x']
    sy = stage['y']
    splatX = stage['splatX']
    splatY = stage['splatY']
    playerIndicies = stage['playerIndicies']
    bw = stage['bw']
    n = len(sx)
    
    print(splatX)
    plt.bar(sx, sy, width=bw*0.9)
    plt.axis([0, max(sx), 0, np.round(n**2)])
    plt.plot(sx[playerIndicies[0]], sy[playerIndicies[0]]+4, '*g', markersize=15)
    plt.plot(sx[playerIndicies[1]], sy[playerIndicies[1]]+4, '*b', markersize=15)  
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
def calcTrajectory(stage, playerNumber, playerBuildingIndex, a, v):
    #global splat

    sx = stage['x']
    sy = stage['y']
    bw = stage['bw']
    n = len(sx)
    
    t = np.arange(0, 1000, 0.1) # time (s)
    g = 9.81
    
    x = v *  np.cos(a) * t
    y = v * np.sin(a) * t - 0.5 * g * t**2
    
    x = sx[playerBuildingIndex] + x
    y = sy[playerBuildingIndex] + 4 + y
    
    
    #Stop the banana when it splats on a building
    #
    # calculate the closest building index for every
    # x value
    buildingIndex = -1
    splatBuildingIndex = -1
    for i in range(1, len(x)):
        
        # We want to limit the trajectoty within the
        # range of x values in stageX
        if x[i] < sx[0] or x[i] > sx[n-1]:
            break
        
        buildingIndex = int(np.round(x[i]/bw))
        if y[i] < sy[buildingIndex]:
            # Hits the building
            np.append(stage['splatX'], x[i])
            np.append(stage['splatY'], y[i])
            splatBuildingIndex = buildingIndex
            print('splatX', stage['splatX'])
            break # breaks the for loop
            
    # we do not need any trajectory beyond the 
    # the current ''th posiiton
    x = x[0:i+1]
    y = y[0:i+1]
    
    return (x, y, splatBuildingIndex)