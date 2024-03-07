## LIST OPERATIONS


## +: Concatenates of two lists
myFriends = ['Fritz', 'Cindy']
yourFriends = ['Lee', 'Pat', 'Sally']

ourFriends = myFriends + yourFriends
print(ourFriends)

## *: Replicates a list. 
#     Can be used to pre-allocate lists to store future results
monthlyRainFall = [0] * 12
print(monthlyRainFall)


## SORT: sorts a list in alphabetical order. The result is stored  
#        in the same list (i.e. the list gets modified)
#        Note: lower-case letters have a "higher value" 
#        than upper case letters
names = ['Fred', 'Ann', 'Sue', 'betsy', 'Zhang']
print(names)

names.sort()
print(names)


## SUM, MAX, MIN on nunerical lists
scores = [100, 50, 50, 150, 200]
print('SUM:', sum(scores))
print('MAX:', max(scores))
print('MIN:', min(scores))

print(scores)
scores.sort()
print(scores)

# MAX and MIN can be applied to non-numeric lists as well
names = ['Fred', 'Ann', 'Sue', 'betsy', 'Zhan']
print('names:', names)
print('max(names):', max(names))
print('min(names):', min(names))


## LIST: createsa deep copy of a list including its data
#        Note: if you simply use assignment operator to assign
#        a list to another variable, it will only copy a reference
#        but not a full clone of the data.

numbers = [2, 4, 6, 8]
numbers_2 = numbers  # numbers_2 is only a reference to numbers
numbers_3 = list(numbers) # numbers_3 is a complete copy of numbers.

numbers[0] = 0 # Change a value of an element in numbers

print('numbers:', numbers)  # new value of numbers after the change
print('numbers_2:', numbers_2) # numbers_2 has also been changed
print('numbers_3:', numbers_3) # numbers_3 has NOT been changed


## : operator is used to "slice" (or take a portion) of a list
 
temperatures = [18, 21, 24, 28, 33, 39, 40, 39, 36, 30, 22, 18]
print('temperatures:', temperatures)
quarter3 = temperatures[6:9] # elements at indicies 6 through 8, inclusive
print('quarter3:', quarter3) # here, 
                             #  1st number is the "inclusive "start index
                             #  2nd number is the "exclusive" end index
                                 
# If the first index is 0, it can be omited.
quarter1 = temperatures[:3] # values at indicies 0 to 2
print('quarter1:', quarter1)

quarter4 = temperatures[9:] # values at indicies from 9 to end
print('quarter4:', quarter4)
                                 
# changing values in a slize will change the original list
temperatures[3:6] = [1, 2, 3]
print('temperatures:', temperatures)

temperatures[6:9] = [0] * 3 # replicate [0] 3 times, resulting in [0, 0, 0]
print('temperatures:', temperatures)






