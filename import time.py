import time
from tkinter import *
from tkinter import messagebox

#Creating Tk window
root= Tk()

# setting gemoetry of tk window
root.geometry("300x250")

#Using title()to display a message in the dialouge box of the message in the title bar.
root.title("Time Counter")
root.configure(bg='blue')

# Declartation of variables
hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=hour)
hourEntry.place(x=80,y=20)
minuteEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=hour)
minuteEntry.place()