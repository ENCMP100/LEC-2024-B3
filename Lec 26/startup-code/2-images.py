## Images

import numpy as np
import matplotlib.pyplot as plt

## Load and display an image
flag = plt.imread('ukr-flag-downloaded.jpg')
plt.subplot(2,1,1)
plt.imshow(flag)
ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

## Create a synthetic image using a 3-D uint8 array

ukrFlag = np.zeros((300, 400, 3), np.uint8) # 300x400 pixels

# upper half has a shade of blue containing R=0, G=91, B=187
ukrFlag[0:150, :, 1] = 91
ukrFlag[0:150, :, 2] = 187

# lower half has a shade of yellow containing R = 255, G=213, B=0
ukrFlag[150:300, :, 0] = 255
ukrFlag[150:300, :, 1] = 213

plt.subplot(2,1,2)
plt.imshow(ukrFlag)
ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.imsave('ukr-flag-created.jpg', ukrFlag)






