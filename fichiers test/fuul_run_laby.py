import random
import time
def mapmaker(longueur, largeur):

    if longueur %2==0:
        longueur +=1

    if largeur %2==0:
        largeur+=1


    L = []
    # generation de la map
    for haut in range(largeur):
        l = []

        if haut%2 ==0:
            for long in range(longueur):
                l.append("■")
            L.append(l)
        else:
            for long in range(longueur):
                if long%2==0:
                    l.append("■")
                else:
                    l.append(" ")
            L.append(l)


    # on setup les caractères aléatoirement (ASCII) dans les cases vide pour pouvoir générer le labyrinthe
    comp = 0
    for x in range(len(L)):
        for y in range(len(L[x])):
            if L[x][y] ==" ":
                L[x][y] = chr(ord("0") + comp)
                comp+=1


    go = True
    # on choisit aléatoirement un mur dans la map (ors côté) 
    while go==True:

        comparateur_1 = -1
        comparateur_2 = -1
        for x in range(len(L)):
            for y in range(len(L[x])):
                if L[x][y] !="■":
                    if comparateur_1 == -1:
                        comparateur_1 = L[x][y] 
                    elif L[x][y] != comparateur_1:
                        comparateur_2 = L[x][y]
        if comparateur_2 == -1:
            go = False



    # Choix des coordonné aléatoirement dans la map
        x = random.randint(1,largeur-2)
        y = random.randint(1,longueur-2)

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
            while i < (largeur-1):
                j = 1
                while j < (longueur-1):
                    if (L[i][j]==cell_2):
                        L[i][j] = cell_1
                    j+=1
                i+=1
            cell_1 = cell_1


    #on remplace les cases de passage par des espace vides pour ue meilleur vision
    for x in range(len(L)):
        for y in range(len(L[x])):
            if L[x][y] != "■":
                L[x][y] = " "

    return L

def Custom_Map(Map, longueur, largeur, Niveau):

    if Niveau ==0 or Niveau ==5:
        L_pnj = ["pnj1","pnj2","pnj3"]
    elif Niveau ==1 or Niveau ==3 or Niveau==6:
        L_pnj = ["pnj1","pnj2","pnj3", "pnj4"]
    elif Niveau ==2 or Niveau ==7:
        L_pnj = ["pnj1","pnj2","pnj3", "pnj4", "pnj5"]
        

    checkboss = False
    if Niveau ==4 or Niveau ==8:
        checkboss = True

    if checkboss != True:
        # On place les pnj
        comp = 0
        for i in range(len(L_pnj)):
            comp +=1
            if comp <=2:      
                x = random.randint(3,(largeur//2 -3))
            else:
                x = random.randint((largeur//2 +2),largeur-3)

            if comp %2 ==1:
                y = random.randint(3,(longueur//2 -3))
            else:
                y = random.randint((longueur//2 +2),longueur-3)

            print( x, y )
            # si jamais les coordonnées ne sont pas un mur / le mur est entre 4murs donc inaccessible
            while Map[x][y] != "■" or (Map[x+1][y] == "■" and Map[x-1][y] == "■" and Map[x][y+1] == "■" and Map[x][y-1] == "■") or (Map[x+1][y] in L_pnj or Map[x+2][y] in L_pnj or Map[x-1][y] in L_pnj or Map[x-2][y] in L_pnj or Map[x][y+1] in L_pnj or Map[x][y+2] in L_pnj or Map[x][y-1] in L_pnj or Map[x][y-2] in L_pnj or Map[x-1][y-1] in L_pnj or Map[x+1][y-1] in L_pnj or Map[x-1][y+1] in L_pnj or Map[x+1][y+1] in L_pnj) :
                if comp <=2:      
                    x = random.randint(3,(largeur//2 -2))
                else:
                    x = random.randint((largeur//2 +2),largeur-3)

                if comp %2 ==1:
                    y = random.randint(3,(longueur//2 -2))
                else:
                    y = random.randint((longueur//2 +2),longueur-3)
                
                print( x, y )

            Map[x][y] = L_pnj[i]

        
        # On place la porte de sortie 
        new_largeur = largeur//2
        new_longueur = longueur//2
        x = random.randint(new_largeur,largeur-3)
        y = random.randint(new_longueur,longueur-3)
        
        while Map[x][y] != "■" or (Map[x+1][y] == "■" and Map[x-1][y] == "■" and Map[x][y+1] == "■" and Map[x][y-1] == "■") or (Map[x+1][y] in L_pnj or Map[x+2][y] in L_pnj or Map[x-1][y] in L_pnj or Map[x-2][y] in L_pnj or Map[x][y+1] in L_pnj or Map[x][y+2] in L_pnj or Map[x][y-1] in L_pnj or Map[x][y-2] in L_pnj or Map[x-1][y-1] in L_pnj or Map[x+1][y-1] in L_pnj or Map[x-1][y+1] in L_pnj or Map[x+1][y+1] in L_pnj) :
            x = random.randint(new_largeur,largeur-3)
            y = random.randint(new_longueur,longueur-3)

        Map[x][y] = "\U0001F6AA"

        #On place la table de craft
        Map[1][0] = "¤"


    else:
        for x in range(14,26):
            for y in range(6,15):
                Map[y][x] = " "
        
        for x in range(16, 24):
            for y in range(7,14):
                Map[y][x] = "boss"


    #On place le joueur
    Map[1][1] = "○"


    return Map


Niveau = 0
#On crée la map 
longueur = 38
largeur = 21
aaa = 0
while aaa != 10000:

    L = mapmaker(longueur,largeur) 

    #On custom la map avec les pnj, portes et joueur....
    L = Custom_Map(L, longueur, largeur, Niveau)
    #On affiche dans le terminal pour check
    for i in range(len(L)):
        print(*L[i], sep=" ")
    
    aaa+=1
    