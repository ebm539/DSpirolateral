#!/usr/bin/python3
### Added the line above to ensure that this script will use the python3 interpreter instead of python 25

#Import the standard python time and sys library. These come installed by default in python
import time
import sys

#import the turtle library which is distributed with python3
import turtle

### Attempt to import the otherSpiroClass.py file that should be in the same directory as this file
## If it doesn't exist, the program will print out an error message and quit after 5 seconds
try:
    import otherSpiroClass as spiroModule
except ModuleNotFoundError:
    print("The otherSpiroClass.py file was not found in this directory")
    time.sleep(5)
    sys.exit()

###Attempt to import the otherSpiroClass.py file that should be in the same directory as this file
##The tkinter module is imported as Tkinter as windows but as tkinter in linux
#This section of code will attempt to import it with the windows spelling
#and will try the linux spelling after

try:
    #Attempt to import the tkinter library with the windows spelling
    import Tkinter as tk
except ModuleNotFoundError:

    try:
        #If this fails, try the linux spelling instead
        import tkinter as tk
    except ModuleNotFoundError:
        #The tkinter library is not installed. Inform the user in the terminal and quit after 5 seconds
        print("The tkinter library is not installed.")
        time.sleep(5)
        sys.exit()

###CLASS SPIROGUI: The reason why this is in a class is because global variable are *way* easier to use in the object method
#This is just down to personal preference, however I do use a class in the otherSpiroClass.py file correctly
class SpiroGui():

    #Init method of the object:
    #This is called whenever SpiroGui is instantiated and sets up the gui and all it's required variables
    def __init__(self):
        self.root = tk.Tk() #This is the root window of the tkinter application.

        self.spiroList = [] #This list will hold all of our spiroObjects which contain the information on each spirolateral

        #This is the current index of the spirolateral displayed on screen
        #It is incremented and decremented whenever the user presses "Prev" and "Next"
        #and wrapped around so that it is always a valid index in our spiroList
        self.currentSpiroIndex = 0

        #Create the frame which will hold the option buttons (i.e. add spiro and delete spiro)
        self.optionFrame = tk.Frame(self.root)
        #Pack this in at the top of the gui using tkinters grid manager
        self.optionFrame.grid(row=0)

        #Create the tkinter canvas which will house the screen where the spirolaterals will be drawn
        self.turtleScreenCanvas = tk.Canvas(self.root, height=400, width=400)
        #Pack the canvas into the middle of our gui
        self.turtleScreenCanvas.grid(row=1)
        #Create the turtle screen where the spirolaterals will be drawn on
        self.turtleScreen = turtle.TurtleScreen(self.turtleScreenCanvas)
        # Set the window size of this turtle screen (TODO: Should this be a variable instead of static?)
        self.turtleScreen.screensize(400, 400)

        #Create the control tkinter frame which will house the buttons for changing spirolaterals
        #and entries which will contain current spirolateral information
        self.controlFrame = tk.Frame(self.root)
        #Pack this frame in the bottom of our gui
        self.controlFrame.grid(row=2)

        #Create the add button with the appropriate text and link it to the correct function
        #This button will put the gui in the "add spiro state" where the user will be prompted
        #To fill in the new spirolateral's information
        self.addButton = tk.Button(self.optionFrame, text="Add new...", command=self.addSpiroState)
        #Pack this button in the top-right most place in the option frame
        self.addButton.grid(row=0, column=0)

        #Similar deal with the add button. This button will put the GUI in the "delete spiro state"
        #Where the user will be asked if they are sure to delete this spirolateral
        self.deleteButton = tk.Button(self.optionFrame, text="Delete", command=self.deleteSpiroState)
        #Pack this next to the addButton in the option frame
        self.deleteButton.grid(row=0, column=1)

        #Create the dialog tkinter label. This will serve as a messenger to the user
        #Informing them on the current state of the gui and how to operate it
        self.dialogLabel = tk.Label(self.controlFrame, text="")
        #Pack this label towards the top of the command frame
        #This will also span the entirety of the width of this frame, which has four columns in it
        self.dialogLabel.grid(row=0, column=0, sticky=tk.N, columnspan=4)
        #Set the text of this label to tell the user that we have no spirolaterals and they need
        #To create a new one in order to proceed
        self.dialogLabel.configure(text="No spirolaterals saved. Please create a new one.")

        #Create the prevCancel button.
        #This button will be the button to view the previous spirolateral or to cancel a pending action
        #Depending on what state the gui is in
        self.prevCancelButton = tk.Button(self.controlFrame, text="<- Prev", command=self.previousSpiro)

        #Pack this button in the left of the command frame. It has a rowspan of two as
        #There will be two labels/entries between this button and the add button
        self.prevCancelButton.grid(row=1, column=0, rowspan=2)

        #Create the label which just tells the user that the entry field beside it
        #Contains the name of the current spirolateral or where the new spirolateral
        #Name is to be inputted
        self.currentSpiroNameLabel = tk.Label(self.controlFrame, text="Name: ")
        #Put this between the prevCancel button and the addConfirm button
        #This will be the upper row between the two buttons
        self.currentSpiroNameLabel.grid(row=1, column=1, sticky=tk.W)

        #Create the string var which will dictate the contents of the name entry field
        #This could either be the name of a spirolateral displayed or the name of a new spirolateral
        self.currentSpiroNameText = tk.StringVar()

        #Create the name entry field. This is used to A.) Show the name of the current spirolateral
        #and B.) provide a place for the user to input a name for a new spirolateral
        #In scenario A it is disabled as it serves as a label while
        #in scenario B it will be enabled and the user will be able to write in it
        self.currentSpiroNameEntry = tk.Entry(self.controlFrame, state="readonly", textvariable=self.currentSpiroNameText)
        #Pack this in between the two buttons in the option frame next to the Name label
        self.currentSpiroNameEntry.grid(row=1, column=2)

        #Multiple label which just tells the user that the entry field beside it
        #Contains the multiple of the current spirolateral or where the new spirolateral
        #multiple is to be inputted
        self.currentSpiroMultipleLabel = tk.Label(self.controlFrame, text="Multiple: ")
        #Put this between the prevCancel button and the addConfirm button
        #This will be the lower row between the two buttons
        self.currentSpiroMultipleLabel.grid(row=2, column=1, sticky=tk.W)

        #Create the string var which will dictate the contents of the name entry field
        #This could either be the multiple of a spirolateral displayed or the multiple of a new spirolateral
        self.currentSpiroMultipleText = tk.StringVar()

        #Create the name entry field. This is used to A.) Show the multiple of the current spirolateral
        #and B.) provide a place for the user to input a multiple for a new spirolateral
        #In scenario A it is disabled as it serves as a label while
        #in scenario B it will be enabled and the user will be able to write in it
        self.currentSpiroMultipleEntry = tk.Entry(self.controlFrame, state="readonly", textvariable=self.currentSpiroMultipleText)
        #Pack this in between the two buttons in the option frame next to the Multiple label
        self.currentSpiroMultipleEntry.grid(row=2, column=2)

        #This button is the same as the prevCancel button however it will be pressed to display the next spirolateral
        #Or to confirm a pending action, depending on what state the gui is in
        self.nextConfirmButton = tk.Button(self.controlFrame, text="Next ->", command=self.nextSpiro)
        #Put this in the rightmost place on the option frame
        self.nextConfirmButton.grid(row=1, column=3, rowspan=2)

        #Instantiate the spiroDrawer which will draw spirolaterals on the turtle screen
        #This spirolateral will have a scale of ten
        self.spiroDrawer = spiroModule.SpirolateralDrawer(self.turtleScreen, 10)

        #Run the normal state function to swap the gui into it's normal state
        self.normalState()
        #Run the tkinter.root.mainloop to start the infinite loop which controls the gui
        self.root.mainloop()

    #normal state function:
    #This is used to set the gui into the "normal" state by configuring the buttons, labels, cetera
    #This state is where the user will spend most of their time
    #It will allow the user to scroll through the existing spirolaterals and
    #Make sure the user can add or delete spirolaterals
    def normalState(self):

        #Wrap around the current spirolateral index to make sure it's valid
        #This means that when the user is at the last spirolateral,
        #They can push "Next" to view the first spirolateral
        if self.currentSpiroIndex < 0:
            self.currentSpiroIndex += len(self.spiroList)
        if self.currentSpiroIndex >= len(self.spiroList):
            self.currentSpiroIndex -= len(self.spiroList)

        #If there are no existing spirolaterals, the user must be informed and prevented
        #from trying actions that don't make sense (i.e.) You can't delete spirolaterals if
        #You don't have any
        if len(self.spiroList) == 0:
            #Prevent the user from pressing the delete button
            #You can't delete spirolaterals you don't have
            self.deleteButton.configure(state="disabled")

            #Set the name and multiple text to empty strings
            #We have no spirolateral information to show
            self.currentSpiroNameText.set("")
            self.currentSpiroMultipleText.set("")

            #Erase any existing spirolateral onscreen
            self.spiroDrawer.clearScreen()

            #Update the dialog label to tell the user we have no spirolaterals
            self.dialogLabel.configure(text="No spirolaterals saved. Please create a new one.")
        else:
            #We have spirolateral now

            #Enable the delete button as there are spirolaterals that the user may want to delete
            self.deleteButton.configure(state="normal")

            #Load the current spirolateral object using the current spiro index
            currentSpiro = self.spiroList[self.currentSpiroIndex]

            #Load currently selected spiro into the drawer
            self.spiroDrawer.loadSpiro(currentSpiro)

            #Configure the text and state for the entry fields and dialog label
            self.dialogLabel.configure(text="Displaying spirolateral {0} of {1}".format(self.currentSpiroIndex + 1, len(self.spiroList)))
            self.currentSpiroNameText.set(currentSpiro.name)
            self.currentSpiroMultipleText.set(currentSpiro.timeTable)
            self.deleteButton.configure(relief=tk.RAISED, state="normal")

        #Regardless of whether or not we have spirolaterals:

        #Configure the entry fields so that the user can't write in them and has the correct text color
        self.currentSpiroNameEntry.configure(state="readonly", textvariable=self.currentSpiroNameText, fg="black")
        self.currentSpiroMultipleEntry.configure(state="readonly", textvariable=self.currentSpiroMultipleText, fg="black")

        #Configure the control buttons to make sure they have the right text on them
        self.prevCancelButton.configure(text="<- Prev", command=self.previousSpiro)
        self.nextConfirmButton.configure(text="Next ->", command=self.nextSpiro)
        self.addButton.configure(relief=tk.RAISED)

    #Add spiro state:
    #Similar to normal state however configures the gui so the user can create a new spirolateral
    def addSpiroState(self):

        #The prev/next buttons now serve as our cancel/confirm buttons for adding a new spirolateral
        #Configure these buttons so they have the correct text and will run the right commands
        #Clicking the now cancel button will abort the spirolateral addition and return the user to the normal state
        #Clciking the now confirm button will attempt to create a new spirolateral using text inside the entry fields
        #and add it to our spiro list if we are successful
        self.prevCancelButton.configure(text=" Cancel", command=self.normalState, state="normal")
        self.nextConfirmButton.configure(text="Confirm", command=self.addNewSpirolateral, state="normal")

        #Disable the delete button. We want the user to pass through the normal state
        #In order to get the the delete state as the normal state resets the gui so that it
        #operates as expected in the delete state
        self.deleteButton.configure(state="disabled")
        #Permanately sink the addButton in as this indicates to the user what mode is currently in use
        self.addButton.configure(relief=tk.SUNKEN)

        #Update the dialog label to ask the user to put in the new spirolateral's name and multiple in the entry fields below
        self.dialogLabel.configure(text="Please enter the new spirolateral's name and multiple below")

        #Enable the name and multiple entries and clear them of past text so the user
        #can put in the name and multiple of the new spirolateral
        self.currentSpiroNameEntry.configure(state="normal", fg="black", textvariable=self.currentSpiroNameText)
        self.currentSpiroMultipleEntry.configure(state="normal", fg="black", textvariable=self.currentSpiroMultipleText)
        self.currentSpiroMultipleText.set("")
        self.currentSpiroNameText.set("")


    #PreviousSpiro
    #This program just decrements the currentSprioIndex and runs the normal state
    #Which will now display the previous spirolateral
    #This is called whenever the user presses the "Next" button
    def previousSpiro(self):
        self.currentSpiroIndex -= 1
        self.normalState()

    #Same diff with the previous spirolateral
    #Increments the currentSprioIndex and runs the normal state
    #Is called whenever the "Prev" button is pressed
    def nextSpiro(self):
        self.currentSpiroIndex += 1
        self.normalState()


    #Add new spirolateral
    #This function takes the current text inside the name and multiple entries
    #And attempts to create a new spirolateral from them
    def addNewSpirolateral(self):
        #Create the list which will keep track on what invalid entries the user has made
        #If this contains something, it is passed to the error state when it is called
        invalidEntries = []

        #Retrieve the value of the name entry
        newSpiroName = self.currentSpiroNameText.get()

        #If nothing has been entered into the name entry, add this into our list
        #Of invalid entries
        if not newSpiroName:
            #Null name is just a code which means that the text for a new name doesn't exist
            invalidEntries.append("nullName")

        try:
            #Retrieve the text inside the multiple entry and try to interpret is as an integer
            newSpiroMultiple = int(self.currentSpiroMultipleText.get())

            #If the number given for the new spirolateral's multiple is less than or equal to 0
            #Add the negMultiple string to our invalidEntryies list
            if newSpiroMultiple <= 0:
                invalidEntries.append("negMultiple")
        #If we have failed to interpret the contents of the multiple entry as an int:
        except ValueError:
            #Try to see if we actually have anything in the entry
            #This just changes what error we'll pass to the error state
            if self.currentSpiroMultipleText.get():
                #We have something but it's invalid
                invalidEntries.append("invMultiple")
            else:
                #We have nothing in the entry
                invalidEntries.append("nullMultiple")

        #If no errors have been added to our invalidEntries list...
        if not invalidEntries:
            #Add our spirolateral with our now validated data
            self.spiroList.append(spiroModule.Spirolateral(newSpiroName, newSpiroMultiple, 90))
            #Set the currentSpiroIndex so that when normalstate is run, it will
            #Show the spirolateral just added
            self.currentSpiroIndex = len(self.spiroList) - 1
            #Run the normal state
            self.normalState()
        else:
            #If we have encountered errors during the validation of our data, pass them
            #To the error state which will inform the user of them
            self.errorState(invalidEntries)

    #Error state:
    #This function is run whenever we have encountered errors processing the data the user
    #Has or has not provided to us to create a new spirolateral with
    def errorState(self, invalidEntries):
        #Disable the entry fields and the next/confirm buttons
        #Were going to print out the errors in those entry fields
        self.currentSpiroNameEntry.configure(state="readonly")
        self.currentSpiroMultipleEntry.configure(state="readonly")
        self.nextConfirmButton.configure(state="disabled")
        self.prevCancelButton.configure(state="disabled")


        if "nullName" in invalidEntries:
            #If the user hasn't given us a name, print out an error into the name entry field
            #Set this text red
            self.currentSpiroNameEntry.configure(fg="red")
            self.currentSpiroNameText.set("Name is required")

        if "invMultiple" in invalidEntries:
            #If the user has given us an invalid multiple, print out an error into the multiple entry field
            #Set this text red
            self.currentSpiroMultipleEntry.configure(fg="red")
            self.currentSpiroMultipleText.set("Must be whole numeral")

        if "nullMultiple" in invalidEntries:
            #If the user hasn't given us a new multiple, print out an error into the multiple entry field
            #Set this text red
            self.currentSpiroMultipleEntry.configure(fg="red")
            self.currentSpiroMultipleText.set("Multiple is required")

        if "negMultiple" in invalidEntries:
            #If the user has given as a multiple that is 0 or less, print out an error into the multiple entry field
            #Set this text red
            self.currentSpiroMultipleEntry.configure(fg="red")
            self.currentSpiroMultipleText.set("Must be more than 0")


        #Wait for two seconds before we return the the addSpiroState so that the user has time to read the errors
        self.root.after(2000, self.addSpiroState)

    #Delete spiro state function:
    #Set up the gui so that it queries the user if they want to delete the current spirolateral
    def deleteSpiroState(self):
        ##Permanately sink the delete button in as this indicates to the user what mode is currently in use
        self.deleteButton.configure(relief=tk.SUNKEN)
        #Disable the add button. We want the user to pass through the normal state
        #In order to get the add state as the normal state resets the gui so that it
        #operates as expected in the add state
        self.addButton.configure(state="disabled")
        #Update the text in the dialog label to ask the user if they are sure to delete the current spirolateral
        self.dialogLabel.configure(text="Are you sure you want to delete this spirolateral?")

        #Update the next/cofnirm and prev/cancel buttons to have the right text
        #and the commands that happen when the buttons are pressed
        #The now yes button will run the deleteSpiro function
        #The now No button will return the gui to the normal state
        self.nextConfirmButton.configure(text="  Yes  ", command=self.deleteSpiro)
        self.prevCancelButton.configure(text="  No  ", command=self.normalState)

    #delete spiro function
    def deleteSpiro(self):
        #Delete the current spirolateral from the spiro list
        del(self.spiroList[self.currentSpiroIndex])
        #Set the current spiro index so that the
        #first spirolateral is the next spirolateral seen by the user
        self.currentSpiroIndex = 0
        #Run the normal state
        self.normalState()

#Instantiate the above spiro gui object to run the main loop of the program
spiroGui = SpiroGui()
