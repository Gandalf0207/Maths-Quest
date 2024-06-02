#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

#############################################################################################################################



# DEBUT py_maths_boss # 



#Ce script permet la réalisation de calculs et la création de différents résultats qui seront nécéssaires pour les questions des niveaux 'boss' 

# Importation des modules nécessaires
import random # Module de l'aléatoire
from math import * # Module math

#Fonction principal de gestion (appelée depuis le script principal)
def choix_exo_niveau_boss(Niveau): # Paramètres : Niveau actuel


   if Niveau ==4: # Si le niveau ==4 : l'exo sera : calcul de points d'intersections et longueur des segments, avec des calculs de volumes

      #fonction de lancement / relancement si les calculs ne sont pas aux normes attendues
      def reload_function():
         XI = 0.0001 # Set des valeurs initiales pour pouvoir rentrer dans la boucle
         YI = 0.0001
         while XI != round(XI,1) or XI != round(XI, 2) or XI != round(XI, 3) or YI != round(YI,1) or YI != round(YI, 2) or YI != round(YI, 3): # Conditon : pas plus de 1 o 2 chiffres après la virgules

               # Calcul coef dirrecteur de l'équation réduite sous la forme mx + p
               m1 = 0.01 # Set valeur initiale pour rentrer dans la boucle
               while m1 != round(m1,1):
                  XA = random.randint(-10,10) # Création de valeurs aléatoires
                  XB = random.randint(-10,10)
                  YA = random.randint(-10,10)
                  YB = random.randint(-10,10)

                  A = (XA, YA) 
                  B = (XB, YB) 

                  if (XA != 0 and XB != 0 and YA != 0 and YB != 0 ) and (XB != XA and YB != YA):
                     m1 = (B[1]- A[1]) / (B[0] - A[0])
                  p1 = A[1] - (m1*A[0]) 

               # Calcul coef dirrecteur de l'équation réduite sous la forme mx + p
               m2 = 0.01 # Set valeur initiale pour rentrer dans la boucle
               while m2 != round(m2,1):

                  XC = random.randint(-10,10) # Création de valeurs aléatoires
                  XD = random.randint(-10,10)
                  YC = random.randint(-10,10)
                  YD = random.randint(-10,10)

                  C = (XC, YC)
                  D = (XD, YD)

                  if (XC != 0 and XD != 0 and YC != 0 and YD != 0)  and (XD != XC and YD != YC):
                     m2 = (D[1]- C[1]) / (D[0] - C[0])
                  p2 = C[1] - (m2*C[0]) 


               if m1 != m2: # Calcul des coordonnées du point d'intersection
                  nbx = m1 - m2
                  nb = -p1 + p2
                  XI = nb/nbx
                  YI = m1*XI + p1


         norme_AI = sqrt((XI - XA)**2 + (YI - YA)**2) # Calculs des longueurs des [AI] et [CI]
         norme_CI = sqrt((XI - XC)**2 + (YI - YC)**2)

         # Création de la permière partie des résultats en fonction des valeurs de calculs
         if norme_AI == norme_CI:
               intersection = "Les deux bateaux vont s'entrechoquer !"
         else:
               intersection = "Les deux bateaux ne vont pas s'entrechoquer !"


         # Bout de script pour le calcul du volumes des barrils
         largeur_barril = random.randint(25,80)
         longeur_barril = random.randint(55,140)

         while longeur_barril < largeur_barril:
               largeur_barril = random.randint(25,80)
               longeur_barril = random.randint(55,140)
         
         base = pi*(largeur_barril/2)**2
         volume = base*longeur_barril
         #conversion en litre, car les données sont en cm
         volume_L = volume/1000
         volume_L = volume_L*85
         volume_L = round(volume_L,2)
         


         return (intersection,volume_L,[A, B, C, D, longeur_barril, largeur_barril]) # On retourne s'il y a intersection, le volume en litre, les coordonnées de points et les dimensions des barils, qui serviront à l'utilisateurs pour faire ses calculs


      valeur = reload_function() # Chargement de la fonction principal 



      # Formatage des résultats en chaînes de caractères + création de fausses réponses pour le qcm

      # qcm 1 
      resultat = f"{valeur[0]}"

      if valeur[0] == "Les deux bateaux vont s'entrechoquer !":
         resultat2 =  "Les deux bateaux ne vont pas s'entrechoquer !"
      else:
         resultat2 =  "Les deux bateaux vont s'entrechoquer !"

      resultat3 = f"La trajectoire des bateau ne se croise jamais !"



      # qcm 2 
      resultat_2 = f"Le bateau b1 transporte un volume de {valeur[1]} L d'huile d'olive."

      fausse_valeur = random.randint (-150, 150)
      fausse_valeur2 = random.randint (-150, 150)
      while (-15 < fausse_valeur < 15) and( -15 < fausse_valeur < 15):
         fausse_valeur = random.randint (-150, 150)
         fausse_valeur2 = random.randint (-150, 150)

      resultat2_2 =  f"Le bateau b1 transporte un volume de {valeur[1] + fausse_valeur} L d'huile d'olive."

      resultat3_2 =  f"Le bateau b1 transporte un volume de {valeur[1]+fausse_valeur2} L d'huile d'olive."

      #Set des coordonnées de points pour pouvoir les renvoyer au fichier pricipal
      A = valeur[2][0]
      B = valeur[2][1]
      C = valeur[2][2]
      D = valeur[2][3]
      longueur_b = valeur[2][4]
      largeur_b = valeur[2][5]

      points=[A, B, C, D, longueur_b, largeur_b]



   #On load tout les éléments de réponse :  eqt / resultat vrai / les trois résultats dont 2 faux
   # qcm1
   L_result_possible_boss = []
   L_result_possible_boss.append(resultat)
   L_result_possible_boss.append(resultat2)
   L_result_possible_boss.append(resultat3)

   # qcm2
   L_result_possible_boss2 = []
   L_result_possible_boss2.append(resultat_2)
   L_result_possible_boss2.append(resultat2_2)
   L_result_possible_boss2.append(resultat3_2)
   
   #on mélange 
   # qcm1
   random.shuffle(L_result_possible_boss)
   btn1_value_boss = L_result_possible_boss[0]
   btn2_value_boss = L_result_possible_boss[1]
   btn3_value_boss = L_result_possible_boss[2]

   # qcm2
   random.shuffle(L_result_possible_boss2)
   btn1_value_boss_2 = L_result_possible_boss2[0]
   btn2_value_boss_2 = L_result_possible_boss2[1]
   btn3_value_boss_2 = L_result_possible_boss2[2]


   #on crée la liste finale
   Liste_exo_all_boss = []
   Liste_exo_all_boss.append(resultat) # vrai résultat toujours en 1er dans l'exo des boss
   Liste_exo_all_boss.append(resultat_2) # vrai résultat 2 toujours en 2e dans l'exo des boss
   Liste_exo_all_boss.append(btn1_value_boss)   # les valeurs mélangées pour les 2 qcm 
   Liste_exo_all_boss.append(btn2_value_boss)   # les valeurs mélangées pour les 2 qcm 
   Liste_exo_all_boss.append(btn3_value_boss)   # les valeurs mélangées pour les 2 qcm 
   Liste_exo_all_boss.append(btn1_value_boss_2) # les valeurs mélangées pour les 2 qcm
   Liste_exo_all_boss.append(btn2_value_boss_2) # les valeurs mélangées pour les 2 qcm
   Liste_exo_all_boss.append(btn3_value_boss_2) # les valeurs mélangées pour les 2 qcm
   if Niveau ==4:
      Liste_exo_all_boss.append(points) # la liste des coordonnées de points pour le niveau 4



   return Liste_exo_all_boss # On retourne cette liste avec toutes les informations nécéssaires à la création de l'exercices dans le fichier principal



# FIN py_maths_boss # 



#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

#############################################################################################################################
