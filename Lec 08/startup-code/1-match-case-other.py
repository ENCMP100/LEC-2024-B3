"""
Jan 27, 2024

@author: ranaweer
"""

dayNum = int(input("Input the day of week (1 tot 7): "))

print("\nPrinting day using if-elif-else")
print("===============================\n")

if dayNum == 1:
    print("Monday")
elif dayNum == 2:
    print("Tuesday")
elif dayNum == 3:
    print("Wednesday")
elif dayNum == 4:
    print("Thursday")
elif dayNum == 5:
    print("Friday")
else:
  print("Weekend")
    

# With Python version 3.10, we have anotehr selection
# statement called match-case. 
# This code will NOT work with Python versions 3.9.x and below.
print("\nPrinting day using match-case-other")
print("===================================\n")


match dayNum:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case other:
        print("Weekend")
