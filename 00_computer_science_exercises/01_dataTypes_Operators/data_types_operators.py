# Data Types and Operators, Elijah Smith, v0.0

# Fundemental Data Types
# String - str - Sequence of letters, numbers, spaces, or other characters
# Strings in Python are inside ' ' or  " "
# idc if you use ' ' or " " just be consistent

# Boolean - bool - True or False values.

# Float - float - any number value with a decimal, +\-

# Integers - int - any whole number, +\-, including 0.

# Data types are stored into a VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER
# came1CaseVariableNames
# snake_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 2529445 # int data types
highScore = 5271296 # int data types

carSpeed = 30.25 # float data type, miles per hour
car_speed = -5.72627372 # float data type, miles per hour

hasAxe = True # boolean data types
isPurple = False # boolean data types

playerName = "Eliah Smith" # string data types
enemyTitle = "Goblin King" # string data types

# ASSIGN NEW VALUES
playerName = "Danny Dooms"
carSpeed = -3.23

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 4.5

# printing Variables to Console / Screen
print(playerName)
print(car_speed)
print(isPurple)
print(high_score)

#printing variables and expressions console / screen
print(car_speed + 2538)
print(3 * 15)
print(car_speed)

#PRINTING VARIABES INSIDE OF STRINGS
print(f"Hello {playerName}. Your high score is {high_score}.\n")

#ARITHMETIC OPERATORS
myInt = 4
myFloat = 4.32
myNum = 0

# Addition
myInt = 2 + 6
myFloat = 3.5 + 2.48

myInt = myInt + 7

myNum = myInt + myFloat
# When you add an int and float together, the answer becomes a float

# Subtraction
myNum = myInt - myFloat
myInt = myFloat - 2.35

# Multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS.
numStudents = 7
numSlicesPizza =  27

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# Exponents **
numSqaured = 5 ** 2 # 5 is the base, 2 is the exponent

# Floor-Division // -- Divides, throws out any decimal
myNum = myInt // myFloat

# Addition Assignment Operator - Mostly used for counters.
myNum = 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness
myNum *= 1
myNum /= 1














# COMPARISON OPERATORS

# IS-EQUAL- TO == Are the two values equal to each other?
# Returns True or False based on evaluation.
x = 12.0 
#print(x == 5)

# NOT-EQUAL-TO != Are the two values not equal?
# Returns True or False based on evaulation.
# print(x != 12)

# # GREATER THAN / GREATER-THAN-OR-EQUAL TO
# print(5 > 3) # Greater Than
# print(12 >= 2) # Greater Than or Equal to

# # LESS THAN / LESS-THAN-OR-EQUAL TO
# print(5 < 3) # LESS Than
# print(12 <= 2) # Less Than or Equal To

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 16
height = 60.7
eyeColor = "Dark Brown"
# In order to ride the Teacups, you must be at least 18 years old and at least 60" tall
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Red"
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE FALSE CONDITION FIRST!!!!
#print(defeatedBoss == True and level > 5 and hasRedKey == True)


# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Red"
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE FALSE CONDITION FIRST!!!!
#print(defeatedBoss == True and level > 5 and hasRedKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT
a = 5 
# print(a == 5)
# print(not (not (a == 5)))

# COMBINING LOGICAL OPERATORS
#print(a == 5 and hasKey == True or isCloud == True)
#TRUE and

# INDENTITY OPERATORS
g = 1.0
h = 1.0 
i = g 
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)