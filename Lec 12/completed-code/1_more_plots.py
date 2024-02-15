"""
This script demonstrates a set of plot functions.
"""

import numpy as np
import matplotlib.pyplot as plt

## EX 1
## ====

# Line Chart
theta = np.arange(0, 2 * np.pi, 0.1) # angle in radians
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)

plt.plot(theta, sin_theta, color='r', label='sine')
plt.plot(theta, cos_theta, color='b', label='cosine')
plt.xlabel('angle (radians)')
plt.ylabel('function value')
plt.title('Trigonometric Functions')
plt.grid(visible=True, color='c') #cyan color
plt.legend()
plt.show()


## EX 2
## ====

# Bar Chart
# Lee page 73, combined book page 137

semester = [1,2,3,4,5,6,7,8,9,10]
grade = [2,4.5,1,2,3.5,2,1,2,3,2]
plt.bar(
        semester, 
        grade, 
        label = "Jim", 
        color = "m",      # m for magenta 
        align =  "center" ) 

plt.title("Results") 
plt.xlabel("Semester") 
plt.ylabel("Grade")
plt.legend()
plt.grid(True, color="y") 
plt.show()


## EX 3
## ====

# Two bar charts in one figure
# Lee page 74, combined book pge 138

semester = [1,2,3,4,5,6,7,8,9,10]
jim_grade = [2,4.5,1,2,3.5,2,1,2,3,2]
tim_grade = [1.2,4.1,0.3,4,5.5,4.7,4.8,5.2,1,1.1]

plt.bar(
        semester, 
        jim_grade, 
        label = "Jim", 
        color = "m",      # m for magenta 
        align =  "center",
        alpha = 0.75) 

plt.bar(
        semester, 
        tim_grade, 
        label = "Tim", 
        color = "g",      # g for green 
        align =  "center",
        alpha = 0.5) 

plt.title("Results") 
plt.xlabel("Semester") 
plt.ylabel("Grade")
plt.legend()
plt.grid(True, color="y") 
plt.show()


## EX 4
## ====

# Changin tick marks
# Lee page 75, combined book page 139

rainfall = [17,9,16,3,21,7,8,4,6,21,4,1] 
months = ['Jan','Feb','Mar','Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']
 
plt.bar(months, rainfall, align='center', color='blue' )
plt.xticks(rotation='vertical')
plt.show()

## EX 5
## ====

# subplot and axis

theta = np.radians(np.arange(0.01, 10000, 0.1)) # angle in radians
y = 1 + np.cos(theta/10) * np.sin(theta)/theta # Some simulated waveform

plt.subplot(221) # 2 rows, 2 columns, 1st plot
plt.plot(theta, y)
plt.grid(visible=True)
plt.title('Default')

plt.subplot(222) # 2 rows, 2 columns, 2nd plot
plt.plot(theta, y)
plt.grid(visible=True)
plt.axis([min(theta), max(theta), min(y), max(y)])
plt.title('Axis Limits Set')

plt.subplot(223) # 2 rows, 2 columns, 3rd plot
plt.plot(theta, y)
plt.axis([15, 75, 0.8, 1.2])
plt.xticks(np.arange(15, 75, 5))
plt.grid(visible=True)
plt.title('Zoomed to an Interval')


plt.subplot(224) # 2 rows, 2 columns, 4th plot
plt.plot(theta, y)
plt.axis([15, 75, 0.8, 1.2])
plt.xticks(np.arange(15, 75, 5), rotation = 'vertical')
plt.grid(visible=True)
plt.title('Zoomed with ticks rotated')

# The following  tight_layout function is
# NOT in the ENCMP100 syllabus but it is a
# useful function to ensure subplots are 
# layed out properly spaced (without overlapping)
# plt.tight_layout()

