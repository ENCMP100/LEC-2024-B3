

# This program prompts the user to enter 
# one or more numbers until the user enters
# a blank line. The program then prints the
# largest and the smallest of the numbers that
# were entered.

# Take the first number and set it as the largest and
# smallest innitially.
largest = float(input("Enter a value: "))
smallest = largest

# Take the second input as a string
inputStr = input("Enter a value: ")

# Continue while the input string is not empty
while inputStr != "" : 
    value = float(inputStr) 
    
    # If the new value is larger than the current largest value,'
    # then keep it as the current largest value
    if value > largest : 
        largest = value
        
    # If the new value is smaller than the current smallesr value,'
    # then keep it as the current smallesr value
    if value < smallest : 
        smallest = value
    
    # Prompt the user to enter another value (or blank to terminte the loop)
    inputStr = input("Enter a value: ")
    
print("Smallest =", smallest, "Lagest =", largest)