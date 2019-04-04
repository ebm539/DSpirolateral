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
        self.ghostTurtle.speed(-1)
        self.turtleObject.speed(-1)
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

            xLocationList.append(currentPosx)
            if currentPosx == startPos[0] and currentPosy == startPos[1]:
                print("NANI?")
                break

if __name__ == "__main__":
    sc = Spirolateral("spiro1", 7, 90, "xyz", (0,0), 10)
    sc.drawBasicSpiro(sc.turtleObject, sc.centerPos, True)
    time.sleep(9999)
