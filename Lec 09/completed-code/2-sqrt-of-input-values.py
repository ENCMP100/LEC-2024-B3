
import numpy as np


# While loop continues as long as its test "condition" is True
"""
# Example 1
# The following loop continues until you enter a negative number
num = float(input('Enter a number: '))

while num >= 0:
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    
    # Take the next number
    num = float(input('Enter a number: '))
"""

"""
# Example 2
# The following loop continues until you enter an empty string
num_string = input('Enter a number: ')
while len(num_string):
    num = float(num_string)
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    
    # Take the next number
    num_string = input('Enter a number: ')
"""
  
while True:
    num_string = input('Enter a number: ')
    
    if num_string == "":
        break
    
    num = float(num_string)
    print("Square root of", num, "is", np.sqrt(num))
    
    
print("Program ended!")


"""
# Example 3
# In this example, we set the condition of the while loop 
# to be True, so it will run as an infinite loop.
# However, when the user enters an empty input, we
# terminate the while loop by executing a 
# "break" statement.
while True:
    num_string = input('Enter a number: ')
    
    if num_string == "":
        break  # Break the loop, which skips the remaining 
               # steps in the loop and terminates the loop.
        
    num = float(num_string)
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    

print("Program ended!")
"""