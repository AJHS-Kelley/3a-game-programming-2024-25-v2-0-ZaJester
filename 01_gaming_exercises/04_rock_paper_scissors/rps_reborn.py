# Rock, Paper, Scissors by Ryan Kelly, V3.3c

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Test Player"
playerChoice = None

# Data Structures -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
def playerName() -> str: # Function Signature -- name of function, (arguments if any)
    """Gets the name from the player and returns it."""
    # The like above is a DOCSTRING, it gives a brief example of what the function does.
    playerName = input("Please type your name and press enter.\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input ("Is that correct? Type yes or no and press enter. \n").lower()
    if isCorrect = "yes":
        print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Please type your name and press enter.\n")
    return playerName

# THE RULES using MULTI-LINE STRINGS
def rule() -> None:
    """This function prints the rules for Rock, Paper, Scissors."""
    print(f"""
    Welcome, {playerName} to the Rock, Paper, Scissors Robot!
    It's Time To Play Rock, Paper, Scissors!

    You will play against the CPU. The first player to score 5 points wins. 
    you will select from ROCk, PAPER, OR SCISSORS.
    The CPU will select ROCK, PAPER, OR SCISSORS at random.

    1) ROCK BEATS SCISSORS
    2) SCISSORS BEATS PAPER
    3) PAPER BEATS ROCK         
    """)
    # Does another part of this program need to access this information?
    # IF YES, YOU MUST HAVE A return STAMENT
    #  IF NO, A return STATEMENT IS NOT REQUIRED

def playerChoice() -> str:
    """Allows the player to choose rock, paper, scissors."""
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input()