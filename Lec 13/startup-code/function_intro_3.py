## Computes the volumne of a cube
# @param sideLength: the length of a side
# @return 
#    The volume of the cube if sideLength is positive, 
#    or None, otherwise
#
def cubeVolume(sideLength):
    if sideLength >= 0:        
        volume = sideLength ** 3
        return volume
   
    

# Testing
print("cubeVolume(5) =", cubeVolume(5))
print("cubeVolume(-2) =", cubeVolume(-2))
