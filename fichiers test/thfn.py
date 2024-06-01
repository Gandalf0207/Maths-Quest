from tkinter import *

def ac():
        intt.set(0)

def acc():
    inttt.set(0)

# Initialiser la fenêtre principale
j = Tk()

# Définir les variables pour les Checkbuttons
intt = IntVar()
inttt = IntVar()

# Créer les Checkbuttons et lier la variable et la commande
b = Checkbutton(j, text="aaa", variable=intt, command=acc)
b.pack()

c = Checkbutton(j, text="bbb", variable=inttt, command=ac)
c.pack()

# Lancer la boucle principale de l'interface graphique
j.mainloop()
