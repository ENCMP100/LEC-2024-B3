## A dictionary is a collection of KEY/VALUE pairs. A Key is unique within the
#  dictionary, so there can be one entry with a given key, but a value can be
#  associated with many entries.


# Creating a dictionary that is initialized with a set of key/value pairs
contacts = { "Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278 }
citizenships = { "Fred": "Canadian", "Mary": "American" }

# Creating an empty disctionary
emptyD1 = dict()
print(emptyD1)

emptyD2 = {}
print(emptyD2)


# Accessing dictionary values
print(contacts["Fred"])

print(contacts["Mala"]) # produce an error since the key "Mala" does not exist

# IN: checks if a key exists in a dictionary
if 'Fred' in contacts:
    print('Fred\'s contact number:', contacts['Fred'])
else:
    print('Fred does not exist within contacts')

if 'Mala' in contacts:
    print('Mala\'s contact number:', contacts['Mala'])
else:
    print('Mala does not exist within contacts')


# GET: returns the value of associated a given key. 
#      Safer to use because it returns None for keys that does not exist. 
print(contacts.get('Mary'))
print(contacts.get('Mala'))


# Adding and Modifying dictionary entries
contacts['Mala'] = 123456
print(contacts)

contacts['Mary'] = "1-888-444-2222"
print(contacts)

## POP: removes an entry from the dictionary
contacts.pop('Bob') # removes the entry with the key 'Bob'. POP also returns 
                    # the value associated with the removed entry
                    
# Trying to pop a non-existing entry produces an error.
# contacts.pop('Rick')


# You can associate the same VALUE with multiple keys
contacts["Lisa"] = "1-888-444-2222"
print(contacts)

# KEYS: returns all keys in a dictionary
k = contacts.keys()
print(k)
for key in contacts.keys():
    print(key)

# VALUES: returns all values in a dictionary
v = contacts.values()
print(v)
for val in contacts.values():
    print(val)
    
# ITEMS: return all items in the dictionary
items = contacts.items()
print(items)
for item in contacts.items():
    print(item) # Item is a tuple
    
# SORTED: returns a sorted list of keys in the dictionary
sortedKeys = sorted(contacts)
print(sortedKeys)

# CLEAR: clears all items in the dictionary
contacts.clear()
print(contacts)
                  
