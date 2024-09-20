# Rock, Paper, Scissors by Elijah Smith v0.0

# MODULE IMPORTS
import random

# DATA STRUCTURES -- Player
playerScore = 0
playerName = "Test Player"
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Type your name and press Enter.\n")
print(f"Hello {playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n")
print(isCorrect)



if isCorrect == "yes":
    print(f"Ok {playerName}, Time to play rock, paper, scissors!\n")
else:
    playerName = input("Type your name and press Enter.\n")

# THE RULES using MULTI-LINE STRINGS
print("""
Welcome, {playerName} to the Rock, Paper, Scissors Robot!
Let's Start the Rock, Paper, Scissors!
      
You will play against the CPU, The first player to score 5 points wins
You will select from Rock, Paper, or Scissors
The Cpu will select Rock, Paper, or Scissors at random.
      
1) Rock beats Scissors
2) Scissors beats Paper
3) Paper beats Rock
""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of double-quotes is just ignored.
use multi- line strings to write large comments
then putting a # in front of 15 different lines.
"""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName}you have {playerScore}points.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissor":
        playerChoice = input("Please enter rock, paper, scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissor":
        print("Play along and try again.\n")
        exit()
    print(f"You have chosen {playerChoice}.\n")
else:
    print(f"You have chosen {playerChoice}.\n")



    # Print the current score for  CPU and Player
    # Let player select rock, paper, scissors
    # Let cpu select choice at random
    # Compare player choice to cpu choice
    # Print the results to the screen
    # award point to winner and output results