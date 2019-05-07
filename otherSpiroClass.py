#Import the standard turtle and time module
import turtle
import time

class SpirolateralDrawer():
    def __init__(self, screen, scale):
        self.screen = screen
        self.turtleObject = turtle.RawTurtle(self.screen)
        self.turtleObject.hideturtle()
        self.ghostTurtle = turtle.RawTurtle(self.screen)
        self.ghostTurtle.hideturtle()
        self.ghostTurtle.speed(0)
        self.turtleObject.speed(0)
        self.centerPos = (0,0)
        self.scale = scale

        self.centerTurtle = turtle.RawTurtle(self.screen)
        self.centerTurtle.shape("circle")
        self.centerTurtle.penup()
        self.centerTurtle.goto(self.centerPos)

    def drawBasicSpiro(self, spiroObject, turtleObject, startPos, visible):
        xLocationList = []
        yLocationList = []

        turtleObject.penup()
        turtleObject.goto(startPos)
        if visible:
            turtleObject.pendown()

        while True:
            for distance in spiroObject.dRootList:
                turtleObject.forward(distance * self.scale)
                turtleObject.right(spiroObject.angle)

            currentPosx, currentPosy = turtleObject.pos()
            currentPosx = round(currentPosx, 3)
            currentPosy = round(currentPosy, 3)

            xLocationList.append(currentPosx)
            yLocationList.append(currentPosy)

            xLocationList.append(currentPosx)
            if currentPosx == startPos[0] and currentPosy == startPos[1]:
                break

        return xLocationList, yLocationList

    def loadSpiro(self, spiroObject):
        self.clearScreen()
        self.screen.tracer(False)
        xLocationList, yLocationList = self.drawBasicSpiro(spiroObject, self.ghostTurtle, self.centerPos, False)
        print("Length of location list:", len(xLocationList))
        minXvalue, maxXvalue = (min(xLocationList), max(xLocationList))
        minYvalue, maxYvalue = (min(yLocationList), max(yLocationList))

        newStartX = round(self.centerPos[0] - (((minXvalue - self.centerPos[0]) + (maxXvalue - self.centerPos[0])) / 2), 3)
        newStartY = round(self.centerPos[1] - (((minYvalue - self.centerPos[1]) + (maxYvalue - self.centerPos[1])) / 2), 3)
        self.drawBasicSpiro(spiroObject, self.turtleObject, (newStartX, newStartY), True)
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
