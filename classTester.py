##Decided to seperate the spirolateral object from the parts that controlled the drawing of the spirolateral

import otherSpiroClass as spiroModule
import tkinter as tk
import time
import turtle

root = tk.Tk()
canvas = tk.Canvas()
canvas.grid()
btn1 = tk.Button(root, text="Help")
btn1.grid()

screen = turtle.TurtleScreen(canvas)

scd = spiroModule.SpirolateralDrawer(screen, 10)
sc = spiroModule.Spirolateral(7, 45)
scd.loadSpiro(sc)

time.sleep(2)
sc2 = spiroModule.Spirolateral(13, 26)
scd.loadSpiro(sc2)
root.mainloop()
6
