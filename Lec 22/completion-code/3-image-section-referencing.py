#E Working with Images

import matplotlib.pyplot as plt

# Loading the image
img = plt.imread('mandrill.jpg')
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Full Image')

#Cropping the image
plt.subplot(1,2,2)
img2 = img[300:900, 200:600, :]
plt.imshow(img2)
plt.title('Cropped Image')

#Saving the cropped image
plt.imsave('mandrill-face.jpg', img2)





