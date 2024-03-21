##
#  This program processes a file containing a count followed by data values.
#  If the file doesn't exist or the format is incorrect, you can specify another file.
#

def main() :
   done = False
   while not done :
      try :
         filename = input("Please enter the file name: ")
         data = readFile(filename)
         
         # As an example for processing the data, we compute the sum.
         total = 0
         for value in data :
            total = total + value
            
         print("The sum is", total)
         done = True
         
      except IOError :
         print("Error: file not found.")
         
      except ValueError : 
         print("Error: file contents invalid.")
         
      except RuntimeError as error :
         print("Error:", str(error))

## Opens a file and reads a data set.
#  @param filename the name of the file holding the data
#  @return a list containing the data in the file
#
def readFile(filename) :
   infile = open(filename, "r")   
   try :
      return readData(infile)
   finally :
      infile.close()

## Reads a data set.
#  @param infile the input file containing the data
#  @return the data set in a list
#
def readData(infile) :
   line = infile.readline()
   numberOfValues = int(line)  # May raise a ValueError exception.
   data = []
   
   for i in range(numberOfValues) :
      line = infile.readline()
      value = float(line)        # May raise a ValueError exception.               
      data.append(value)
      
   # Make sure there are no more values in the file.
   line = infile.readline()
   if line != "" :          
      raise RuntimeError("End of file expected.")
   
   return data
   
# Start the program.
main()

