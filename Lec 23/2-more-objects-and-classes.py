## Object and Classes
#
# This script shows an improved counter that was used in
# the first script. It also shows the use of counter 
# to track tallys of two instances.


# Class Definition
# ================
# A simple simulated counter
class Counter:
         
    # Constructor
    # Constructor is autimatcalled when creating an instance of the class
    # @param owner: a string parameter to be used as the 
    # prefix in the print method.
    def __init__(self, owner):
        self._value = 0
        self._owner = owner
    
    # Advances the counter value by 1
    def click(self):
        self._value = self._value + 1

    # Prints the counter value
    def print(self):
        print(f"{self._owner}: {self._value}")
        return self._value


# Using the counter class in the script
# =====================================

ahamad = Counter("Ahamad")
tanya = Counter("Tanya")
   
ahamad.click() #Increment Ahmad's count but not Tanya's
ahamad.print() 
tanya.print()

ahamad.click() #Increment Ahmad's count but not Tanya's
ahamad.print()
tanya.print()

tanya.click() #Increment Tanya's count but not Ahmads's
ahamad.print()
tanya.print()

tanya.click() #Increment Tanya's count but not Ahmads's
ahamad.print()
tanya.print()

tanya.click() #Increment Tanya's count but not Ahmads's
ahamad.print()
tanya.print()

tanya.click() #Increment Tanya's count but not Ahmads's
ahamad.print()
tanya.print()
    



