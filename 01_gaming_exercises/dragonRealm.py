# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

# Module Import
import random
import time
import datetime

# Saving Data To A File
# Step 1 -- Create the file name to use.
logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
# logFileName ="dragonrealm"
#Example: dragonRealLog1132AM.txt

# Step 2 -- Create / open the file to save the data
saveData = open(logFileName, "x") 
# FILE MODES
# "x" Creates File, If File Exists, Exit With Error Message,.
# "w" Creates File, If File Exists, Erase And Overwrite File Contents.
# "a" Creates File, If File Exists, Append Data To The File.

saveData.write("Game Started" + " " + str(datetime.datetime.now()) + "\n" )

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

    if chosenPath == str('1'):
        print('Gives you his treasure!')
    elif chosenPath == str('2'):
        print('Flies you out of the forest')
    elif chosenPath == str ('3'):
        print('Gobbles you down in one bite!')
    

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    locationNumber = choosePath()
    checkPath(locationNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()

# Close File
saveData.close()