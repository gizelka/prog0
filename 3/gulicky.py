import tkinter
import random

canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()

x0, y0 = 10, 10
s = 30
for y in range(y0, 250, s+2):
        for x in range(x0, 550, s+2):
                    r = random.randrange(256)
                            g = random.randrange(256)
                                    b = random.randrange(256)
                                            farba = f'#{r:02x}{g:02x}{b:02x}'
                                                    canvas.create_oval(x, y, x+s, y+s, fill=farba)
