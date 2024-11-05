# Functions practice, Elijah Smith, v0.0

import random

def helloWorldMulti(): # Function Signature
    """This funtion will output Hello, Wolrd! in a a language the user choose.""" # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.

    print("Welcome to Hello, World! Translator.\n")
    print("The following languages are avialble.\n")
    print("[E]nglish.\n")
    print("[S]panish.\n")
    print("[T]agalog.\n")
    print("[G]erman.\n")
    print("[F]rench.\n")
    
    # allow the user to select (input) a choice for the language.
    language = input("Choose the language you want.\n Please type the first Letter you want.\n").lower()
    
     # print "Hello, World!" to the screen in that language.
    if language == "e":
        print("In Enlgish:\nHello, World!\n")
    elif language == "s":
        print("In Spanish:\nHola, Mundo!\n")
    elif language == "t":
        print("In Tagalog:\nKumasta, Mundo!\n")
    elif language == "g":
        print("In German:\nHallo, Walt!\n")
    elif language == "f":
        print("In French:\nBon jour, Le Monde!\n")
    else:
        print("Please try again using the languages given.\n")
#helloWorldMulti() # Function Call

# Function to determine Even / Odd Numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1: int) -> bool: # requires one Argument (argument) and returns a Boolean value
    """Determines if an interger value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False
    
print(isEven(argument1))

# Function with Multiple Arguments
def canRideRollerCaoster(age: int, height: int) -> bool:
    if age > 10 and height > 4: 
        print("You can Ride.\n")
        return True
    else: 
        print("You can not ride.\n")
        return False
    
canRideRollerCaoster(10, 4) # Arguments must passed in the same order as the function signature indicates.
