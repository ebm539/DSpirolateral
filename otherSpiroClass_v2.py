import turtle
import time

class Spirolateral():
    def __init__(self, name, timeTable, angle, screen, centerPos, scale):
        self.name = str(name)
        self.timeTable = int(timeTable)
        self.angle = int(angle)
        self.turtleObject = turtle.Turtle()
        self.turtleObject.hideturtle()
        self.ghostTurtle = turtle.Turtle()
        self.ghostTurtle.hideturtle()
        self.ghostTurtle.speed(0)
        self.turtleObject.speed(0)
        self.centerPos = centerPos
        self.scale = scale
        self.dRootList = self.genDrootList()

        self.centerTurtle = turtle.Turtle()
        self.centerTurtle.shape("circle")
        self.centerTurtle.penup()
        self.centerTurtle.goto(self.centerPos)

    def genDrootList(self):
        rootList = []
        x = 0
        while True:
            x += 1
            multiple = x * self.timeTable
            dRoot = (multiple - 1) % 9 + 1 #if multiple else 0
            if dRoot in rootList:
                break
            else:
                rootList.append(dRoot)

        return(rootList)

    def drawBasicSpiro(self, turtleObject, startPos, visible):
        print((self.dRootList))
        self.genDrootList()
        xLocationList = []
        yLocationList = []

        turtleObject.penup()
        turtleObject.goto(startPos)
        if visible:
            turtleObject.pendown()

        while True:
            for distance in self.dRootList:
                turtleObject.forward(distance * self.scale)
                turtleObject.right(self.angle)

            currentPosx, currentPosy = turtleObject.pos()
            currentPosx = round(currentPosx, 3)
            currentPosy = round(currentPosy, 3)
            print(currentPosx, currentPosy)

            xLocationList.append(currentPosx)
            yLocationList.append(currentPosy)

            xLocationList.append(currentPosx)
            if currentPosx == startPos[0] and currentPosy == startPos[1]:
                print("NANI?")
                break
            
        return xLocationList, yLocationList

    def drawCenteredSpiro(self):
        turtle.tracer(False)
        xLocationList, yLocationList = self.drawBasicSpiro(self.ghostTurtle, self.centerPos, False)
        turtle.tracer(True)
        minXvalue, maxXvalue = (min(xLocationList), max(xLocationList))
        minYvalue, maxYvalue = (min(yLocationList), max(yLocationList))

        newStartX = round(self.centerPos[0] - (((minXvalue - self.centerPos[0]) + (maxXvalue - self.centerPos[0])) / 2), 3)
        newStartY = round(self.centerPos[1] - (((minYvalue - self.centerPos[1]) + (maxYvalue - self.centerPos[1])) / 2), 3)
        turtle.tracer(False)
        self.drawBasicSpiro(self.turtleObject, (newStartX, newStartY), True)
        turtle.tracer(True)
        
        
        

if __name__ == "__main__":
    sc = Spirolateral("spiro1", 8, 90, "xyz", (10,10) , 10)
    sc.drawCenteredSpiro()
    time.sleep(1)
