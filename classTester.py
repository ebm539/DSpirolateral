import otherSpiroClass_v4 as spiroModule
import tkinter as tk
import time
import turtle

root = tk.Tk()
canvas = tk.Canvas()
canvas.grid()
btn1 = tk.Button(root, text="Help")
btn1.grid()

screen = turtle.TurtleScreen(canvas)

sc = spiroModule.Spirolateral("spiro1", 24, 45, screen, (25, -25), 10)
sc.drawCenteredSpiro()
time.sleep(2)
sc.clearScreen()
sc.timeTable = 7
sc.angle = 36
sc.drawCenteredSpiro()
root.mainloop()
