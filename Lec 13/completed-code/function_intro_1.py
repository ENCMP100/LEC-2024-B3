
def main():
    side = 5
    vol1 = cubeVolume(side)
    print(vol1)

    vol2 = cubeVolume(10)
    print(vol2)

    vol3 = cubeVolume(-5)
    print(vol3)

main()


## Computes the volumne of a cube
# @param sideLength: the length of a side of the cube
# @return the volume of the cube
#
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume
    






