## This file implements BankAccount class.
#  Note: the BankAccount class has a "class variable"
#  Which is used to assign unique account numbers to 
#  BankAccount instances

class BankAccount:
    _lastAssignedNumber = 1000 # A class variable
    OVERDRAFT_FEE = 49.95  # A class constant
    OVERDRAFT_LIMIT = 2500 # A class constant
    
    def __init__(self, accountHolder):
        self._accountHolder = accountHolder
        self._balance = 0
        
        # Set the account number to be the next number that comes
        # after the last account's number
        self._accountNumber = BankAccount._lastAssignedNumber + 1
        
        # Uodate the last account's number to be the account
        # number of this account
        BankAccount._lastAssignedNumber = self._accountNumber
        
    def deposit(self, amount):
        self._balance = self._balance + amount
        
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance = self._balance - amount
        elif self._balance + BankAccount.OVERDRAFT_LIMIT >= amount:
            self._balance = self._balance - amount - BankAccount.OVERDRAFT_FEE                
        else:
            # Here, we raise an error, which must be 
            # handled by the caller
            raise ValueError("Insufficient balance")
            
    def printInfo(self):
        print("Account Info")
        print("    Owner:", self._accountHolder)
        print("    Account Number:", self._accountNumber)
        print("    Balance:", self._balance, "\n")
        
    
    
