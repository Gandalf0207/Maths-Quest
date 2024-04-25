import random


def Custom_Map(Map, longueur, largeur):

    Map[1][0] = "○"
    L_pnj = ["pnj1","pnj2","pnj3","pnj4"]

    # On place les personnages
    for i in range(4):      
        x = random.randint(1,largeur-2)
        y = random.randint(1,longueur-2)

        while Map[x][y] != "■":
            x = random.randint(1,largeur-2)
            y = random.randint(1,longueur-2)
        
        Map[x][y] = L_pnj[i]

    
    # On place la porte de sortie 
    new_largeur = largeur//2
    new_longueur = longueur//2
    x = random.randint(new_largeur,largeur-2)
    y = random.randint(new_longueur,longueur-2)
    
    while Map[x][y] != "■":
        x = random.randint(new_largeur,largeur-2)
        y = random.randint(new_longueur,longueur-2)

    Map[x][y] = "\U0001F6AA"


    return Map