#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


## Drawing Shapes
#  ==============

plt.axis([0, 299, 0, 299]) # sets xmin, xmax, ymin, ymax of the axes

ax = plt.gca() # Get Current Axes

# Set the figure to have equal axes to avoid 
# deforming figures.
ax.set_aspect('equal') # same as ax.set_aspect(1)

# Drawing a red circle with radius 25, which is
# centred at (x,y) = (50,50)
cir = Circle((50,50), 25)
cir.set_facecolor('red')
ax.add_patch(cir)
cir.set_edgecolor('blue')



# Drawing a gree rectangle of width 100, height 50
# and placed at 100, 100 (xmin,ymin position).
# Here, we specify the color while creating the patch
# instead of using set_facecolor method of the patch
rec = Rectangle((100,100), 100, 50, facecolor='green', edgecolor='red')
ax.add_patch(rec)

# Let's add some text starting from 100, 200 (x,y) position
ax.text(100,200, "My First Graphic", color='#7727AB')

# Let's hide the axis labels
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.savefig('my_graphic.png', dpi=600)
plt.savefig('my_graphic.svg')

plt.show()

