## String Manipulation
#  ===================


# REPLACE: replaces a given substring with a another string
sentense = "Thin slices of apples should be used to make apple pie"
print(sentense)
print(sentense.replace("apple", "banana"))

## STRIP: strips white spaces or given specific characters from the begining
#         and end of a string
sentense = " Hello World \n"
print(sentense)
print("----") # Print a line after the previous print statements. See the blank line
sentense2 = sentense.strip()
print(sentense2)
print("----") # No blank line above this line

## RSTRIP: strips white spaces or given specific characters at the end of a string
sentense = " Hello World \n"
sentense3 = sentense.rstrip()
print(sentense)
print("----") # Print a line after the previous print statements. See the blank line
print(sentense3) # White space at the begining is retained.
print("----") # Print a line after the previous print statements. See the blank line

# Using STRIP and RSTRIP to strip non-white spaces
url = "https://www.ualberta.ca/"

domainName = url.strip("htps:/")
print(domainName)


# SPLIT: splits a string by white spaces or a given substring
sentense = "Mary had a little       lamb"
words = sentense.split() # split by white spaces. Removes empty strings
                         # created by multiple consecutive white spaces
                         # The result is returned as a list
print(words)

parts = sentense.split(maxsplit=1) # Splits only once, starting from the begining 
print(parts)

# RSPLIT: splits from the end. Useful only when we set maxsplit
parts2 = sentense.rsplit(maxsplit=1) # Splits only once, starting from the end
print(parts2)

# SPLIT and RSPLIT with a given character
csv = "12,4,54,455,213,34,6,78,0,16" # comma-separated value string
vals = csv.split(",")
print(vals)

parts3 = csv.split(",", maxsplit=1)
print(parts3)

parts4 = csv.rsplit(",", maxsplit=1)
print(parts4)

## SPLITLINES: splits a string by new-line characters

rhyme = "Row, row, row your boat\nGently down the stream\nMerrily, merrily, merrily, merrily\nLife is but a dream"
print(rhyme)

lines = rhyme.splitlines()
print(lines)









