## Working with Images

import matplotlib.pyplot as plt

# Loading the image
img = plt.imread('mandrill.jpg')
plt.imshow(img)

ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)


