import tkinter as tk
import math
import random
import requests


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

canvas = tk.Canvas(bg = 'white', width = 800, height = 800)
canvas.pack()

suradnice = [(150,500,250,550),(200,200,200,500),
(200,200,400,200),(200,250,250,200),(400,200,400,225),
(375,225,425,275),(400,275,400,300),(400,300,370,375),
(400,300,430,375),(400,300,400,400),(400,400,350,475),
(400,400,450,475)]

#slova = ['jablcko','mrkvicka','melonik','ceresnicka','vortex']
word_file = "/usr/share/dict/words"
slova = open(word_file).read().splitlines()
#word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

#response = requests.get(word_site)
#slova = response.content.splitlines()

#response = urllib2.urlopen(word_site)
#txt = response.read()
#WORDS = txt.splitlines()

hadane_slovo = random.randrange(len(slova))
slova[hadane_slovo] = slova[hadane_slovo].lower()
pocet_zivotov = 12
uhadnute = []
counter = len(slova[hadane_slovo])
dlzka_medzier = 10
dlzka_ciary = 20
prepare(len(slova[hadane_slovo]),200,650,dlzka_medzier,dlzka_ciary,canvas)

while ((pocet_zivotov > 0) & (counter > 0)):
    c = input('Tipnite si pismenko: ')
    if c in slova[hadane_slovo]:
        if c not in uhadnute:
            print('Ano, je tam')
            uhadnute.append(c)
            counter -= slova[hadane_slovo].count(c)
            for i in range(len(slova[hadane_slovo])):
                if slova[hadane_slovo][i] == c:
                    vypis_pismenko(210,640,i,dlzka_medzier,dlzka_ciary,canvas,c)

        else:
            print('Toto si uz tipol')
    else:
        pocet_zivotov -= 1
        kresli_obesenca(pocet_zivotov,suradnice,canvas)
        print('Smola, nie je tam')

if counter == 0:
    print("Uhadol si!!!")
    print(slova[hadane_slovo])
    canvas.create_oval(200,200,600,600,fill='green')
if pocet_zivotov == 0:
    print("GAME OVER")
    print(slova[hadane_slovo])

canvas.mainloop()
