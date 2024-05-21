### EN FONCTION DU NIVEAU IL FAUT SET UP LA GENERATION / CUSTOM / TEXT DES PNJ ET ITEMS ###

from tkinter import *
from tkinter import ttk
import random
import time 

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


import labyrinthe
import custom_labyrinthe
import py_maths_exo
import py_maths_boss

plt.rcParams['text.usetex'] = True


### Pour avoir une certaine sécurité lors de la récupération des fragements de clé; il a fallut faire en sorte
# de ne pourvoir ouvrir qu'une seule fenetre à la fois pour eviter de donner plus de fragments de clé que prévus
# nous avons donc utilisé l'ia pour apprendre et comprendre comment fonctionne le protocole utilisé... ###

### C'est pourquoi il est possible de voir des commentaires : #code ia
# Cela signifie que cette partie du code n'a pas été réalisée uniquement par nous meme....
global Label_btn_suivant_discussion_pnj
Label_btn_suivant_discussion_pnj = None

# Variable pour suivre l'état de la deuxième fenêtre pour les problèmes de la porte
global second_window_probleme
second_window_probleme= None

global boss_window
boss_window= None

# Valeurs permettant de déterminer le nombre d'indices utilisé et de pouvoir afficher le résultats
global indices_give_1
global indices_give_2
indices_give_1 = 0
indices_give_2 = 0

def Gestion_Jouer(fenetre, Niveau, type_partie):

    global Label_btn_suivant_discussion_pnj
    Label_btn_suivant_discussion_pnj = None

    # Variable pour suivre l'état de la deuxième fenêtre pour les problèmes de la porte
    global second_window_probleme
    second_window_probleme= None

    global boss_window
    boss_window= None




    #le "fenetre" correspond à la fenetre tk qui est en cours de loop
    # Le permir passage se sera la fenetre 'Lancement', puis les autres tours se sera les fenetres de 'Jeu'
    # Ce fonctionnement permet de faire tourner le programme pour le nombre de niveaux disponible !
    fenetre.destroy()


    Jeu = Tk()
    if type_partie =='all':
        tours = 9
    elif type_partie =='seconde':
        tours = 5
    elif type_partie == 'premiere':
        tours = 9

    if Niveau < tours:
        #On crée la map 
        longueur = 38
        largeur = 21
        L = labyrinthe.mapmaker(longueur,largeur) 

        #On custom la map avec les pnj, portes et joueur....
        L = custom_labyrinthe.Custom_Map(L, longueur, largeur, Niveau)


        #On load les img pour pouvoir les afficher

        porte = PhotoImage(file="image/porte.png")
        porte_moyen = PhotoImage(file="image/porte.png")
        carre = PhotoImage(file="image/CARRE.png")
        craft_table_ = PhotoImage(file="image/craft.png")

        Perso = PhotoImage(file="image/perso.png")
        idee = PhotoImage(file="image/idee.png")

        Volume_nv1 = PhotoImage(file="image/volume.png")

        #en fonction du niveau, on choisit les murs / les pnjs

        if Niveau ==0 or Niveau ==5:
                Grande_cle = PhotoImage(file="image/Cle_1_repare.png")

                loot_vide_pnj1 = PhotoImage(file="image/clepnj1_.png")
                loot_vide_pnj2 = PhotoImage(file="image/clepnj2_.png")
                loot_vide_pnj3 = PhotoImage(file="image/clepnj3_.png")

                loot_pnj1 = PhotoImage(file="image/clepnj1.png")
                loot_pnj2 = PhotoImage(file="image/clepnj2.png")
                loot_pnj3 = PhotoImage(file="image/clepnj3.png")

        elif Niveau == 1 or Niveau==6:
                Grande_cle = PhotoImage(file="image/Cle_2_repare.png")

                loot_vide_pnj1 = PhotoImage(file="image/clepnj1_.png")
                loot_vide_pnj2 = PhotoImage(file="image/clepnj2_.png")
                loot_vide_pnj3 = PhotoImage(file="image/clepnj3_.png")
                loot_vide_pnj4 = PhotoImage(file="image/Glue_Ombre.png")

                loot_pnj1 = PhotoImage(file="image/clepnj1.png")
                loot_pnj2 = PhotoImage(file="image/clepnj2.png")
                loot_pnj3 = PhotoImage(file="image/clepnj3.png")
                loot_pnj4 = PhotoImage(file="image/Glue.png")

        elif Niveau ==2 or Niveau ==3 or Niveau ==7:
                Grande_cle = PhotoImage(file="image/Cle_3_repare.png")

                loot_vide_pnj1 = PhotoImage(file="image/clepnj1_.png")
                loot_vide_pnj2 = PhotoImage(file="image/clepnj2_.png")
                loot_vide_pnj3 = PhotoImage(file="image/clepnj3_.png")
                loot_vide_pnj4 = PhotoImage(file="image/Glue_Ombre.png")
                loot_vide_pnj5 = PhotoImage(file="image/Kit_de_nettoyage_ombre.png")

                loot_pnj1 = PhotoImage(file="image/clepnj1-.png")
                loot_pnj2 = PhotoImage(file="image/clepnj2-.png")
                loot_pnj3 = PhotoImage(file="image/clepnj3-.png")
                loot_pnj4 = PhotoImage(file="image/Glue.png")
                loot_pnj5 = PhotoImage(file="image/Kit_de_nettoyage.png")


        #exo 1 et 5 : 1er degré + 2nd degré 
        if Niveau ==0 or Niveau == 5:
            mur1 = PhotoImage(file="image/Water.png")
            mur2 = PhotoImage(file="image/Water_rock.png")
            mur3 = PhotoImage(file="image/Water_Lotus.png")

            pnj1 = PhotoImage(file = "image/pnj1.png")
            pnj2 = PhotoImage(file = "image/Iggy.png")
            pnj3 = PhotoImage(file = "image/pnj3.png")

            pnj1_moyen = PhotoImage(file="image/sorcier1.png")
            pnj2_moyen = PhotoImage(file="image/sorcier2.png")
            pnj3_moyen = PhotoImage(file="image/sorcier3.png")

            pnj1_grand = PhotoImage(file="image/sorcier1.png")
            pnj2_grand = PhotoImage(file="image/sorcier2.png")
            pnj3_grand = PhotoImage(file="image/sorcier3.png")

        #exo 2 et 6 : volume + Derivation
        elif Niveau ==1 or Niveau ==6:
            mur1 = PhotoImage(file="image/Water.png")
            mur2 = PhotoImage(file="image/Water_rock.png")
            mur3 = PhotoImage(file="image/Water_Lotus.png")

            pnj1 = PhotoImage(file = "image/pnj1.png")
            pnj2 = PhotoImage(file = "image/pnj2.png")
            pnj3 = PhotoImage(file = "image/Marchand_de_glace.png")
            pnj4 = PhotoImage(file = "image/pnj2.png")

            pnj1_moyen = PhotoImage(file="image/sorcier1.png")
            pnj2_moyen = PhotoImage(file="image/sorcier2.png")
            pnj3_moyen = PhotoImage(file="image/sorcier3.png")
            pnj4_moyen = PhotoImage(file="image/sorcier4.png")

            pnj1_grand = PhotoImage(file="image/sorcier1.png")
            pnj2_grand = PhotoImage(file="image/sorcier2.png")
            pnj3_grand = PhotoImage(file="image/sorcier3.png")
            pnj4_grand = PhotoImage(file="image/sorcier4.png")


        # exo 3 et 7: fonction affiche tangente pente + Suite
        elif Niveau ==2 or Niveau ==3 or Niveau==7:
            mur1 = PhotoImage(file="image/Wall1.png")
            mur2 = PhotoImage(file="image/Wall2.png")
            mur3 = PhotoImage(file="image/Wall3.png")

            pnj1 = PhotoImage(file = "image/pnj1.png")
            pnj2 = PhotoImage(file = "image/pnj2.png")
            pnj3 = PhotoImage(file = "image/pnj3.png")
            pnj4 = PhotoImage(file = "image/pnj2.png")
            pnj5 = PhotoImage(file = "image/pnj2.png")

            pnj1_moyen = PhotoImage(file="image/sorcier1.png")
            pnj2_moyen = PhotoImage(file="image/sorcier2.png")
            pnj3_moyen = PhotoImage(file="image/sorcier3.png")
            pnj4_moyen = PhotoImage(file="image/sorcier4.png")
            pnj5_moyen = PhotoImage(file = "image/pnj2.png")

            pnj1_grand = PhotoImage(file="image/sorcier1.png")
            pnj2_grand = PhotoImage(file="image/sorcier2.png")
            pnj3_grand = PhotoImage(file="image/sorcier3.png")
            pnj4_grand = PhotoImage(file="image/sorcier4.png")
            pnj5_grand = PhotoImage(file = "image/pnj2.png")


        #les deux niveaux de boss
        elif Niveau==4 or Niveau ==8:
            mur1 = PhotoImage(file="image/Wall_red.png")
            mur2 = PhotoImage(file="image/Wall_red_with_symbols.png")
            mur3 = PhotoImage(file="image/Wall_red_flower.png")

            pnj_boss = PhotoImage(file = "image/pnj2.png")
            pnj_boss_moyen = PhotoImage(file = "image/pnj2.png")
            pnj_boss_grand = PhotoImage(file = "image/BOSS.png")





        #On affiche dans le terminal pour check
        for i in range(len(L)):
            print(*L[i], sep=" ")
        
        #Fonction qui gère le déplacement du personnage; MAJ de la map tkinter, les interractions avec les pnj
        def deplacement(event):
            
            global ordonne
            global abscisse

            touche = event.keysym
            check = ["■" ,"\U0001F6AA", "¤", "boss"]
            pnj_liste = ["pnj1", "pnj2", "pnj3", "pnj4", "pnj5"]


            if touche == "Up":
                if ordonne-1 > 0 and L[ordonne-1][abscisse] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne-1][abscisse] in pnj_liste) and (L[ordonne-2][abscisse] not in check) and (L[ordonne-2][abscisse] not in pnj_liste):
                        ordonne-=2
                    elif L[ordonne-1][abscisse] in pnj_liste :
                        print("C'est un PNJ")
                    else:
                        ordonne-=1
                    
                    L[ordonne][abscisse] = "○"
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                else :
                    print("C'est un mur !")


            elif touche=="Left" :
                if abscisse-1 > 0 and L[ordonne][abscisse-1] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne][abscisse-1] in pnj_liste) and (L[ordonne][abscisse-2] not in check ) and (L[ordonne][abscisse-2] not in pnj_liste):
                        abscisse-=2
                    elif L[ordonne][abscisse-1] in pnj_liste :
                        print("C'est un PNJ")
                    else:
                        abscisse-=1

                    L[ordonne][abscisse] = "○"
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                else :
                    print("C'est un mur !")


            elif touche=="Down" :
                if ordonne+1 < len(L) and L[ordonne+1][abscisse] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne+1][abscisse] in pnj_liste) and (L[ordonne+2][abscisse] not in check) and (L[ordonne+2][abscisse] not in pnj_liste):
                        ordonne+=2
                    elif L[ordonne+1][abscisse] in pnj_liste :
                        print("C'est un PNJ")
                    else:
                        ordonne+=1

                    L[ordonne][abscisse] = "○"
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                else :
                    print("C'est un mur !")


            elif touche=="Right" :
                if abscisse+1 < len(L[ordonne]) and L[ordonne][abscisse +1] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne][abscisse+1] in pnj_liste) and (L[ordonne][abscisse+2] not in check) and (L[ordonne][abscisse+2] not in pnj_liste):
                        abscisse+=2
                    elif L[ordonne][abscisse+1] in pnj_liste :
                        print("C'est un PNJ")
                    else:
                        abscisse+=1

                    L[ordonne][abscisse] = "○"
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)

                else :
                    print("C'est un mur !")


            print("Abscisse : ", abscisse)
            print("Ordonne : ", ordonne)

            canvas_infos_possibilite_discussion.delete('all')

            #verif si table de craft dispo et si oui on affiche le msg d'information
            if L[ordonne][abscisse-1] == "¤":
                Label_text_possibilite_strvar.set("Appuie sur 'C' pour assembler la grande Clé !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=craft_table_)

            #check si c'est la porte et on met à jour les infos dans le cadre e bas à gauche
            elif (L[ordonne-1][abscisse] == "\U0001F6AA" or L[ordonne+1][abscisse]== "\U0001F6AA" or L[ordonne][abscisse-1]== "\U0001F6AA" or L[ordonne][abscisse+1]== "\U0001F6AA"):
                Label_text_possibilite_strvar.set("Appuie sur 'espace' pour ouvrir la porte !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=porte_moyen)

            #check de si on parle au boss ou non :
            elif (L[ordonne-1][abscisse] == "boss" or L[ordonne+1][abscisse]== "boss" or L[ordonne][abscisse-1]== "boss" or L[ordonne][abscisse+1]== "boss"):
                Label_text_possibilite_strvar.set("Appuie sur 'espace' pour m'affronter !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj_boss_moyen)

            #Script permettant d'afficher si une discution est possible avec les pnj ou non
            elif (L[ordonne-1][abscisse] in pnj_liste or L[ordonne+1][abscisse] in pnj_liste or L[ordonne][abscisse-1] in pnj_liste or L[ordonne][abscisse+1] in pnj_liste):
                #PNJ 1
                if (L[ordonne-1][abscisse] == pnj_liste[0] or L[ordonne+1][abscisse]== pnj_liste[0] or L[ordonne][abscisse-1]== pnj_liste[0] or L[ordonne][abscisse+1]== pnj_liste[0]):
                    Label_text_possibilite_strvar.set("Appuie sur 'espace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj1)

                #PNJ 2
                elif (L[ordonne-1][abscisse] == pnj_liste[1] or L[ordonne+1][abscisse]== pnj_liste[1] or L[ordonne][abscisse-1]== pnj_liste[1] or L[ordonne][abscisse+1]== pnj_liste[1]):
                    Label_text_possibilite_strvar.set("Appuie sur 'espace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj2)

                #PNJ3
                elif (L[ordonne-1][abscisse] == pnj_liste[2] or L[ordonne+1][abscisse]== pnj_liste[2] or L[ordonne][abscisse-1]== pnj_liste[2] or L[ordonne][abscisse+1]== pnj_liste[2]):
                    Label_text_possibilite_strvar.set("Appuie sur 'espace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj3)

                #PNJ4
                elif (L[ordonne-1][abscisse] == pnj_liste[3] or L[ordonne+1][abscisse]== pnj_liste[3] or L[ordonne][abscisse-1]== pnj_liste[3] or L[ordonne][abscisse+1]== pnj_liste[3]):
                    Label_text_possibilite_strvar.set("Appuie sur 'escpace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj4)

                #PNJ5
                elif (L[ordonne-1][abscisse] == pnj_liste[4] or L[ordonne+1][abscisse]== pnj_liste[4] or L[ordonne][abscisse-1]== pnj_liste[4] or L[ordonne][abscisse+1]== pnj_liste[4]):
                    Label_text_possibilite_strvar.set("Appuie sur 'escpace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj5)

            else:

                if Niveau ==0 or Niveau ==5:
                    if pnj1_infos == False or pnj2_infos == False or pnj3_infos == False:
                        Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés !")
                    elif assemble_cle == False:
                        Label_text_possibilite_strvar.set("Objectif : Assembler la clé à la table de fabrication !")
                    elif assemble_cle == True:
                        Label_text_possibilite_strvar.set("Objectif : Ouvrir la porte !")
                elif Niveau ==1 or Niveau==6:
                    if pnj1_infos == False or pnj2_infos == False or pnj3_infos == False or pnj3_infos == False:
                        Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés et le tube de colle !")
                    elif assemble_cle == False:
                        Label_text_possibilite_strvar.set("Objectif : Assembler la clé à la table de fabrication !")
                    elif assemble_cle == True:
                        Label_text_possibilite_strvar.set("Objectif : Ouvrir la porte !")
                elif Niveau ==2 or Niveau ==3 or Niveau ==7:
                    if pnj1_infos == False or pnj2_infos == False or pnj3_infos == False or pnj3_infos == False and pnj5_infos == False:
                        Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés, le tube de colle et le kit de nettoyage !")
                    elif assemble_cle == False:
                        Label_text_possibilite_strvar.set("Objectif : Assembler la clé à la table de fabrication !")
                    elif assemble_cle == True:
                        Label_text_possibilite_strvar.set("Objectif : Ouvrir la porte !")
                elif Niveau ==4 or Niveau==8:
                        Label_text_possibilite_strvar.set("Objectif : Affronter le BOSS")


                canvas_infos_possibilite_discussion.delete('all')
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image = idee)

                #on clear si jamais la personne s'en va
                canvas_tete_pnj_grand.delete("all")
                Label_texte_parole_discussion_pnj_strvar.set("")
                #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
                if Label_btn_suivant_discussion_pnj is not None:
                    if Label_btn_suivant_discussion_pnj.winfo_exists():
                        Label_btn_suivant_discussion_pnj.destroy()
                c = 0




        #Fonction de MAJ et affichage de l'inventaire du joueur ### pas terminé , manque les crafts possible !
        def load_inv(Niveau):
            global pnj1_infos
            global pnj2_infos
            global pnj3_infos
            global pnj4_infos
            global pnj5_infos

            global assemble_cle

            if assemble_cle == True:
                canvas_inv.delete("all")
                canvas_inv.config(width = 150, height = 50)
                canvas_inv.create_image(0,0, anchor = NW, image=Grande_cle)

            else:
                if pnj1_infos == False and pnj2_infos == False and pnj3_infos == False and pnj4_infos == False and pnj5_infos == False:
                    
                    if Niveau !=4 and Niveau!=8:
                        canvas_inv.create_image(0,0, anchor = NW, image=loot_vide_pnj1)
                        canvas_inv.create_image(50,0, anchor = NW, image=loot_vide_pnj2)
                        canvas_inv.create_image(100,0, anchor = NW, image=loot_vide_pnj3)
                        if Niveau == 1 or Niveau ==6:
                            canvas_inv.create_image(150,0, anchor = NW, image=loot_vide_pnj4)
                        elif Niveau ==2 or Niveau ==3 or Niveau ==7:
                            canvas_inv.create_image(150,0, anchor = NW, image=loot_vide_pnj4)
                            canvas_inv.create_image(200,0, anchor = NW, image=loot_vide_pnj5)


                if pnj1_infos == True:
                    canvas_inv.create_image(0,0, anchor = NW, image=loot_pnj1)

                if pnj2_infos == True:
                    canvas_inv.create_image(50,0, anchor = NW, image=loot_pnj2)

                if pnj3_infos == True:
                    canvas_inv.create_image(100,0, anchor = NW, image=loot_pnj3)
                
                if pnj4_infos == True:
                    canvas_inv.create_image(150,0, anchor = NW, image=loot_pnj4)

                if pnj5_infos == True:
                    canvas_inv.create_image(200,0, anchor = NW, image=loot_pnj5)

        def load_cours(Niveau, num_pnj):
            Liste_cours = [
            "Lors de la résolution d’une équation du 1er degré il faut respecter l’égalité comme pour l’équilibre d’une balance \u2696 si on enlève un poids on le fait des 2 côtés.",
            "Si une équation possède des x des 2 côtés de l’égalité il faut tous les faire passer d’un seul côté. Exemple : 3x + 2 = 5x + 3 devient 3x + 2 - 3x = 5x + 2 - 3x il suffit ensuite d’une résolution classique.",
            "Dans une équation il faut annuler les étapes ainsi la soustraction s’oppose à l’addition et la division à la multiplication. Exemple de résolution d’équation : 3x + 2 = 5 devient 3x + 2 - 2 = 5 - 2 puis 3x/3 = 3/3 donc x = 1.", 
            
            "La formule de l’aire de la base d’un disque qui est π x rayon².",
            "Le volume du cylindre est base x hauteur soit π x rayon² x h.",
            "Le volume du cône est celui du cylindre divisé par 3 soit (π x rayon² x h)/3.",
            "La formule pour le parallélépipède rectangle est largeur x hauteur x longueur, le cube en est un cas particulier tous sont égaux.",
            
            "cours 1 nv3",
            "cours 2 nv3",
            "cours 3 nv3",
            "cours 4 nv3",
            "cours 5 nv3",

            "cours 1 nv4",
            "cours 2 nv4",
            "cours 3 nv4",
            "cours 4 nv4",
            "cours 5 nv4", 



            "cours 1 nv5",
            "cours 2 nv5",
            "cours 3 nv5",

            "cours 1 nv6",
            "cours 2 nv6",
            "cours 3 nv6",
            "cours 4 nv6", 
            
            "cours 1 nv7",
            "cours 2 nv7",
            "cours 3 nv7",
            "cours 4 nv7",
            "cours 5 nv7",
    
            ]

            def ajouter_element(Texte): #Une partie de la gestion du code de la liste box provient d'internet
                global listbox
                element = Texte.strip()
                listbox.config(state=NORMAL)
                if element:
                    listbox.insert(END, element + "\n")
                listbox.insert(END, "\n")                

            #partie load du premier chargement
            if num_pnj ==0 or num_pnj==1:

                if num_pnj==0:
                    global listbox
                    listbox = Text(Label_Frame_Cours_Affiche, width =35,wrap="word",bg=None)
                    listbox.pack(side=LEFT, fill=BOTH)

                    scrollbar = Scrollbar(Label_Frame_Cours_Affiche, orient=VERTICAL, command=listbox.yview)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    listbox.config(yscrollcommand=scrollbar.set)
                    listbox.config(state=DISABLED)

                elif num_pnj==1:
                    listbox.config(state=NORMAL)
                    listbox.delete(1.0,END)
                    listbox.config(state=DISABLED)



                #chargement pour le reload de la fonction global quand on change de niveau
                #pour eviterd'ecrire à deux fois le meme code de 200 ligne; des optimisation sont faite 
                #ces optimisations consistent en conditions  : 
                #    - pour reload au changement de niveau
                #    - pour reload et mettre en ordre le cours au moment de passer la porte
                listbox.config(state=NORMAL)

                if (Niveau ==0 and num_pnj==0):
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")

                elif (Niveau ==1 and num_pnj==0) or (Niveau==0 and num_pnj==1):
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")

                    for i in range(3):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    if num_pnj==0:
                        listbox.insert(END, "--Volume--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau ==2 and num_pnj==0) or (Niveau== 1 and num_pnj==1):
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(3):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Volume--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(3,7):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    if num_pnj==0:
                        listbox.insert(END, "--Fonction Affine--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau ==3 and num_pnj==0) or (Niveau== 2 and num_pnj==1):
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(3):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Volume--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(3,7):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Fonction Affine--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(7,12):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    if num_pnj==0:
                        listbox.insert(END, "--Equation à 2 inconnues--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau ==4 and num_pnj==0) or (Niveau== 3 and num_pnj==1):
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(3):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Volume--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(3,7):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Fonction Affine--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(7,12):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Equation à 2 inconnues--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(12,16):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")



                elif (Niveau ==5 and num_pnj==0):
                    listbox.insert(END, "--Equation du second degré--" + "\n")
                    listbox.insert(END, "\n")

                elif (Niveau ==6 and num_pnj==0) or (Niveau== 5 and num_pnj==1):
                    listbox.insert(END, "--Equation du second degré--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(16,19):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    if num_pnj==0:
                        listbox.insert(END, "--Dérivation--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau==7 and num_pnj==0) or (Niveau== 6 and num_pnj==1):
                    listbox.insert(END, "--Equation du second degré--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(16,19):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Dérivation--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(19,23):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    if num_pnj==0:
                        listbox.insert(END, "--Suite--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau==8 and num_pnj==0) or (Niveau== 7 and num_pnj==1):
                    listbox.insert(END, "--Equation du second degré--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(16,19):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Dérivation--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(19,23):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")

                    listbox.insert(END, "--Suite--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(23,28):
                        ajouter_element(Liste_cours[i])
                    listbox.insert(END, "\n")
                
                listbox.config(state=DISABLED)



            # Pour chaque pnj qui donnera son cours : 
            listbox.config(state=NORMAL)

            if Niveau ==0:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[0])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[1])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[2])
            
            elif Niveau ==1:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[3])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[4])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[5])       
                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[6]) 

            elif Niveau ==2:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[7])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[8])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[9])       
                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[10]) 
                elif num_pnj=="pnj5":
                    ajouter_element(Liste_cours[11])

            elif Niveau ==3:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[12])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[13])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[14])       
                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[15])
                elif  num_pnj=="pnj5":
                    ajouter_element(Liste_cours[16]) 

            elif Niveau ==5:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[17])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[18])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[19])
            
            elif Niveau ==6:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[20])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[21])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[22])       
                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[23]) 

            elif Niveau ==7:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[24])
                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[25])
                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[26])       
                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[27]) 
                elif num_pnj=="pnj5":
                    ajouter_element(Liste_cours[28])
                
            listbox.config(state=DISABLED)


        def table_craft(event):
            global pnj1_infos
            global pnj2_infos
            global pnj3_infos
            global pnj4_infos
            global pnj5_infos

            global assemble_cle


            canvas_infos_possibilite_discussion.delete('all')
            canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=idee)
             
            if L[ordonne][abscisse-1] == "¤":

                if assemble_cle == False:

                    if Niveau ==0 or Niveau ==5:
                        if pnj1_infos == True and pnj2_infos == True and pnj3_infos == True:
                            assemble_cle = True
                            load_inv(Niveau)
                            Label_text_possibilite_strvar.set("Vous avez fabriqué la grande Clé !")

                        else:
                            Label_text_possibilite_strvar.set("Vous n'avez pas collecté toutes les clés !")


                    elif Niveau == 1 or Niveau==6:
                        if pnj1_infos == True and pnj2_infos == True and pnj3_infos == True and pnj4_infos == True:
                            assemble_cle = True
                            load_inv(Niveau)
                            Label_text_possibilite_strvar.set("Vous avez assemblé la grande Clé !")
                        else:
                            if pnj4_infos == False:
                                Label_text_possibilite_strvar.set("Vous n'avez pas collecté le bâton de colle !")
                            else:
                                Label_text_possibilite_strvar.set("Vous n'avez pas collecté toutes les clés !")
            
                    elif Niveau == 2 or Niveau ==3 or Niveau==7:
                        if pnj1_infos == True and pnj2_infos == True and pnj3_infos == True and pnj4_infos == True and pnj5_infos == True:
                            assemble_cle = True
                            load_inv(Niveau)
                            Label_text_possibilite_strvar.set("Vous avez fabriqué et nettoyé la grande Clé !")
                        else:
                            if pnj4_infos == False:
                                Label_text_possibilite_strvar.set("Vous n'avez pas collecté le bâton de colle !")
                            elif pnj5_infos == False:
                                Label_text_possibilite_strvar.set("Vous n'avez pas collecté le kit de nettoyage !")
                            else:
                                Label_text_possibilite_strvar.set("Vous n'avez pas collecté toutes les clés !")
            
            
                else:
                    Label_text_possibilite_strvar.set("Vous avez déjà fabriqué la Grande Clé ! !")

            else:
                Label_text_possibilite_strvar.set("Vous devez vous trouver à coté de la table de fabrication pour fabriquer quelque chose !")





        def parler_pnj(event):

            def affiche_prog(pnj, pnj_infos, Niveau):
                global c
                c += 1

                text_complet = ""
                # comme cette partie est commune; on l'affiche au debut si c'est le bon tour
                if pnj_infos == False:

                    # on fait en fonction du pnj parce que le cours est unique à chaque pnj
                    if pnj == "pnj1":
                        # et le cours est différent en fonction du niveau (map qui change)
                        if Niveau ==0:
                            if c==1:
                                text_complet = "Leilégalité : B’jour jeune aventurier, je pense que j’pourrais bien t’apprendre un truc aujourd’hui."
                            elif c==2:
                                text_complet = "Leilégalité : Pour résoudre une équation il faut respecter un certain équilibre comme une balance \u2696 , si une partie de l’égalité change alors l’autre coté aussi."
                            elif c==3:
                                text_complet = "Leilégalité : Tiens voila pour m’avoir écouté; un fragment de clé que j’ai ramené lors de mon dernier voyage !"

                        elif Niveau ==1:
                            if c==1:
                                text_complet = "Paπ : Tiens je parie que tu as croisé ma femme toi ! Eh oui je reconnais cet objet il est à moi mais trêve de plaisanterie je pense que si tu es la jeune aventurier c’est pour continuer ton périple"
                            elif c==2:
                                text_complet = "Paπ : Pour cela, il te faudra connaitre la formule de l’aire de la base d’un disque qui est π x rayon²."
                            elif c==3:
                                text_complet = "Paπ : Tiens voila pour la suite, un bout de quelque chose dans l’ancien temps !"

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""
                        
                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==5:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_texte_parole_discussion_pnj_strvar.set("")
                            Label_btn_suivant_discussion_pnj.destroy()

                            global pnj1_infos
                            pnj1_infos = True
                            num_pnj = "pnj1"

                            load_inv(Niveau)
                            load_cours(Niveau, num_pnj)
                            Label_text_possibilite_strvar.set("Vous venez d'obtenir un fragment de clé !")

                    elif pnj == "pnj2":
                        # et le cours est différent en fonction du niveau (map qui change)
                        if Niveau ==0:
                            if c==1:
                                text_complet = "Iggy : Wouf Wouf, Wouf Wouf Wouf, Wouf Wouf Woaf ! Wouf ?(Votre waf français est un peu rouillé mais vous comprenez : “Salut moi c’est Iggy, retiens bien ce que je vais te dire !"
                            elif c==2:
                                text_complet = "Iggy : Quand tu résous une équation s’il y a des x des deux côtés essaie de tout mettre du même côté ce sera plus simple tu verras ! Par exemple avec 3x + 2 = 5x + 3 qui devient 3x + 2 - 3x = 5x + 2 - 3x après il faut juste que tu la résolve."
                            elif c==3:
                                text_complet = "Iggy : D’ailleurs t’aurais pas des croquettes contre mon os doré ?"

                        elif Niveau ==1:
                            if c==1:
                                text_complet = "Cécylindre : Salut toi t’aurais pas envie de savoir calculer le volume d’un cylindre par hasard ? Nan ? "
                            elif c==2:
                                text_complet = "Cécylindre : Bon si jamais c’est la hauteur multipliée par l’aire de la base. "
                            elif c==3:
                                text_complet = "Cécylindre : Tiens je te passe ça comme t’as l’air sympa."

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""
                        
                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==5:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_texte_parole_discussion_pnj_strvar.set("")
                            Label_btn_suivant_discussion_pnj.destroy()


                            global pnj2_infos
                            pnj2_infos = True
                            num_pnj = "pnj2"

                            load_inv(Niveau)
                            load_cours(Niveau, num_pnj)
                            Label_text_possibilite_strvar.set("Vous venez d'obtenir un fragment de clé !")

                    elif pnj == "pnj3":
                        # et le cours est différent en fonction du niveau (map qui change)
                        if Niveau ==0:
                            if c==1:
                                text_complet = "Mathémami : Qu’est ce tu dis ?! Que tu n’as pas parlé ? Autant pour moi mon petit mes oreilles ne fonctionnent plus aussi bien qu’avant, j’ai l’impression que t’essais d’aller en ville pour que tu puisses passer je vais te montrer un truc."
                            elif c==2:
                                text_complet = "Mathémami : Si tu prends l’équation 3x + 2 = 5, il faudra que tu retires l’étape qui arrive en dernier, ici c’est 3x + 2 - 2 = 5 - 2 car la soustraction et l’addition s’oppose et la multiplication et la division aussi, après il ne te reste plus qu’à faire 3x/3 = 3/3 et tu obtiens x = 1."
                            elif c==3:
                                text_complet = "Mathémami : Tiens avant de partir prends ce bidule il appartient à mon mari redonne lui si tu le vois en ville."

                        elif Niveau ==1:
                            if c==1:
                                text_complet = "Marchand de glace : Dis donc toi, il fait aujourd’hui un petit rafraichissement ? "
                            elif c==2:
                                text_complet = "Marchand de glace : D’ailleurs tu savais qu’un cône avait pour volume celui d’un cylindre divisé par 3."
                            elif c==3:
                                text_complet = "Marchand de glace : Allez tiens c’est pas une glace mais ça te sera utile je pense."

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""
                        
                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==5:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""


                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_texte_parole_discussion_pnj_strvar.set("")
                            Label_btn_suivant_discussion_pnj.destroy()

                            global pnj3_infos
                            pnj3_infos = True
                            num_pnj = "pnj3"

                            load_inv(Niveau)
                            load_cours(Niveau, num_pnj)
                            Label_text_possibilite_strvar.set("Vous venez d'obtenir un fragment de clé !")

                    elif pnj == "pnj4":
                        # et le cours est différent en fonction du niveau (map qui change)
                        if Niveau ==1:
                            if c==1:
                                text_complet = "Titouan : Zalut monzieur dis tu zavais qu’il pozait des zénigmes à la porte ? Apparemment faut zavoir calculer le volume d’un cube et d’un paralléléchouette rectangle, du coup z’ai appris et en fait z’est zuper zimple."
                            elif c==2:
                                text_complet = "Titouan : Il suffit de faire longueur x largeur x hauteur et z’est la même pour tous. "
                            elif c==3:
                                text_complet = "Titouan : Tient au fait z’arrête pas de m’en mettre partout."

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""
                        
                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""
                        
                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_texte_parole_discussion_pnj_strvar.set("")
                            Label_btn_suivant_discussion_pnj.destroy()

                            global pnj4_infos
                            pnj4_infos = True
                            num_pnj = "pnj4"

                            load_inv(Niveau)
                            load_cours(Niveau,num_pnj)

                            Label_text_possibilite_strvar.set("Vous venez d'obtenir le tube de colle !")

                    elif pnj == "pnj5":
                        # et le cours est différent en fonction du niveau (map qui change)
                        if Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = "Voici un kit de nettoyage ! Il vous sera utile pour que votre clé fonctionne ! "

                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                            elif c==3:
                                text_complet = ""
                        
                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_texte_parole_discussion_pnj_strvar.set("")
                            Label_btn_suivant_discussion_pnj.destroy()

                            global pnj5_infos
                            pnj5_infos = True
                            num_pnj = "pnj5"

                            load_inv(Niveau)
                            load_cours(Niveau, num_pnj)
                            Label_text_possibilite_strvar.set("Vous venez d'obtenir un kit de nettoyage !")


                #de nouveau une partie commune mais cette fois quand on a déjà vu le pnj  
                else:
                    #pnj 1 alternatif
                    if pnj == "pnj1":
                        if Niveau ==0:
                            if c==1:
                                text_complet = "Leilégalité : On s’recroise dit donc ! T’as oublié ce qu’j’ai dit ? Alors écoute bien j’vais répéter, pour résoudre une équation il faut respecter un certain équilibre comme une balance \u2696, si une partie de l’égalité change alors l’autre coté aussi."
                            elif c==2:
                                text_complet = "Leilégalité : Je t'ai déjà donné mon fragment de clé; bon courage dans ta quete !"

                        elif Niveau ==1:
                            if c==1:
                                text_complet = "Paπ : Alors aussi mauvaise mémoire que ma femme ? Écoute bien cette fois la formule de l’aire de la base d’un disque qui est π x rayon²."
                            elif c==2:
                                text_complet = "Paπ : Malheuresement dans l'ancien temps c'est bidule étaient rar donc je n'en ai plus pour toi !"

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==5:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                    #pnj 2 alternatif
                    elif pnj == "pnj2":
                        if Niveau ==0:
                            if c==1:
                                text_complet = "Iggy : Wouf Wouf Wouf ? Wouf Wouf, Wouf. (Vous comprenez : “T’as oublié tout ce que j’ai dit ? Ça va te couter cher en croquettes mais je vais répéter, quand tu résous une équation s’il y a des x des deux côtés essaie de tout mettre du même côté par exemple avec 3x + 2 = 5x + 3 qui devient 3x + 2 - 3x = 5x + 2 - 3x après il faut juste que tu la résolve."
                            elif c==2:
                                text_complet = "Iggy : Je n'est plus d'os dorépour toi... Mais il te reste des croquettes ?"

                        elif Niveau ==1:
                            if c==1:
                                text_complet = "Cécylindre : Finalement t’as pas écouté et tu aurais dû ? Le volume du cylindre c’est la hauteur multipliée par l’aire de la base."
                            elif c==2:
                                text_complet = "Cécylindre : Il me semble t'avoir déjà donné quelque chose non ?"

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
        
                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==5:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                    #pnj 3 alternatif
                    elif pnj == "pnj3":
                        if Niveau ==0:
                            if c==1:
                                text_complet = "Mathémami : ZzZ ZzZ… Ah ! Tu m’as fait peur, je suis vieille tu sais. Comment ? Tu veux que je réexplique ? Alors je vais te remontrer, si tu prends l’équation 3x + 2 = 5, il faudra que tu retires l’étape qui arrive en dernier, ici c’est 3x + 2 - 2 = 5 - 2 car la soustraction et l’addition s’oppose et la multiplication et la division aussi, après il ne te reste plus qu’à faire 3x/3 = 3/3 et tu obtiens x = 1."
                            elif c==2:
                                text_complet = "Mathémami : Je n'ai plus rien à te donner, bonne nuit !"

                        elif Niveau ==1:
                            if c==1:
                                text_complet = "Marchand de glace : Tu veux une glace au final ? Désolé mais les enfants m’ont tout pris, je te propose de réécouter mon histoire de cône, pour calculer le volume d’un cône c’est le volume du cylindre que tu divises par 3."
                            elif c==2:
                                text_complet = "Marchand de glace : Sur pour la glace ?"

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==5:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                    #pnj 4 alternatif
                    elif pnj == "pnj4":
                        if Niveau ==1:
                            if c==1:
                                text_complet = "Titouan : T’as pas réussi à passer la porte ? Alors ze vais te réexpliquer, pour calculer le volume du cube et du paralléléchouette rectangle il zuffit de faire longueur x largeur x hauteur et z’est la même pour tous."
                            elif c==2:
                                text_complet = "Titouan : z'ai plus de zolle pour zoi dézolé"

                        elif Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==6:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""
                    #pnj 5 alternatif
                    elif pnj == "pnj5":
                        if Niveau ==2:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        if Niveau ==3:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        elif Niveau ==7:
                            if c==1:
                                text_complet = ""
                            elif c==2:
                                text_complet = ""

                        
                    if c == 3 : 
                        #on clear si jamais la personne s'en va
                        canvas_tete_pnj_grand.delete("all")
                        Label_texte_parole_discussion_pnj_strvar.set("")
                        #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
                        if Label_btn_suivant_discussion_pnj is not None:
                            if Label_btn_suivant_discussion_pnj.winfo_exists():
                                Label_btn_suivant_discussion_pnj.destroy()
                        c = 0



                if (c < 4 and pnj_infos == False) or (c != 0 and pnj_infos == True):

                    Label_btn_suivant_discussion_pnj['state'] = DISABLED
                    for i in range(len(text_complet)):
                        text_partiel = text_complet[:i+1]
                        Label_texte_parole_discussion_pnj_strvar.set(f"{text_partiel}")
                        Label_texte_parole_discussion_pnj_widget.update()
                        time.sleep(0.01)
                    Label_btn_suivant_discussion_pnj['state'] = NORMAL

            global pnj1_infos
            global pnj2_infos
            global pnj3_infos
            global pnj4_infos  
            global pnj5_infos

            pnj_List = ["pnj1" , "pnj2" ,"pnj3" ,"pnj4", "pnj5"]

            global c
            c = 0

            # check si on se trouve bien dans une zone avec pnj quand la fonction est chargée  
            if (L[ordonne-1][abscisse] in pnj_List or L[ordonne+1][abscisse] in pnj_List or L[ordonne][abscisse-1] in pnj_List or L[ordonne][abscisse+1] in pnj_List ):
                    
                    #PNJ 1
                    if (L[ordonne-1][abscisse] == pnj_List[0] or L[ordonne+1][abscisse]== pnj_List[0] or L[ordonne][abscisse-1]== pnj_List[0] or L[ordonne][abscisse+1]== pnj_List[0]):
                        pnj_ = "pnj1"
                        pnj_infos_ = pnj1_infos
                        canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj1_grand)

                    #PNJ 2
                    elif (L[ordonne-1][abscisse] == pnj_List[1] or L[ordonne+1][abscisse]== pnj_List[1] or L[ordonne][abscisse-1]== pnj_List[1] or L[ordonne][abscisse+1]== pnj_List[1]):
                        pnj_ = "pnj2"
                        pnj_infos_ = pnj2_infos
                        canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj2_grand)
###

                    #PNJ3
                    elif (L[ordonne-1][abscisse] == pnj_List[2] or L[ordonne+1][abscisse]== pnj_List[2] or L[ordonne][abscisse-1]== pnj_List[2] or L[ordonne][abscisse+1]== pnj_List[2]):
                        pnj_ = "pnj3"
                        pnj_infos_ = pnj3_infos
                        canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj3_grand)


                    #PNJ4
                    elif (L[ordonne-1][abscisse] == pnj_List[3] or L[ordonne+1][abscisse]== pnj_List[3] or L[ordonne][abscisse-1]== pnj_List[3] or L[ordonne][abscisse+1]== pnj_List[3]):
                        pnj_ = "pnj4"
                        pnj_infos_ = pnj4_infos
                        canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj4_grand)

                    #PNJ5
                    elif (L[ordonne-1][abscisse] == pnj_List[4] or L[ordonne+1][abscisse]== pnj_List[4] or L[ordonne][abscisse-1]== pnj_List[4] or L[ordonne][abscisse+1]== pnj_List[4]):
                        pnj_ = "pnj5"
                        pnj_infos_ = pnj5_infos
                        canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj5_grand)


                    global Label_btn_suivant_discussion_pnj

                    if Label_btn_suivant_discussion_pnj is not None:
                        if Label_btn_suivant_discussion_pnj.winfo_exists():
                            Label_btn_suivant_discussion_pnj.destroy()
                    #On crée le bouton pour faire discuter le pnj avec l'utilisateur et on set le texte de bienvenue          
                    Label_texte_parole_discussion_pnj_strvar.set("Salut ! Clique sur suivant !")
                    Label_btn_suivant_discussion_pnj = Button(Label_Frame_Discussion_pnj, text="Suivant", command=lambda: affiche_prog(pnj_, pnj_infos_, Niveau))
                    Label_btn_suivant_discussion_pnj.pack(side=BOTTOM, anchor="e", pady=5, padx=2)
            
            # check si autour il y a la porte ou non
            elif (L[ordonne-1][abscisse] == "\U0001F6AA" or L[ordonne+1][abscisse]== "\U0001F6AA" or L[ordonne][abscisse-1]== "\U0001F6AA" or L[ordonne][abscisse+1]== "\U0001F6AA"):
                global assemble_cle
                print(assemble_cle)
                if assemble_cle == True:
                    porte_enigme(Niveau)
                    load_cours(Niveau, 1)
                else:
                    Label_text_possibilite_strvar.set("Vous devez d'abord assemblé votre Clé pour pouvoir ouvrir la porte !")
                    canvas_infos_possibilite_discussion.delete('all')
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=idee)

            #check s'il y le boss autour ou non:
            elif (L[ordonne-1][abscisse] == "boss" or L[ordonne+1][abscisse]== "boss" or L[ordonne][abscisse-1]== "boss" or L[ordonne][abscisse+1]== "boss"):
                boss_enigme(Niveau)

            else:
                canvas_infos_possibilite_discussion.delete('all')
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=idee)
                Label_text_possibilite_strvar.set("Il n'y a personne autour de vous avec qui discuter !")
                #on clear si jamais la personne s'en va
                canvas_tete_pnj_grand.delete("all")
                Label_texte_parole_discussion_pnj_strvar.set("")
                #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
                if Label_btn_suivant_discussion_pnj is not None:
                    if Label_btn_suivant_discussion_pnj.winfo_exists():
                        Label_btn_suivant_discussion_pnj.destroy()
                c = 0



        #Fonction de la porte avec verif nb fenetre et gestion de l'exo
        def porte_enigme(Niveau):
            global second_window_probleme


            if not second_window_probleme or not second_window_probleme.winfo_exists():  # Vérifie si la deuxième fenêtre existe
                def affiche_consigne(Niveau):
                    global erreur
                    global c_sw
                    c_sw  += 1

                    text_complet_consignes = ""
                    
                    if c_sw==1:
                        text_complet_consignes = "Pour pouvoir tourner la clé et ainsi dévérouiller la porte, vous devez résoudre cette exercice ! "
                    elif c_sw==2:
                        text_complet_consignes = "Toutes les parties du cours que vous avez collectées vous serviront pour répondre ! Vous pouvez les consulter "
                    elif c_sw==3:
                        if Niveau ==0:
                            text_complet_consignes = "Vous devez résoudre cette équation du premier degré en trouvant la valeur de x. Apres avoir résolu cette equation; selectionnez la bonne case et faites valider"
                        elif Niveau ==1:
                            text_complet_consignes = f"Vous devez résoudre ce calcul de volume, il vous faudra trouver le volume totale; selectionnez la bonne case et faites valider Attention; toutes les valerus donn&es sont en m etle résultat attendu en  m cube. Données : a = {Exo_correction[5][0]}; b ={Exo_correction[5][1]}; c ={Exo_correction[5][2]}; d ={Exo_correction[5][3]}; e ={Exo_correction[5][4]}; f ={Exo_correction[5][5]}; r ={Exo_correction[5][6]}"
                        elif Niveau ==2:
                            text_complet_consignes = f"Vous devez résoudre ce rpoblème : Trouver les coordonnées de l'intersection entre [AB] et [CD]. Voici les coordonnées des points : A = {Exo_correction[5][0]}; B ={Exo_correction[5][1]}; C ={Exo_correction[5][2]}; D ={Exo_correction[5][3]}"
                        elif Niveau==3:
                            text_complet_consignes = "Vous devez résoudre cet exo pas encore fait"
                        elif Niveau==5:
                            text_complet_consignes = "Vous devez résoudre cet exo pas encore fait"
                        elif Niveau==6:
                            text_complet_consignes = "Vous devez résoudre cet exo pas encore fait"
                        elif Niveau==7:
                            text_complet_consignes = "Vous devez résoudre cet exo pas encore fait"
        
                    elif c_sw==4:
                        Label_btn_suivant_second_window ['state'] = DISABLED
                        # on affcihe les btns de réponses
                        Label_btn_result_possible_1 = Button(Label_Frame_Reponse_Verif_2, text=value_btn_1, command=lambda:verif_reponse_sw(value_btn_1,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                        Label_btn_result_possible_1.pack(side = LEFT, padx = 25, pady = 5)

                        Label_btn_result_possible_2 = Button(Label_Frame_Reponse_Verif_2, text=value_btn_2, command=lambda:verif_reponse_sw(value_btn_2,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                        Label_btn_result_possible_2.pack(side = LEFT, padx = 25, pady = 5)

                        Label_btn_result_possible_3 = Button(Label_Frame_Reponse_Verif_2, text=value_btn_3, command=lambda:verif_reponse_sw(value_btn_3,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                        Label_btn_result_possible_3.pack(side = LEFT, padx= 25, pady = 5)
                    elif c_sw==5:
                        if erreur == 0:
                            text_complet_consignes = "Bravo ! Vous avez trouvé la bonne solution !"
                        else:
                            text_complet_consignes = "Vous n'avez pas trouvé la bonne solution, cliquez sur suivant pour recommencer !"

                    elif c_sw==6:
                        if erreur == 0:
                            if Niveau ==0:
                                text_complet_consignes ="Cliquez sur suivant pour passez au niveau suppérieur !"
                            elif Niveau ==1:
                                text_complet_consignes ="Cliquez sur suivant pour passez au niveau suppérieur !"
                            elif Niveau ==3:
                                text_complet_consignes ="Cliquez sur suivant pour passez au niveau suppérieur !"

                        else:
                            second_window_probleme.destroy()

                    else:
                        Niveau +=1
                        second_window_probleme.destroy()
                        global type_partie
                        Gestion_Jouer(Jeu, Niveau, type_partie)



                    
                    if  4 > c_sw  or 5 <= c_sw <7:

                        Label_btn_suivant_second_window ['state'] = DISABLED
                        for i in range(len(text_complet_consignes)):
                            text_partiel_second_window = text_complet_consignes[:i+1]
                            Label_Text_Explication_Exercice_strvar.set(f"{text_partiel_second_window}")
                            Label_Text_Explication_Exercice_widget.update()
                            time.sleep(0.01)
                        Label_btn_suivant_second_window ['state'] = NORMAL
    
                def verif_reponse_sw(reponse, correction,Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3):
                    Label_btn_result_possible_1.destroy()
                    Label_btn_result_possible_2.destroy()
                    Label_btn_result_possible_3.destroy()
                    global erreur
                    erreur = 0
                    if reponse == correction:
                        affiche_consigne(Niveau)
                    else:
                        erreur = 1
                        affiche_consigne(Niveau)


                
                global c_sw
                c_sw = 0

                second_window_probleme = Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
                # second_window_probleme.geometry("400x600") 

                ####frame global de la fenetre
                Label_Frame_global_second_window = Frame(second_window_probleme, bg = "#BBC4E3")
                Label_Frame_global_second_window.pack(expand=True, fill="both")

                ###frame qui conteintdra toutes les consignes / explications et le btn suivant
                Label_Frame_Canvas_consignes_explication_btn = Frame(Label_Frame_global_second_window, bg= None)
                Label_Frame_Canvas_consignes_explication_btn.pack(side=TOP, fill='x', pady= 5, padx=5)

                #on load les element de consignes
                Label_Text_Explication_Exercice_strvar = StringVar()
                Label_Text_Explication_Exercice_strvar.set("Cliquez sur suivant !")
                len_wrap = 330
                if Niveau==1:
                    len_wrap =625
                Label_Text_Explication_Exercice_widget = Label(Label_Frame_Canvas_consignes_explication_btn,wraplength=len_wrap, textvariable = Label_Text_Explication_Exercice_strvar, justify="left"  )
                Label_Text_Explication_Exercice_widget.pack(fill='x',side = LEFT, padx= 5, pady=5)
                Label_btn_suivant_second_window = Button(Label_Frame_Canvas_consignes_explication_btn, text="Suivant !", command=lambda:affiche_consigne(Niveau))
                Label_btn_suivant_second_window.pack(side=TOP, anchor="e", pady=5, padx=5)

                ### frame qui contient le canvas qui affichera la formule
                Label_Frame_Canvas_formule_exo = Frame(Label_Frame_global_second_window, bg="#99A6D0")
                Label_Frame_Canvas_formule_exo.pack(side=TOP, fill='y', pady= 5, padx=5)

                # on recupère la formule et la correction
                Exo_correction = py_maths_exo.choix_exo_niveau(Niveau,Label_Frame_Canvas_formule_exo)
                print(Exo_correction)

                if Niveau !=1 and Niveau !=2:
                    #On load le canvas avec sa formule qu'on a recup depuis le ficheir py-math_exo
                    #Code Ia /Internet # Formater la formule avec les nombres aléatoires
                    formule = Exo_correction[0]
                    # Créer une figure matplotlib sans légendes et sans box
                    fig = Figure(figsize=(5, 2), dpi=100, frameon=False)  # Taille initiale de la figure sans boîte englobante
                    # Ajouter un sous-graphique
                    ax = fig.add_subplot(111)
                    # Supprimer les légendes et la boîte englobante
                    ax.axis('off')
                    # Ajouter la formule mathématique
                    ax.text(0.5, 0.5, formule, fontsize=20, ha='center')
                    # Obtenir les limites de la boîte englobante de la formule
                    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
                    # Redimensionner la figure en fonction de la taille de la formule
                    fig.set_size_inches(5, bbox.height)
                    # Créer un canvas Tkinter
                    canvas_formule_exo_sw = FigureCanvasTkAgg(fig, master=Label_Frame_Canvas_formule_exo)
                    canvas_formule_exo_sw.draw()
                    # Afficher le canvas
                    canvas_formule_exo_sw.get_tk_widget().pack(padx=5, pady=5)



                elif Niveau ==1:
                    Label_canvas_img_sw = Canvas(Label_Frame_Canvas_formule_exo, width = 713, height = 487, bg = "#ffffff")
                    Label_canvas_img_sw.pack(padx=5,pady=5)
                    Label_canvas_img_sw.create_image(0,0,anchor=NW, image=Volume_nv1)

                #le nv 2 ce gère tout seul



                ## Frame global de la frame qui contient les trois valeur de réponse avec les cases à cocher et le bouton valider
                Label_Frame_Reponse_Verif = Frame(Label_Frame_global_second_window, bg= None)
                Label_Frame_Reponse_Verif.pack(side=TOP, fill='x', pady= 5, padx=5, )
                #Frame avec les 3 btn 
                Label_Frame_Reponse_Verif_2 = Frame(Label_Frame_Reponse_Verif, bg = None)
                Label_Frame_Reponse_Verif_2.pack(anchor=CENTER)
                # on définit les trois valeur qui vont s'afficher dans les boutons
                value_btn_1 = Exo_correction[2]
                value_btn_2 = Exo_correction[3]
                value_btn_3 = Exo_correction[4]


                # Lie la fermeture de la fenêtre à la réinitialisation de second_window_probleme
                second_window_probleme.protocol("WM_DELETE_WINDOW", lambda: reset_second_window())
        
        def reset_second_window():
            global second_window_probleme
            if second_window_probleme:
                second_window_probleme.destroy()  # Détruit la fenêtre
            second_window_probleme= None


        #Fonction qui gère les deuxsalles de boss
        def boss_enigme(Niveau):
            global boss_window

            if not boss_window or not boss_window.winfo_exists():  # Vérifie si la deuxième fenêtre existe

                #on reset le nombred d'indices donnée si jamais il y a eu plusieurs tentatives
                global indices_give_1
                global indices_give_2
                if Niveau ==4:
                    indices_give_1 = 0
                elif Niveau ==8:
                    indices_give_2 = 0

                def affiche_consigne_boss(Niveau):
                    global erreur_boss
                    global c_boss
                    c_boss  += 1

                    text_complet_consignes_boss = ""

                    if c_boss==1:
                        if Niveau==4:
                            text_complet_consignes_boss = "Pour pouvoir tourner la clé et ainsi dévérouiller la porte, vous devez résoudre cette exercice ! "
                    elif c_boss==2:
                        if Niveau==4:
                            text_complet_consignes_boss = "Toutes les parties du cours que vous avez collectées vous serviront pour répondre ! Vous pouvez les consulter "
                    elif c_boss==3:
                        if Niveau==4:
                            text_complet_consignes_boss = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab "

                    elif c_boss==4:
                        Label_btn_suivant_boss_window ['state'] = DISABLED
                        # on affcihe les btns de réponses
                        Label_btn_result_possible_1_boss = Button(Label_Frame_Reponse_Verif_boss_2, text=value_btn_1_boss, command=lambda:verif_reponse_boss(value_btn_1_boss,Exo_correction_boss[1],Label_btn_result_possible_1_boss,Label_btn_result_possible_2_boss,Label_btn_result_possible_3_boss))
                        Label_btn_result_possible_1_boss.pack(side =LEFT, padx = 5, pady = 5)

                        Label_btn_result_possible_2_boss = Button(Label_Frame_Reponse_Verif_boss_2, text=value_btn_2_boss, command=lambda:verif_reponse_boss(value_btn_2_boss,Exo_correction_boss[1],Label_btn_result_possible_1_boss,Label_btn_result_possible_2_boss,Label_btn_result_possible_3_boss))
                        Label_btn_result_possible_2_boss.pack(side =LEFT, padx = 5, pady = 5)

                        Label_btn_result_possible_3_boss = Button(Label_Frame_Reponse_Verif_boss_2, text=value_btn_3_boss, command=lambda:verif_reponse_boss(value_btn_3_boss,Exo_correction_boss[1],Label_btn_result_possible_1_boss,Label_btn_result_possible_2_boss,Label_btn_result_possible_3_boss))
                        Label_btn_result_possible_3_boss.pack(side =LEFT, padx= 5, pady = 5)
                    elif c_boss==5:
                        if erreur_boss == 0:
                            text_complet_consignes_boss = "Bravo ! Vous avez trouvé la bonne solution !"
                        else:
                            text_complet_consignes_boss = "Vous n'avez pas trouvé la bonne solution, cliquez sur suivant pour recommencer !"

                    elif c_boss==6:
                        if erreur_boss == 0:
                            if Niveau ==0:
                                text_complet_consignes_boss ="Cliquez sur suivant pour passez au niveau suppérieur !"
                            elif Niveau ==1:
                                text_complet_consignes_boss ="Cliquez sur suivant pour passez au niveau suppérieur !"
                            elif Niveau ==3:
                                text_complet_consignes_boss ="Cliquez sur suivant pour passez au niveau suppérieur !"

                        else:
                            boss_window.destroy()

                    else:
                        Niveau +=1
                        boss_window.destroy()
                        global type_partie
                        Gestion_Jouer(Jeu, Niveau, type_partie)

                    
                    if  4 > c_boss  or 5 <= c_boss <7:

                        Label_btn_suivant_boss_window ['state'] = DISABLED
                        for i in range(len(text_complet_consignes_boss)):
                            text_partiel_boss = text_complet_consignes_boss[:i+1]
                            Label_Text_Explication_boss_strvar.set(f"{text_partiel_boss}")
                            Label_Text_Explication_boss_widget.update()
                            time.sleep(0.01)
                        Label_btn_suivant_boss_window ['state'] = NORMAL
    
                def verif_reponse_boss(reponse, correction,Label_btn_result_possible_1_boss,Label_btn_result_possible_2_boss,Label_btn_result_possible_3_boss):
                    Label_btn_result_possible_1_boss.destroy()
                    Label_btn_result_possible_2_boss.destroy()
                    Label_btn_result_possible_3_boss.destroy()
                    global erreur_boss
                    erreur_boss = 0
                    if reponse == correction:
                        affiche_consigne_boss(Niveau)
                    else:
                        erreur_boss = 1
                        affiche_consigne_boss(Niveau)

   
                
                def Give_indices_boss(Niveau):

                    def ajouter_element_indices(Texte_): #Une partie de la gestion du code de la liste box provient d'internet
                        global listbox_indices
                        element_ = Texte_.strip()
                        listbox_indices.config(state=NORMAL)
                        if element_:
                            listbox_indices.insert(END, element_ + "\n")
                        listbox_indices.insert(END, "\n")
                        listbox_indices.config(state=DISABLED)


                    global indices_give_1
                    global indices_give_2

                    L_indices_1 = [
                        "Indices 1 boss 1 : ",
                        "Indices 2 boss 1 : ",
                        "Indices 3 boss 1 : ",
                        "Vous avez utilisé tout les indices !"
                        ]
                    L_indices_2 = [
                        "Indices 1 boss 2 : ",
                        "Indices 2 boss 2 : ",
                        "Indices 3 boss 2 : ",
                        "Vous avez utilisé tout les indices !"
                        ]

                    if Niveau ==4:
                        if indices_give_1 < 3:
                            ajouter_element_indices(L_indices_1[indices_give_1])
                            indices_give_1 +=1
                        elif indices_give_1 == 3:
                            ajouter_element_indices(L_indices_1[indices_give_1])
                            Label_btn_get_indices.destroy()



                    elif Niveau == 8:
                        if indices_give_2 < 3:
                            ajouter_element_indices(L_indices_2[indices_give_2])
                            indices_give_2 +=1
                        elif indices_give_2 ==3:
                            ajouter_element_indices(L_indices_2[indices_give_2])
                            Label_btn_get_indices.destroy()









                global c_boss
                c_boss = 0


                boss_window = Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
                # boss_window.geometry("400x600") 

                #####frame global de la fenetre
                Label_Frame_global_boss = Frame(boss_window, bg = "#BBC4E3")
                Label_Frame_global_boss.pack(expand=True, fill="both")

                #### frame globale des element de droite / des indices
                Label_frame_indices_boss = Frame(Label_Frame_global_boss, bg ="#99A6D0", width= 100)
                Label_frame_indices_boss.pack(expand=True, fill = 'both', side=RIGHT)

                ###frame box de la listbox des indices
                Label_Frame_box_listbox_indices_boss = Frame(Label_frame_indices_boss, bg = None)
                Label_Frame_box_listbox_indices_boss.pack(side =TOP, pady= 5, padx = 5)
                #on crée la box pour les indices s'il sont demandé par l'utilisateur
                global listbox_indices
                listbox_indices = Text(Label_Frame_box_listbox_indices_boss, width =35,wrap="word",bg=None)
                listbox_indices.pack(side=LEFT, fill=BOTH)

                scrollbar_indices = Scrollbar(Label_Frame_box_listbox_indices_boss, orient=VERTICAL, command=listbox_indices.yview)
                scrollbar_indices.pack(side=RIGHT, fill=Y)

                listbox_indices.config(yscrollcommand=scrollbar_indices.set)
                
                listbox_indices.insert(END, "--Indices--" + "\n")
                listbox_indices.insert(END, "\n")
                listbox_indices.config(state=DISABLED)


                Label_btn_get_indices = Button(Label_frame_indices_boss,text="Obtenir un indice", command=lambda:Give_indices_boss(Niveau))
                Label_btn_get_indices.pack(pady=10, side=TOP)

                ###frame global des éléments de gauche
                Label_frame_global_element_gauche_boss = Frame(Label_Frame_global_boss, bg = "#99A6D0")
                Label_frame_global_element_gauche_boss.pack(expand=True, fill='y', side=LEFT)

                ###frame qui conteintdra toutes les consignes / explications et le btn suivant
                Label_Frame_Canvas_consignes_explication_btn_boss = Frame(Label_frame_global_element_gauche_boss, bg=None)
                Label_Frame_Canvas_consignes_explication_btn_boss.pack(side=TOP, fill='x', pady= 5, padx=5)

                #on load les element de consignes
                Label_Text_Explication_boss_strvar = StringVar()
                Label_Text_Explication_boss_strvar.set("Cliquez sur suivant !")
                Label_Text_Explication_boss_widget = Label(Label_Frame_Canvas_consignes_explication_btn_boss,wraplength=300, textvariable = Label_Text_Explication_boss_strvar, justify="left"  )
                Label_Text_Explication_boss_widget.pack(fill='x',side = LEFT, padx= 5, pady=5)
                Label_btn_suivant_boss_window = Button(Label_Frame_Canvas_consignes_explication_btn_boss, text="Suivant !", command=lambda:affiche_consigne_boss(Niveau))
                Label_btn_suivant_boss_window.pack(side=TOP, anchor="e", pady=5, padx=5)

                ### frame qui contient le canvas qui affichera la formule
                Label_Frame_Canvas_formule_boss = Frame(Label_frame_global_element_gauche_boss, bg="#99A6D0")
                Label_Frame_Canvas_formule_boss.pack(side=TOP, fill='y', pady= 5, padx=5)

                if Niveau ==4:
                    # on recupère la formule et la correction
                    Exo_correction_boss = py_maths_boss.choix_exo_niveau_boss(Niveau,Label_Frame_Canvas_formule_boss)
                    print(Exo_correction_boss)


                    # on définit les trois valeur qui vont s'afficher dans les boutons
                    value_btn_1_boss = Exo_correction_boss[2]
                    value_btn_2_boss = Exo_correction_boss[3]
                    value_btn_3_boss = Exo_correction_boss[4]
                elif Niveau==8:
                    a = 1
                    #il faut load l'img et et selec le resultat            

                ## Frame global qui contient la frame ave les trois valeur de réponse avec les cases à cocher et le bouton valider
                Label_Frame_Reponse_Verif_boss = Frame(Label_frame_global_element_gauche_boss, bg= None)
                Label_Frame_Reponse_Verif_boss.pack(side=TOP, fill='x', pady= 5, padx=5, anchor=CENTER)
                Label_Frame_Reponse_Verif_boss_2 = Frame(Label_Frame_Reponse_Verif_boss, bg=None)
                Label_Frame_Reponse_Verif_boss_2.pack(anchor = CENTER)

                # Lie la fermeture de la fenêtre à la réinitialisation de boss_window
                boss_window.protocol("WM_DELETE_WINDOW", lambda: reset_boss_window())

        def reset_boss_window():
            global boss_window
            if boss_window:
                boss_window.destroy()  # Détruit la fenêtre
            boss_window= None




        def regle_infos_jeu(event):
            Regle = Toplevel()
            Regle.geometry("600x400")
            Label_titre_regle = Label(Regle, text="Maze-Maths : Règles").pack(pady=5)

            Label_Frame_Touche = Frame(Regle, bg = "#000000")
            Label_Frame_Touche.pack(expand=True, fill="both")

            Label_frame_1 = Frame(Label_Frame_Touche, bg = "blue", width=250)
            Label_frame_1.pack(fill='y', side=LEFT, pady=5, padx=5)

            Label_touche_box = Frame(Label_frame_1, height=200, bg="white", width=250)
            Label_touche_box.pack(fill='x', padx=5, pady=5, side = TOP)


            close_btn = Button(Regle, command=Regle.destroy, text="Fermer").pack(side=BOTTOM)
            Regle.mainloop()

        #fonction pass à supp dans version final
        def pass_(event):
            global Niveau
            global type_partie
            Niveau +=1
            Gestion_Jouer(Jeu, Niveau, type_partie)

        # coordonnées
        global ordonne
        global abscisse
        abscisse = 1
        ordonne = 1

        # état de visite des pnj  : donner ou non les elements
        global pnj1_infos
        global pnj2_infos
        global pnj3_infos
        global pnj4_infos
        global pnj5_infos
        pnj1_infos = True
        pnj2_infos = True
        pnj3_infos = True
        pnj4_infos = True  
        pnj5_infos = True

        # quad un elment est fabriqué, pour l'afficher correctement

        global assemble_cle
        assemble_cle = False





        ######On place tout les elements sur la fenetre#####

        #####Frame global qui contient les deux partie du jeu
        Label_Frame_Global = Frame(Jeu, bg='#BBC4E3')
        Label_Frame_Global.pack(expand=True, fill="both")

        ####Partie Gauche : 
        Label_Frame_Jeu_Inv = Frame(Label_Frame_Global, bg='#BBC4E3') 
        Label_Frame_Jeu_Inv.pack(side = 'left', fill='y', padx=5, pady=5)

        #Jeu partie Gauche haut : 
        long_c = len(L[0])*24
        larg_c = len(L)*24
        canvas = Canvas(Label_Frame_Jeu_Inv, width=long_c, height=larg_c, bg = "#ffffff", borderwidth= 1)

        #On affiche dans tkinter
        for x in range(len(L)):
            for y in range(len(L[x])):
                if L[x][y] == "■":
                    choice_mur = random.randint(1,20)
                    if choice_mur <=12:
                        canvas.create_image(24*y, 24*x, anchor=NW, image=mur1)
                    elif 12 < choice_mur < 18:
                        canvas.create_image(24*y, 24*x, anchor=NW, image=mur2)
                    else:
                        canvas.create_image(24*y, 24*x, anchor=NW, image=mur3)
                elif L[x][y] == "pnj1":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=pnj1)
                elif L[x][y] == "pnj2":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=pnj2)
                elif L[x][y] == "pnj3":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=pnj3)
                elif L[x][y] == "pnj4":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=pnj4)
                elif L[x][y] == "pnj5":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=pnj4)
                elif L[x][y] == "\U0001F6AA":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=porte)
                elif L[x][y] == "○":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=Perso)
                elif L[x][y] == "¤":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=craft_table_)
                    
        if Niveau==4 or Niveau==8:
            canvas.create_image(24*16, 24*7, anchor=NW, image=pnj_boss_grand)

        canvas.pack(side="top",padx=5, pady=5)

        ###Frame gauche bas pour clé + pouvoir parler infos
        Label_Frame_pnj_Text = Frame(Label_Frame_Jeu_Inv, bg="#99A6D0")
        Label_Frame_pnj_Text.pack(side=TOP, fill='x',padx=5, pady=5)

        ##Frame affiche le texte si on peut parler à un pnj ou faire un action
        Label_Frame_Text_Info_Discussion_pnj = Frame(Label_Frame_pnj_Text, bg= None)
        Label_Frame_Text_Info_Discussion_pnj.pack(fill='y', padx=5, pady=5, side='left')

        #On load les elements pour afficher les msg de possibilité de discution 
        canvas_infos_possibilite_discussion = Canvas(Label_Frame_Text_Info_Discussion_pnj, bg=None, height=50, width=50)
        canvas_infos_possibilite_discussion.pack(anchor="c", side=LEFT, padx=15)
        Label_text_possibilite_strvar = StringVar()
        canvas_infos_possibilite_discussion.create_image(0,0, anchor=NW, image=idee)
        if Niveau ==0 or Niveau ==5:
            Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés !")
        elif Niveau ==1 or Niveau ==6:
            Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés et le tube de colle !")
        elif Niveau ==2 or Niveau ==3 or Niveau ==7:
            Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés,le tube de colle et le kit de nettoyage !")
        elif Niveau ==4 or Niveau ==8:
            Label_text_possibilite_strvar.set("Objectif : Affronter le BOSS")

        Label_text_possibilite_widget = Label(Label_Frame_Text_Info_Discussion_pnj, textvariable=Label_text_possibilite_strvar, wraplength=150, width = 25, justify="left", bg = None)
        Label_text_possibilite_widget.pack(side="left", pady=5, padx=5)
    
        ## Frame de box de discussion avec les pnj 
        Label_Frame_Discussion_pnj = Frame(Label_Frame_pnj_Text, bg=None)
        Label_Frame_Discussion_pnj.pack(expand=True, fill=BOTH, padx=5, pady=5, side='right')

        #On load les element qui serviron aux boites de discussion des pnjs
        canvas_tete_pnj_grand = Canvas(Label_Frame_Discussion_pnj, bg=None, height=100, width=200)
        canvas_tete_pnj_grand.pack(anchor="c", padx=10,pady=5, side=LEFT)
        Label_texte_parole_discussion_pnj_strvar = StringVar()
        Label_texte_parole_discussion_pnj_widget = Label(Label_Frame_Discussion_pnj, textvariable=Label_texte_parole_discussion_pnj_strvar, wraplength=320, justify="left")
        Label_texte_parole_discussion_pnj_widget.pack(side=LEFT, padx=5, pady=5)



        ####Partie Droite : 
        Label_Frame_Cours_cle = Frame(Label_Frame_Global, bg="#99A6D0")
        Label_Frame_Cours_cle.pack(side='right', expand=True, fill="both", padx=5, pady=5)

        ##Frame qui affiche le cours actuel
        Label_Frame_Cours_Affiche = Frame(Label_Frame_Cours_cle,bg='white')
        Label_Frame_Cours_Affiche.pack(side='top', expand=True, fill="both", padx=5, pady=5)

        #On load le cours actuel : 
        load_cours(Niveau,0)
        
        ##Frame affiche l'inventaire (clé(s))
        Label_Frame_Inv_Cle = Frame(Label_Frame_Cours_cle, bg='#99A6D0')
        Label_Frame_Inv_Cle.pack(side='bottom', padx=5, pady=5, fill='x')

        #On load l'inventaire de base 
        long_canvas_inv = 150
        if Niveau ==1 or Niveau ==6:
            long_canvas_inv = 200
        elif Niveau == 2 or Niveau ==3 or Niveau ==7:
            long_canvas_inv = 250

        canvas_inv = Canvas(Label_Frame_Inv_Cle, width=long_canvas_inv, height=50, bg = "#7786BA")

        if Niveau !=4 and Niveau !=8:
            canvas_inv.create_image(0,0,anchor=NW, image = loot_vide_pnj1)
            canvas_inv.create_image(50,0,anchor=NW, image = loot_vide_pnj2)
            canvas_inv.create_image(100,0,anchor=NW, image = loot_vide_pnj3)

            if Niveau == 1 or Niveau ==6:
                canvas_inv.create_image(150,0,anchor=NW, image = loot_vide_pnj4)
            elif Niveau ==2 or Niveau ==3 or Niveau ==7:
                canvas_inv.create_image(150,0,anchor=NW, image = loot_vide_pnj4)
                canvas_inv.create_image(200,0,anchor=NW, image = loot_vide_pnj5)

        canvas_inv.pack(pady=10)




        #deplacement
        Jeu.focus_set()

        Jeu.bind("<KeyPress-Up>", deplacement)
        Jeu.bind("<KeyPress-Down>", deplacement)
        Jeu.bind("<KeyPress-Left>", deplacement)
        Jeu.bind("<KeyPress-Right>", deplacement)

        Jeu.bind("<space>", parler_pnj)

        Jeu.bind("<KeyPress-c>", table_craft)

        Jeu.bind("<Escape>", regle_infos_jeu)

        Jeu.bind("<KeyPress-r>", pass_)

        def app(event):
            boss_enigme(Niveau)
        Jeu.bind("<KeyPress-t>", app)



    elif Niveau == tours:
        def text_choix_medaille(type_partie_ , nb_check):


            L_Text_resultat_medaille = [
                "Médailles Diamond Bravo, vous avez utilisé 0 indices ! blablabla",
                "Médailles glod Très bien, vous avez utilisé 1 indices ! blablabla",
                "Médailles silver Bien, vous avez utilisé 2 indices ! blablabla",
                "Médailles Bronze, vous avez utilisé 3 indices ! blablabla",
            ]

            if type_partie_=='seconde':
                text_medaille.set(L_Text_resultat_medaille[indices_give_1])
            elif type_partie_=='premiere':
                text_medaille.set(L_Text_resultat_medaille[indices_give_2])
            else:
                if nb_check==0:
                    text_medaille.set(L_Text_resultat_medaille[indices_give_1])
                elif nb_check ==1:
                    text2_medaille.set(L_Text_resultat_medaille[indices_give_2])



        if type_partie=='seconde':
            if indices_give_1 ==0:
                img_resultat =  PhotoImage(file="image/diamond.png") 
            elif indices_give_1 ==1:
                img_resultat = PhotoImage(file = "image/gold.png")
            elif indices_give_1 ==2:
                img_resultat = PhotoImage(file = "image/silver.png")
            elif indices_give_1 ==3:
                img_resultat = PhotoImage(file = "image/bronze.png")

        if type_partie=='premiere':
            if indices_give_2 ==0:
                img_resultat = PhotoImage(file="image/diamond.png") 
            elif indices_give_2 ==1:
                img_resultat = PhotoImage(file = "image/gold.png")
            elif indices_give_2 ==2:
                img_resultat = PhotoImage(file = "image/silver.png")
            elif indices_give_2 ==3:
                img_resultat = PhotoImage(file = "image/bronze.png")

        if type_partie =='all':
            if indices_give_1 ==0:
                img_resultat = PhotoImage(file="image/diamond.png") 
            elif indices_give_1 ==1:
                img_resultat = PhotoImage(file = "image/gold.png")
            elif indices_give_1 ==2:
                img_resultat = PhotoImage(file = "image/silver.png")
            elif indices_give_1 ==3:
                img_resultat = PhotoImage(file = "image/bronze.png") 

            if indices_give_2 ==0:
                img_resultat2 = PhotoImage(file="image/diamond.png") 
            elif indices_give_2 ==1:
                img_resultat2 = PhotoImage(file = "image/gold.png")
            elif indices_give_2 ==2:
                img_resultat2 = PhotoImage(file = "image/silver.png")
            elif indices_give_2 ==3:
                img_resultat2 = PhotoImage(file = "image/bronze.png")  


        Label_titre_resultat_partie = Label(Jeu, text = 'Résultats')
        Label_titre_resultat_partie.pack(pady=10)

        #Frame global pour afficher les éléments des résultats
        Label_Frame_global_resultat = Frame(Jeu, bg = 'red')
        Label_Frame_global_resultat.pack(expand=True, fill=BOTH, pady= 5, padx = 5)

        if type_partie !='all':
            #Frame avec les elements des resulat (sous frame)
            Label_Frame_resultat_titre_elements = Frame(Label_Frame_global_resultat, bg = 'green')
            Label_Frame_resultat_titre_elements.pack(expand=True, fill=BOTH, pady=5, padx=5)

            Label_titre_type_partie_resultat = Label(Label_Frame_resultat_titre_elements, text = type_partie, anchor = NW)
            Label_titre_type_partie_resultat.pack(pady=5, padx=5, side=TOP)

            #frame avec le canvas de la médaille en fonction des indices est du text correspondant de félicitation(sous-sous frame)
            Label_Frame_resultat_canvas_text = Frame(Label_Frame_resultat_titre_elements, bg='blue')
            Label_Frame_resultat_canvas_text.pack(side=TOP, pady=5, padx=5)

            Label_canvas_medailles = Canvas(Label_Frame_resultat_canvas_text, width=75, height=75)
            Label_canvas_medailles.pack(side=LEFT, pady=5, padx=5)

            text_medaille= StringVar()
            Label_text_resultat = Label(Label_Frame_resultat_canvas_text, textvariable=text_medaille)
            Label_text_resultat.pack(side=RIGHT, pady=5, padx=5)

            text_choix_medaille(type_partie, -1)
            Label_canvas_medailles.create_image(0,0,anchor=NW, image=img_resultat)

        else:
            ### ELEMENT POUR LA PARTIE SECONDE
            #Frame avec les elements des resulat (sous frame)
            Label_Frame_resultat_titre_elements = Frame(Label_Frame_global_resultat, bg = 'green')
            Label_Frame_resultat_titre_elements.pack(expand=True, fill=BOTH, pady=5, padx=5)

            Label_titre_type_partie_resultat = Label(Label_Frame_resultat_titre_elements, text = "seconde", anchor = NW)
            Label_titre_type_partie_resultat.pack(pady=5, padx=5, side=TOP)

            #frame avec le canvas de la médaille en fonction des indices est du text correspondant de félicitation(sous-sous frame)
            Label_Frame_resultat_canvas_text = Frame(Label_Frame_resultat_titre_elements, bg='blue')
            Label_Frame_resultat_canvas_text.pack(side=TOP, pady=5, padx=5)

            Label_canvas_medailles = Canvas(Label_Frame_resultat_canvas_text, width=75, height=75)
            Label_canvas_medailles.pack(side=LEFT, pady=5, padx=5)

            text_medaille= StringVar()
            Label_text_resultat = Label(Label_Frame_resultat_canvas_text, textvariable=text_medaille)
            Label_text_resultat.pack(side=RIGHT, pady=5, padx=5)

            text_choix_medaille(type_partie, 0)
            Label_canvas_medailles.create_image(0,0,anchor=NW, image=img_resultat)



            #### ELEMENT POUR LA PARTIE PREMIERE
            #Frame avec les elements des resulat (sous frame)
            Label_Frame_resultat_titre_elements2 = Frame(Label_Frame_global_resultat, bg = 'green')
            Label_Frame_resultat_titre_elements2.pack(expand=True, fill=BOTH, pady=5, padx=5)

            Label_titre_type_partie_resultat2 = Label(Label_Frame_resultat_titre_elements2, text = "premiere", anchor = NW)
            Label_titre_type_partie_resultat2.pack(pady=5, padx=5, side=TOP)

            #frame avec le canvas de la médaille en fonction des indices est du text correspondant de félicitation(sous-sous frame)
            Label_Frame_resultat_canvas_text2 = Frame(Label_Frame_resultat_titre_elements2, bg='blue')
            Label_Frame_resultat_canvas_text2.pack(side=TOP, pady=5, padx=5)

            Label_canvas_medailles2 = Canvas(Label_Frame_resultat_canvas_text2, width=75, height=75)
            Label_canvas_medailles2.pack(side=LEFT, pady=5, padx=5)

            text2_medaille= StringVar()
            Label_text_resultat2 = Label(Label_Frame_resultat_canvas_text2, textvariable=text2_medaille)
            Label_text_resultat2.pack(side=RIGHT, pady=5, padx=5)

            text_choix_medaille(type_partie, 1)
            Label_canvas_medailles2.create_image(0,0,anchor=NW, image=img_resultat2)




    else:
        Label_Titre_Credits = Label(Jeu, text = "Crédits")
        Label_Titre_Credits.pack(pady=15)
    
    Jeu.mainloop()




##################################################################################################
#ACCUEIL#
def verif_lancement():
    global type_partie
    global Niveau
    if Label_choix_partie_courte.get() ==1:
        if Label_partie_courte_selection.get() == "seconde":
            type_partie = 'seconde'
            Gestion_Jouer(Lancement, Niveau, type_partie)
        elif Label_partie_courte_selection.get() == "premiere":
            type_partie = 'premiere'
            Niveau = 5
            Gestion_Jouer(Lancement, Niveau, type_partie)
        else:
            text_erreur_lancement.set("Vous devez sélectionner le niveau de votre partie courte !")
    elif Label_choix_partie_long.get() ==1:
        type_partie = 'all'
        Gestion_Jouer(Lancement, Niveau, type_partie)
    else:
        text_erreur_lancement.set("Vous devez sélectionner le type de partie !")

def desac_btn_1():
    if Label_choix_partie_courte.get() ==1:
        Label_choix_partie_long.set(0)
        btn_long.config(state=DISABLED)
        btn_court_seconde.config(state=NORMAL)
        btn_court_premiere.config(state=NORMAL)
    else:
        btn_long.config(state=NORMAL)
        btn_court_seconde.config(state=DISABLED)
        btn_court_premiere.config(state=DISABLED)


def desac_btn_2():
    if Label_choix_partie_long.get() ==1:
        Label_choix_partie_courte.set(0)
        btn_court.config(state=DISABLED)
        btn_court_seconde.config(state=DISABLED)
        btn_court_premiere.config(state=DISABLED)
    else:
        btn_court.config(state=NORMAL)
        btn_court_seconde.config(state=NORMAL)
        btn_court_premiere.config(state=NORMAL)


global Niveau
Niveau = 0

Lancement = Tk()
Lancement.title("Maze-Maths : Lancement  Théo | Quentin")
Lancement.geometry("350x400")
Lancement.config(bg = "#BBC4E3")

Label_titre_lancement = Label(Lancement, text="Maze-Maths",fg = "#01548d", font=("Arial", 25),bg = "#BBC4E3")
Label_titre_lancement.pack(pady = 10)

#frame global du choix
Frame_choix = Frame(Lancement, bg = '#99A6D0')
Frame_choix.pack(expand=True, fill='x', padx=5, pady=5)

Label_titre_choix_lancement = Label(Frame_choix, text="Choix du type de partie", anchor=CENTER, bg = "#99A6D0")
Label_titre_choix_lancement.pack(pady = 5, side=TOP)

###frame partie gauche
Frame_choix_gauche = Frame(Frame_choix, bg=  None)
Frame_choix_gauche.pack(expand=True, fill='x', pady=5, padx=5, side=LEFT)

Label_choix_partie_courte = IntVar()
btn_court = Checkbutton(Frame_choix_gauche,variable = Label_choix_partie_courte, text="Courte", command=desac_btn_1)
btn_court.pack()

##Frame pour le choix de partie courte
Frame_choix_courte_selection = Frame(Frame_choix_gauche, bg= None)
Frame_choix_courte_selection.pack(pady= 5 , padx = 5)

Label_partie_courte_selection = StringVar()
btn_court_seconde = Radiobutton(Frame_choix_courte_selection, text="Seconde", variable=Label_partie_courte_selection, value='seconde', state=DISABLED)
btn_court_seconde.pack(pady=5, padx=5)

btn_court_premiere = Radiobutton(Frame_choix_courte_selection, text="Première", variable=Label_partie_courte_selection, value='premiere', state=DISABLED)
btn_court_premiere.pack(pady=5, padx=5)

###frame partie droite
Frame_choix_droite = Frame(Frame_choix, bg=  None)
Frame_choix_droite.pack(expand=True, fill=BOTH, pady=5, padx=5, side=RIGHT)

Label_choix_partie_long = IntVar()
btn_long = Checkbutton(Frame_choix_droite,variable = Label_choix_partie_long, text="Longue", command=desac_btn_2)
btn_long.pack()

Frame_ = Frame(Lancement, bg = '#99A6D0')
Frame_.pack(expand=True, fill=BOTH)

btn = ttk.Button(Frame_, text="Jouer !",command=verif_lancement).pack( pady=20)

text_erreur_lancement = StringVar()
Label_text_erreur_lancement = Label(Frame_, textvariable=text_erreur_lancement,bg = "#99A6D0", wraplength = 200, justify='center', fg='#9A0004')
Label_text_erreur_lancement.pack()


Lancement.mainloop()
##################################################################################################

