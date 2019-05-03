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

class SpiroGui():
    def __init__(self):
        self.root = tk.Tk()
        self.spiroList = [1,2,3,4,5]

        self.optionFrame = tk.Frame(self.root)
        self.optionFrame.grid(row=0)

        self.turtleScreenCanvas = tk.Canvas(self.root, height=400, width=400)
        self.turtleScreenCanvas.grid(row=1)
        self.turtleScreen = turtle.TurtleScreen(self.turtleScreenCanvas)
        self.turtleScreen.screensize(400, 400)

        self.controlFrame = tk.Frame(self.root)
        self.controlFrame.grid(row=2)

        self.addButton = tk.Button(self.optionFrame, text="Add new...", command=self.addNewDialog)
        self.addButton.grid(row=0, column=0)

        self.deleteButton = tk.Button(self.optionFrame, text="Delete")
        self.deleteButton.grid(row=0, column=1)

        self.prevCancelButton = tk.Button(self.controlFrame, text="<- Prev", command=self.previousSpiro)
        self.prevCancelButton.grid(row=2, column=0, rowspan=2)

        self.testLabel1 = tk.Label(self.controlFrame, text="test1")
        self.testLabel1.grid(row=2, column=1)

        self.testEntry1 = tk.Entry(self.controlFrame)
        self.testEntry1.grid(row=2, column=2)

        self.testLabel2 = tk.Label(self.controlFrame, text="test2")
        self.testLabel2.grid(row=3, column=1)

        self.testEntry2 = tk.Entry(self.controlFrame)
        self.testEntry2.grid(row=3, column=2)


        self.nextConfirmButton = tk.Button(self.controlFrame, text="Next ->", command=self.nextSpiro)
        self.nextConfirmButton.grid(row=2, column=3, rowspan=2)

        self.spiroDrawer = spiroModule.SpirolateralDrawer(self.turtleScreen, 10)

        self.root.mainloop()

    def previousSpiro(self):
        print("Prev")
    def nextSpiro(self):
        print("Next")

    def addNewDialog(self):
        self.prevCancelButton.configure(text="Cancel", command=self.addCancel)
        self.nextConfirmButton.configure(text="Confirm", command=self.addNewSpirolateral)
        self.addButton.configure(relief=tk.SUNKEN)


    def addNewSpirolateral(self):
        
        self.prevCancelButton.configure(text="<- Prev", command=self.previousSpiro)
        self.nextConfirmButton.configure(text="Next ->", command=self.nextSpiro)

    def addCancel(self):
        print("Canceling spiro addition")
        self.prevCancelButton.configure(text="<- Prev", command=self.previousSpiro)
        self.nextConfirmButton.configure(text="Next ->", command=self.nextSpiro)
        self.addButton.configure(relief=tk.RAISED)

#sc = spiroModule.Spirolateral(7, 45)
#scd.loadSpiro(sc)

#time.sleep(2)
#sc2 = spiroModule.Spirolateral(13, 26)
#scd.loadSpiro(sc2)

spiroGui = SpiroGui()
