import tkinter,random,time

n = 30

rr = 20
d = 40
height = 300
width = 300

canvas = tkinter.Canvas(height=height, width=width)
canvas.pack()

for i in range(n):

    x = random.randint(1, width-d)
    y = random.randint(1, height-d)
    text = random.randint(1, 9)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f"#{r:02x}{g:02x}{b:02x}"

    canvas.update()
    time.sleep(0.1)

    canvas.create_oval(x, y, x+d, y+d, fill=color)
    canvas.create_text(x+rr, y+rr, text=text, font='arial 30')




canvas.mainloop()
