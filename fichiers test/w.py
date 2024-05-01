from tkinter import *


def Gestion_Jouer(fenetre):
    fenetre.destroy()
    jeu = Tk()

    # Création du cadre global pour le jeu
    Label_Frame_Global = Frame(jeu, width=300, height=300, relief=GROOVE,bg="#000000")
    Label_Frame_Global.pack(fill="both")

    # Partie Gauche :
    Label_Frame_Jeu_Inv = Frame(Label_Frame_Global, width=150, height=300, bg="#000000", relief=GROOVE)
    Label_Frame_Jeu_Inv.pack(side='left', fill="y")

    # Création d'une étiquette dans la frame de gauche
    L = Label(Label_Frame_Jeu_Inv, text="bonjour", fg="white", relief=GROOVE)
    L.pack(side=TOP)  # Ajustement de l'étiquette à la taille de la frame

    jeu.mainloop()


Lancement = Tk()

Frame_y = Frame(Lancement, bg="black", width=150, height=145, relief=GROOVE)

btn = Button(Frame_y, text="Jouer !", command=lambda: Gestion_Jouer(Lancement))
btn.pack(pady=20)
Frame_y.pack()

Lancement.mainloop()
