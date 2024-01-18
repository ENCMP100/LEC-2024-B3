"""
Created on Sun Jan 15 19:35:17 2023

@author: ranaweer
"""

# Defiing a string
greeting = "Hello Armstrong"

# Length of the string
length_of_sentense = len(greeting)



# String concatenation. 
# Check the results in the Variable explorer after running these statements
string_1 = "Hello" 
string_2 = "World"
result1 = string_1 + string_2
result2 = string_1 + " " + string_2


# str function
# ============
#
# Strings cannot be concatenated with other types like integers and arrays.
# We can convert such types to strings using the str function before 
# concatenating them

name = "Tim"
age = 16
sentense = name + " is " + str(age) + " years old."
print(sentense)
print() # printing a blank line, just because ...


# input
# =====
#
# The input function allows you to take user inputs interactively through
# the console.
#

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

fullName = firstName + " " + lastName 
##fact = fullName + " is Awesome!!!";
##print(fact)

input_value = input("Enter a number: ")
##input_num = int(input_value)
