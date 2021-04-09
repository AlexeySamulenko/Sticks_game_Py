from tkinter import *
from random import *

cane = 20


def s1():
    global cane
    u = 1
    cane = cane - u
    if cane <= 0:
        sticks.config(text="Computer wins")
        sticks.place(x=75, y=70)
    else:
        sticks.config(text=cane * "| ")


def s2():
    global cane
    u = 2
    cane = cane - u
    if cane <= 0:
        sticks.config(text="Computer wins")
        sticks.place(x=75, y=70)
    else:
        sticks.config(text=cane * "| ")


def s3():
    global cane
    u = 3
    cane = cane - u
    if cane <= 0:
        sticks.config(text="Computer wins")
        sticks.place(x=75, y=70)
    else:
        sticks.config(text=cane * "| ")


def pc():
    global cane
    a = randint(1, 3)
    if cane == 4:
        a = 3
    elif cane == 3:
        a = 2
    elif cane == 2:
        a = 1
    cane = cane - int(a)
    if cane <= 0:
        sticks.config(text="Player win")
        sticks.place(x=140, y=70)
    else:
        sticks.config(text=cane * "| ")


root = Tk()
root.geometry("560x200")
root.resizable(0, 0)
root.title("Sticks")

text1 = Label(root, text="How many sticks to take?")
text1.pack()

button1 = Button(root, text="1", command=s1)
button1.place(x=210, y=30)

button2 = Button(root, text="2", command=s2)
button2.place(x=265, y=30)

button3 = Button(root, text="3", command=s3)
button3.place(x=320, y=30)

pc_button = Button(root, text="Enemy turn", width=30, command=pc)
pc_button.place(x=170, y=150)

sticks = Label(root, text=cane * "| ")
sticks.config(font=("Arial", 30, 'bold'))
sticks.place(x=5, y=70)

root.mainloop()