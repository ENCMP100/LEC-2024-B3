## LIST OPERATIONS

## APPEND: appends elements to the end of a list
friends = [] # An empty list
print(friends)

friends.append('Harry')
print(friends)

friends.append('Emily')
print(friends)

friends.append('Bob')
print(friends)

friends.append('Cari')
print(friends)

## INSERT: inserts an element to a specific position or index
# Note: the index is ZERO-based. Negative index specifies the
# position from the end of the list.
friends.insert(2, 'Mala') # insert as at position 3
print(friends)

friends.insert(0, 'Eric') # insert as at the begining
print(friends)

friends.insert(-1, 'Aiyana') # insert at the last position
print(friends)               # the current last one is shifted


## IN: check whether an element exists in a list
if 'Mala' in friends:
    print("Mala is a friend")
else:
    print("Mala is not friend")
    
if 'Max' in friends:
    print("Max is a friend")
else:
    print("Max is not a friend")
    
## REMOVE: remove an element
friends.remove('Bob')
print(friends)

# Note: attempting to remove a non-existing element will raise
# an exception. To avoid such run-time errors, you should check
# whether an element exists before attempting to remove it.
# E.g.
if 'Beth' in friends:
    friends.remove('Beth')
    
##POP: removes an element from a list 
#      and returns the removed element

x = friends.pop() # removes the element at the end
print(x)
print(friends)

y = friends.pop(2)  # removes the element at index 2 (i.e. 3rd element)
print(y)
print(friends)

##INDEX: returns the index of a given element within the list
t = friends.index('Mala')
print(t)

twister = ['Betty', 'Botter', 'bought', 'a', 'bit', 'of', 'butter',
           'but', 'the', 'bit', 'of', 'butter', 'was', 'bitter', 
           'so', 'Betty', 'Botter', 'bought', 'a', 'bit', 'of', 'better', 
           'butter', 'to', 'make', 'the', 'bit', 'of', 'bitter', 'butter',
           'better']

print(twister.index('butter')) # index of first occurance from the beginning

print(twister.index('butter', 10)) # index of occurance starting from
                                       # index 10 (inclusive)
                
               
                
               
                
               
