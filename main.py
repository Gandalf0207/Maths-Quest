from tkinter import *
from tkinter import ttk

import labyrinthe
import custom_labyrinthe

def Gestion_Jouer(Lancement):
    #Nettoyage de la page
    Lancement.destroy()

    Jeu = Tk()


    #On crée la map 
    longueur = int(Label_Longueur_Map.get())
    largeur = int(Label_Largeur_Map.get())
    L = labyrinthe.mapmaker(longueur,largeur) 

    #On custom la map avec les pnj, portes et joueur....
    L = custom_labyrinthe.Custom_Map(L, longueur, largeur)


    #On load les img pour pouvoir les afficher
    Perso = PhotoImage(file="image/perso.png")
    Arbre = PhotoImage(file="image/okok.png")
    pnj1 = PhotoImage(file = "image/pnj1.png")
    porte = PhotoImage(file="image/porte.png")
    carre = PhotoImage(file="image/CARRE.png")


    #On affiche dans le terminal pour check
    for i in range(len(L)):
        print(*L[i], sep=" ")
        
    #Fonction qui gère le déplacement du personnage; MAJ de la map tkinter, les interractions avec les pnj
    def deplacement(event):
        
        global ordonne
        global abscisse

        touche = event.keysym
        check = ["■" , "pnj1" , "pnj2" ,"pnj3" ,"pnj4" , "\U0001F6AA"]

        if touche == "z":
            if ordonne-1 > 0 and L[ordonne-1][abscisse] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)
                ordonne-=1
                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")


        elif touche=="q" :
            if abscisse-1 >= 0 and L[ordonne][abscisse-1] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)
                abscisse-=1
                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")


        elif touche=="s" :
            if ordonne+1 < len(L) and L[ordonne+1][abscisse] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)
                ordonne+=1
                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")


        elif touche=="d" :
            if abscisse+1 < len(L[ordonne]) and L[ordonne][abscisse +1] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)
                abscisse+=1
                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")

        else:
            print("suite des fonctionnalités pas encore faites")

        print("Abscisse : ", abscisse)
        print("Ordonne : ", ordonne)

    global ordonne
    global abscisse

    abscisse = 0
    ordonne = 1
    


    long_c = len(L[0])*16
    larg_c = len(L)*16

    canvas = Canvas(Jeu, width=long_c, height=larg_c, bg= "white")

    #On affiche dans tkinter
    for x in range(len(L)):
        for y in range(len(L[x])):
            if L[x][y] == "■":
                canvas.create_image(16*y, 16*x, anchor=NW, image=Arbre)
            elif L[x][y] == "pnj1":
                canvas.create_image(16*y, 16*x, anchor=NW, image=pnj1)
            elif L[x][y] == "\U0001F6AA":
                canvas.create_image(16*y, 16*x, anchor=NW, image=porte)
    
    #On affiche le joueur
    L[1][0] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
    L[1][0] = "○"




    canvas.focus_set()
    canvas.bind("<KeyPress-z>", deplacement)
    canvas.bind("<KeyPress-q>", deplacement)
    canvas.bind("<KeyPress-s>", deplacement)
    canvas.bind("<KeyPress-d>", deplacement)

    canvas.pack()





    Jeu.mainloop()


    
    




    





##################################################################################################
#ACCUEIL#

Lancement = Tk()
Lancement.title("RPG : Lanncement  Théo | Quentin")

Lancement.geometry("350x400")

Frame = ttk.Frame(Lancement, bg = None)

Label_Longueur_Map = StringVar()
Label_Longueur_Map.set(45)
Lmap = Scale(Frame, variable=Label_Longueur_Map, orient=HORIZONTAL, from_=30, to=70).pack()

Label_Largeur_Map = StringVar()
Label_Largeur_Map.set(20)
lmap = Scale(Frame, variable=Label_Largeur_Map, from_=10, to=30).pack()

btn = ttk.Button(Frame, text="Jouer !",command=lambda:Gestion_Jouer(Lancement)).pack( pady=20)
Frame.pack()

Lancement.mainloop()
##################################################################################################






