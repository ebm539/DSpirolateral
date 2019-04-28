import turtle
import time

class Spirolateral ():
    def __init__(self, name, segments, angle, screen, centerPos, scale):
        self.name = str(name)
        self.segments = int(segments)
        self.angle = int(angle)
        self.turtleObject = turtle.Turtle()
        self.turtleObject.hideturtle()
        self.ghostTurtle = turtle.Turtle()
        self.ghostTurtle.hideturtle()
        self.ghostTurtle.speed(-1)
        self.turtleObject.speed(-1)
        self.centerPos = centerPos
        self.scale = scale

        self.centerTurtle = turtle.Turtle()
        self.centerTurtle.shape("circle")
        self.centerTurtle.penup()
        self.centerTurtle.goto(self.centerPos)

    def drawBasicSpiro(self, turtleObject, startPos, visible):
        xLocationList = []
        yLocationList = []
        drawComplete = False
        turtleObject.penup()
        turtleObject.goto(startPos)
        if visible:
            turtleObject.pendown()
        startPosx, startPosy = turtleObject.pos()
        startPosx = round(startPosx, 3)
        startPosy = round(startPosy, 3)
        #startPos = (startPosx, startPosy)
        turtle.tracer(False)
        cycles = 0

        while not drawComplete:
            for distance in range(1, self.segments + 1):
                #print(distance)
                turtleObject.right(180 - self.angle)
                turtleObject.forward(distance * self.scale)

                cycles += 1


                currentPosx, currentPosy = turtleObject.pos()
                currentPosx = round(currentPosx, 3)
                currentPosy = round(currentPosy, 3)
                xLocationList.append(currentPosx)
                yLocationList.append(currentPosy)
                print("Current cycle", cycles)

                print("startPos: {0}, currentPos: {0}".format((currentPosx, currentPosy), (currentPosx, currentPosy)))

                if startPosx == currentPosx and startPosy == currentPosy:
                    print("We're done here")
                    turtle.tracer(True)
                    drawComplete = True

        return(xLocationList, yLocationList)

    def drawCenteredSpiro(self):
        xLocationList, yLocationList = self.drawBasicSpiro(self.ghostTurtle, (0,0), False)
        xMax = max(xLocationList)
        xMin = min(xLocationList)
        yMax = max(yLocationList)
        yMin = min(yLocationList)
        print("xMax {0}, xMin {1}, yMax {2}, yMin {3}".format(xMax, xMin, yMax, yMin))

        newStartX = self.centerPos[0] - ((xMax + xMin) / 2)
        newStartY = self.centerPos[1] - ((yMax + yMin) / 2)

        self.drawBasicSpiro(self.turtleObject, (newStartX, newStartY), True)




if __name__ == "__main__":
    sc = Spirolateral("spiro1", 5, 16, "xyz", (0,0), 50)
    sc.drawCenteredSpiro()
    time.sleep(999)
