#!/bin/python3.6
import random
import tkinter as tk

#initial values
text = "Monty Python"
canvas_width = 666
canvas_height = 666
bg_colour = 'white'
# Create canvas
canvas = tk.Canvas(bg = bg_colour, width = canvas_width, height = canvas_height)
canvas.pack()

font_size = 0
font_colors = ['red','blue','green','yellow','black']
fonts = ['Copper Black', 'Brush Script MT', 'Courier New']

# main for
for i in range(5):
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    farba = f'#{r:02x}{g:02x}{b:02x}'
    font_size = random.randrange(canvas_width // 10)    # preistotu celosiselne delenie ak by nahodou niekto specifikoval canvas_width ako float (=100.0)
    #x = random.randrange(canvas_width-len(text)*font_size)
    x = random.randrange(500)
    y = random.randrange(500)

    canvas.create_text(x,y,text = text, fill = 'blue', font = (fonts[0],40))

# mainloop event, thus app can stay openth
canvas.mainloop()
