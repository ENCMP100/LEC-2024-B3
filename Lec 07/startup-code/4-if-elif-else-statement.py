##
#  This program prints a description of an earthquake, given the Richter scale 
#  magnitude.
#

# Obtain the user input.
richter = float(input("Enter a magnitude on the Richter scale: "))


# Print the description using if-else
if richter >= 8.0 :
   print("Most structures fall")
else:
    if richter >= 7.0 :
       print("Many buildings destroyed")
    else:
        if richter >= 6.0 :
           print("Many buildings considerably damaged, some collapse")
        else:
            if richter >= 4.5 :
               print("Damage to poorly constructed buildings")
            else : 
               print("No destruction of buildings")


# Print the description using if-else
if richter >= 8.0 :
   print("Most structures fall")
elif richter >= 7.0 :
   print("Many buildings destroyed")
elif richter >= 6.0 :
   print("Many buildings considerably damaged, some collapse")
elif richter >= 4.5 :
   print("Damage to poorly constructed buildings")
else : 
   print("No destruction of buildings")

