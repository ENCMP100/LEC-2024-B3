"""
Created on Jan 22, 2024

@author: ranaweer
"""


import numpy as np


# reshape function
# ================
#
# The "reshape" function allows us to reshape an array or a matrix by changing
# its number of rows and columns AS LONG AS we keep the total number of 
# elements unchanged.
# The reshape function returns a shallo copy of the original.

x = np.arange(1, 13) # a 12-element vector
print('v1:\n', x)

# Reshaping v2 as a matrix (2-D array) of 2 rows and while letting reshape to
# automatically calculate the number of columns 
m1 = x.reshape(2, -1)
print('m1:\n', m1)

# Reshaping v2 as a matrix of 3 columns and while letting reshape to
# automatically calculate the number of rows 
m2 = x.reshape(-1, 3) 
print('m2:\n', m2)

# Since reshape creates a shallo copy, the x, m1, and m2 refers to 
# the same data in memory. Changing values of one of them will change
# the corresponding values on the others.

x[2] = 100 # Change the third element in x
print('x:\n', x)
print('m1:\n', m1)
print('m2:\n', m2)



# shape property
# ==============
#
# The shape property of an array allows us to retrieve its dimensions as a tuple.
# It also allows us to modify the shape of the array.

x2 = np.arange(1,13) # a 12 element vector
print('x2:', x2)
print('shape of x2', x2.shape)

# Reshape x2 itself to be a matrix with 4 rows without creating a shallow copy
x2.shape = 4,-1  # -1 indicates that the columns should be calculated automatically.
                 # Alternatively, we could have specified column count to be 3 
                 # because 4x3 is 12, which is the original length of x2




# view function
# =============
#
# The view function creates a shallow copy of the orginal array that will not
# change its shape when the original array's shape is changed.
#

x3 = np.array([[1,2,3], 
               [4,5,6],
               [7,8,9]])

x3_a = x3; #Create a "reference" copy by assignment
x3_b = x3.view() # Create a "shallow copy" using the view function
x3_c = x3.copy()

print('x3.shape:', x3.shape)
print('x3_a.shape:', x3_a.shape)
print('x3_b.shape:', x3_b.shape)

# reshape x3 using shape property to be a 9x1 vector
x3.shape = 9,-1
print('x3.shape after reshaping x3:', x3.shape)
print('x3_a.shape after reshaping x3:', x3_a.shape) # NOTE: the shape of x3_a has change identical to x3
print('x3_b.shape after reshaping x3:', x3_b.shape) # NOTE: the shape of x3_b remains unchanged




# copy function -- making a deep copy
# ===================================
#
# Assigning an array to another array simply make a duplicate "reference"
# to the orginal array. The "view" function creates a "shallow copy". In both of 
# these cases, the element values in the new array refers to the same values 
# in the original. If you change any element using either the original or the 
# new variabe, the corresponding elements in the other will also be changed.
#
# If you want to make a complete copy of the data, you should use the copy
# function to create a deep copy.
#

x4 = np.arange(1,5) # a 5 element vector
x4_copy = x4.copy()

print('x4:', x4)
print('x4_copy:', x4_copy)

# Change the 3nd element inf x4 to 100
x4[1] = 100
print('x4 after changing x4:', x4)
print('x4_copy after changing x4:', x4_copy)


