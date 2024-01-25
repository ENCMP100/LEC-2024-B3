"""
Created on Wed Jan 22 20:32:47 2024

@author: ranaweer
"""


# Relational operators tests a condition (compare two operands) 
# and produces True or False depending on whether the 
# tested condition is satisfied or not.
# True and False are called Boolean values.


# Using Relational Operartors with Numeric Values
# ===============================================

# Relational operator examples
# Hortsmann chapter 3.2 Table 2
# Relational
3 <= 4  # True  (less than or equal)
3 < 4
3 > 4   # False (greater than)
4 == 4  # True (equal)
4 <= 4 
4 >= 4
5 >= 4


5 != 4 # True (not equal)

# Never test floating-point results for equality because
# floating point operations can have round-off errors due to
# limited precision in floating-point number representation
# and algorithms.
#e.g.
import numpy as np
root_two = np.sqrt(2)

# Mathematically, the following test is True but when 
# computed in computer, the result is false.
equality_test = root_two * root_two == 2


# To compare equality between two floating point values, we 
# should check whether the absolute difference is smaller
# than a maximum allowable error for the application.
# e.g.
epsilon = 10 ** -6 # maximum allowable error
approximately_equal_test = np.abs(root_two * root_two - 2) <= epsilon



# Using Relational Operators with Strings 
# =======================================

# Every upper-case character is "smaller" in value than 
# any other lowercase characters

"A" < "a" # True

"Z" < "a" # ??

# Characters comes earlier in the alphabet are smaller than
# the ones come after

"e" < "f" # True

"e" < "F" # Explain the result of this relational operation

# Relational operators compare strings character by character
# from the start of the string until it finds a difference
# between characters in corresponding positions.

"Hellobadfuyawgvfkutwevfkutqcf" > "Help"  # ??

"hello" > "Help"  # ??


# Using Relational Operators with Arrays
# ======================================

import numpy.random as rand # import random number module from numpy 

# Create a random vector of length 10 and test
# which elements of it is smaller than 0.5
rand_vec = rand.random(10)
result_1 = rand_vec < 0.5
print(rand_vec)
print(result_1)


# Create a random array of 4x3 and test
# which elements of it is smaller than 0.5
rand_array = rand.random((4,3))
result_2 = rand_array < 0.5
print(rand_array)
print(result_2)











