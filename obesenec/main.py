import tkinter as tk
import math
import random
import requests
import sys

word_file = "/usr/share/dict/words"
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

def load_from_web(slova):
    response = requests.get(word_site)
    slova += response.content.splitlines()
#def load_from_file(slova):
#    try:
#        tmp_word_file = open(word_file).read()
#        slova += (tmp_word_file.splitlines())
#    except OSError as err:
#        print("Error when opening file", format(err))
#        print("Please wait")
#        load_from_web(slova)

def prepare(n,x,y,d,l,canvas):
    for i in range(n):
        posun = (d+l)*i
        canvas.create_line(x+posun,y,x+l+posun,y)

def vypis_pismenko(x,y,n,d,l,canvas,c):
    canvas.create_text(x+(d+l)*n,y,text=c,font='arial 15')


def kresli_obesenca(n,polohy,canvas):
    if n == 11:
        canvas.create_rectangle(polohy[0][0],polohy[0][1],polohy[0][2],polohy[0][3])
    if n == 6:
        canvas.create_oval(polohy[5][0],polohy[5][1],polohy[5][2],polohy[5][3])
    if (n != 11) & (n != 6):
        canvas.create_line(polohy[11-n][0],polohy[11-n][1],polohy[11-n][2],polohy[11-n][3])

def game(slova, canvas):
    splna = True
    while (splna):
        #hadane_slovo = slova[random.randrange(len(slova))]
        hadane_slovo = slova[random.randrange(len(slova))].decode('utf-8')
        if "'" not in hadane_slovo:
             splna = False


    hadane_slovo = hadane_slovo.lower()
    pocet_zivotov = 12
    uhadnute = []
    neuhadnute = []
    counter = len(hadane_slovo)
    dlzka_medzier = 10
    dlzka_ciary = 20
    prepare(len(hadane_slovo),200,650,dlzka_medzier,dlzka_ciary,canvas)

    while ((pocet_zivotov > 0) & (counter > 0)):
        c = input('Tipnite si pismenko: ')
        if c in hadane_slovo:
            if c not in uhadnute:
                print('Ano, je tam')
                uhadnute.append(c)
                counter -= hadane_slovo.count(c)
                for i in range(len(hadane_slovo)):
                    if hadane_slovo[i] == c:
                        vypis_pismenko(210,640,i,dlzka_medzier,dlzka_ciary,canvas,c)
            else:
                print('Toto si uz tipol')
        elif c in neuhadnute:
            print('Toto si uz tipol')
        elif c != '':
            pocet_zivotov -= 1
            kresli_obesenca(pocet_zivotov,suradnice,canvas)
            print('Smola, nie je tam')
            neuhadnute.append(c)

    if counter == 0:
        print("Uhadol si!!!")
        print(hadane_slovo)
        canvas.create_text(300,300,text='YOU WON',font='arial 50',fill='green')
    if pocet_zivotov == 0:
        print("GAME OVER")
        print(hadane_slovo)
        canvas.create_text(300,300,text='GAME OVER',font='arial 50',fill='red')

#mainloop
canvas = tk.Canvas(bg = 'white', width = 600, height = 800)
canvas.pack()

suradnice = [(150,500,250,550),(200,200,200,500),
(200,200,400,200),(200,250,250,200),(400,200,400,225),
(375,225,425,275),(400,275,400,300),(400,300,370,375),
(400,300,430,375),(400,300,400,400),(400,400,350,475),
(400,400,450,475)]

slova = []
load_from_web(slova)
game(slova, canvas)
while(True):
    d = input('Skusit znova?(Y/N)')
    if d == 'Y' or d == 'y':
        canvas.create_rectangle(0,0,600,800,fill = 'white')
        game(slova, canvas)
    else:
        sys.exit()
        break

canvas.mainloop()
