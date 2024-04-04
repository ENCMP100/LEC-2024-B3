## This script imports a user defined class called BankAccount and 
#  tests its deposit, withdraw, and printInfo funcrions
#


from BankAccountDefinition import BankAccount

bill_account = BankAccount("Bill")
li_account = BankAccount("Li")
rose_account = BankAccount("Rose")

# Print account info. Note the incremental account numbers
bill_account.printInfo()
li_account.printInfo()
rose_account.printInfo()


bill_account.deposit(1000)
bill_account.printInfo() # Balance should be 1000

bill_account.withdraw(500)
bill_account.printInfo() # Balance should be 500

bill_account.withdraw(1500) 
bill_account.printInfo() # Balance should be -1049.50 with Over Draft fee

# The following statement should raise an insufficient-balance exception
#bill_account.withdraw(1500)


## Reference Assignment
#  Class objects are complex objects (i.e. not primitives 
#  like int, float, or string).
#  When you assign such a complex object to another variable, it
#  will only assign a reference instead of creating a complete clone

william_account = bill_account # the vriables william_account points at
                               # the same object as bill_account.
                               # Therefore, william_account is an "alias"
                               # to bill_account
           
print("Bill", end=" ")                            
bill_account.printInfo()
print("William", end=" ")                            
william_account.printInfo()

william_account.deposit(5000)
print("Bill", end=" ")                            
bill_account.printInfo()
print("William", end=" ")                            
william_account.printInfo()

## IS: True when two variables are aliases to the same object
if william_account is bill_account:
    print("william_account is an alias to bill_account")
else:
    print("william_account is not an alias to bill_account")


## IS NOT: True when two variables are NOT aliases to the same object
if li_account is not rose_account:
    print("li_account is not an alias to rose_account")
else:
    print("li_account is an alias to rose_account")

