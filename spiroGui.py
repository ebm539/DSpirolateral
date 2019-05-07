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

        self.addButton = tk.Button(self.optionFrame, text="Add new...", command=self.addSpiroState)
        self.addButton.grid(row=0, column=0)

        self.deleteButton = tk.Button(self.optionFrame, text="Delete", command=self.deleteSpiroState)
        self.deleteButton.grid(row=0, column=1)

        self.dialogLabel = tk.Label(self.controlFrame, text="")
        self.dialogLabel.grid(row=0, column=0, sticky=tk.N, columnspan=4)
        self.dialogLabel.configure(text="No spirolaterals saved. Please create a new one.")

        self.prevCancelButton = tk.Button(self.controlFrame, text="<- Prev", command=self.previousSpiro)
        self.prevCancelButton.grid(row=1, column=0, rowspan=2)

        self.currentSpiroNameLabel = tk.Label(self.controlFrame, text="Name: ")
        self.currentSpiroNameLabel.grid(row=1, column=1, sticky=tk.W)

        self.currentSpiroNameText = tk.StringVar()

        self.currentSpiroNameEntry = tk.Entry(self.controlFrame, state="readonly", textvariable=self.currentSpiroNameText)
        self.currentSpiroNameEntry.grid(row=1, column=2)

        self.currentSpiroMultipleLabel = tk.Label(self.controlFrame, text="Multiple: ")
        self.currentSpiroMultipleLabel.grid(row=2, column=1, sticky=tk.W)

        self.currentSpiroMultipleText = tk.StringVar()

        self.currentSpiroMultipleEntry = tk.Entry(self.controlFrame, state="readonly", textvariable=self.currentSpiroMultipleText)
        self.currentSpiroMultipleEntry.grid(row=2, column=2)


        self.nextConfirmButton = tk.Button(self.controlFrame, text="Next ->", command=self.nextSpiro)
        self.nextConfirmButton.grid(row=1, column=3, rowspan=2)

        self.spiroDrawer = spiroModule.SpirolateralDrawer(self.turtleScreen, 10)

        self.root.mainloop()

    def normalState(self):
        #Wrap around index
        if self.currentSpiroIndex < 0:
            self.currentSpiroIndex += len(self.spiroList)
        if self.currentSpiroIndex >= len(self.spiroList):
            self.currentSpiroIndex -= len(self.spiroList)

        print(self.currentSpiroIndex)

        if len(self.spiroList) == 0:
            self.deleteButton.configure(state="disabled")
            self.currentSpiroNameText.set("")
            self.currentSpiroMultipleText.set("")
            self.spiroDrawer.clearScreen()
            self.dialogLabel.configure(text="No spirolaterals saved. Please create a new one.")
        else:
            currentSpiro = self.spiroList[self.currentSpiroIndex]

            #Load currently selected spiro into the drawer
            self.spiroDrawer.loadSpiro(currentSpiro)

            #Configure the text and state for the entry fields
            self.dialogLabel.configure(text="Displaying spirolateral {0} of {1}".format(self.currentSpiroIndex + 1, len(self.spiroList)))
            self.currentSpiroNameText.set(currentSpiro.name)
            self.currentSpiroMultipleText.set(currentSpiro.timeTable)
            self.deleteButton.configure(relief=tk.RAISED, state="normal")

        self.currentSpiroNameEntry.configure(state="readonly", textvariable=self.currentSpiroNameText, fg="black")
        self.currentSpiroMultipleEntry.configure(state="readonly", textvariable=self.currentSpiroMultipleText, fg="black")

        #Configure the control buttons to make sure they have the right text on them
        self.prevCancelButton.configure(text="<- Prev", command=self.previousSpiro)
        self.nextConfirmButton.configure(text="Next ->", command=self.nextSpiro)
        self.addButton.configure(relief=tk.RAISED)

    def addSpiroState(self):
        self.prevCancelButton.configure(text=" Cancel", command=self.addCancel)
        self.nextConfirmButton.configure(text="Confirm", command=self.addNewSpirolateral)
        self.addButton.configure(relief=tk.SUNKEN)

        self.dialogLabel.configure(text="Please enter the new spirolateral's name and multiple below")

        self.currentSpiroNameEntry.configure(state="normal", fg="black", textvariable=self.currentSpiroNameText)
        self.currentSpiroNameText.set("")

        self.currentSpiroMultipleEntry.configure(state="normal", fg="black", textvariable=self.currentSpiroMultipleText)
        self.currentSpiroMultipleText.set("")



    def previousSpiro(self):
        self.currentSpiroIndex -= 1
        print("Current spiro: ", self.currentSpiroIndex + 1)
        print("Prev")
        self.normalState()

    def nextSpiro(self):
        self.currentSpiroIndex += 1
        print("Current spiro: ", self.currentSpiroIndex + 1)
        print("Next")
        self.normalState()



    def addNewSpirolateral(self):
        invalidEntries = []
        newSpiroName = self.currentSpiroNameText.get()
        if not newSpiroName:
            invalidEntries.append("nullName")

        try:
            newSpiroMultiple = int(self.currentSpiroMultipleText.get())
        except ValueError:
            if self.currentSpiroMultipleText.get():
                invalidEntries.append("invMultiple")
            else:
                invalidEntries.append("nullMultiple")

        if not invalidEntries:
            self.spiroList.append(spiroModule.Spirolateral(newSpiroName, newSpiroMultiple, 90))
            self.currentSpiroIndex = len(self.spiroList) - 1
            self.normalState()
            print("Spiro added ;)")
        else:
            self.errorState(invalidEntries)

    def deleteSpiroState(self):
        self.deleteButton.configure(relief=tk.SUNKEN)
        self.dialogLabel.configure(text="Are you sure you want to delete this spirolateral?")
        self.nextConfirmButton.configure(text="  Yes  ", command=self.deleteSpiro)
        self.prevCancelButton.configure(text="  No  ", command=self.normalState)

    def deleteSpiro(self):
        del(self.spiroList[self.currentSpiroIndex])
        self.currentSpiroIndex = 0
        self.normalState()


    def addCancel(self):
        print("Canceling spiro addition")
        self.normalState()

    def errorState(self, invalidEntries):
        self.currentSpiroNameEntry.configure(state="readonly")
        self.currentSpiroMultipleEntry.configure(state="readonly")

        if "nullName" in invalidEntries:
            self.currentSpiroNameEntry.configure(fg="red")
            self.currentSpiroNameText.set("Name is required")

        if "invMultiple" in invalidEntries:
            self.currentSpiroMultipleEntry.configure(fg="red")
            self.currentSpiroMultipleText.set("Must be whole numeral")

        if "nullMultiple" in invalidEntries:
            self.currentSpiroMultipleEntry.configure(fg="red")
            self.currentSpiroMultipleText.set("Multiple is required")



        self.root.after(2000, self.addSpiroState)

spiroGui = SpiroGui()
