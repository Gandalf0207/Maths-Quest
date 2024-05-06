### EN FONCTION DU NIVEAU IL FAUT SET UP LA GENERATION / CUSTOM / TEXT DES PNJ ET ITEMS ###

from tkinter import *
from tkinter import ttk
import random
import time 

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


import labyrinthe
import custom_labyrinthe
import py_maths_exo

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


def Gestion_Jouer(fenetre, Niveau):

    global Label_btn_suivant_discussion_pnj
    Label_btn_suivant_discussion_pnj = None

    # Variable pour suivre l'état de la deuxième fenêtre pour les problèmes de la porte
    global second_window_probleme
    second_window_probleme= None

    #le "fenetre" correspond à la fenetre tk qui est en cours de loop
    # Le permir passage se sera la fenetre 'Lancement', puis les autres tours se sera les fenetres de 'Jeu'
    # Ce fonctionnement permet de faire tourner le programme pour le nombre de niveaux disponible !
    fenetre.destroy()


    Jeu = Tk()

    #On crée la map 
    longueur = 38
    largeur = 20
    L = labyrinthe.mapmaker(longueur,largeur) 

    #On custom la map avec les pnj, portes et joueur....
    L = custom_labyrinthe.Custom_Map(L, longueur, largeur, Niveau)


    #On load les img pour pouvoir les afficher

    porte = PhotoImage(file="image/porte.png")
    carre = PhotoImage(file="image/CARRE.png")
    craft_table_ = PhotoImage(file="image/craft.png")

    Perso = PhotoImage(file="image/perso.png")

    pnj1 = PhotoImage(file = "image/pnj1.png")
    pnj2 = PhotoImage(file = "image/pnj2.png")
    pnj3 = PhotoImage(file = "image/pnj3.png")
    pnj4 = PhotoImage(file = "image/pnj4.png")
    pnj5 = PhotoImage(file = "image/pnj4.png")

    pnj1_grand = PhotoImage(file="image/sorcier1.png")
    pnj2_grand = PhotoImage(file="image/sorcier2.png")
    pnj3_grand = PhotoImage(file="image/sorcier3.png")
    pnj4_grand = PhotoImage(file="image/sorcier4.png")
    pnj5_grand = PhotoImage(file = "image/pnj4.png")

    clepnj1 = PhotoImage(file="image/clepnj1.png")
    clepnj2 = PhotoImage(file="image/clepnj2.png")
    clepnj3 = PhotoImage(file="image/clepnj3.png")
    clepnj1_ = PhotoImage(file="image/clepnj1_.png")
    clepnj2_ = PhotoImage(file="image/clepnj2_.png")
    clepnj3_ = PhotoImage(file="image/clepnj3_.png")

    glue2 = PhotoImage(file="image/glue.png")
    glue = PhotoImage(file="image/glue0.png")

    mur1 = PhotoImage(file="image/Wall1.png")
    mur2 = PhotoImage(file="image/Wall2.png")
    mur3 = PhotoImage(file="image/Wall3.png")



    #On affiche dans le terminal pour check
    for i in range(len(L)):
        print(*L[i], sep=" ")
        
    #Fonction qui gère le déplacement du personnage; MAJ de la map tkinter, les interractions avec les pnj
    def deplacement(event):
        
        global ordonne
        global abscisse

        touche = event.keysym
        check = ["■" ,"\U0001F6AA", "¤"]
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
        #verif si table de craft dispo et si oui on affiche le msg d'information
        if L[ordonne][abscisse-1] == "¤":
            Label_text_possibilite_strvar.set("Appuie sur 'C' pour assembler la grande Clé !")
            canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=craft_table_)

        #check si c'est la porte et on met à jour les infos dans le cadre e bas à gauche
        elif (L[ordonne-1][abscisse] == "\U0001F6AA" or L[ordonne+1][abscisse]== "\U0001F6AA" or L[ordonne][abscisse-1]== "\U0001F6AA" or L[ordonne][abscisse+1]== "\U0001F6AA"):
            Label_text_possibilite_strvar.set("Appuie sur 'espace' pour ouvrir la porte !")
            canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=porte)


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
            if Niveau ==0:
                if pnj1_infos == False or pnj2_infos == False or pnj3_infos == False:
                    Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés !")
                elif assemble_cle == False:
                    Label_text_possibilite_strvar.set("Objectif : Assembler la clé à la table de fabrication !")
                elif assemble_cle == True:
                    Label_text_possibilite_strvar.set("Objectif : Ouvrir la porte !")
            elif Niveau ==1:
                if pnj1_infos == False or pnj2_infos == False or pnj3_infos == False or pnj3_infos == False:
                    Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés et le tube de colle !")
                elif assemble_cle == False:
                    Label_text_possibilite_strvar.set("Objectif : Assembler la clé à la table de fabrication !")
                elif assemble_cle == True:
                    Label_text_possibilite_strvar.set("Objectif : Ouvrir la porte !")
            elif Niveau ==2:
                if pnj1_infos == False or pnj2_infos == False or pnj3_infos == False or pnj3_infos == False and pnj5_infos == False:
                    Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés, le tube de colle et le kit de nettoyage !")
                elif assemble_cle == False:
                    Label_text_possibilite_strvar.set("Objectif : Assembler la clé à la table de fabrication !")
                elif assemble_cle == True:
                    Label_text_possibilite_strvar.set("Objectif : Ouvrir la porte !")


            canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=carre)
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

            if Niveau == 0:
                canvas_inv.create_image(10,0, anchor = NW, image=clepnj1)
                canvas_inv.create_image(60,0, anchor = NW, image=clepnj2)
                canvas_inv.create_image(110,0, anchor = NW, image=clepnj3)

            elif Niveau == 1 :
                canvas_inv.create_image(30,0, anchor = NW, image=clepnj1)
                canvas_inv.create_image(80,0, anchor = NW, image=clepnj2)
                canvas_inv.create_image(130,0, anchor = NW, image=clepnj3)

            elif Niveau ==2:

                canvas_inv.create_image(30,0, anchor = NW, image=clepnj1)
                canvas_inv.create_image(80,0, anchor = NW, image=clepnj2)
                canvas_inv.create_image(130,0, anchor = NW, image=clepnj3)

        else:
            if pnj1_infos == False and pnj2_infos == False and pnj3_infos == False and pnj4_infos == False and pnj5_infos == False:
                canvas_inv.create_image(0,0, anchor = NW, image=clepnj1)
                canvas_inv.create_image(60,0, anchor = NW, image=clepnj2)
                canvas_inv.create_image(120,0, anchor = NW, image=clepnj3)
                if Niveau == 1:
                    canvas_inv.create_image(180,0, anchor = NW, image=glue)
                elif Niveau ==2:
                    canvas_inv.create_image(180,0, anchor = NW, image=glue)
                    canvas_inv.create_image(240,0, anchor = NW, image=glue)


            if pnj1_infos == True:
                canvas_inv.create_image(0,0, anchor = NW, image=clepnj1)

            if pnj2_infos == True:
                canvas_inv.create_image(60,0, anchor = NW, image=clepnj2)

            if pnj3_infos == True:
                canvas_inv.create_image(120,0, anchor = NW, image=clepnj3)
            
            if pnj4_infos == True:
                canvas_inv.create_image(180,0, anchor = NW, image=glue2)

            if pnj5_infos == True:
                canvas_inv.create_image(240,0, anchor = NW, image=glue2)

    def load_cours(Niveau, num_pnj):
        Liste_cours = [
        "Pour résoudre une équation du 1er degré il faut bien faire gaffe à respecter l’égalité partout. Oublie pas surtout ! Et tiens voilà pour m’avoir écouté.",
        "Quand tu résous une équation s’il y a des x des deux côtés essaie de tout mettre du même ce sera plus simple tu verras ! T’aurais pas des croquettes contre mon os doré ?”)",
        "Il faut toujours annuler l’opération qui est venu en dernier lors du calcul, pour te souhaiter bon courage je te passe ce bidule, il appartient à mon mari redonne lui si tu le vois en ville.", 
        
        "cours 1 nv2",
        "cours 2 nv2",
        "cours 3 nv2",
        "cours 4 nv2",
        
        "cours 1 nv3",
        "cours 2 nv3",
        "cours 3 nv3",
        "cours 4 nv3",
        "cours 5 nv3",
        ]

        def ajouter_element(Texte): #Une partie de la gestion du code de la liste box provient d'internet
            global listbox
            element = Texte.strip()
            if element:
                listbox.insert(END, element + "\n")
            listbox.insert(END, "\n")

        if num_pnj ==0:
            global listbox
            listbox = Text(Label_Frame_Cours_Affiche, width =35,wrap="word")
            listbox.pack(side=LEFT, fill=BOTH)

            scrollbar = Scrollbar(Label_Frame_Cours_Affiche, orient=VERTICAL, command=listbox.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            listbox.config(yscrollcommand=scrollbar.set)

            #chargement pour le reload de la fonction global quand on change de niveau
            if Niveau ==0:
                listbox.insert(END, "--Equation du 1er degré--" + "\n")
                listbox.insert(END, "\n")

            if Niveau ==1:
                listbox.insert(END, "--Equation du 1er degré--" + "\n")
                listbox.insert(END, "\n")

                for i in range(3):
                    ajouter_element(Liste_cours[i])
                listbox.insert(END, "\n")

                listbox.insert(END, "--Equation à deux inconnues--" + "\n")
                listbox.insert(END, "\n")

            elif Niveau ==2:
                listbox.insert(END, "--Equation du 1er degré--" + "\n")
                listbox.insert(END, "\n")
                for i in range(3):
                    ajouter_element(Liste_cours[i])
                listbox.insert(END, "\n")

                listbox.insert(END, "--Equation à deux inconnues--" + "\n")
                listbox.insert(END, "\n")
                for i in range(3,7):
                    ajouter_element(Liste_cours[i])
                listbox.insert(END, "\n")

                listbox.insert(END, "--Exos à définir--" + "\n")
                listbox.insert(END, "\n")

            elif Niveau ==3:
                listbox.insert(END, "--Equation du 1er degré--" + "\n")
                listbox.insert(END, "\n")
                for i in range(3):
                    ajouter_element(Liste_cours[i])
                listbox.insert(END, "\n")

                listbox.insert(END, "--Equation à deux inconnues--" + "\n")
                listbox.insert(END, "\n")
                for i in range(3,7):
                    ajouter_element(Liste_cours[i])
                listbox.insert(END, "\n")

                listbox.insert(END, "--Exos à définir--" + "\n")
                listbox.insert(END, "\n")
                for i in range(7,12):
                    ajouter_element(Liste_cours[i])
                listbox.insert(END, "\n")


        # Pour chack pnj qui donnera son cours : 
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

    def table_craft(event):
        global pnj1_infos
        global pnj2_infos
        global pnj3_infos
        global pnj4_infos
        global pnj5_infos

        global assemble_cle

        if L[ordonne][abscisse-1] == "¤":
            if assemble_cle == False:

                if Niveau ==0:
                    if pnj1_infos == True and pnj2_infos == True and pnj3_infos == True:
                        assemble_cle = True
                        load_inv(Niveau)
                        Label_text_possibilite_strvar.set("Vous avez fabriqué la grande Clé !")

                    else:
                        Label_text_possibilite_strvar.set("Vous n'avez pas collecté toutes les clés !")


                elif Niveau == 1:
                    if pnj1_infos == True and pnj2_infos == True and pnj3_infos == True and pnj4_infos == True:
                        assemble_cle = True
                        load_inv(Niveau)
                        Label_text_possibilite_strvar.set("Vous avez fabriqué la grande Clé !")
                    else:
                        if pnj4_infos == False:
                            Label_text_possibilite_strvar.set("Vous n'avez pas collecté le bâton de colle !")
                        else:
                            Label_text_possibilite_strvar.set("Vous n'avez pas collecté toutes les clés !")
           
                elif Niveau == 2:
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
                            text_complet = "Leilégalité : B’jour jeune aventurier, je pense que j’pourrais bien t’apprendre un truc aujourd’hui. "
                        elif c==2:
                            text_complet = "Leilégalité : Pour résoudre une équation du 1er degré il faut bien faire gaffe à respecter l’égalité partout. Oublie pas surtout ! Et tiens voilà pour m’avoir écouté."
                        elif c==3:
                            text_complet = "Leilégalité : Bravo ! Vous avez obtenu 1 fragment de clé !"

                    elif Niveau ==1:
                        if c==1:
                            text_complet = ""
                        elif c==2:
                            text_complet = ""
                        elif c==3:
                            text_complet = ""

                    elif Niveau ==2:
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
                            text_complet = "Iggy : Wouf Wouf, Wouf Wouf Wouf, Wouf Wouf Woaf ! Wouf ?(Votre chien est un peu rouillé mais vous comprenez : “Salut moi c’est Iggy, retiens bien ce que je vais te dire !"
                        elif c==2:
                            text_complet = "Iggy : Quand tu résous une équation s’il y a des x des deux côtés essaie de tout mettre du même ce sera plus simple tu verras ! T’aurais pas des croquettes contre mon os doré ?”)"
                        elif c==3:
                            text_complet = "Iggy : Bravo ! Vous avez obtenu 1 fragment de clé !"

                    elif Niveau ==1:
                        if c==1:
                            text_complet = ""
                        elif c==2:
                            text_complet = ""
                        elif c==3:
                            text_complet = ""

                    elif Niveau ==2:
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
                            text_complet = "Mathémami : Qu’est ce tu dis ?! Que tu n’as pas parlé ? Autant pour moi mon petit mes oreilles ne fonctionnent plus aussi bien qu’avant, j’ai l’impression que t’essais d’aller en ville pour passer il te faudra savoir que pour progresser dans une équation."
                        elif c==2:
                            text_complet = "Mathémami : Il faut toujours annuler l’opération qui est venu en dernier lors du calcul, pour te souhaiter bon courage je te passe ce bidule, il appartient à mon mari redonne lui si tu le vois en ville. "
                        elif c==3:
                            text_complet = "Mathémami : Bravo ! Vous avez obtenu 1 fragment de clé !"

                    elif Niveau ==1:
                        if c==1:
                            text_complet = ""
                        elif c==2:
                            text_complet = ""
                        elif c==3:
                            text_complet = ""

                    elif Niveau ==2:
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
                            text_complet = ""
                        elif c==2:
                            text_complet = ""
                        elif c==3:
                            text_complet = "Bravo ! Vous avez obtenue un bâton de colle !"

                    elif Niveau ==2:
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
                if c ==1:
                    if pnj=="pnj4":
                        text_complet = "Vous avez déjà obtenu le bâton de colle de ce sorcier !" 
                    elif pnj == "pnj5":
                        text_complet = "Vous avez déjà obtenu le kit de nettoyage ! !" 
                    else:
                        text_complet = "Vous avez déjà obtenu le fragment de clé de ce sorcier !" 
                elif c == 2 :
                    text_complet = "Vous pouvez consulter la partie du cours obtenue dans la page 'cours'. bla bla vlblslki sd f  g d d s gsd ds s df d dg'"
                elif c == 3 : 
                    #on clear si jamais la personne s'en va
                    canvas_tete_pnj_grand.delete("all")
                    Label_texte_parole_discussion_pnj_strvar.set("")
                    #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
                    if Label_btn_suivant_discussion_pnj is not None:
                        if Label_btn_suivant_discussion_pnj.winfo_exists():
                            Label_btn_suivant_discussion_pnj.destroy()
                    c = 0



            if (c < 4 and pnj_infos == False) or (c < 3 and pnj_infos == True):

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
                    canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj1_grand)
            
                global Label_btn_suivant_discussion_pnj

                if Label_btn_suivant_discussion_pnj is not None:
                    if Label_btn_suivant_discussion_pnj.winfo_exists():
                        Label_btn_suivant_discussion_pnj.destroy()
                #On crée le bouton pour faire discuter le pnj avec l'utilisateur et on set le texte de bienvenue          
                Label_texte_parole_discussion_pnj_strvar.set("Salut ! Clique sur suivant !")
                Label_btn_suivant_discussion_pnj = Button(Label_Frame_Discussion_pnj, text="Suivant", command=lambda: affiche_prog(pnj_, pnj_infos_, Niveau))
                Label_btn_suivant_discussion_pnj.pack(side=BOTTOM, anchor="e", pady=5)
        
        # check si autour il y a la porte ou non
        elif (L[ordonne-1][abscisse] == "\U0001F6AA" or L[ordonne+1][abscisse]== "\U0001F6AA" or L[ordonne][abscisse-1]== "\U0001F6AA" or L[ordonne][abscisse+1]== "\U0001F6AA"):
            global assemble_cle
            print(assemble_cle)
            if assemble_cle == True:
                porte_enigme(Niveau)
            else:
                Label_text_possibilite_strvar.set("Vous devez d'abord assemblé votre Clé pour pouvoir ouvrir la porte !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=porte)



        else:
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
                        text_complet_consignes = "Vous devez résoudre cette equation à deux inconnues n trouvant l valeur de y et y. Apres avoir résolu cette equation; selectionnez la bonne case et faites valider"
                    elif Niveau ==2:
                        text_complet_consinges = "Vous devez résoudre cette exo pas encore fait"
                elif c_sw==4:
                    Label_btn_suivant_second_window ['state'] = DISABLED
                    # on affcihe les btns de réponses
                    Label_btn_result_possible_1 = Button(Label_Frame_Reponse_Verif, text=value_btn_1, command=lambda:verif_reponse_sw(value_btn_1,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                    Label_btn_result_possible_1.pack(side="left", padx = 5, pady = 5)

                    Label_btn_result_possible_2 = Button(Label_Frame_Reponse_Verif, text=value_btn_2, command=lambda:verif_reponse_sw(value_btn_2,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                    Label_btn_result_possible_2.pack(side ='left', padx = 5, pady = 5)

                    Label_btn_result_possible_3 = Button(Label_Frame_Reponse_Verif, text=value_btn_3, command=lambda:verif_reponse_sw(value_btn_3,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                    Label_btn_result_possible_3.pack(side='left', padx= 5, pady = 5)
                elif c_sw==5:
                    if erreur == 0:
                        text_complet_consignes = "Bravo ! Vous avez trouvé la bonne solution !"
                    else:
                        text_complet_consignes = "Vous n'avez pas trouvé la bonne solution, cliquez sur suivant pour recommencer !"

                elif c_sw==6:
                    if erreur == 0:
                        if Niveau ==0:
                            text_complet_consignes ="avant de passez la porte vous découvrez un message gravé dessus msg nv1 : Cliquez sur suivant pour passez au niveau suppérieur !"
                        elif Niveau ==1:
                            text_complet_consignes ="avant de passez la porte vous découvrez un message gravé dessus msg nv2: Cliquez sur suivant pour passez au niveau suppérieur !"
                        elif Niveau ==3:
                            text_complet_consignes ="avant de passez la porte vous découvrez un message gravé dessus msg nv3: Cliquez sur suivant pour passez au niveau suppérieur !"

                    else:
                        second_window_probleme.destroy()

                else:
                    Niveau +=1
                    second_window_probleme.destroy()
                    Gestion_Jouer(Jeu, Niveau)



                
                if  4 > c_sw  or 5 <= c_sw <7:

                    Label_btn_suivant_second_window ['state'] = DISABLED
                    for i in range(len(text_complet_consignes)):
                        text_partiel_second_window = text_complet_consignes[:i+1]
                        Label_Text_Explication_Exercice_strvar.set(f"{text_partiel_second_window}")
                        Label_Text_Explication_Exercice_widget.update()
                        time.sleep(0.03)
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

                ok = 1
            
            global c_sw
            c_sw = 0

            second_window_probleme = Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
            # second_window_probleme.geometry("400x600") 
            # on recupère la formule et la correction
            Exo_correction = py_maths_exo.choix_exo_niveau(Niveau)
            print(Exo_correction)

            ####frame global de la fenetre
            Label_Frame_global_second_window = Frame(second_window_probleme, bg = "yellow")
            Label_Frame_global_second_window.pack(expand=True, fill="both")

            ###frame qui conteintdra toutes les consignes / explications et le btn suivant
            Label_Frame_Canvas_consignes_explication_btn = Frame(Label_Frame_global_second_window, bg="#000000")
            Label_Frame_Canvas_consignes_explication_btn.pack(side=TOP, fill='x', pady= 5, padx=5)

            #on load les element de consignes
            Label_Text_Explication_Exercice_strvar = StringVar()
            Label_Text_Explication_Exercice_strvar.set("Cliquez sur suivant !")
            Label_Text_Explication_Exercice_widget = Label(Label_Frame_Canvas_consignes_explication_btn,wraplength=300, textvariable = Label_Text_Explication_Exercice_strvar, justify="left"  )
            Label_Text_Explication_Exercice_widget.pack(fill='x',side = LEFT, padx= 5, pady=5)
            Label_btn_suivant_second_window = Button(Label_Frame_Canvas_consignes_explication_btn, text="Suivant !", command=lambda:affiche_consigne(Niveau))
            Label_btn_suivant_second_window.pack(side=TOP, anchor="e", pady=5, padx=5)

            ### frame qui contient le canvas qui affichera la formule
            Label_Frame_Canvas_formule_exo = Frame(Label_Frame_global_second_window, bg="#000000")
            Label_Frame_Canvas_formule_exo.pack(side=TOP, fill='y', pady= 5, padx=5)

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

            ## Frame qui contient les trois valeur de réponse avec les cases à cocher et le bouton valider
            Label_Frame_Reponse_Verif = Frame(Label_Frame_global_second_window, bg= "#000000")
            Label_Frame_Reponse_Verif.pack(side=TOP, fill='x', pady= 5, padx=5)

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

        
    def regle_infos_jeu(event):
        Regle = Toplevel()
        Regle.geometry("600x400")
        Label_titre_regle = Label(Regle, text="Maze-Thon : Règles").pack(pady=5)

        Label_Frame_Touche = Frame(Regle, bg = "#000000")
        Label_Frame_Touche.pack(expand=True, fill="both")

        Label_frame_1 = Frame(Label_Frame_Touche, bg = "blue", width=250)
        Label_frame_1.pack(fill='y', side=LEFT, pady=5, padx=5)

        Label_touche_box = Frame(Label_frame_1, height=200, bg="white", width=250)
        Label_touche_box.pack(fill='x', padx=5, pady=5, side = TOP)


        close_btn = Button(Regle, command=Regle.destroy, text="Fermer").pack(side=BOTTOM)
        Regle.mainloop()


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
    pnj1_infos = False
    pnj2_infos = False
    pnj3_infos = False
    pnj4_infos = False  
    pnj5_infos = False

    # quad un elment est fabriqué, pour l'afficher correctement

    global assemble_cle
    assemble_cle = False

 



    # Jeu.geometry("1300x700")
    ######On place tout les elements sur la fenetre#####

    #####Frame global qui contient les deux partie du jeu
    Label_Frame_Global = Frame(Jeu, bg='yellow')
    Label_Frame_Global.pack(expand=True, fill="both")

    ####Partie Gauche : 
    Label_Frame_Jeu_Inv = Frame(Label_Frame_Global, bg='#000000') 
    Label_Frame_Jeu_Inv.pack(side = 'left', fill='y', padx=5, pady=5)

    #Jeu partie Gauche haut : 
    long_c = len(L[0])*24
    larg_c = len(L)*24
    canvas = Canvas(Label_Frame_Jeu_Inv, width=long_c, height=larg_c)

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
    canvas.pack(side="top",padx=5, pady=5)

    ###Frame gauche bas pour clé + pouvoir parler infos
    Label_Frame_pnj_Text = Frame(Label_Frame_Jeu_Inv, bg="red")
    Label_Frame_pnj_Text.pack(side=TOP, fill='x',padx=5, pady=5)

    ##Frame affiche le texte si on peut parler à un pnj ou faire un action
    Label_Frame_Text_Info_Discussion_pnj = Frame(Label_Frame_pnj_Text, bg="blue")
    Label_Frame_Text_Info_Discussion_pnj.pack(fill='y', padx=5, pady=5, side='left')

    #On load les elements pour afficher les msg de possibilité de discution 
    canvas_infos_possibilite_discussion = Canvas(Label_Frame_Text_Info_Discussion_pnj, bg='white', height=50, width=50)
    canvas_infos_possibilite_discussion.pack(anchor="c", side=LEFT, padx=15)
    Label_text_possibilite_strvar = StringVar()
    if Niveau ==0:
        Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés !")
    elif Niveau ==1:
        Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés et le tube de colle !")
    elif Niveau ==2:
        Label_text_possibilite_strvar.set("Objectif : Récupérer tous les fragments de clés,le tube de colle et le kit de nettoyage !")

    Label_text_possibilite_widget = Label(Label_Frame_Text_Info_Discussion_pnj, textvariable=Label_text_possibilite_strvar, wraplength=200, justify="left")
    Label_text_possibilite_widget.pack(side="left", pady=5, padx=5)
   
    ## Frame de box de discussion avec les pnj 
    Label_Frame_Discussion_pnj = Frame(Label_Frame_pnj_Text, bg="blue")
    Label_Frame_Discussion_pnj.pack(expand=True, fill=BOTH, padx=5, pady=5, side='right')

    #On load les element qui serviron aux boites de discussion des pnjs
    canvas_tete_pnj_grand = Canvas(Label_Frame_Discussion_pnj, bg='white', height=100, width=200)
    canvas_tete_pnj_grand.pack(anchor="c", padx=10,pady=5, side=LEFT)
    Label_texte_parole_discussion_pnj_strvar = StringVar()
    Label_texte_parole_discussion_pnj_widget = Label(Label_Frame_Discussion_pnj, textvariable=Label_texte_parole_discussion_pnj_strvar, wraplength=320, justify="left")
    Label_texte_parole_discussion_pnj_widget.pack(side=LEFT, padx=5, pady=5)



    ####Partie Droite : 
    Label_Frame_Cours_cle = Frame(Label_Frame_Global, bg="#000000")
    Label_Frame_Cours_cle.pack(side='right', expand=True, fill="both", padx=5, pady=5)

    ##Frame qui affiche le cours actuel
    Label_Frame_Cours_Affiche = Frame(Label_Frame_Cours_cle,bg='white')
    Label_Frame_Cours_Affiche.pack(side='top', expand=True, fill="both", padx=5, pady=5)

    #On load le cours actuel : 
    load_cours(Niveau,0)
    
    ##Frame affiche l'inventaire (clé(s))
    Label_Frame_Inv_Cle = Frame(Label_Frame_Cours_cle, bg='white')
    Label_Frame_Inv_Cle.pack(side='bottom', padx=5, pady=5, fill='x')

    #On load l'inventaire de base 
    long_canvas_inv = 180
    if Niveau ==1:
        long_canvas_inv = 240
    elif Niveau == 2:
        long_canvas_inv = 300

    canvas_inv = Canvas(Label_Frame_Inv_Cle, width=long_canvas_inv, height=50, bg = "blue")
    canvas_inv.create_image(0,0,anchor=NW, image = clepnj1_)
    canvas_inv.create_image(60,0,anchor=NW, image = clepnj2_)
    canvas_inv.create_image(120,0,anchor=NW, image = clepnj3_)
    if Niveau == 1:
        canvas_inv.create_image(180,0,anchor=NW, image = glue)
    elif Niveau ==2:
        canvas_inv.create_image(180,0,anchor=NW, image = glue)
        canvas_inv.create_image(240,0,anchor=NW, image = glue)

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


    Jeu.mainloop()






##################################################################################################
#ACCUEIL#

global Niveau
Niveau = 1

Lancement = Tk()
Lancement.title("RPG : Lanncement  Théo | Quentin")

Lancement.geometry("350x400")

Frame_ = ttk.Frame(Lancement, bg = None)


btn = ttk.Button(Frame_, text="Jouer !",command=lambda:Gestion_Jouer(Lancement, Niveau)).pack( pady=20)
Frame_.pack()

Lancement.mainloop()
##################################################################################################

