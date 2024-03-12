# Scope of a variable determines where that variable 
# is visible (or can be accessed).


# GLOBAL VARIABLES
# ================

# Varialbles declared outside of functions are have "global scope".
# They are visible inside the funtions. However, if a function
# needs to modify a global variable and make that modification
# visible to outside of the function, the function should re-declare
# that variable with "global" keyword.

balance = 1000 # a global variable
print()
def withdraw(amount):
   
    global balance # This function intends to update the balance
                   # that is defined outside of the function, so
                   # we should declare it here as a "global" variable
    
    if balance >= amount:
        balance = balance - amount
        

print("Initial balance:", balance)
withdraw(100)
print("new balance after withdrawing 100:", balance)
    
    
                 

