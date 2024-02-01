"""
Created on Wed Jan 25 18:52:37 2023

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
    
#print("\nPrinting day using match-case-other")
#print("===================================\n")

