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
# .lower() makes everything lowercase


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
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissor":
        playerChoice = input("Please enter rock, paper, scissors and press enter.\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissor":
            print("Play along and try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    # Print the current score for  CPU and Player
    # Let player select rock, paper, scissors
    # Let cpu select choice at random
    cpuChoice = random.randint(0, 2) # randomly select 0, 1, or 2.
    if cpuChoice == 0:
        cpuChoice = "scissors"
    elif cpuChoice == 1:
        cpuChoice = "rock"
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("unable to determine CPU choice.\nPlease restart.\n")
        exit()
    print(f"CPU Choice: {cpuChoice}.\n")
    # Compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins this round.\n")
        cpuScore += 1
    # Cpu wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("The player wins this round")
        playerScore += 1
    # Player wins
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("Its a draw")
    # Draw
    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("The player wins this round")
        playerScore += 1
    # player wins
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("The CPU wins this round")
        cpuScore += 1
    # CPU wins
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("Its a draw")
    # Draw
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("its a draw")
    # Draw
    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("The CPU wins this round")
        cpuScore += 1
    # CPU wins
    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n ")
        print("The player wins this round")
        playerScore += 1
    # CPU wins
    else:
        print("Error, please try again.\n")
        exit()


print(f"Your final score: {playerScore}\nCPU Final Score: {cpuScore}")
if playerScore > cpuScore:
    print(f"WHAT, You actually won? T-That's impossible!")
if playerScore < cpuScore:
    print(f"I knew you couldn't do it. I never had faith in you to begin with. Now think about what you've done you LOSER!")
else:
    print(f"Now look what you've done. Try again.")
    # Print the results to the screen
    # award point to winner and output results