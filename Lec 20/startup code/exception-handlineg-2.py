# Exception Handling with Multiple Exception Types


# Different types of exceptions are raised based on
# the type of the error. E.g. IOError is raised when
# a the program attemts to open a non-existing file.
# A ValueError is raised when the program tries to
# convert a string representation of a non-integer 
# into an integer using the int() function.

# Python provides TRY/EXCEPT/FINALLY statements to
# handle exceptions.


try:
    # Note: The valid file name is data.txt
    # Enter a different name first and to
    # see the exception-handling behavior
    inFileName = input("Input file name:")  
    
    inFile = open(inFileName, "r")
    
    for line in inFile:
        num = int(line)
        print("Number:", num)
        
    inFile.close()
except IOError:
    print("Cannot open file", inFileName)
  
except ValueError:
    print("Cannot convert to int:", line)
    inFile.close()
 
except Exception: #Handles any other exeption
    print("An uknown error happed")
    inFile.close()

print("Program completed ...")

