from tkinter import *
from tkinter import ttk

import labyrinthe
import custom_labyrinthe
import Tk_affiche_map

def Gestion_Jouer(Jeu):
    
    Jeu.geometry()
    Clear()
    Map = Generation_Map()
    Map = Custom_Map(Map)
    Affiche_Map(Map,Jeu)



def Clear():
    Frame.destroy()

def Generation_Map():
    longueur = int(Label_Longueur_Map.get())
    largeur = int(Label_Largeur_Map.get())

    Map = labyrinthe.mapmaker(longueur,largeur)
    return Map

def Custom_Map(L):
    #Faut finir de la custom la map mais y'a une base
    longueur = int(Label_Longueur_Map.get())
    largeur = int(Label_Largeur_Map.get())

    Map = custom_labyrinthe.Custom_Map(L, longueur, largeur)
    return(Map)

def Affiche_Map(L,Jeu):
    #On affiche dans le terminal pour check
    for i in range(len(L)):
        print(*L[i], sep=" ")

    #On affiche dans tkinter
    Tk_affiche_map.Affiche_Map(L,Jeu)



Jeu = Tk()
Jeu.geometry("350x400")
Jeu.title("RPG    Théo | Quentin")

Frame = ttk.Frame(Jeu, bg = None)

Label_Longueur_Map = StringVar()
Label_Longueur_Map.set(45)
Lmap = Scale(Frame, variable=Label_Longueur_Map, orient=HORIZONTAL, from_=30, to=70).pack()

Label_Largeur_Map = StringVar()
Label_Largeur_Map.set(20)
lmap = Scale(Frame, variable=Label_Largeur_Map, from_=10, to=30).pack()

btn = ttk.Button(Frame, text="Jouer !", command=lambda:Gestion_Jouer(Jeu)).pack( pady=20)





Frame.pack()
Jeu.mainloop()