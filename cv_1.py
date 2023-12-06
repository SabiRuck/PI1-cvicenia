import tkinter
import random

w = 450
h = 785

canvas = tkinter.Canvas(width=w, height=h, bg="#54db48")
canvas.pack()

x = 10
y = 10
d = 25

count = (w-x)//(2*d+5)
count2 = (h-y)//(2*d+5)

print(count, count2)



for i in range(count2):
    for j in range(count):

        color = random.choice(("red", "purple", "pink", "blue"))
        canvas.create_oval(x, y, x + d, y + d, fill=color)
        canvas.create_oval(x, y + d, x + d, y + 2 * d, fill=color)
        canvas.create_oval(x + d, y, x + 2 * d, y + d, fill=color)
        canvas.create_oval(x + d, y + d, x + 2 * d, y + 2 * d, fill=color)
        canvas.create_oval(x + d // 2, y + d // 2, x + d + d // 2, y + d + d // 2, fill="yellow")
        x = x + 2*d+5
    y = y + 2*d+5
    x = x - (2*d+5)*count















canvas.mainloop()