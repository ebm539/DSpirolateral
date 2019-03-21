import turtle

turtle1 = turtle.Turtle()
turtle1.speed(-1)

angle = 107
segments = 2
complete = False

startPosx, startPosy = turtle1.pos()
startPos = (startPosx, startPosy)

cycles = 0

while not complete:
    for distance in range(1, segments + 1):
        print(distance)
        turtle1.right(180 - angle)
        turtle1.forward(distance * 90)

    cycles += 1
        

    currentPosx, currentPosy = turtle1.pos()
    currentPos = (round(currentPosx, 3), round(currentPosy, 3))
    print("Current cycle", cycles)

    if currentPos == startPos:
        print("We're done here")
        complete = True
