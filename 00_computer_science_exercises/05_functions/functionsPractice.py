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
    
helloWorldMulti()