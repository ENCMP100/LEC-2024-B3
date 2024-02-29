## Computes the volumne of a cube
# @param sideLength: the length of a side
# @return 
#    The volume of the cube if sideLength is positive, 
#    or zero otherwise
#
def cubeVolume(sideLength):
    if sideLength < 0:
        return 0 #Returns the function immediately
    
    volume = sideLength ** 3
    return volume

