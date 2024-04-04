##
#  This module defines the Menu class.
#

## A menu that is displayed in the terminal window.
#
class Menu :
   ## Constructs a menu with an optional list of options.
   #
   def __init__(self, options) :
      self._options = options
   
   ## Adds an option to the end of this menu.
   #  @param option the option to add
   #
   def addOption(self, option) :
      self._options.append(option)
      
   ## Gets the option text of an option at a given position
   #
   def getOptionLabel(self, userChoice):
       if userChoice >= 0 and userChoice < len(self._options) :
          return self._options[userChoice]
       else:
           return None
   
   ## Displays the menu, with options numbered starting with 1, and prompts
   #  the user for input. Repeats until a valid input is supplied.
   #  @return the number that the user supplied
   #
   def getInput(self, prompt = "Your choice: ") :
      done = False
      while not done :
         for i in range(len(self._options)) :
            print("    %d %s" % (i, self._options[i]))
    
         userChoice = int(input(prompt))
         if userChoice >= 0 and userChoice < len(self._options) :
            done = True
         else:
             print("Inalid choice:", userChoice, "\n")
           
      return userChoice

