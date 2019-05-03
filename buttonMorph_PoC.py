##Decided to seperate the spirolateral object from the parts that controlled the drawing of the spirolateral

import otherSpiroClass as spiroModule
import Tkinter as tk
import time
import turtle

global command

root = tk.Tk()

spiroList = []

def command1():
    print("Command 1")
    command.configure(text="Command2", command=command2)

def command2():
    print("Command 2")
    command.configure(text="Command1", command=command1)

def buildGui():
    global command
    optionFrame = tk.Frame()
    optionFrame.grid(row=1)
    command = tk.Button(optionFrame, text="Command1", command=command1)
    command.grid(row=0, column=0)
    deleteButton = tk.Button(optionFrame, text="Delete")
    deleteButton.grid(row=0, column=1)

#def addNewSpiro()

buildGui()

canvas = tk.Canvas()
canvas.grid()
btn1 = tk.Button(root, text="Help")
btn1.grid()

screen = turtle.TurtleScreen(canvas)

scd = spiroModule.SpirolateralDrawer(screen, 10)
sc = spiroModule.Spirolateral(7, 45)
scd.loadSpiro(sc)

time.sleep(2)
sc2 = spiroModule.Spirolateral(13, 26)
scd.loadSpiro(sc2)


root.mainloop()
