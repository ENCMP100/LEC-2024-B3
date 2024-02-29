## 
#  This program demonstrates a reusable function.
#  

def main() :
   print("Please enter a time: hours, then minutes.")
   hours = readIntBetween(0, 23)
   minutes = readIntBetween(0, 59)
   print("You entered %d hours and %d minutes." % (hours, minutes))


## Prompts a user to enter a value within a given range until the user provides 
#  a valid input.
#  @param low an integer indicating the smallest allowable input
#  @param high an integer indicating the largest allowable input
#  @return the integer value provided by the user (between low and high, 
#  inclusive)   
#
def readIntBetween(low, high) :
   value = int(input("Enter a value between " + str(low) + " and " + 
                     str(high) + ": "))
   while value < low or value > high :
      print("Error: value out of range.")
      value = int(input("Enter a value between " + str(low) + " and " + 
                        str(high) + ": "))
 
   return value    

# Start the program.
main()   

