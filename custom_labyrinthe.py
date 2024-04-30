import random


def Custom_Map(Map, longueur, largeur, Niveau):

    if Niveau ==0:
        L_pnj = ["pnj1","pnj2","pnj3"]
    elif Niveau ==1:
        L_pnj = ["pnj1","pnj2","pnj3", "pnj4"]


    # On place les pnj
    comp = 0
    for i in range(len(L_pnj)):
        comp +=1
        if comp <=2:      
            x = random.randint(1,(largeur//2 -2))
        else:
            x = random.randint((largeur//2 +2),largeur-2)

        if comp %2 ==1:
            y = random.randint(1,(longueur//2 -2))
        else:
            y = random.randint((longueur//2 +2),longueur-2)

        # si jamais les coordonnées ne sont pas un mur / le mur est entre 4murs donc inaccessible
        while Map[x][y] != "■" or (Map[x+1][y] == "■" and Map[x-1][y] == "■" and Map[x][y+1] == "■" and Map[x][y-1] == "■"):
            if comp <=2:      
                x = random.randint(1,(largeur//2 -2))
            else:
                x = random.randint((largeur//2 +2),largeur-2)

            if comp %2 ==1:
                y = random.randint(1,(longueur//2 -2))
            else:
                y = random.randint((longueur//2 +2),longueur-2)
        
        Map[x][y] = L_pnj[i]

    
    # On place la porte de sortie 
    new_largeur = largeur//2
    new_longueur = longueur//2
    x = random.randint(new_largeur,largeur-2)
    y = random.randint(new_longueur,longueur-2)
    
    while Map[x][y] != "■" or (Map[x+1][y] == "■" and Map[x-1][y] == "■" and Map[x][y+1] == "■" and Map[x][y-1] == "■"):
        x = random.randint(new_largeur,largeur-2)
        y = random.randint(new_longueur,longueur-2)

    Map[x][y] = "\U0001F6AA"

    #On place le joueur
    Map[1][1] = "○"

    #On place la table de craft
    Map[1][0] = "¤"


    return Map