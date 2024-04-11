
class Clicker:
    _lastUsedId = 0
    
    def __init__(self, name):
        self._id = Clicker._lastUsedId + 1
        Clicker._lastUsedId = self._id
        
        self._clicks = 0
        self._name = name
        
    def click(self):
        self._clicks = self._clicks + 1
        print("Clicked ", self._name)
        
        
    def print(self):
        print("Clicker", self._name)
        print("    id:", self._id)
        print("    clicks:", self._clicks)
        print()
        

# Using the class
c1 = Clicker("C1")
c2 = Clicker("C2")

c1.print()
c2.print()

c1.click()
c1.click()
c1.print()
c2.print()

c2.click()
c1.print()
c2.print()
