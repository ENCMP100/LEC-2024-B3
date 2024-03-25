"""
Gorillas game Version 4

"""
import matplotlib.pyplot as plt
from gorillasMethods import createStage, getPlayerIndicies, plotStage, plotTrajectory, getThrowParameters, calcTrajectory

N = 11
BW = 12


stage = createStage(N, BW)
playerIndicies = getPlayerIndicies(N)
stage['playerIndicies'] = playerIndicies

plotStage(stage)
plt.show()
   
winner = ''
play = True
while play:
    
    for playerNum in range(2):
        (angle, velocity) = getThrowParameters(playerNum)
        (trajectoryX, trajectoryY, splatBuildingIndex) = calcTrajectory(
            stage, playerNum, playerIndicies[playerNum], angle, velocity)

        plotStage(stage)           
        plotTrajectory(trajectoryX, trajectoryY)
        plt.show()
    
    
        if playerNum == 0:
            target = 1
        else:
            target = 0
        if splatBuildingIndex == playerIndicies[target]:
            winner = 'Player ' + str(playerNum + 1)
            play = False
            break # breaks the for loop


# Done playing
# ============
if not winner == '':
    print(winner, 'Won! Game Over ...')

print('Thank you for playing.')
    
