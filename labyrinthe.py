import random
import os
import time
from math import *

def generation(L, max_grille,affiche,temps):

    if max_grille %2==0:
        max_grille +=1

    if L  ==  []:
        # generation de la map
        for hauteur in range(max_grille):
            l = []

            if hauteur%2 ==0:
                for longeur in range(max_grille):
                    l.append("■")
                L.append(l)
            else:
                for longeur in range(max_grille):
                    if longeur%2==0:
                        l.append("■")
                    else:
                        l.append(" ")
                L.append(l)


            # on setup les caractères aléatoirement dans les cases vide pour pouvoir générer le labyrinthe
        comp = 0
        for List_P in range(len(L)):
            for i in range(len(L[List_P])):
                if L[List_P][i] ==" ":
                    L[List_P][i] = chr(ord("0") + comp)
                    comp+=1


        go = True
            # on choisit aléatoirement un mur dans la map (ors côté) 
        while go==True:

            get_max_grille = max_grille

            comparateur_1 = -1
            comparateur_2 = -1
            for List_P in range(len(L)):
                for i in range(len(L[List_P])):
                    if L[List_P][i] !="■":
                        if comparateur_1 == -1:
                            comparateur_1 = L[List_P][i] 
                        elif L[List_P][i] != comparateur_1:
                            comparateur_2 = L[List_P][i]
            if comparateur_2 == -1:
                go = False



        # Choix des coordonné aléatoirement dans la map
            x = random.randint(1,max_grille-2)
            y = random.randint(1,get_max_grille-2)

            if L[x-1][y] != "■" and L[x+1][y] != "■":
                cell_1 = L[x-1][y]
                cell_2 = L[x+1][y]
            elif L[x][y-1] != "■" and L[x][y+1] != "■":
                cell_1 = L[x][y-1]
                cell_2 = L[x][y+1]
            else:
                continue  # Skip this iteration as we cannot compare a cell with a wall       # ce bout de code a été réalisé avec copilot et légèrement modifier par moi 


            # on les compare et on agit en fonction

            if cell_1 != cell_2:

                L[x][y] = cell_1
                i = 1
                while i < (get_max_grille-1):
                    j = 1
                    while j < (get_max_grille-1):
                        if (L[i][j]==cell_2):
                            L[i][j] = cell_1
                        j+=1
                    i+=1
                cell_1 = cell_1
            


            if affiche  == 1 : 
            #on affiche le labyrinthe en cours de formation
                for i in range(len(L)):
                    print(*L[i], sep=" ")

                time.sleep(temps)
                os.system('cls')



        #on remplace les cases de passage par des espace vides pour ue meilleur vision
        for clean1 in range(len(L)):
            for i in range(len(L[clean1])):
                if L[clean1][i] != "■":
                    L[clean1][i] = " "


        #on met les entrées et sorties
        L[1][0] = "○"
        L[-2][-1] = " "

        return L

    else:

        print("le code de listes déjà existance n'est pas encore fait")
