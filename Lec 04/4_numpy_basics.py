#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:17:37 2023

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
array_1 = np.array(list_1)

list_2 = [[1,2,3], [4,5,6]]
array_2 = np.array(list_2)

# arange
# ======
#
# Allows us to create 1-dimensional arrays (or vectors)

# Creating a range from 0 to 10, inclusive
a1 = np.arange(0, 11)

# Creating a range from -5 to 5, inclusive
a2 = np.arange(-5,6)

# Creating a range from -5 to 5, inclusive, in steps of 0.5 increments
a3 = np.arange(-5,5.1, 0.5)


# zeros
# =====
#
# Allows us to create vectors and multi-dimensional arrays filled with zeros

# Creating a one-dimensional vector of 10 zeros
v1 = np.zeros(10)

# Creating a 4x3 matrix of zeros
m1 = np.zeros((4,3))
#print('m1:\n', m1) 

# Finding the shape of m1
print('m1 shape:', m1.shape)

# full
# ====
#
# Allows us to create vectors and arrays filled with a given number

# creating a five-element array filled with number 3
v5 = np.full(5, 3)
print('v5:\n', v5)

# Creating a 4x3 array (or matrix) that is full of value 8
m2 = np.full((4,3), 8)
print('m2:\n', m2)


