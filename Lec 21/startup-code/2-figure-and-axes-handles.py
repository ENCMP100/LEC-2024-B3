## SUBPLOTS allows us to create one or more subplots and
#  plot on them using handles

import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

## A figure with just one subplot
#  ==============================
fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_title('A Single Plot')


## A figure with two side-by-side subplots
#  =======================================
fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x, y, 'green')
ax2.plot(x, y, '--r')

# Since we use apprpriate axes to refer to each subplot, we
# no longer need to finish the work of one subplot before 
# work with the other.
ax1.set_title('First Subplot')
ax2.set_title('Second Subplot')

# Let's add a title to the figure
fig.suptitle('Figure Title') # NOT IN EXAM SYLLABUS