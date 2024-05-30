import random
from math import *

eqt = "Aucune equation nécéssaire"

for i in range(100):
    #Script provenat de stack overflow et adapté par nous
    def reload_function():
        XI = 0.0001
        YI = 0.0001
        while XI != round(XI,1) or XI != round(XI, 2) or XI != round(XI, 3) or YI != round(YI,1) or YI != round(YI, 2) or YI != round(YI, 3):

            m1 = 0.01
            while m1 != round(m1,1):
                XA = random.randint(-10,10)
                XB = random.randint(-10,10)
                YA = random.randint(-10,10)
                YB = random.randint(-10,10)

                A = (XA, YA) 
                B = (XB, YB) 

                if (XA != 0 and XB != 0 and YA != 0 and YB != 0 ) and (XB != XA and YB != YA):
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

                if (XC != 0 and XD != 0 and YC != 0 and YD != 0)  and (XD != XC and YD != YC):
                    m2 = (D[1]- C[1]) / (D[0] - C[0])
                p2 = C[1] - (m2*C[0]) 


            if m1 != m2:
                nbx = m1 - m2
                nb = -p1 + p2
                XI = nb/nbx
                YI = m1*XI + p1


        print (XI, YI)

        norme_AI = sqrt((XI - XA)**2 + (YI - YA)**2)
        norme_CI = sqrt((XI - XC)**2 + (YI - YC)**2)

        if norme_AI == norme_CI:
            intersection = "Les deux bateaux vont s'entrechoquer ! "
        else:
            intersection = "Les deux bateaux ne vont pas s'entrechoquer ! "


        largeur_barril = random.randint(25,80)
        longeur_barril = random.randint(55,140)

        while longeur_barril < largeur_barril:
            largeur_barril = random.randint(25,80)
            longeur_barril = random.randint(55,140)
        
        base = pi*(largeur_barril/2)**2
        volume = base*longeur_barril
        volume_L = round(volume/1000, 2)
        


        return (intersection,volume_L[A, B, C, D])


    valeur = reload_function()



    # Formatage des résultats en chaînes de caractères
    resultat = f"{valeur[0]} Le bateau b1 transporte un volume de {valeur[1]} L d'huile d'olive."
    print(resultat)

    fausse_valeur = random.randint (-150, 150)
    while -15 < fausse_valeur < 15:
        fausse_valeur = random.randint (-150, 150)
    resultat2 =  f"{valeur[0]} Le bateau b1 transporte un volume de {valeur[1] + fausse_valeur} L d'huile d'olive."

    if valeur[0] == "Les deux bateaux vont s'entrechoquer ! ":
        resultat3 =  f"Les deux bateaux ne vont pas s'entrechoquer ! Le bateau b1 transporte un volume de {valeur[1]} L d'huile d'olive."
    else:
        resultat3 =  f"Les deux bateaux vont s'entrechoquer ! Le bateau b1 transporte un volume de {valeur[1]} L d'huile d'olive."


    A = valeur[2][0]
    B = valeur[2][1]
    C = valeur[2][2]
    D = valeur[2][3]