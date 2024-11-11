#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

#############################################################################################################################



# DEBUT py_maths_exo # 



# Importation des modules nécessaires
import random  # Module de l'aléatoire
from math import * # Module math

import matplotlib.pyplot as plt # Module de génération de figures mathématiques
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Elément spécifique du module pour générer la figure

#Fonction principal de gestion (appelée depuis le script principal)
def choix_exo_niveau(Niveau,Label_Frame_Canvas_formule_exo): # Paramètres niveau actuel, la box dans laquelle il faut afficher la figure si c'est nécéssaire
    
    # Petite fonction
    def pgcd(a,b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a

    # Set des valeurs initiales pour pouvoir rentrer dans la boucle
    resultat = 0.1
    result_y = 0.1
    Liste_exo_all = []

    if Niveau ==0:

        while type(resultat) != int: # conditon pour obtenir des valeurs entières

            nb1 = random.randint(2,20)
            nb2 = random.randint(2,20)
            nb3 = random.randint(2,20)
            nb4 = random.randint(2,20)
            #Pour éviter des divisons par zéro et des éléments = à zéro
            if nb1 == nb4:
                while nb1 == nb4:
                    nb4=random.randint(2,20)

            #equation latex qui sera ensuite affichée 
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


            v1 = random.randint(-7,7) # valeurs aléatoires
            v2 = random.randint(-7,7)
            while v1 ==0 or v2== 0 or v1==v2 :
                v1 = random.randint(-7,7)
                v2 = random.randint(-7,7)
            resultat2 = resultat+v1
            resultat3 = resultat+v2


    elif Niveau ==1:
        eqt = "Aucune equation nécéssaire" #Aucune équation est nécéssaire pour cette exercice

        # Génération + calcul des volumes
        a = random.randint(5,15)
        b = random.randint(25,50)
        c = b/4
        d = a + 3
        r = random.randint(4,8)
        f = r - 1.5
        h_cyl = random.randint(5,12)
        e = sqrt((r**2)+(h_cyl**2))
        while e != round(e,3) :
            a = random.randint(5,15)
            b = random.randint(25,50)
            c = b/4
            d = a + 3
            r = random.randint(4,8)
            f = r - 1.5
            h_cyl = random.randint(5,12)
            e = sqrt((r**2)+(h_cyl**2))

        b_cyl = pi*r*r
        v_cyl_1 = b_cyl*a
        v_cyl_2 = b_cyl*d
        v_gros_rectangle = b*f*a
        v_petit_rectangle = c*f*(d-a)
        v_cone = (b_cyl*h_cyl)/3

        v_chateau = v_gros_rectangle+v_petit_rectangle+v_cyl_1+v_cyl_2+(v_cone*2)
        
        L_valeurs  = [a, b, c, d, e, f, r] # on retourne les valeurs nécéssaires au joueur pour calculer
        resultat = round(v_chateau,2) # formatage des résultats
        resultat2 = round((v_chateau + a),2)
        resultat3 = round((v_chateau - b),2)

    elif Niveau ==2:
        eqt = "Aucune equation nécéssaire"
        # equation réduite de droite : génération des valeurs
        def reload_function():
            XA = random.randint(-10,10)
            XB = random.randint(-10,10)
            XC = random.randint(-10,10)
            XD = random.randint(-10,10)

            YA = random.randint(-10,10)
            YB = random.randint(-10,10)
            YC = random.randint(-10,10)
            YD = random.randint(-10,10)

            #calculs avec conditon pour éviter les erreurs, et obtenir des valeurs correctes (meme principe que le script du fichier py_maths_boss)
            m1 = 0.01
            while m1 != round(m1,1):
                XA = random.randint(-10,10)
                XB = random.randint(-10,10)
                YA = random.randint(-10,10)
                YB = random.randint(-10,10)

                A = (XA, YA) 
                B = (XB, YB) 

                if (XA != 0 and XB != 0 and XC != 0 and XD != 0 and YA != 0 and YB != 0 and YC != 0 and YD != 0) and (XB != XA and YB != YA):
                    m1 = (B[1]- A[1]) / (B[0] - A[0])
                p1 = A[1] - (m1*A[0]) 

            #calculs avec conditon pour éviter les erreurs, et obtenir des valeurs correctes (meme principe que le script du fichier py_maths_boss)
            m2 = 0.01
            while m2 != round(m2,1):

                XC = random.randint(-10,10)
                XD = random.randint(-10,10)
                YC = random.randint(-10,10)
                YD = random.randint(-10,10)

                C = (XC, YC)
                D = (XD, YD)

                if (XC != 0 and XD != 0 and XC != 0 and XD != 0 and YC != 0 and YD != 0 and YC != 0 and YD != 0) and (XD != XC and YD != YC):
                    m2 = (D[1]- C[1]) / (D[0] - C[0])
                p2 = C[1] - (m2*C[0]) 



            return ([m1, round(p1,1), m2, round(p2,1), A, B, C, D]) # Retour des valeurs pour les équations réduites + coordonnées


        valeur = reload_function() # Appel pour lancer la fonction



        # Formatage des résultats en chaînes de caractères
        resultat = f"Equation réduite de (AB) : {valeur[0]}x + {valeur[1]} \n Equation réduite de (CD) : {valeur[2]}x + {valeur[3]}"

        resultat2 =  f"Equation réduite de (AB) : {valeur[1]}x + {valeur[0]} \n Equation réduite de (CD) : {valeur[3]}x + {valeur[2]}"
        resultat3 =  f"Equation réduite de (AB) : {valeur[2]}x + {valeur[3]} \n Equation réduite de (CD) : {valeur[0]}x + {valeur[1]}"
        A = valeur[4] # Récupération des coordonnées
        B = valeur[5]
        C = valeur[6]
        D = valeur[7]
        points = [A, B, C, D]

        # Créer un graphique Matplotlib
        fig, ax = plt.subplots()
        compteur_pts = 0
        l_pts = ["A","B","C","D"]
        for x, y in points:
            
            ax.scatter(x, y, color='blue', marker='o', label=f"({x}, {y})")
            ax.text(x, y, f"({x}, {y})", ha='center', va='bottom')  # Ajouter l'étiquette
            ax.text(x, y-0.3, l_pts[compteur_pts], ha='center', va='top') # Ajout nom des points
            compteur_pts+=1

        # Supprimer les axes
        ax.axis('off')  # Ajouter cette ligne pour masquer les axes

        # Afficher le graphique dans le canvas Tkinter
        canvas_widget = FigureCanvasTkAgg(fig, master=Label_Frame_Canvas_formule_exo)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()


    elif Niveau ==3: 
        #Script pour les systèmes à 2 inconnues
        value_x = 0
        value_y = 0

        go = True
        while go == True:
            nb1 = random.randint(1,3) # Génération des valeurs aléatoirement
            nb2 = random.randint(1,3)
            nb3 = random.randint(-50,50)
            nb4 = random.randint(1,3)
            nb5 = random.randint(1,3)
            nb6 = random.randint(-50,50)
            eqt = r"$\left\{ \begin{array}{lr} %sx + %sy & = %s \\ %sx - %sy & = %s \end{array} \right.$"%(nb1,nb2,nb3,nb4,nb5,nb6) # equation en latex
            for x in range(-50,50): # modèle de brute force pour trouver un système et les valeurs possible pour les 2 équations
                for y in range(-50,50):
                    if x*nb1 + y*nb2 == nb3 and x*nb4 - nb5*y == nb6:

                        value_x = x
                        value_y = y
                        go = False
                



        # Formatage des résultats en chaînes de caractères
        resultat = f"x = {value_x} | y = {value_y}"
        resultat2 = f"x = {value_x+nb1} | y = {value_y-nb2}"
        resultat3 = f"x = {value_x-nb4} | y = {value_y+nb5}"


    elif Niveau == 5 :

        # Calcul de delta dans les polynômes
        x1 =0.001 # set des valeurs pour rentrer dans la boucle
        x2 = 0.001
        x_simple = 0.001
        good = True
        while good == True:

            nb1 = random.randint(-7,7) # Génération aléatoire des valeurs
            nb2 =random.randint(2,25)
            nb3 = random.randint(2,10)

            while nb1 ==0 or nb1 ==-1 or nb1==1: # on évite les valeurs non utilisables
                nb1 = random.randint(-15,15)

            eqt = r"$P(x) = %sx{^2} + %sx + %s$"%(nb1, nb2, nb3) # formule latex

            delta = nb2**2 - (4*nb1*nb3) # calcul delta

            #en fonction de la valeur de delta positif ou = 0, on détermine la valeur du / des résultat(s)
            if delta > 0:
                x1 = (-nb2 - sqrt(delta)) / (2*nb1)
                x2 = (-nb2 + sqrt(delta)) / (2*nb1)
                if (x1 == round(x1,1) or x1 == round(x1, 2)) and (x2 == round(x2,1) or x2 == round(x2, 2)):
                    good = False
            elif delta ==0:
                x_simple = (-nb2) / (2*nb1)
                if x_simple == round(x_simple, 1) or x_simple == round(x_simple,2):
                    good = False


        #formatage des résultats
        if delta > 0 :
            resultat = f"x1 = {x1} \nx2 = {x2}"
            resultat2 = f"x1 = {x2*3} \nx2 = {x1*2}"
            resultat3 = f"x1 = {x1+1} \nx2 = {x2}"
        elif delta ==0:
            resultat = f"x = {x_simple}"
            resultat2 = f"x = {x_simple*2}"
            resultat3 = f"x = {x_simple-nb1}"


    elif Niveau ==6:

        # exo sur les dérivées
        choix_derive = random.randint(1,2) # choix entre les deux formules possibles
        f_prime = 0.001 # set valeur pour rentrer dans la boucle

        while f_prime != round(f_prime,1) and f_prime != round(f_prime,2):
            num_resolve = random.randint(1,8) # génération des valeurs aléatoirement
            num1 = random.randint(1, 3)
            num2 = random.randint(-20, 20)
            num3 = random.randint(-20, 20)
            num4 = random.randint(2, 4)
            num5 = random.randint(3, 5)
            num6 = random.randint(3, 10)


            while num1 == 0 or num2 == 0 or num3==0 or num4 == 0 or num1==num6:
                num1 = random.randint(1,3)  # génération des valeurs aléatoirement
                num2 = random.randint(-20, 20)
                num3 = random.randint(-20, 20)
                num4 = random.randint(2, 4)
                num6 = random.randint(3, 10)

            if choix_derive == 1:
                #dérivée 1 
                eqt = r"$f(x) = x^{%s} + \frac{x^%s}{%sx} - %sx$"%(num5, num1, num4, num6)
                deriv1 = num5 * (num_resolve**(num5-1))
                u = num_resolve**num1
                u_prime = num1*(num_resolve**(num1-1))
                v = num4*num_resolve
                v_prime = num4

                deriv2 = ((u_prime*v) - (u*v_prime))/v**2
                deriv3 = num6
                f_prime = deriv1 + deriv2 - deriv3
        
            else:
                #dérivée 2
                eqt = r"$f(x) = \sqrt{x} + %sx - %sx^{%s}$"%( num5, num4, num1)

                deriv1 = (1) / (2*(sqrt(num_resolve)))
                deriv2 = num5
                deriv3 = num4*(num1*(num_resolve**(num1-1)))

                f_prime = deriv1 + deriv2 - deriv3


        # Formatage des résultats en chaînes de caractères
        resultat = f"f'({num_resolve}) = {f_prime}"
        resultat2 = f"f'({num_resolve}) = {f_prime+num1}"
        resultat3 = f"f'({num_resolve}) = {f_prime+num6}"

    elif Niveau ==7:

        #script generation des suites
        U0 = random.randint(-10,10)
        r = random.randint(-10,10)
        n = random.randint(4,15)

        while U0 == 0 or r == 0: #on évite les valeurs == 0
            U0 = random.randint(-10,10)
            r = random.randint(-10,10)

        if random.randint(0,1) == 0 : # suite SA
            U1 = U0 + r
            U2 = U1 + r
            eqt = "Aucune équation nécéssaire"
            somme_suite = (n/2)*(2*U0+(n-1)*r)
        else : #suite SG
            U1 = U0*r
            U2 = U0*(r**2)
            eqt = "Aucune équation nécéssaire"
            somme_suite = U0*((1-(r**n))/(1-r))


        infos_suite = [U0, U1, U2, n] #info comme les 3 premiers termes pour déterminer le type de suite  + le nombre de terme attendu pour la somme 

        # formatage des résultats 
        resultat = f"{somme_suite}"
        resultat2 = f"{somme_suite-1000}"
        resultat3 = f"{somme_suite+(U0*r**3)}"


        


    #On load tout les elements de réponse :  eqt / resultat vrai / les trois résultats dont 2 faux
    L_result_possible = []
    L_result_possible.append(resultat)
    L_result_possible.append(resultat2)
    L_result_possible.append(resultat3)

    #on mélange 
    random.shuffle(L_result_possible)
    btn1_value = L_result_possible[0]
    btn2_value = L_result_possible[1]
    btn3_value = L_result_possible[2]




    #on crée la liste finale
    Liste_exo_all.append(eqt)
    Liste_exo_all.append(resultat)
    Liste_exo_all.append(btn1_value)
    Liste_exo_all.append(btn2_value)
    Liste_exo_all.append(btn3_value)
    if Niveau ==1:
        Liste_exo_all.append(L_valeurs) #ajout des longueurs
    elif Niveau ==2:
        Liste_exo_all.append(points) # ajout des coordonnées
    elif Niveau==6:
        Liste_exo_all.append(num_resolve) # ajout valeur de x pour dériver et touver le résultat
    elif Niveau ==7:
        Liste_exo_all.append(infos_suite) # ajout des infos comme les "n" termes



    return Liste_exo_all # retour des éléments qui seront utilisés dans le fichier principal pour les exercices



# FIN  py_maths_exo # 



#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

#############################################################################################################################
