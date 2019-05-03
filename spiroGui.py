#!/usr/bin/python3
### Added the line above to ensure that this script will use the python3 interpreter instead of python 25

##Decided to seperate the spirolateral object from the parts that controlled the drawing of the spirolateral

import otherSpiroClass as spiroModule

try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk


import time
import turtle


root = tk.Tk()

spiroList = []

def buildGui():
    global canvas
    global prevCancelButton, nextConfirmButton, addButton
    optionFrame = tk.Frame(root)
    optionFrame.grid(row=0)

    canvas = tk.Canvas(root, height=400, width=400)
    canvas.grid(row=1)

    controlFrame = tk.Frame(root)
    controlFrame.grid(row=2)

    addButton = tk.Button(optionFrame, text="Add new...", command=addNewDialog)
    addButton.grid(row=0, column=0)

    deleteButton = tk.Button(optionFrame, text="Delete")
    deleteButton.grid(row=0, column=1)

    prevCancelButton = tk.Button(controlFrame, text="<- Prev", command=previousSpiro)
    prevCancelButton.grid(row=2, column=0)

    nextConfirmButton = tk.Button(controlFrame, text="Next ->", command=nextSpiro)
    nextConfirmButton.grid(row=2, column=2)

def previousSpiro():
    print("Prev")
def nextSpiro():
    print("Next")

def addNewDialog():
    prevCancelButton.configure(text="Cancel", command=addCancel)
    nextConfirmButton.configure(text="Confirm", command=addNewSpirolateral)
    addButton.configure(relief=tk.SUNKEN)


def addNewSpirolateral():
    print("Spiro added ;)")
    prevCancelButton.configure(text="<- Prev", command=previousSpiro)
    nextConfirmButton.configure(text="Next ->", command=nextSpiro)

def addCancel():
    print("Canceling spiro addition")
    prevCancelButton.configure(text="<- Prev", command=previousSpiro)
    nextConfirmButton.configure(text="Next ->", command=nextSpiro)
    addButton.configure(relief=tk.RAISED)



#def addNewSpiro()

buildGui()

screen = turtle.TurtleScreen(canvas)
screen.screensize(400, 400)

scd = spiroModule.SpirolateralDrawer(screen, 10)
sc = spiroModule.Spirolateral(7, 45)
scd.loadSpiro(sc)

time.sleep(2)
sc2 = spiroModule.Spirolateral(13, 26)
scd.loadSpiro(sc2)


root.mainloop()
