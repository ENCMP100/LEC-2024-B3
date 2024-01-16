
"""
Created on Wed Jan 11 16:17:37 2023

@author: ranaweer
"""

# List
# ====
#
# Basic Python "List" can hold multiple values of any type of data. e.g.
# To define a List with a set of initial values, we can enclose the values 
# within square brackets:
my_list = [10, 'Hello World!', 200, 12.5]

# Create a list that contains integers from 0 to 5
my_list2 = [0, 1, 2, 3, 4, 5]

# Create a list that contains integers from -2 to 2
my_list3 = [-2. -1, 0, 1, 2]

# Modify the first element in the my_list3 to 100
my_list3[0] = 100

# Create an example list of a lists as a two-dimensional
my_list4 = [[1,2,3], [4, 5, 6]]


# Tuple
# =====
#
# Tuples also hold multiple values like a list, but once a tuple is created, 
# they cannot be modified. To create a tuple, specify its values using parantheses
my_tuple = (10, 'Hello World!', 200, 12.5)
my_tuple2 = (4,2)
my_tuple3 = (4,)  # Remember the comma. Otherwise, this will be an integer.

# Try to change the first value in my_tuple to 100. 
# This would generate a syntax error since Tuples are read-only.
