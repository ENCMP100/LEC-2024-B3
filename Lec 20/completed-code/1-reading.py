
# Note: The valid file name is data.txt
# Enter data.txt and mydata.txt as input in 
# two iterations of this script and observe
# the output.

inFileName = input("Input file name:")  

inFile = open(inFileName, "r")

for line in inFile:
    print(line, end="")       
    
inFile.close()
    
print("Thank you for running this Python script ...")    
    
    
