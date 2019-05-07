#Import the standard turtle and time module
import turtle
import time

#Spirolateral drawer class:
#This class handles the drawing of spirolaterals by loading in a spirolateral object and drawing
#it in the gui
class SpirolateralDrawer():
    #Init method which is called whenever this is instantiated
    def __init__(self, screen, scale):
        #This screen is the turtle.screen object where the turtle graphics runs from
        self.screen = screen
        #This turtle object Is the visible turtle object which draws out spirolaterals as the user sees
        #In the gui. It is a raw turtle so it can be used in the tkinter application
        self.turtleObject = turtle.RawTurtle(self.screen)

        #Hide the visible turtle object's arrow
        self.turtleObject.hideturtle()

        #This turtle object is invisible. This is used to sketch out the spirolateral to be drawn
        #In an "invisible" line so that information can be gathered about the spirolateral's shape
        #which can be used to center it on screen
        self.ghostTurtle = turtle.RawTurtle(self.screen)
        #Hide the invisible turtle's arrow so it's not just a floating arrow
        self.ghostTurtle.hideturtle()

        #Set both turtle's speed to zero. This doesn't really affect the code, but it sets
        #The turtles to their fastest speed.
        self.ghostTurtle.speed(0)
        self.turtleObject.speed(0)

        #The position in the self.screen where the spirolaterals will be centered from
        self.centerPos = (0,0)

        #The scale determines how large the spirolateral will be on screen
        self.scale = scale

        #This turtle object is simply going to be a circle placed in the center of each spirolateral.
        #This should not be moved.
        self.centerTurtle = turtle.RawTurtle(self.screen)
        #Set the shape of the center turtle
        self.centerTurtle.shape("circle")

        #Lift the pen on the center turtle so that when we place it to the
        #center pos it doesn't leave a line.
        self.centerTurtle.penup()
        self.centerTurtle.goto(self.centerPos)

    #This function is used to draw the spirolateral with either the ghost or main
    #Turtle object.
    #This is only used internally, so I've added the double _ in front of it
    #to imply privacy

    #Spiro object is the spirolateral object, turtleObject is the object used to draw the spiro
    #startPos is position (x,y) where the spiro needs to start and visible is a boolean of whether
    #or not the spirolateral is to be visible
    def __drawBasicSpiro(self, spiroObject, turtleObject, startPos, visible):
        #These lists keep track of the location of the turtle object as it travels across the screen
        xLocationList = []
        yLocationList = []

        #Lift up the pen of this turtle object so we can move it to the center
        #pos without leaving a trail
        turtleObject.penup()
        turtleObject.goto(startPos)

        #If this spirolateral is to be visible, place the pen down so that you can see
        #what it draws
        if visible:
            turtleObject.pendown()

        #Repeat the following loop until the spirolateral is finished
        while True:
            #For each number in the spiro object's digital root:
            for distance in spiroObject.dRootList:
                #Move the turtle object forward that distance multiplied by the scale
                turtleObject.forward(distance * self.scale)
                #Rotate the object right the angle stored in spirolateral
                turtleObject.right(spiroObject.angle)

            #Record the current location of turtle object using
            #The builtin pos method
            currentPosx, currentPosy = turtleObject.pos()
            #Round the co-ordinates to 3 decimal places. This is to ensure that
            #when the turtle object returns to it's start pos we can read that as
            #current pos == start pos. Python has a nasty habit of making 0.9999999999999999999999999999999999999999999999999
            #not equal to 1
            currentPosx = round(currentPosx, 3)
            currentPosy = round(currentPosy, 3)

            #Append this location to our location lists
            xLocationList.append(currentPosx)
            yLocationList.append(currentPosy)

            #If we have reached our start pos
            if currentPosx == startPos[0] and currentPosy == startPos[1]:
                #We have completed our spirolateral and need to break out of this loop
                break

        #Return our location lists
        return xLocationList, yLocationList

    #This is the method we call to load in a spiro object and draw it
    #onto the screen
    #spiroObject is the spiro object containing all of the data required to draw the spirolateral
    def loadSpiro(self, spiroObject):
        #Clean out the screen by running the clearScreen method to prepare the screen for a new spirolateral
        self.clearScreen()
        #Sets the tracer of the screen to false. This is to fully disable the animation of the turtle drawing
        #And makes the creation of these spirolaterals instant
        self.screen.tracer(False)

        #Draw a ghost spirolateral 
        xLocationList, yLocationList = self.__drawBasicSpiro(spiroObject, self.ghostTurtle, self.centerPos, False)
        print("Length of location list:", len(xLocationList))
        minXvalue, maxXvalue = (min(xLocationList), max(xLocationList))
        minYvalue, maxYvalue = (min(yLocationList), max(yLocationList))

        newStartX = round(self.centerPos[0] - (((minXvalue - self.centerPos[0]) + (maxXvalue - self.centerPos[0])) / 2), 3)
        newStartY = round(self.centerPos[1] - (((minYvalue - self.centerPos[1]) + (maxYvalue - self.centerPos[1])) / 2), 3)
        self.__drawBasicSpiro(spiroObject, self.turtleObject, (newStartX, newStartY), True)
        self.screen.tracer(True)

    def clearScreen(self):
        print("Called clear screen")
        self.turtleObject.clear()
        self.ghostTurtle.clear()
        pass

class Spirolateral():
    def __init__(self, name, timeTable, angle):
        self.name = name
        self.timeTable = timeTable
        self.angle = angle
        self.dRootList = self.genDrootList(self.timeTable)

    def genDrootList(self, timeTable):
        rootList = []
        x = 0
        while True:
            x += 1
            multiple = x * self.timeTable
            dRoot = (multiple - 1) % 9 + 1 if multiple else 0
            if dRoot in rootList:
                break
            else:
                rootList.append(dRoot)

        return(rootList)




#if __name__ == "__main__":
#    sc = Spirolateral("spiro1", 8, 90, "", (10,10) , 10)
#    sc.drawCenteredSpiro()
#    time.sleep(1)
