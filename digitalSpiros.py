import turtle

turtle1 = turtle.Turtle()

def genDigitalList(multiple):
    dRoots = []
    x = 0
    while True:
        x += 1
        num1 = x * multiple
        dRoot = (num1 - 1) % 9 + 1 if num1 else 0
        if dRoot in dRoots:
            break
        else:
            dRoots.append(dRoot)
        
            
    print(dRoots)
    

genDigitalList(5)
