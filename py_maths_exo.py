import random
from math import *

 
def choix_exo_niveau(Niveau):
    def pgcd(a,b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a


    result_x = 0.1
    Liste_exo_corec = []

    while type(result_x ) != int:

        nb1 = random.randint(2,20)
        nb2 = random.randint(2,20)
        nb3 = random.randint(2,20)
        nb4 = random.randint(2,20)
        nb5 = random.randint(2,20)
        nb6 = random.randint(2,20)

        #Pour éviter des divisons par zéro est des éléments = à zéro
        if nb1 == nb4:
            while nb1 == nb4:
                nb4=random.randint(2,20)
        # if Niveau == 0 :
        #     print('bonjour')
        eqt = r"$ \Leftrightarrow %sx - %s = %s + %sx $" %(nb1, nb2, nb3, nb4)
        
        nb = nb2 + nb3
        nbx = nb1 - nb4

        if nbx != 1:
            pgcd_frac = pgcd(nb,nbx)
            nb = nb//pgcd_frac
            nbx = nbx//pgcd_frac
            if nbx!=1:
                result_x = nb/nbx
            else:
                result_x = nb
        else:
            result_x = nb
    
    
    
    Liste_exo_corec.append(eqt)
    Liste_exo_corec.append(result_x)
    print(Liste_exo_corec)

    return Liste_exo_corec

