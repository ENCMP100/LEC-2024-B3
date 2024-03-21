# Exception Handling: Cleaning up with FINALLY

# This program reads data from an input file and 
# writes the output to an output file.
# It uses variablew isInFileOpened and isOutfileOpened to keep 
# track of whether the opening of the files were successful. 
# It also uses the FINALLY clause of TRY to close the opened files.
# Note: the FINALLY clause of TRY is always executed irrespective
# of whether an exception is raised or not.


try:
    # None of the files are opened yet
    isInFileOpened = False
    isOutfileOpened = False
    
    # Note: The valid file name is data.txt
    # Enter a different name first and to
    # see the exception-handling behavior
    inFileName = input("Input file name:")  
    inFile = open(inFileName, "r")
    
    # If the execution comes to this line, that means the input
    # file was opened successfully without rasing any exception
    isInFileOpened = True
    
    outFileName = input("Output file name:")  
    outFile = open(outFileName, "w")
    
    # If the execution comes to this line, that means the output
    # file was opened successfully without rasing any exception
    isOutfileOpened = True
    
    for line in inFile:
        num = int(line)
        outFile.write("Number: " + str(num) + "\n")
        
except IOError:
    print("Cannot open file", inFileName)
    
except ValueError:
    print("Cannot convert to int:", line)

finally:
    if isInFileOpened:
        print("Closing the input file ...")
        inFile.close()
        
    if isOutfileOpened:
        print("Closing the output file ...")
        outFile.close()
        
