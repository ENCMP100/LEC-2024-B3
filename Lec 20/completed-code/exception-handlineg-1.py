# Exception Handling

# Exceptions are raised by Python when it encounter
# an error during run-time of the program that it 
# cannot handle. 

# Different types of exceptions are raised based on
# the type of the error. E.g. IOError is raised when
# a the program attemts to open a non-existing file.

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
        print(num)       
        
    inFile.close()
except IOError:
    print("Cannot open file", inFileName)
except ValueError:
    print("You have an invalid value in a line")
    
print("Thank you for running this Python script ...")    
    
    
