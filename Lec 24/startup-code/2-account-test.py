## This script imports a user defined class called BankAccount and 
#  tests its deposit, withdraw, and printInfo funcrions
#


from BankAccountDefinition import BankAccount

beth_account = BankAccount("Beth")
li_account = BankAccount("Li")
rose_account = BankAccount("Rose")

# Print account info. Note the incremental account numbers
beth_account.printInfo()
li_account.printInfo()
rose_account.printInfo()


beth_account.deposit(1000)
beth_account.printInfo() # Balance should be 1000

beth_account.withdraw(500)
beth_account.printInfo() # Balance should be 500

beth_account.withdraw(1500) 
beth_account.printInfo() # Balance should be -1049.50 with Over Draft fee

# The following statement should raise an insufficient-balance exception
#beth_account.withdraw(1500)


## Reference Assignment
#  Class objects are complex objects (i.e. not primitives 
#  like int, float, or string).
#  When you assign such a complex object to another variable, it
#  will only assign a reference instead of creating a complete clone

fred_account = rose_account # the vriables fred_account points at
                            # the same object as rose_account.
                            # Therefore, fred_account is an "alias"
                            # to rose_account
           
print("Rose", end=" ")                            
rose_account.printInfo()
print("Fred", end=" ")                            
fred_account.printInfo()

fred_account.deposit(5000)
print("Rose", end=" ")                            
rose_account.printInfo()
print("Fred", end=" ")                            
fred_account.printInfo()

## IS: True when two variables are aliases to the same object
if fred_account is rose_account:
    print("fred_account is an alias to rose_account")
else:
    print("fred_account is not an alias to rose_account")


## IS NOT: True when two variables are NOT aliases to the same object
if li_account is not rose_account:
    print("li_account is not an alias to rose_account")
else:
    print("li_account is an alias to rose_account")

