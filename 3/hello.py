import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_text(190, 130, text='Python', font='arial 40')
canvas.create_text(40, 130, text='vlavo')
canvas.create_text(340, 130, text='vpravo')
canvas.create_text(190, 50, text='hore')
canvas.create_text(190, 210, text='dole')

canvas.mainloop() #important, otherwise the app exits right after opening
