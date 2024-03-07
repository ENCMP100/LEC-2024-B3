# Scope of a variable determines where that variable 
# is visible (or can be accessed).

# LOCAL VARIABLES
# ===============

# A variable defined inside a function is called a 
# "local variable". It's scope extends from where it is 
# declared to the end of the function.
# A loop varable in a for loop is also visible to the end of
# the function in which it is defined.
def test1():
    total = 0;
    for i in range(11):
        total = total + i ** 2
    
    print("total:", total)
    print("i:", i)
    
# calling the function
test1()

# total and i are not visible outside of teh function.
# Therefore, the following statements produce syntax errors
print("total:", total)
print("i:", i)

       

