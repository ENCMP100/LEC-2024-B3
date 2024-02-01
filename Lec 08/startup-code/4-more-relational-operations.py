"""
Created on Sun Jan 29 14:50:30 2023

@author: ranaweer
"""

# Chaining Relational Operators
# =============================
waterTemp = 20 # Celsius

# Classic combining
isInLiquidForm = 0 <= waterTemp and waterTemp <= 100

# Chaining. 
# Python automatically combines the two relational 
# operations using logical "and" operator
isInLiquidForm2 = 0 <= waterTemp <= 100


# Short-circuit Evaluation
# ========================

totalPrice = float(input("Enter price ($): "))
quantity = int(input("Quantity (kg): "))

# Since the following expression combines the results
# of the left and righht relarions using "and", it
# will not even evaluare the right expression when
# the left expression is False. This is called
# short-circuit (terminology comes from parallel
# electrical circuits).
if quantity > 0 and totalPrice/quantity < 10:
    print("That's a low price")
    

# Likewise, since the following expression uses "or" to
# combine the results, and since "or" produces True when
# either side is True, the following expression will not 
# even evaluate the right-hand expression when the left-hand
# expression is True.
age = int(input("Age (years): "))

if age < 18 or input("Country of residence in upper case: ") != 'CANADA':
    print("No need to file Canadian taxes.")
else:
    print("You should file Canadian taxes.")
    
    

# De Morgan's Law
# ===============

A = input("A: ") == 'True'
B = input("B: ") == 'True'

# Form 1: not (A and B) is the same as not A or not B
print("not (A and B):", not (A and B))
print("not A or not B:", not A or not B)
print()

# Form 2: not (A or B) is the same as not A and not B
print("not (A or B):", not (A or B))
print("not A and not B:", not A and not B)
print()





