import random
import labyrinthe
import os

from tkinter import *



max_grille = int(input("nb impaire sinon modif auto"))

if max_grille != 0000:

    affiche = int(input("Voulez-vous voir la formation du labyrinthe en temps réel (peux avoir des problème lors de la génération de trop grande map !) : Oui = 1 ; Non = 0"))
    temps = 0
    jeu = int(input("Jouer ou juste générer une map ? Oui = 1 | Non = 0"))
    if affiche == 1:
        temps= float(input("Temps entre chaque 'génération' en s : 500ms = 0.5"))

    L = []
    L = labyrinthe.generation(L, max_grille, affiche, temps)
    

else:
    max_grille = 12
    affiche = 0
    temps = 0
    jeu = 1
    L = []
    L = labyrinthe.generation(L, max_grille, affiche, temps)



if jeu == 0:
    #on affiche le labyrinthe
    for i in range(len(L)):
        print(*L[i], sep=" ")

else:

    abscisse = 0
    ordonne = 1
    L[-2][-1] = "\U0001F44D"

    Tk = Tk()
    canvas = Canvas(Tk,width=1200, height=1200)

    while L[-2][-1] != L[ordonne][abscisse] :

        photo_perso = PhotoImage(file="perso.png")
        L[ordonne][abscisse] = canvas.create_image(50*abscisse, 50*ordonne, anchor=NW, image=photo_perso)
        L[ordonne][abscisse] = "○"


        #on affiche le terminal tkinter
        photo = PhotoImage(file="newarbre3.png")
        for x in range(len(L)):
            for y in range(len(L[x])):
                if L[y][x] == "■":
                    canvas.create_image(50*x, 50*y, anchor=NW, image=photo)
        canvas.pack()

        #on affiche le labyrinthe terminal
        for i in range(len(L)):
            print(*L[i], sep=" ")



        déplacement = str(input("déplacement ? : "))
        clear = lambda: os.system('cls')
        clear()

        if déplacement.upper() == "Z" :
            L[ordonne][abscisse] = " "
            if ordonne-1 > 0 and L[ordonne-1][abscisse] != "■" :
                ordonne-=1
            else :
                print("C'est un mur !")


        elif déplacement.upper() =="Q" :
            L[ordonne][abscisse] = " "
            if abscisse-1 >= 0 and L[ordonne][abscisse-1] != "■" :
                abscisse-=1
            else :
                print("C'est un mur !")


        elif déplacement.upper() =="S" :
            L[ordonne][abscisse] = " "
            if ordonne+1 < len(L) and L[ordonne+1][abscisse] != "■" :
                ordonne+=1
            else :
                print("C'est un mur !")


        elif déplacement.upper() =="D" :
            L[ordonne][abscisse] = " "
            if abscisse+1 < len(L) and L[ordonne][abscisse +1] != "■" :
                abscisse+=1
            else :
                print("C'est un mur !")

        else :
            print("l'entrée est invalide")



    print("Vous avez trouvé le trésor")

    # conditions à revoir




Tk.mainloop()