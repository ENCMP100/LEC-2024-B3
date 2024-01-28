"""
Jan 27, 2024

@author: ranaweer
"""


import numpy as np

# 1-D array indexing and slicing
# ==============================
v = np.arange(10)
print(v)
print(v[2:5])

v[2:5] = -1
print(v)


# 2-D array (matrix) indexing and slicing
# =======================================

a = np.array([[1,2,3,4,5], 
              [4,5,6,7,8], 
              [9,8,7,6,5]])

print(a)

# Referring to the element at second row, third column
print(a[1,2]) # indicies start from 0
a[1,2] = 100
print(a)


# Referring to the entire second row
print("\nSecond row:", a[1,:])

# Referring to the entire third column
#print("\nThird Column:", ??)


# Referencing multiple columns and multiple rows
b = np.array([[1,2,3,4,5,6,7,8,9,10], 
              [11,12,13,14,15,16,17,18,19,20], 
              [21,22,23,24,25,26,27,28,29,30],
              [31,32,33,34,35,36,37,38,39,40]])

print("\nb = \n", b)


x = b[1:3, 4:7]
print("\nx = b[1:3, 4:7] = \n", x)

# Slices are references, so if we modify values in a slice, 
# it will modify the original array
# 
#b[1:3, 4:7]= 0;
#print("\nb = \n", b)


# Array Logical Indexing
# ======================
v = np.arange(1,11)
print("\nv = ", v)

index1 = np.array([True, True, False, False, False, False, False, False, True, True])
print("\nindex = ", index1)
#print("\nv[index] = ", v[index1])
#v[index1] = -2
#print(v)

# dimensions of the index must match the dimensions of the array
#index2 = np.array([True, True, False, True])
#print("\nindex = ", index2)
#print("\nv[index] = ", v[index2])


index3 = v <=3
print("\nindex = ", index3)
print("\nv[index] = ", v[index3])

m = np.random.random((2,3))
print("\nm = \n", m)

idx = m < 0.5
print("\nidx = \n", idx)

print("\nm[idx] = \n", m[idx])

