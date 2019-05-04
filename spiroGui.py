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
        self.spiroList = []
        self.currentSpiroIndex = 0

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

        self.currentSpiroNameLabel = tk.Label(self.controlFrame, text="Name: ")
        self.currentSpiroNameLabel.grid(row=2, column=1, sticky=tk.W)

        self.currentSpiroNameText = tk.StringVar()

        self.currentSpiroNameEntry = tk.Entry(self.controlFrame, state="readonly", textvariable=self.currentSpiroNameText)
        self.currentSpiroNameEntry.grid(row=2, column=2)

        self.currentSpiroMultipleLabel = tk.Label(self.controlFrame, text="Multiple: ")
        self.currentSpiroMultipleLabel.grid(row=3, column=1, sticky=tk.W)

        self.currentSpiroMultipleText = tk.StringVar()

        self.currentSpiroMultipleEntry = tk.Entry(self.controlFrame, state="readonly", textvariable=self.currentSpiroMultipleText)
        self.currentSpiroMultipleEntry.grid(row=3, column=2)


        self.nextConfirmButton = tk.Button(self.controlFrame, text="Next ->", command=self.nextSpiro)
        self.nextConfirmButton.grid(row=2, column=3, rowspan=2)

        self.spiroDrawer = spiroModule.SpirolateralDrawer(self.turtleScreen, 10)

        self.spiroList.append(spiroModule.Spirolateral("Pandas", 5, 90))
        self.spiroList.append(spiroModule.Spirolateral("Ferocity", 7, 90))
        self.spiroList.append(spiroModule.Spirolateral("Highrise", 42, 90))
        self.spiroList.append(spiroModule.Spirolateral("Velocity", 100, 90))
        self.spiroList.append(spiroModule.Spirolateral("notPandas", 10, 90))

        self.spiroDrawer.loadSpiro(self.spiroList[0])
        self.currentSpiroNameText.set(self.spiroList[0].name)
        self.currentSpiroMultipleText.set(self.spiroList[0].timeTable)

        self.root.mainloop()

    def previousSpiro(self):
        self.currentSpiroIndex -= 1
        if self.currentSpiroIndex < 0:
            self.currentSpiroIndex += len(self.spiroList)
        print("Current spiro: ", self.currentSpiroIndex + 1)
        self.spiroDrawer.loadSpiro(self.spiroList[self.currentSpiroIndex])
        self.currentSpiroNameText.set(self.spiroList[self.currentSpiroIndex].name)
        self.currentSpiroMultipleText.set(self.spiroList[self.currentSpiroIndex].timeTable)
        print("Prev")

    def nextSpiro(self):
        self.currentSpiroIndex += 1
        if self.currentSpiroIndex >= len(self.spiroList):
            self.currentSpiroIndex -= len(self.spiroList)
        print("Current spiro: ", self.currentSpiroIndex + 1)
        self.spiroDrawer.loadSpiro(self.spiroList[self.currentSpiroIndex])
        self.currentSpiroNameText.set(self.spiroList[self.currentSpiroIndex].name)
        self.currentSpiroMultipleText.set(self.spiroList[self.currentSpiroIndex].timeTable)
        print("Next")

    def addNewDialog(self):
        self.prevCancelButton.configure(text="Cancel", command=self.addCancel)
        self.nextConfirmButton.configure(text="Confirm", command=self.addNewSpirolateral)
        self.addButton.configure(relief=tk.SUNKEN)

        self.currentSpiroNameEntry.configure(state="normal")
        self.currentSpiroNameText.set("")


    def addNewSpirolateral(self):
        self.prevCancelButton.configure(text="<- Prev", command=self.previousSpiro)
        self.nextConfirmButton.configure(text="Next ->", command=self.nextSpiro)
        self.addButton.configure(relief=tk.RAISED)

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
