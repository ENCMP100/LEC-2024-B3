
# Lists
#======
my_list = [10, 'Hello World!', 200, 12.5]
list_of_list_as_2d_list = [[1,2,3], [4,5,6]]

# Tuples
# ======
my_tuple = (10, "Hello", 12.5) # Once created, you cannot modify tuple elements


# Numpy Arrays and array indexing (slicing)
# =========================================
import numpy as np

a1 = np.array([1, 2, 3, 4, 5]) # converts the input argument list to an array
a2 = np.array([[1,2,3], [4,5,6]]) # 2D array

v1 = np.zeros(10)
m1 = np.zeros((4,3))

v1 = np.full(10, 3)
m1 = np.full((8,8), 3)

v1[2:4] = 100
m1[2:4, 3:5] = 20
m1[5,:] = 30


# Sets
# ====
empty_set = set()
set_1 = {1, 2, 'apple', 'banana'}

set_1.add(10)
set_1.add('kiwi')
set_1.add('kiwi') # No duplicates are created
set_1.add('kiwi') # No duplicates are created

set_1.discard('kiwi')

check1 = 'apple' in set_1
check2 = 'orange' in set_1

# Set Operations
canadian = { "Red", "White" } 
british = { "Red", "Blue", "White" } 
italian = { "Red", "White", "Green" }

check1 = canadian.issubset(british) # True, because canadian colors are a subset of bristish colors
check2 = italian.issubset(british) # False

result1 = british.union(italian)
result2 = british.intersection(italian)
diff1 = british.difference(italian) # elements in british but not in italian
diff2 = italian.difference(british) # elements in italian but not in british



# Dictionary
# ==========
empty_dectionary = dict()
empty_dectionary2 = {}

contacts = { "Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278 }
citizenships = { "Fred": "Canadian", "Mary": "American" }

check1 = 'Fred' in contacts
check2 = 'Mala' in contacts

# GET: returns the value of associated a given key. 
#      Safer to use because it returns None for keys that does not exist. 
print(contacts.get('Mary'))
print(contacts.get('Mala'))

# Adding and Modifying dictionary entries
contacts['Mala'] = 123456
contacts['Mary'] = "1-888-444-2222"


## POP: removes an entry from the dictionary
contacts.pop('Bob') # removes the entry with the key 'Bob'. POP also returns 
                    # the value associated with the removed entry

# Trying to pop a non-existing entry produces an error.
# contacts.pop('Rick')

# KEYS: returns all keys in a dictionary
k = contacts.keys()
print(k)

# VALUES: returns all values in a dictionary
v = contacts.values()
print(v)

# ITEMS: return all items in the dictionary
items = contacts.items()
print(items)

# SORTED: returns a sorted list of keys in the dictionary
sortedKeys = sorted(contacts)
print(sortedKeys)

# CLEAR: clears all items in the dictionary
contacts.clear()
