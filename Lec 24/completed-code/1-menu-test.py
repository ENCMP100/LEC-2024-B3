##
#   This program tests the Menu class.
#

from menu import Menu

vegieMenu = Menu(["Leeks", "Yams", "Potatoes"])
vegieMenu.addOption("Beans") #Adds another item to the menu
choice = vegieMenu.getInput()
print("You selected:", vegieMenu.getOptionLabel(choice))


fruitsMenu = Menu(["Apple", "Banana", "Orange", "Pineapple"])
choice = fruitsMenu.getInput("Your favorite fruit:") # Custom prompt 
print("You selected:", fruitsMenu.getOptionLabel(choice))



