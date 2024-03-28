## Working with Images

import matplotlib.pyplot as plt
import numpy as np

# Loading the image
img = plt.imread('mandrill.jpg')
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')
ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)


## Creating a full copy of img so that we can modify it.

# Allocate img2 to be an n-dimensional array of zeros with 
# the same size and same type as img
img2 = np.zeros(img.shape,img.dtype)

# Copying each color plane of img to corresponding plane in img2
img2[:,:,:] = img[:,:,:] # Note: img2 = img would NOT work since 
                         # it will simply make img2 a reference 
                         # to img instead a complete clone of data


# Let's add a black border of 50 pixels around img2.
# We do it by setting zero to all color planes in this border

h,w,_ = img2.shape # width and height. We don't care about
                   # rge number of planes, hence use _ to
                   # ignore the third output value
                   
img2[0:50, :, :] = 0   # Top border (first 50 rows, all columns, all planes)
img2[:, 0:50, :] = 0   # Left border (all rows, first 50 columns, all planes)
img2[h-50:h, :, :] = 0 # Bottom border (last 50 rows, all columns, all planes)
img2[:, w-50:w, :] = 0 # Right border (all rows, last 50 columns, all planes)

plt.subplot(1,2,2)
plt.imshow(img2)
ax2 = plt.gca()
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
plt.title('Image with Border')
plt.show()

"""
plt.subplot(1,2,1)
imUint8 = np.zeros((256,256,3), np.uint8)
imUint8[:,:,0] = 204
plt.imshow(imUint8)
plt.title('UNIT8 image')

plt.subplot(1,2,2)
imFloat = np.zeros((256,256,3))
imFloat[:,:,0] = 0.8
plt.imshow(imFloat)
plt.title('Float image')
"""

