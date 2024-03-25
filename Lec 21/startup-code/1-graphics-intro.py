## Introduction to Graphics

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

## Manipulating axes with GCA (Get Current Axes)
#  =============================================

y = np.random.randint(5, 20, 10)
x = np.arange(0, len(y))

# Let's use subplot to create two plots in the same figure 
# for comparison and plot y vs x in both subplots
plt.subplot(1,2,1)
plt.bar(x, y)

plt.subplot(1,2,2)
plt.bar(x, y)

# GCA: get the current axes, which is the axes of the second plot
ax = plt.gca() 

# INVERT_YAXIS: inverts the y axis
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.show() #complete the current figure


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
rec = Rectangle((100,100), 100, 50, color='green')
ax.add_patch(rec)

# Let's add some text starting from 100, 200 (x,y) position
ax.text(100,200, "My First Graphic", color='#8B0000')

# Let's hide the axis labels
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
