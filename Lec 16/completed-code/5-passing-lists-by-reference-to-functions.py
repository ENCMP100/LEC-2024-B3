
# Modifying elements in a list inside a function
# ==============================================

# IMPORTANT: When a list is passed into a function, it is
# passed as a reference. This means if you modify the list 
# inside the function, the changes will appear in the origina
# list that is outside of the function. This is not true for
# primitive values like numbers.

def mutiplyElements(values, multiplier):
    for index in range(len(values)):
        values[index] = values[index] * multiplier
        
    # Let's multiply the multiplier to see whether 
    # the change will be effective to outside of the function
    multiplier = multiplier * 100
        
# Testing the multiplyElements function
print() # prints a blank line

numbers = [1, 2, 3, 4, 5]
multiplier = 2

print('List BEFORE the function call:', numbers)
print('Multiplier BEFORE the function call:', multiplier)
mutiplyElements(numbers, 2)
print('\nList AFTER the function call:', numbers)
print('Multiplier AFTER the function call:', multiplier)
