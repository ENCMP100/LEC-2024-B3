## Object and Classes
#
# In Object Oriented Programming (OOB), 
# each object has its own data and a set of
# methods that acts on that data.
#
# A CLASS defines the data (properties) of an
# object and its methods.
#


# Class Definition
# ================
# A simple simulated counter
class Counter:  
         
    # Resets the counter value
    def __init__(self):
        self._value = 0
    
    # Advances the counter value by 1
    def click(self):
        self._value = self._value + 1

    # Gets the counter value
    # @return the current counter value
    def getValue(self):
        return self._value


# Using the counter class in the script
# =====================================
tally = Counter()

tally.click()
print('Num Clicks', tally.getValue()) 

tally.click()
print('Num Clicks', tally.getValue())

tally.click()
print('Num Clicks', tally.getValue())     

tally.click()
print('Num Clicks', tally.getValue())     



