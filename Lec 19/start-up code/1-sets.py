## Introdction to Sets
#
# Unlike lists, Sets contains a unique seto fo values.
#

# Creating a set
fruits = {"Banana", "Apple", "Mango", "Cherry"}
print(fruits) #Note the order can be different than what you specified

# Creating an empty set
emptySet = set()
print(emptySet) # IMPORTANT: you cannot use {} to create an empty set because 
              # {} creates an empty DICTIONARY, which we will learn next. 

# ADD: adds another value to a se
fruits.add("Pineapple")
print(fruits)

# Adding the same value to a set does not create duplicate values
fruits.add("Pineapple")
fruits.add("Pineapple")
fruits.add("Pineapple")
fruits.add("Pineapple")
print(fruits)


# SORTED: returns a LIST that contains values in the SET sorted in 
#         ascending order
sortedFruits = sorted(fruits)
print(sortedFruits)

# DISCARD: Removes a value from the set
fruits.discard("Mango")
print(fruits)

# LEN: returns how many values are in the set
print("Number of values in set:", len(fruits))

# CLEAR: empties a set
fruits.clear()
print(fruits)

# Converting a list to a set
flowerList = ["Rose", "Lily", "Tulip", "Orchid", "Tulip", "Tulip"]
flowerSet = set(flowerList)


#IN: Checks whether a value is in a set
check1 = 'Tulip' in flowerSet
print(check1)

check2 = 'Carnation' in flowerSet
print(check2)

# Iterating through values in a set
for flower in flowerSet:
    print(flower)


## SET OPERATOPNS
## ==============

# Flag colours
canadian = { "Red", "White" } 
british = { "Red", "Blue", "White" } 
italian = { "Red", "White", "Green" }


check1 = canadian.issubset(british) # True, because canadian colors are 
print(check1)                       # a subset of bristish colors

check2 = italian.issubset(british) # False
print(check2)

# UNION
result1 = british.union(italian)
print(result1)

# INTERSECTION
result2 = british.intersection(italian)
print(result2)

# DIFFERENCE
diff1 = british.difference(italian) # elements in british but not in italian
print(diff1)

diff2 = italian.difference(british) # elements in italian but not in british
print(diff2)


## SET Example
## ===========

# Finding Unique Words
file = open('peter-piper.txt', 'r')
uniqueWords = set()
for line in file:
    line = line.rstrip('\n.?,').lower()
    words = line.split()
    for word in words:
        uniqueWords.add(word)
        
file.close()
print(uniqueWords)