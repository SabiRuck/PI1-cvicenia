import random,tkinter

n = 20

x = 50
y = 50
d = 10*n
height = n*10+2*x
width = n*10+2*y

color = "red"

canvas = tkinter.Canvas(height=height, width=width)
canvas.pack()

for i in range(n):
    if color == "red":
        color = "blue"
    elif color == "blue":
        color = "yellow"
    elif color == "yellow":
        color = "red"

    canvas.create_rectangle(x, y, x+d, y+d, fill=color)
    x = x+5
    y = y+5
    d = d-10







canvas.mainloop()
