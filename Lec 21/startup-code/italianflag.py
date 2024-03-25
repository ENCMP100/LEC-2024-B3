##
#  This program draws an Italian flag using the ezgraphics module.
#

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.axis((0, 299, 0, 299))
ax = plt.gca()
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Define variables with the upper-left position and the size.
xLeft = 100
yTop = 100
width = 90

# Draw the flag.
ax.add_patch(Rectangle([xLeft, yTop], width/3, width*2/3,
                       facecolor='green', edgecolor='black'))
ax.add_patch(Rectangle([xLeft + 2*width/3, yTop], width/3, width*2/3,
                       facecolor='red', edgecolor='black'))
ax.add_patch(Rectangle([xLeft + width/3, yTop], width/3, width*2/3,
                       facecolor='white', edgecolor='black'))

# Wait for the user to close the window.
plt.show()
