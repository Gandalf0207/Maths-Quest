#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################



# DEBUT custom_labyrinthe # 



# Ce script permet de concevoir les position des éléments sur une carte donnée par le script principal.
# Il permet de positionner les personnages non-joueurs, portes, tables de fabrication... en fonction du Niveau actuel lors de la partie.

# Importation du module nécessaire
import random # Module de l'aléatoire


#Fonction principale de gestion (appelée depuis le script principal)
def Custom_Map(Map, longueur, largeur, Niveau): # Paramètres : La carte, les dimensions, et le Niveau

    # En fonction du niveau, le script sélectionne les bons éléments à rajouter
    if Niveau ==0 or Niveau ==5:
        L_pnj = ["pnj1","pnj2","pnj3"]
    elif Niveau ==1 or Niveau==6:
        L_pnj = ["pnj1","pnj2","pnj3", "pnj4"]
    elif Niveau ==2 or Niveau ==3 or Niveau ==7:
        L_pnj = ["pnj1","pnj2","pnj3", "pnj4", "pnj5"]
        

    # Si c'est un niveau 'boss' alors le script le définit et permet l'execution d'un élément autre. 
    checkboss = False
    if Niveau ==4 or Niveau ==8:
        checkboss = True


    if checkboss != True:
        # On place les pnjs de manière aléatoire dans des zones différentes
        comp = 0 # Définitions des zones par les maths
        for i in range(len(L_pnj)):
            comp +=1 
            if comp <=2:      
                x = random.randint(3,(largeur//2 -3)) # Détermination des coordonnées x  y
            else:
                x = random.randint((largeur//2 +2),largeur-3)

            if comp %2 ==1:
                y = random.randint(3,(longueur//2 -3))
            else:
                y = random.randint((longueur//2 +2),longueur-3)

            # Si jamais les coordonnées ne sont pas un mur / sont entre 4 murs donc inaccessibles. Les coordonnées sont rechoisies aléatoirment jusqu'à ce que la condition soit respectée pour passer à la suite
            # et Vérification de la progimité des pnjs autour pour éviter de retrouver 2 pnjs à côtés
            while Map[x][y] != "■" or (Map[x+1][y] == "■" and Map[x-1][y] == "■" and Map[x][y+1] == "■" and Map[x][y-1] == "■") or (Map[x+1][y] in L_pnj or Map[x+2][y] in L_pnj or Map[x-1][y] in L_pnj or Map[x-2][y] in L_pnj or Map[x][y+1] in L_pnj or Map[x][y+2] in L_pnj or Map[x][y-1] in L_pnj or Map[x][y-2] in L_pnj or Map[x-1][y-1] in L_pnj or Map[x+1][y-1] in L_pnj or Map[x-1][y+1] in L_pnj or Map[x+1][y+1] in L_pnj) :
                if comp <=2:      
                    x = random.randint(3,(largeur//2 -2)) # Nouvelle détermination des coordonnées x  y
                else:
                    x = random.randint((largeur//2 +2),largeur-3)

                if comp %2 ==1:
                    y = random.randint(3,(longueur//2 -2))
                else:
                    y = random.randint((longueur//2 +2),longueur-3)
                

            Map[x][y] = L_pnj[i] # Une fois les coordonnées déterminées, on affiche le pnj sur la carte 

        

        # On place la porte de sortie avec le meme principe que celui des pnjs
        new_largeur = largeur//2
        new_longueur = longueur//2
        x = random.randint(new_largeur,largeur-3) # Détermination des coordonnées x  y
        y = random.randint(new_longueur,longueur-3)
        

        # Si jamais les coordonnées ne sont pas un mur / sont entre 4 murs donc inaccessibles. Les coordonnées sont rechoisies aléatoirment jusqu'à ce que la condition soit respectée pour passer à la suite
        # et Vérification de la progimité des pnjs autour pour éviter de retrouver 2 pnjs à côtés
        while Map[x][y] != "■" or (Map[x+1][y] == "■" and Map[x-1][y] == "■" and Map[x][y+1] == "■" and Map[x][y-1] == "■") or (Map[x+1][y] in L_pnj or Map[x+2][y] in L_pnj or Map[x-1][y] in L_pnj or Map[x-2][y] in L_pnj or Map[x][y+1] in L_pnj or Map[x][y+2] in L_pnj or Map[x][y-1] in L_pnj or Map[x][y-2] in L_pnj or Map[x-1][y-1] in L_pnj or Map[x+1][y-1] in L_pnj or Map[x-1][y+1] in L_pnj or Map[x+1][y+1] in L_pnj) :
            x = random.randint(new_largeur,largeur-3)
            y = random.randint(new_longueur,longueur-3)

        Map[x][y] = "\U0001F6AA" # Une fois les coordonnées déterminées, on affiche la porte sur la carte

        #On place la table de fabrication
        Map[1][0] = "¤"


    else: # Si c'est un niveau 'boss', on remplace les elements centraux de la carte, par des éléments 'boss' pour pouvoir intéragir avec le fichier script principal
        for x in range(14,26): # Set de vide autour du boss
            for y in range(6,15):
                Map[y][x] = " "
        
        for x in range(16, 24): # Set des éléments boss
            for y in range(7,14):
                Map[y][x] = "boss"


    #On place le joueur
    Map[1][1] = "○"


    return Map # On donne la nouvelle carte au script principal pour qu'il puisse l'exploiter



# FIN custom_labyrinthe # 



#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################