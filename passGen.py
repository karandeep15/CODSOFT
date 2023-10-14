# importing the dependencies
from tkinter import *
import tkinter as tk
import pyperclip
import random

# initializing the tkinter
root = Tk()

# dimensions of the gui application
root.geometry("700x700")   
root.title("Python Password Generator Application")
root.configure(bg="Light Green") 

# declaring a string variable to store the password generated
passstr = StringVar()

# declaring an integer variable to store the length of the password
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate the password 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*']

    password = ""

    # loop to generate the random password of the length entered by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)


heading_label = tk.Label(root, text="Task 3", font=("Arial", 12, "bold"))
heading_label.pack(pady=10)

# Creating a text label widget
Label(root, text="Python Password Generator Application", font="Arial 20 bold").pack()

# Creating a text label widget
Label(root, text="Enter password length", font="Arial 10 bold").pack(pady=3)

# Creating a entry widget to take password length entered by the user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", command=generate, font="Arial 10 bold").pack(pady=7)

Entry(root, textvariable=passstr).pack(pady=3)

Button(root, text="Print Password", command=copytoclipboard, font="Arial 10 bold").pack()


heading_label = tk.Label(root, text="Made by Karandeep Singh @ CodSoft", font=("Arial", 10, "bold"))
heading_label.pack(pady=10)

root.mainloop()        