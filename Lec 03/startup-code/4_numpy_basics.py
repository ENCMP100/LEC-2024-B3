"""

@author: ranaweer
"""

# Numpy
# =====
# Numpy substantially increases the storage and access effiency by giving us
# functions to create and manipulates arrays of values of the same type ((usually
# numerical)

import numpy as np
import numpy.random as rand

# array
# ===== 
#
# Converts a list to an array
list_1 = [1, 2, 3, 4, 5]
#array_1 = 

list_2 = [[1,2,3], [4,5,6]]
#array_2 = 

# arange
# ======
#
# Allows us to create 1-dimensional arrays (or vectors)

# Creating a range from 0 to 10, inclusive
#a1 = 

# Creating a range from -5 to 5, inclusive
#a2 = 

# Creating a range from -5 to 5, inclusive, in steps of 0.5 increments


# zeros
# =====
#
# Allows us to create multi-dimensional arrays

# Creating a one-dimensional vector of zeros
#v1 = 

# Creating a 4x3 matrix of zeros
#m1 = 
#print('m1:\n', m1) 

# Finding the shape of m1
#print('m1 shape:', m1.shape)

# Creating a 4x3 array (or matrix) that is full of value 8
#m2 = 
#print('m2:\n', m2)

# Creating a vector of 10 random numbers
#rand_vec_10 = 
#print('rand_vec_10:', rand_vec_10)

# Creating a 4x3 array filled with random numbers
#m3 = 
#print('m3:\n', m3)

# reshaping a matrix
v2 = np.arange(1, 13) # a 12-element vector
print('v2:\n', v2)

# Reshaping v2 as a 2x6 matrix
#m2x6 =
#print('m4:\n', m2x6)

# Reshaping v2 as a 4x3 matrix
#m4x3 = 
#print('m4:\n', m4x3)


# Copying an array
#v2_copy = 

# Cumulative sum of values in an array v2
#v2_cumsum = 
#print(v2)
#print(v2_cumsum)

