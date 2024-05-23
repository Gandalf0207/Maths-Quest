import random
from math import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def choix_exo_niveau(Niveau,Label_Frame_Canvas_formule_exo):
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


            v1 = random.randint(-7,7)
            v2 = random.randint(-7,7)
            while v1 ==0 or v2== 0 or v1==v2 :
                v1 = random.randint(-7,7)
                v2 = random.randint(-7,7)
            resultat2 = resultat+v1
            resultat3 = resultat+v2


    elif Niveau ==1:
        eqt = "Aucune equation nécéssaire"

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
        
        L_valeurs  = [a, b, c, d, e, f, r]
        resultat = round(v_chateau,2)
        resultat2 = round((v_chateau + a),2)
        resultat3 = round((v_chateau - b),2)

    elif Niveau ==2:
        eqt = "Aucune equation nécéssaire"
        #Script provenat de stack overflow et adapté par nous
        def reload_function():
            XA = random.randint(-10,10)
            XB = random.randint(-10,10)
            XC = random.randint(-10,10)
            XD = random.randint(-10,10)

            YA = random.randint(-10,10)
            YB = random.randint(-10,10)
            YC = random.randint(-10,10)
            YD = random.randint(-10,10)

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



            return ([m1, round(p1,1), m2, round(p2,1), A, B, C, D])


        valeur = reload_function()

        # Label_Frame_Canvas_formule_exo.delete('all')


        # Formatage des résultats en chaînes de caractères
        resultat = f"Equation réduite de (AB) : {valeur[0]}x + {valeur[1]} \n Equation réduite de (CD) : {valeur[2]}x + {valeur[3]}"
        print(resultat)

        resultat2 =  f"Equation réduite de (AB) : {valeur[1]}x + {valeur[0]} \n Equation réduite de (CD) : {valeur[3]}x + {valeur[2]}"
        resultat3 =  f"Equation réduite de (AB) : {valeur[2]}x + {valeur[3]} \n Equation réduite de (CD) : {valeur[0]}x + {valeur[1]}"
        A = valeur[4]
        B = valeur[5]
        C = valeur[6]
        D = valeur[7]
        points = [A, B, C, D]

        # Créez un graphique Matplotlib
        fig, ax = plt.subplots()  # Ajoutez "ax" ici
        compteur_pts = 0
        l_pts = ["A","B","C","D"]
        for x, y in points:
            
            ax.scatter(x, y, color='blue', marker='o', label=f"({x}, {y})")
            ax.text(x, y, f"({x}, {y})", ha='center', va='bottom')  # Ajoutez l'étiquette
            ax.text(x, y-0.3, l_pts[compteur_pts], ha='center', va='top')
            compteur_pts+=1

        # Supprimez les axes
        ax.axis('off')  # Ajoutez cette ligne pour masquer les axes

        # Affichez le graphique dans le canvas Tkinter
        canvas_widget = FigureCanvasTkAgg(fig, master=Label_Frame_Canvas_formule_exo)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()


    elif Niveau ==3: 
        value_x = 0
        value_y = 0

        go = True
        while go == True:
            nb1 = random.randint(1,3)
            nb2 = random.randint(1,3)
            nb3 = random.randint(-50,50)
            nb4 = random.randint(1,3)
            nb5 = random.randint(1,3)
            nb6 = random.randint(-50,50)
            eqt = r"$\left\{ \begin{array}{lr} %sx + %sy & = %s \\ %sx - %sy & = %s \end{array} \right.$"%(nb1,nb2,nb3,nb4,nb5,nb6)
            for x in range(-50,50):
                for y in range(-50,50):
                    if x*nb1 + y*nb2 == nb3 and x*nb4 - nb5*y == nb6:
                        print(f"{nb1}x + {nb2}y = {nb3}")
                        print(f"{nb4}x - {nb5}y = {nb6}")
                        value_x = x
                        value_y = y
                        print(f"x = {x}, y = {y}")
                        go = False
                



        # Formatage des résultats en chaînes de caractères
        resultat = f"x = {value_x} | y = {value_y}"
        print(resultat)
        resultat2 = f"x = {value_x+nb1} | y = {value_y-nb2}"
        resultat3 = f"x = {value_x-nb4} | y = {value_y+nb5}"



        


    #On load tout les elements de réponse :  eqt / resultat vrai / les trois résultat dont 2 faux
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
        Liste_exo_all.append(L_valeurs)
    elif Niveau ==2:
        Liste_exo_all.append(points)



    return Liste_exo_all

