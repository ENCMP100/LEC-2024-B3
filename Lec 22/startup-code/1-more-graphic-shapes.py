## Introduction to Graphics

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


## Drawing an Ellipse
#  ==================

plt.axis([0, 299, 0, 299]) # sets xmin, xmax, ymin, ymax of the axes

ax = plt.gca() # Get Current Axes

# Set the figure to have equal axes to avoid 
# deforming figures.
ax.set_aspect('equal') # same as ax.set_aspect(1)

# Drawing an ellipse
# centred at (x,y) = (50,50)
my_ellipse = Ellipse((100,100), # centre
                     100, # width
                     50, # height
                     45) # angle of rotation in degrees
my_ellipse.set_facecolor('red')
my_ellipse.set_edgecolor('blue')
ax.add_patch(my_ellipse)

plt.show()


## Drawing a Pie Chart on the Current Axes
#  =======================================

labels = ["Chrome", "Internet Explorer", "Firefox", "Edge","Safari", "Sogou Explorer","Opera","Others"]
marketshare = [61.64, 11.98, 11.02, 4.23, 3.79, 1.63, 1.52, 4.19] 
explode = (0,0,0,0,0,0,0,0) 
#explode = (0,0.05,0,0.1,0,0.1,0.05,0.1) 

plt.pie(marketshare,
        explode = explode, # fraction of the radius with which to # offset each wedge
        labels = labels, 
        autopct = "%.1f%%", # string or function used to label the # wedges with their numeric value
        shadow = True, 
        startangle = 45) # rotates the start of the pie chart by # angle degrees counterclockwise from the # x-axis

plt.title("Web Browser Marketshare - 2018")
plt.show()



## Drawing a Pie Chart on a Specifix Axes
#  =======================================

labels = ["Chrome", "Internet Explorer", "Firefox", "Edge","Safari", "Sogou Explorer","Opera","Others"]
marketshare = [61.64, 11.98, 11.02, 4.23, 3.79, 1.63, 1.52, 4.19] 
explode = (0,0.05,0,0.1,0,0.1,0.05,0.1) 

ax = plt.gca() # Get Current Axes

ax.pie(marketshare,
       explode = explode, # fraction of the radius with which to # offset each wedge
       labels = labels, 
       autopct = "%.1f%%", # string or function used to label the # wedges with their numeric value
       shadow = True, 
       startangle = 45) # rotates the start of the pie chart by # angle degrees counterclockwise from the # x-axis

plt.title("Web Browser Marketshare - 2018")

plt.show()
