# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Good job so far.  The only thing I see immediately is you need to at least one item / weapon for the player to select. 
# 2024-12-09 -- Code Check -- 85%.  Nice job!  Tough project to complete, but you stuck with it. 

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

items = 0

def displayIntro():

    print('You are in a land full of monsters on a quest for buried treasure. In front of you,')
    print('you see three paths. On one path, a gloomy atmosphere that makes you feel uneasy.')
    print('The next path has a misty atmosphere blurring your sense of direction.')
    print('The final path has an overwhelming atmosphere, this causes your heart to race.')
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
    print('You feel as if you\'re being watched...')
    time.sleep(2)
    print('Suddenly you wander too far and...')
    print()
    time.sleep(2)

    if chosenPath == ('1'):
        print('Find a group of goblins that give you the map to their treaure.')
    elif chosenPath == ('2'):
        print('Get ripped to shreds by a group of Orcs leaving only your skinned flesh to remain!')
    elif chosenPath == ('3'):
        print('Fall into a lake full of beautiful mermaids.')
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
    elif chosenPath == ('3'):
        print('Despite this, you feel as if you should try to swim away.')
        time.sleep(2)
        print('You notice something underneath the water constantly circling you,')
        time.sleep(2)
        print('suddendly you feel something tugging your leg pulling you closer and closer towards the bottom')
        time.sleep(2)
        print('You try to resist but whatever is pulling you is too strong.')
        time.sleep(2)
        print('You start to struggle, you are losing oxygen.')
        time.sleep(2)
        print('Your eyes slowly close but before you go out you see the culprit of your downfall.')
        time.sleep(1)
        print('Those beautiful women laying across the rocks weren\'t mermaids, they were sirens.')

    # Confused on how to utilize items for each path
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    item = input("Please type the number of the weapon you wish to choose, [1]Shotgun [2]Torch")
    if item == '1':
        hasShotgun = True
    if item == '2':
        hasTorch = True
        
    locationNumber = choosePath()
    checkPath(locationNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()

# Close File
saveData.write("END OF GAME LOG\n\n")
saveData.close()