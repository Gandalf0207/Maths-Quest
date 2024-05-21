import random


def Custom_Map(Map, longueur, largeur, Niveau):

    if Niveau ==0 or Niveau ==5:
        L_pnj = ["pnj1","pnj2","pnj3"]
    elif Niveau ==1 or Niveau==6:
        L_pnj = ["pnj1","pnj2","pnj3", "pnj4"]
    elif Niveau ==2 or Niveau ==3 or Niveau ==7:
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