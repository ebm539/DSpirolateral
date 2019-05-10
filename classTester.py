##Decided to seperate the spirolateral object from the parts that controlled the drawing of the spirolateral
###Signing test signing test2

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
sc = spiroModule.Spirolateral("one", 7, 45)
scd.loadSpiroObject(sc)

time.sleep(2)
sc2 = spiroModule.Spirolateral("two", 13, 26)
scd.loadSpiroObject(sc2)
time.sleep(2)
scd.loadRawValues("Thing", 3, 45)
time.sleep(2)
root.mainloop()
