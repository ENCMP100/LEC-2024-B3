"""
Created on Sun Jan 15 20:19:50 2023

@author: ranaweer
"""

import numpy as np
import matplotlib.pyplot as plt

# Line Chart
# ==========
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


# Bar Chart
# =========
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


# Two bar charts in one figure
# Lee page 74, combined book pge 138

plt.show()
semester = [1,2,3,4,5,6,7,8,9,10]
jim_grade = [2,4.5,1,2,3.5,2,1,2,3,2]
tim_grade = [1.2,4.1,0.3,4,5.5,4.7,4.8,5.2,1,1.1]

plt.bar(
        semester, 
        jim_grade, 
        label = "Jim", 
        color = "m",      # m for magenta 
        align =  "center",
        alpha = 0.5) 

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


# Changin tick marks
# Lee page 75, combined book page 139
"""
plt.show()

rainfall = [17,9,16,3,21,7,8,4,6,21,4,1] 
months = ['Jan','Feb','Mar','Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']
 
plt.bar(months, rainfall, align='center', color='orange' ) 

plt.xticks(rotation='vertical')
"""

# subplot and axis
# ================

"""
plt.show()
theta = np.radians(np.arange(10000)) # angle in radians
y = 1 + np.cos(theta/10) * np.sin(theta)/theta # Some simulated waveform

plt.subplot(221)
plt.plot(theta, y)
plt.grid(visible=True)
plt.title('Full Wave Form')

plt.subplot(222)
plt.plot(theta, y)
plt.axis([15, 75, 0.8, 1.2])
plt.xticks(np.arange(15, 75, 5), rotation = 'vertical')
plt.grid(visible=True)
plt.title('Zoomed Interval')

"""



