"""
Examples of array math with Numpy

Reference: Lee 2

"""

import numpy as np

# Ex 1: Array addition
x1 = np.array([[1,2,3],[4,5,6]]) 
y1 = np.array([[7,8,9],[2,3,4]])
z1 = x1 + y1
print(x1)
print(y1)
print(z1)


# Ex 2: Array division and exponent (works on element-byelement-basis) 
# Calculating the Body Mass Index of a set of data
heights = np.array([1.5, 1.78, 1.6]) 
weights = np.array([65, 46, 59]) 
bmi = weights / heights**2
print("BMI:", bmi)


# EX 3: dot product
x = np.array([2,3]) 
y = np.array([4,2]) 
z = np.dot(x,y)  # 2x4 + 3x2 = 14
print("x dot y =", z)


# EX 5: Cumulative Sum for a vector (1-D array)
v = np.array([1,2,3,4,5,6,7,8,9]) 
print(v)
c1 = v.cumsum() # Cumulative sum of all elements in the vector
print(c1)


# EX 5: Cumulative Sum for a matrix (2-D array)
a = np.array([(1,2,3),(4,5,6), (7,8,9)]) 
print(a)
c2 = a.cumsum() # A vector that contains the cumulative sum of all elements in the array
print(c2)


