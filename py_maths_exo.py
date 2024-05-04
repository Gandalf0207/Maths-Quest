import random
from math import *

 
def choix_exo_niveau(Niveau):
    def pgcd(a,b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a


    resultat = 0.1
    result_y = 0.1
    Liste_exo_all = []

    if Niveau ==0:

        while type(resultat) != int:

            nb1 = random.randint(2,20)
            nb2 = random.randint(2,20)
            nb3 = random.randint(2,20)
            nb4 = random.randint(2,20)
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
                    resultat = nb/nbx
                else:
                    resultat = nb
            else:
                resultat = nb
          

    elif Niveau ==1: # CODE DE GENERATION DE L'EXO, GENERE PAR IA POUR LE NV 2 (nv1 dans python)

        # Génération de valeurs aléatoires pour les coefficients du système
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = random.randint(1, 10)
        while (a*d - c*b) ==0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            d = random.randint(1, 10) 
        
        # Création des équations du système
        eq1_constant = random.randint(1, 100)
        eq2_constant = random.randint(1, 100)

        eqt = r"$\left\{ \begin{array}{lr} %sx + %sy & = %s \\ %sx - %sy & = %s \end{array} \right.$"%(a,b,c,d,eq1_constant,eq2_constant)
        determinant = (a*d - c*b)
        x_val_num, x_val_denom = eq1_constant * d - b * eq2_constant, determinant
        y_val_num, y_val_denom = a * eq2_constant - eq1_constant * c, determinant
        
        # Formatage des résultats en chaînes de caractères
        resultat = f"x = {x_val_num}/{x_val_denom} | y = {y_val_num}/{y_val_denom}"
        resultat2 = f"x = {x_val_num-1}/{x_val_denom+2} | y = {y_val_num+4}/{y_val_denom-3}"
        resultat3 = f"x = {x_val_num+1}/{x_val_denom-3} | y = {y_val_num-2}/{y_val_denom+4}"


        


    #On load tout les elements de réponse :  eqt / resultat vrai / les trois résultat dont 2 faux
    v1 = random.randint(-7,7)
    v2 = random.randint(-7,7)
    
    while v1 ==0 or v2== 0 or v1==v2 :
        v1 = random.randint(-7,7)
        v2 = random.randint(-7,7)

    L_result_possible = []
    if Niveau ==0:
        L_result_possible.append(resultat) 
        L_result_possible.append(resultat + v1)
        L_result_possible.append(resultat + v2)
    elif Niveau ==1:
        L_result_possible.append(resultat)
        L_result_possible.append(resultat2)
        L_result_possible.append(resultat3)
        
    random.shuffle(L_result_possible)
    btn1_value = L_result_possible[0]
    btn2_value = L_result_possible[1]
    btn3_value = L_result_possible[2]





    Liste_exo_all.append(eqt)
    Liste_exo_all.append(resultat)
    Liste_exo_all.append(btn1_value)
    Liste_exo_all.append(btn2_value)
    Liste_exo_all.append(btn3_value)



    return Liste_exo_all

