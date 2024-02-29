## 
#  This program creates passwords of a given length.
#  

import numpy as np


def main() :
    pw_length = int(input("Password length: "))
    password = createPassword(pw_length)
    print("Password:", password)
   
## Returns a random password of the given length.
#  A generated password should contain at least one digit and one
#  special symbol.
#  @param pwLength an integer specifying the password length
#  @return the created password   
#
def createPassword(pwLength) :
    #ALGORITHM
    # 1. Starts with an empty string representing the password.
    # 2. Append pwLength-2 number of randomly selected letters to 
    #    the password.
    # 3. Select a random digit and insert it to a random position
    #    of the password.
    # 4. Select a random special character and insert it to a 
    #    random position of the password
    
    # DEFINE CHARACTER SOURCES
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '+-*/?!@#$%&'
    
    password = ""
    
    for i in range(pwLength-2):
        c = getRandomCharacter(letters)
        password = password + c
    
    digit = getRandomCharacter(digits)
    password = insertAtRandomPosition(password, digit)
    
    special_char = getRandomCharacter(special_chars)
    password = insertAtRandomPosition(password, special_char)
    
    return password    

def getRandomCharacter(values):
    
    index = np.random.randint(len(values))
    
    return values[index]
  
def insertAtRandomPosition(target, insertChar):
    
    position = np.random.randint(len(target))
    
    result = ""
    for i in range(position):
        result = result + target[i]
        
    result = result + insertChar
        
    for i in range(position, len(target)):
        result = result + target[i]
        
    return result
    
    
# Start the program.
main()   

