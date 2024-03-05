##
# Main function
def main() :
    boxprint('Hello world! How are you?')

##
# Prints the given message in the console inside  a "box"
def boxprint(message):
    n = len(message) + 4
    print('-' * n)
    print(f'| {message} |')
    print('-' * n)
    
# Calling the main function
main()
