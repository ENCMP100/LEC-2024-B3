## String Basics
#  =============

myString1 = "He said hello"
myString2 = 'He said hello'
myString3 = "He said 'hello'" # Here, single quotes inside the string are 
                              # treated as just characters
myString4 = 'He said "Hello"' # Here, the double quotes in the string are
                              # treated as just characters

myString5 = "He said \"hello\" to Kelly's Father"
myString5 = 'He said "hello" to Kelly\'s Father'
print(myString5)


# LEN functions returns the length of a string
length1 = len(myString1)
print("Length of myString1:", length1)

# Empty strings are strings with no characters in them. Their length is 0
myEmptyString1 = ""
myEmptyString2 = ''


## Concatenating Strings
#  =====================
firstName = "Henry"
lastName = "Ford"

fullName = firstName + lastName  # Concatenated the two strings
print(fullName) # Does not automatically insert a white space.

fullName = firstName + " " + lastName
print(fullName) # Better! We delibrately concatenated a white space too.

# IN and NOT IN: test whether or not a substring exist within a string
name = "John Wayne"
print("Way" in name) # True, since "Way" is in Wayne

if "-" not in name:
    print("The name has no hyphen")
else:
    print("The name has a hyphen")
    
## Converting Between Numbers and Strings
#  ======================================
planeModel = "Boeing " + 747 # Produces error because strings cannot be 
                             # concatenated with numbers
planeModel = "Boeing " + str(747) # Works! because the function STR converts
                                  # the number 747 into the string '747'
                                  
myNum1 = int('1299') # INT function converts the string '1299' to number 1299
myPrice = float("12.99") # converts the string to a floating point number 12.99

# INT and FLOAT functions raise errors if the input is not a string 
# representation of a valid numeric value. E.g. the followings raise errors
x1 = int('2*2')
x2 = float("2.3.4")
x3 = int('2.5')


## String Methods
#  ==============
#
# Python strings are software "objects" and they have "Methods", which are 
# similar to functions but they operate on the actual string, instead of 
# working standalone. Methods are invoked using the dot (.) operator.

name = "Pablo Picasso"

# LOWER and UPPER methods
print(name.lower())
print(name.upper())

# COUNT: counds all occurrences of given substring 
sentense = "nuts are nutritious but eating nuts every day sounds nuts"
N = sentense.count("nut")
print("N:", N)

val = input('Enter a number: ')
if val.count('.') > 1:
    print('Inavlid input')
else:
    floatVal = float(val)

# FIND: returns the index of the first occurrence of a substring from a given index
print(sentense.find("nut")) # first occurrence from the begining
print(sentense.find("nut", 1)) # first occurrence from the position 1
print(sentense.find("banana")) # -1, since there is no banana 

sentense = "nuts are nutritious but eating nuts every day sounds nuts"

index = 0
while index >= 0:
    index = sentense.find("nut", index)
    if index >= 0:
        print('Found a nut at index:', index)
        index = index + 1


# ISALPHA: returns True if the string contains only letters
test1 = "Boeing".isalpha()
print(test1) 
print("Boeing".isalpha()) # This is equivallent to the above two statements
                          # because we call the method and then print the result
                         
print("Boeing 747".isalpha())
print("747".isalpha())
print("".isalpha()) # False, since there are no letters in the empty string

# ISDIGIT: returns True if the string contains only digits
print("747".isdigit())
print("Boeing 747".isdigit())

print("12.99".isdigit()) # False because the period is not a digit
print("-5".isdigit()) # False because the negative sign is not a digit
print("".isdigit()) # False, since there are no digits in the empty string
                
# ENDSWITH and STARTSWITH
url = "https://www.ualberta.ca"
isCanadianDomain = url.endswith(".ca")
isSecure = url.startswith("https://")
          
# ISLOWER: returns True if all "letters" are lower-case letters
print("Jason".islower())
print("jason".islower())
print("boeing 747".islower()) # True because all "letters" are lower. 
                              # ISLOWER ignores all non-alphabetical characters
                              
print("Boeing 747".islower())  # False since there is one upper-case letter


# ISUPPER: returns True if all "letters" are upper-case letters
print("Jason".isupper())
print("JASON".isupper())
print("Price: $12.98".isupper())  # False since there are lower-case letters
print("PRICE: $12.98".isupper())  # True since all "letters" are upper case

# E.g. 1 - counting upper-case letters in a stirng
sentense = "The Quick Brown Fox Jumps Over the Lazy Dog"
numUpperCaseLetters = 0
for char in sentense:
    if char.isupper():
        numUpperCaseLetters = numUpperCaseLetters + 1

print("Number of upper case letters:", numUpperCaseLetters)

# E.g. 2 - counting vowels
vowelCount = 0
for char in sentense:
    if char.lower() in "aeiou":
        vowelCount = vowelCount + 1

print("Number of vowels:", vowelCount)

# E.g. 3 - counting non-vowels
nonVowelCount = 0
for char in sentense:
    if char.lower() not in "aeiou":
        nonVowelCount = nonVowelCount + 1

print("Number of non-vowels:", nonVowelCount)

        
        