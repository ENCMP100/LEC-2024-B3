## Array Math

import numpy as np

# Array math
heights = np.array([1.5, 1.78, 1.6]) 
weights = np.array([65, 46, 59]) 
bmi = weights / heights**2

# Dot product
x = np.array([2,3]) 
y = np.array([4,2]) 
z = np.dot(x,y)  # 2x4 + 3x2 = 14
print("x dot y =", z)

# Cumulative Sum for a vector (1-D array)
v = np.array([1,2,3,4,5,6,7,8,9]) 
print(v)
c1 = v.cumsum() # Cumulative sum of all elements in the vector
print(c1)

# Cumulative Sum for a matrix (2-D array)
a = np.array([(1,2,3),(4,5,6), (7,8,9)]) 
print(a)
c2 = a.cumsum() # A vector that contains the cumulative sum of all elements in the array
print(c2)


## DOT: dot product 

# with Rank 1  (1-D) arrays
x = np.array([2,3])
y = np.array([4,2])
print(np.dot(x,y)) # 2x4 + 3x2 = 14


# with Rank 2 (2D) arrays
x2 = np.array([[1,2,3],[4,5,6]]) 
y2 = np.array([[7,8],[9,10], [11,12]])

print("x2=\n", x2)
print("y2=\n", y2)
print("x2.y2=\n", np.dot(x2,y2))


