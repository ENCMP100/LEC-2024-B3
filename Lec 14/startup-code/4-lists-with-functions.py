# Lists in functions

# A funcrion that returns a value
# ===============================
# LISTSUM returns the sum of values
def listsum(values):
    total = 0
    for val in values:
        total = total + val
    
    return total


# Testing the listsum function
print('Sum of [100, 50, 200, 25]:', listsum([100, 50, 200, 25]))


# A function that returns list
# ============================
# SQUARES retunrs the whole squares from 1 to n, the input value
def squares(n):
    result = []
    for k in range(1, n):
        result.append(k ** 2)
        
    return result

# Testing the squares function
print('\nSquares from 1 to 5:', squares(6))


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
