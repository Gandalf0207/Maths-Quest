from tkinter import *
from tkinter import ttk


def Affiche_Map(L,Jeu):

    

    abscisse = 0
    ordonne = 1

    Perso = PhotoImage(file="perso.png")
    Arbre = PhotoImage(file="arbre.png")
    pnj1 = PhotoImage(file = "pnj1.png")
    # pnj2 = PhotoImage(file = "")
    # pnj3 = PhotoImage(file = "")
    # pnj4 = PhotoImage(file = "")
    porte = PhotoImage(file="porte.png")
    carre = PhotoImage(file="CARRE.png")

    canvas = Canvas(Jeu, width=len(L[0])*16, height=len(L)*16)

    for x in range(len(L)):
        print('ok')
        for y in range(len(L[x])):
            if L[x][y] == "■":
                canvas.create_image(16*y, 16*x, anchor=NW, image=Arbre)
            elif L[x][y] == "pnj1":
                canvas.create_image(16*y, 16*x, anchor=NW, image=pnj1)
            elif L[x][y] == "\U0001F6AA":
                canvas.create_image(16*y, 16*x, anchor=NW, image=porte)

    L[1][0] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
    L[1][0] = "○"
    
    # def deplacement(event):
    #     touche = event.keysym

    #     if touche == "z":
    #         L[ordonne][abscisse] = " "
    #         L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)
    #         if ordonne-1 > 0 and L[ordonne-1][abscisse] != "■" :
    #             ordonne-=1
    #         else :
    #             print("C'est un mur !")

    # canvas.bind("<KeyPress-z>", deplacement)

    canvas.pack()




       






    

            


    #     elif déplacement.upper() =="Q" :
    #         L[ordonne][abscisse] = " "
    #         if abscisse-1 >= 0 and L[ordonne][abscisse-1] != "■" :
    #             abscisse-=1
    #         else :
    #             print("C'est un mur !")


    #     elif déplacement.upper() =="S" :
    #         L[ordonne][abscisse] = " "
    #         if ordonne+1 < len(L) and L[ordonne+1][abscisse] != "■" :
    #             ordonne+=1
    #         else :
    #             print("C'est un mur !")


    #     elif déplacement.upper() =="D" :
    #         L[ordonne][abscisse] = " "
    #         if abscisse+1 < len(L) and L[ordonne][abscisse +1] != "■" :
    #             abscisse+=1
    #         else :
    #             print("C'est un mur !")

    #     else :
    #         print("l'entrée est invalide")



    # print("Vous avez trouvé le trésor")

