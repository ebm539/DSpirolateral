# Import the standard turtle and time module
import turtle
import time

# Spirolateral drawer class:
# This class handles the drawing of spirolaterals by loading in a spirolateral object and drawing
# it in the gui


class SpirolateralDrawer():
    # Init method which is called whenever this is instantiated
    def __init__(self, screen, scale):
        # This screen is the turtle.screen object where the turtle graphics runs from
        self.screen = screen
        # This turtle object Is the visible turtle object which draws out spirolaterals as the user sees
        # In the gui. It is a raw turtle so it can be used in the tkinter application
        self.turtleObject = turtle.RawTurtle(self.screen)

        # Hide the visible turtle object's arrow
        self.turtleObject.hideturtle()

        # This turtle object is invisible. This is used to sketch out the spirolateral to be drawn
        # In an "invisible" line so that information can be gathered about the spirolateral's shape
        # which can be used to center it on screen
        self.ghostTurtle = turtle.RawTurtle(self.screen)
        # Hide the invisible turtle's arrow so it's not just a floating arrow
        self.ghostTurtle.hideturtle()

        # Set both turtle's speed to zero. This doesn't really affect the code, but it sets
        # The turtles to their fastest speed.
        self.ghostTurtle.speed(0)
        self.turtleObject.speed(0)

        # The position in the self.screen where the spirolaterals will be centered from
        self.centerPos = (0, 0)

        # The scale determines how large the spirolateral will be on screen
        self.scale = scale

        # This turtle object is simply going to be a circle placed in the center of each spirolateral.
        # This should not be moved.
        self.centerTurtle = turtle.RawTurtle(self.screen)
        # Set the shape of the center turtle
        self.centerTurtle.shape("circle")

        # Lift the pen on the center turtle so that when we place it to the
        # center pos it doesn't leave a line.
        self.centerTurtle.penup()
        self.centerTurtle.goto(self.centerPos)

    # This function is used to draw the spirolateral with either the ghost or main
    # Turtle object.
    # This is only used internally, so I've added the double _ in front of it
    # to imply privacy

    # Spiro object is the spirolateral object, turtleObject is the object used to draw the spiro
    # startPos is position (x,y) where the spiro needs to start and visible is a boolean of whether
    # or not the spirolateral is to be visible
    def __drawBasicSpiro(self, spiroObject, turtleObject, startPos, visible):
        # These lists keep track of the location of the turtle object as it travels across the screen
        xLocationList = []
        yLocationList = []

        # Lift up the pen of this turtle object so we can move it to the center
        # pos without leaving a trail
        turtleObject.penup()
        turtleObject.goto(startPos)

        # If this spirolateral is to be visible, place the pen down so that you can see
        # what it draws
        if visible:
            turtleObject.pendown()

        # Repeat the following loop until the spirolateral is finished
        while True:
            # For each number in the spiro object's digital root:
            for distance in spiroObject.dRootList:
                # Move the turtle object forward that distance multiplied by the scale
                turtleObject.forward(distance * self.scale)
                # Rotate the object right the angle stored in spirolateral
                turtleObject.right(spiroObject.angle)

            # Record the current location of turtle object using
            # The builtin pos method
            currentPosx, currentPosy = turtleObject.pos()
            # Round the co-ordinates to 3 decimal places. This is to ensure that
            # when the turtle object returns to it's start pos we can read that as
            # current pos == start pos. Python has a nasty habit of making 0.9999999999999999999999999999999999999999999999999
            # not equal to 1
            currentPosx = round(currentPosx, 3)
            currentPosy = round(currentPosy, 3)

            # Append this location to our location lists
            xLocationList.append(currentPosx)
            yLocationList.append(currentPosy)

            # If we have reached our start pos
            if currentPosx == startPos[0] and currentPosy == startPos[1]:
                # We have completed our spirolateral and need to break out of this loop
                break

        # Return our location lists
        return xLocationList, yLocationList

    # This is the method we call to load in a spiro object and draw it
    # onto the screen
    # spiroObject is the spiro object containing all of the data required to draw the spirolateral
    def loadSpiroObject(self, spiroObject):
        # Clean out the screen by running the clearScreen method to prepare the screen for a new spirolateral
        self.clearScreen()
        # Sets the tracer of the screen to false. This is to fully disable the animation of the turtle drawing
        # And makes the creation of these spirolaterals instant
        self.screen.tracer(False)

        # Draw a ghost spirolateral using the spiro object we've been given
        xLocationList, yLocationList = self.__drawBasicSpiro(
            spiroObject, self.ghostTurtle, self.centerPos, False)

        # Calculate the minimum and maximum x and y values in our location list
        minXvalue, maxXvalue = (min(xLocationList), max(xLocationList))
        minYvalue, maxYvalue = (min(yLocationList), max(yLocationList))

        # Generate an averagres for the min x and max x and the min y and max y
        # These can be subtracted from our current position so we now know where to
        # State the drawing of the spirolateral for it to be cenetered around self.centerPos
        newStartX = round(
            self.centerPos[0] - (((minXvalue - self.centerPos[0]) + (maxXvalue - self.centerPos[0])) / 2), 3)
        newStartY = round(
            self.centerPos[1] - (((minYvalue - self.centerPos[1]) + (maxYvalue - self.centerPos[1])) / 2), 3)

        # Draw the visible spirolateral using thespirolateral object and our corrected start position
        self.__drawBasicSpiro(spiroObject, self.turtleObject,
                              (newStartX, newStartY), True)
        # Turn on the screen tracer so the user can see what we've drawn
        self.screen.tracer(True)

    def loadRawValues(self, name, timeTable, angle):
        tempObject = Spirolateral(name, timeTable, angle)
        self.loadSpiroObject(tempObject)

    # Clear screen method
    # This clears the turtle screen of any existing spirolaterals
    def clearScreen(self):
        self.turtleObject.clear()
        self.ghostTurtle.clear()
        pass

# spirolateral class:
# This class erves as a container for the information required to draw a spirolateral
# It includes the spirolateral name, time table (int) and angle (int/float)


class Spirolateral():
    def __init__(self, name, timeTable, angle):
        self.name = name  # The name of this spirolateral
        self.timeTable = timeTable  # The timetable number used to draw this spirolateral
        # The angle that the turtle object will turn between distances in the drootlist
        self.angle = angle
        self.dRootList = self.genDrootList(self.timeTable)  # Digital root list

    # Gen rootlist:
    # This method generates a digital root list of the time table
    def genDrootList(self, timeTable):
        rootList = []  # Create the intermediary root list
        loop = 0  # Set the number of loops to zero
        while True:
            loop += 1  # Increment the loop number
            product = loop * self.timeTable  # Multiple the loop number to our multiple
            # Get the digital root of this product.
            # A digital root is the sum of each individual number of the product
            # If the sum is 10 or greater the process repeats until we have a single digit number
            dRoot = (product - 1) % 9 + 1 if product else 0
            # If the droot is already in our list
            if dRoot in rootList:
                # We can stop now, the pattern only repeats after this
                break
            else:
                # We haven't had this root appear yet, append it to our list
                rootList.append(dRoot)
        # Return our final digital root list
        return(rootList)


# if __name__ == "__main__":
#    sc = Spirolateral("spiro1", 8, 90, "", (10,10) , 10)
#    sc.drawCenteredSpiro()
#    time.sleep(1)
