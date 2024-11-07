# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see three paths. On one path, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print('The final dragon will lead you home')
    print('because it does not wish to deal with humans.')
    print()

def choosePath():
    path = ''
    while path != '1' and path != '2' and path != '3' :
        print('Which path will you choose?')
        print("[1]The path with a gloomy atmosphere.\n[2]The path with a misty atmosphere\n[3] Or the path with a overwhelming atmostphere.\n")
        path = input("Type the number of the path you wish to choose and press enter.").lower()
    return path

def checkPath(chosenPath):
    print('You approach the path...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    safePath = random.randint(1, 3)

    if chosenPath == str(safePath):
        print('Gives you his treasure!')
    elif chosenPath == str():
        print('Flies you out of the forest')
    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    locationNumber = choosePath()
    checkPath(locationNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()