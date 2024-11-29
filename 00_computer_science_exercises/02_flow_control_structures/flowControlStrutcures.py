# Flow Control Structures, Elijah Smith
# Making Computer programs Make Decisions

temperature = 78.43
color = "Red"
height = 6
likesPinappleOnPizza = False

# SINGLE DECISION POINT - if Statement
# if CONDITIONAL_EXPRESSION <-- This will use a COMPARISION OPERATOR 99% of the time.
    # runThisCode if the CONDITIONAL_EXPRESSION is True

if height < 10:
    print("he is quite the tall one.\n")

if temperature < 100:
    print("It is pretty nice outside.\n")

# CHEAT CODE FOPR IF STATEMENTS THAT USE BOOLEANS
if likesPinappleOnPizza:
    print("Yucky")

# What if we want something differentto happen?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = INSTEAD OF ==
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color.\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height to ride.
    
# When writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >=
if height >= 6:
    print("You're tall enough to ride the Tea Cups!\n")
elif height >= 3:
    print("You're too tall to tide the Tea Cups!\n")
else: # "oh, no, something's wrong!"
    print("Error, height not detected. Do Not Ride.\n")


# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3:
    print("You're not tall enough to ride the Tea Cups!\n")
elif height <= 6:
    print("You're too tall to tide the Tea Cups!\n")
else: # "oh, no, something's wrong!"
    print("Error, height not detected. Do Not Ride.\n") 

# Create an if-elif-else block that checks temperature
# If the temperature is at least 100, print that its too hot outside
# If the temperature is at least 50 degrees but less than 100, print that recess is allowed
# If the temperature is less than 50 degrees but greater than 0, print that recess is in the gym.
# If no temperature is detected, print and error message.
temperature = 99
if temperature >= 100:
    print("It's too hot outside, children cannot play outdoors.\n")
elif temperature >= 50:
    print("Recess is allowed today.\n")
elif temperature > 0:
    print("Recess will be in the gym.\n")
else:
    print("Error detecting temperature.\n")
