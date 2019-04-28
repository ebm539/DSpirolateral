import tkinter as tk
import turtle

root = tk.Tk()

#btn = tk.Button(root, text = "A button", bg = "black", fg = "black")
#btn.pack()
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()
t = turtle.RawTurtle(canvas)
