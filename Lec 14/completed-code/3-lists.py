# Accessing lists

names = ['Ng','John', 'Hynto', 'Mary', 'Ravi', 'Mary', 'Eric ']

print('First value:', names[0])
print ('Second value:', names[1])
print('Last value:', names[-1])
print('Second last value:', names[-2])

print()
# You can use the "in" operator to check whether an element exist in a list.
check1 = 'Hynto' in names
print('Check for Hynto:', check1)

check2 = 'Liem' in names
print('Check for Liem:', check2)

print('\nIterating through VALUES:')
# Iterating throug values using the "in" operator
for x in names:
    print(x)
    
print('\nIterating through INDICIES:')
# Iterating throug indicies using the "in" operator
for index in range(len(names)):
    print(names[index])
    
    
for index in range(len(names)):
    print(f'name {index + 1} = {names[index]}')

    
    
    
    
    
    