# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Good job so far.  The only thing I see immediately is you need to at least one item / weapon for the player to select. 

# Module Import
import random
import time
import datetime

# Saving Data To A File
# Step 1 -- Create the file name to use.
logFileName = "dragonRealmLog.txt"
#Example: dragonRealLog1132AM.txt

# Step 2 -- Create / open the file to save the data
saveData = open(logFileName, "a") 
# FILE MODES
# "x" Creates File, If File Exists, Exit With Error Message,.
# "w" Creates File, If File Exists, Erase And Overwrite File Contents.
# "a" Creates File, If File Exists, Append Data To The File.

saveData.write("Game Started" + " " + str(datetime.datetime.now()) + "\n" )

def displayIntro():

    print('You are in a land full of monsters on a quest for buried treasure. In front of you,')
    print('you see three paths. On one path, the monsters are helpful.')
    print('and will share their treasure map with you. The other monsters')
    print('are ruthless, and will tear you apart aggressively on sight.')
    print('The final group will lead you home while youre blindfolded')
    print('because they do not wish to deal with humans.')
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
    print('A group of monsters look at you and...')
    print()
    time.sleep(2)

    if chosenPath == ('1'):
        print('Give you a map to a dragons lair.')
    elif chosenPath == ('2'):
        print('Rip you to shreds leaving only your skinned flesh to remain!')
    elif chosenPath == ('3'):
        print('Tie you up and blidnfold you, leaving you to wake back up outside the forest.')
    
    time.sleep(2)
    if chosenPath == ('1'):
        print('You wander farther ahead to where the map leads and discover an X hat marks the spot.')
        time.sleep(2)
        print('You dig and dig until you hear a thud, finally you found the treasure you were searching for.')
    elif chosenPath == ('2'):
        print('You lie there waiting for what feels like an eternity.')
        time.sleep(2)
        print('Your body starts feeling colder and you start feeling sleepy')
        time.sleep(2)
        print('eventually, your eyes close and your body starts to evaporate into the mist leaving no trace of you left.')

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    locationNumber = choosePath()
    checkPath(locationNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# Close File
saveData.write("END OF GAME LOG\n\n")
saveData.close()