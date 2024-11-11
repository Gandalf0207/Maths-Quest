#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################



# DEBUT labyrinthe # 



# Ce script permet de générer une carte aléatoirement à chaque demande duscript princiapl
# Ce script est inspiré d'un algorinthe "Fusion aléatoire de chemins"

# Importation du module nécessaire
import random # Module de l'aléatoire

#Fonction principal de gestion (appelé depuis le script principal)
def mapmaker(longueur, largeur): # Paramètres : Dimensions de la carte

    if longueur %2==0: # Set du cadrillage de base
        longueur +=1

    if largeur %2==0: # Set du cadrillage de base
        largeur+=1


    L = []
    # Generation de la map
    for haut in range(largeur): # Création de la matrice dans la liste 
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


    # On setup les caractères aléatoirement (ASCII) dans les cases vide pour pouvoir générer le labyrinthe
    comp = 0
    for x in range(len(L)):
        for y in range(len(L[x])):
            if L[x][y] ==" ":
                L[x][y] = chr(ord("0") + comp)
                comp+=1


    go = True
    # on choisit aléatoirement un mur dans la map (ors côté) 
    while go==True:

        #check de s'il reste des cases non trouvé / non accessible par le joueur
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



    # Choix des coordonnés aléatoirement dans la map
        x = random.randint(1,largeur-2)
        y = random.randint(1,longueur-2)

        if L[x-1][y] != "■" and L[x+1][y] != "■":
            cell_1 = L[x-1][y]
            cell_2 = L[x+1][y]
        elif L[x][y-1] != "■" and L[x][y+1] != "■":
            cell_1 = L[x][y-1]
            cell_2 = L[x][y+1]
        else:
            continue 


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


    #on remplace les cases de passage par des espace vides pour une meilleur vision
    for x in range(len(L)):
        for y in range(len(L[x])):
            if L[x][y] != "■":
                L[x][y] = " "

    return L # On retourne la carte généré aléatoirement, vide 



# FIN labyrinthe #



#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################