

# FOR loops can be used to repeat a set of statements
# for a known number of times.

# Consider the following use of WHILE loop to print a given
# string one character at a time. 
# We have to use an index "i" to access characters of 
# the string and increment it in each iteration.

string_value = 'Alberta'
i = 0;
while i < len(string_value):
    print(string_value[i])
    i = i + 1
    
"""
# Since we know we need to iterate the loop for each character,
# we cause a FOR loop as follows, which gives a simpler code.
print()
string_value = 'Alberta'
for letter in string_value:
    print(letter)
 
# If we want to use the index in each iteration cycle, we should rather
# iterate through indicies and then access the element at a particular index
# as string_value[index]. See the following example of iterating through indicies
# this way.
print()
string_value = 'Alberta'
for index in range(len(string_value)):
    letter = string_value[index]
    print('Letter', index, 'is', letter)
    
    
# Iterating through a range of values using a FOR loop

for n in range(10):
    print(n)
    
odd_numbers = range(1, 10, 2)
for n in odd_numbers:
    print(n)
"""
