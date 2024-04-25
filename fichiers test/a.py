from tkinter import *

fenetre = Tk()


def clavier(event):
    touche = event.keysym
    print(touche)
canvas = Canvas(fenetre, width=500, height=500)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()


fenetre.mainloop()