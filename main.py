#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################



# DEBUT main # 



# Ce script est le fichier principal, il execute toutes les fonctions et fait appel aux autres fichier secondaire pour récupérer les informations nécéssaires


# Importantion des modules
from tkinter import * # Module de GUI
from tkinter import scrolledtext # Module de GUI
from tkinter import font, Toplevel # Module de GUI
import random # Module de l'aléatoire
import time  # Module du temps
import webbrowser # Module pour ouvrir dans le navigateur

from matplotlib.figure import Figure # Module de graphique
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Module de graphique
import matplotlib.pyplot as plt # Module de graphique


# Importation des scripts secondaires
import labyrinthe
import custom_labyrinthe
import py_maths_exo
import py_maths_boss
import formule_latex

# Élément permettant l'utilisation des dépendances latex, nécéssaires  à la création des images avec le bon affichage
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

### Pour avoir une certaine sécurité lors de la récupération des fragements de clé ou autre; il a fallut faire en sorte
# de ne pourvoir ouvrir qu'une seule fenetre à la fois. Il est donc impossible, d'ouvrir plus de 1 fois la meme fenetre en meme temps

# Variable pour suivre l'état de la deuxième fenêtre en fonction des elements
global Label_btn_suivant_discussion_pnj
Label_btn_suivant_discussion_pnj = None

global second_window_probleme
second_window_probleme= None

global boss_window
boss_window= None

global Regle
Regle= None

global f
f = None

global new_window_admin
new_window_admin = None



# Valeurs permettant de déterminer le nombre d'indice utilisé et de pouvoir afficher le résultat
global indices_give_1
global indices_give_2
indices_give_1 = 0
indices_give_2 = 0

def Gestion_Jouer(fenetre, Niveau, type_partie): #Fonction parent (gestion de tout le script), elle est reload pour changer de niveau 

    # Variable pour suivre l'état de la deuxième fenêtre en fonction des elements
    global Label_btn_suivant_discussion_pnj
    Label_btn_suivant_discussion_pnj = None

    global second_window_probleme
    second_window_probleme= None

    global boss_window
    boss_window= None

    global Regle
    Regle= None

    global deplacement_perso
    deplacement_perso = True

    global new_window_admin
    new_window_admin = None


    #on détruit la fenetre précédente
    fenetre.destroy()


    #création de la fenetre
    Jeu = Tk()
    Jeu.config(bg = "#BBC4E3")



    # La séquence de touches pour le code 'admin'
    konami_code = ['a', 'd', 'm', 'i', 'n']
    current_input = []

    def check_konami_code(event):
        # Ajouter la touche pressée à la sequence actuelle
        current_input.append(event.char)
        
        # Vérifier si la séquence actuelle dépasse la longueur du Konami Code (code admin)
        if len(current_input) > len(konami_code):
            current_input.pop(0)
        
        # Vérifier si la séquence actuelle correspond au Konami Code (code admin)
        if current_input == konami_code:
            open_new_window()

    def open_new_window():
        global new_window_admin # check pour ne pas ouvrir 2 fois la meme fenetre
        if not new_window_admin or not new_window_admin.winfo_exists():

            def check_command_admin(type_command): # fonction qui dépendant du paramètre, va executer les éléments admin sélectionnés
                #on recup les globals modifiables
                global Niveau
                global type_partie

                global pnj1_infos
                global pnj2_infos
                global pnj3_infos
                global pnj4_infos
                global pnj5_infos

                global assemble_cle

                global type_partie

                if type_command =="supnv": # on passe au niveau supérieur
                    if Niveau <9:
                        
                        Niveau +=1
                        Gestion_Jouer(Jeu, Niveau, type_partie) #reload pour passer au niveau suivant
                    else:
                        infos_label_admin.set("Vous êtes sur le dernier niveau possible, il n'existe aucun niveau superieur !") # infos si dernier niveau
                
                if type_command=='infnv': # on passe au niveau inférieur
                    if Niveau > 0:
                        Niveau -=1
                        Gestion_Jouer(Jeu, Niveau, type_partie) # reload pour passer au niveau inférieur
                    else:
                        infos_label_admin.set("Vous êtes sur le premier niveau possible, il n'existe aucun niveau inférieur !") # infos si premier niveau
                

                if type_command =='autre': # obtention des clés et de l'assemblage de la clé
                    
                    # on récupère les valeurs des checkbutton cochés ou non
                    p1 = var_pnj1_admin.get()
                    p2 = var_pnj2_admin.get()
                    p3 = var_pnj3_admin.get()
                    p4 = var_pnj4_admin.get()
                    p5 = var_pnj5_admin.get()
                    assemble_cle_admin = var_cle_admin.get()

                    #en fonction des valeurs, on donne ou non les fragments clés + assemble clé
                    if p1 == 0:
                        pnj1_infos = False
                    else:
                        pnj1_infos = True

                    if p2 == 0:
                        pnj2_infos = False
                    else:
                        pnj2_infos = True

                    if p3 == 0:
                        pnj3_infos = False
                    else:
                        pnj3_infos = True

                    if p4 == 0:
                        pnj4_infos = False
                    else:
                        pnj4_infos = True

                    if p5 == 0:
                        pnj5_infos = False
                    else:
                        pnj5_infos = True

                    if assemble_cle_admin ==0:
                        assemble_cle = False
                    else:
                        assemble_cle = True

                    load_inv(Niveau)


                    #on ferme apres la validation
                    new_window_admin.destroy()


                if type_command =='exo': # on affiche l'exo du cours / boss du niveau actuel (bypass pour éviter de prendre toutes les fragments de clés...)
                    if Niveau !=4 and Niveau !=8:
                        porte_enigme() #on ouvre la fenetre
                        load_cours(Niveau, 1) # on load le cours
                    else:
                        boss_enigme() #on ouvre la fenetre

                    #on ferme apres la validation
                    new_window_admin.destroy()

                if type_command =="game": # changement du type de partie (nombre de niveau ...)

                    type1_admin = type1_admin_game_intvar.get() # on récupère les valeurs sélectionnées (checkbutton)
                    type2_admin = type2_admin_game_intvar.get()
                    type3_admin = type3_admin_game_intvar.get()
                    
                    #on execute dépendemment de la fonction reload et on reset au début du type sélectionné, sauf pour 'all'
                    if type1_admin ==1:
                        type_partie = 'seconde'
                        Niveau = 0
                        Gestion_Jouer(Jeu, Niveau, type_partie)
                    elif type2_admin ==1:
                        type_partie = 'premiere'
                        Niveau = 5
                        Gestion_Jouer(Jeu, Niveau, type_partie)
                    elif type3_admin ==1:
                        type_partie = 'all'
                        Gestion_Jouer(Jeu, Niveau, type_partie)
                    


            #fonction pour supprimer la sélection des autres checkbuttons pour le choix de type de partie (coché / décoché)
            def check_type_partie_admin_checkbutton_1():
                type2_admin_game_intvar.set(0) 
                type3_admin_game_intvar.set(0)
            def check_type_partie_admin_checkbutton_2():
                type1_admin_game_intvar.set(0)
                type3_admin_game_intvar.set(0)
            def check_type_partie_admin_checkbutton_3():
                type1_admin_game_intvar.set(0)
                type2_admin_game_intvar.set(0) 


            #fenetre panel admin 
            new_window_admin = Toplevel()
            new_window_admin.title("Maths-Quest | Admin Panel      © PLADEAU Quentin LUBAN Théo") # titre (haut)


            label_admin = Label(new_window_admin, text="Panel Admin") # Titre
            label_admin.pack(pady=20, padx=20)

            #frame global des element modifiables (contient les petite frames)
            Label_frame_pack_admin = Frame(new_window_admin, bg = None)
            Label_frame_pack_admin.pack(expand=True, fill=BOTH, pady= 5, padx =5)

            #sous - frame par type d'elements
            Label_frame_gestion_niveau_admin = Frame(Label_frame_pack_admin, bg = "#99A6D0")
            Label_frame_gestion_niveau_admin.pack(side = LEFT, expand=True, fill=BOTH, pady = 5, padx = 5)

            btn_niv_supp = Button(Label_frame_gestion_niveau_admin, text="Niveau sup", command=lambda:check_command_admin('supnv')) # btn niveau sup
            btn_niv_supp.pack(padx = 5, pady = 5)

            btn_niv_inf = Button(Label_frame_gestion_niveau_admin, text="Niveau inf", command=lambda:check_command_admin('infnv')) # btn niveau inf
            btn_niv_inf.pack(padx = 5, pady = 5)

            #sous - frame get clé + cours des perso
            Label_frame_gestion_perso_admin = Frame(Label_frame_pack_admin, bg = "#99A6D0")
            Label_frame_gestion_perso_admin.pack(side = LEFT, expand=True, fill=BOTH, pady = 5, padx = 5)


            # en fonction du type des variables, on affiche si on possède les elements ou non (check / non check)
            if pnj1_infos == False:
                var_pnj1_admin = IntVar(value=0)
            else:
                var_pnj1_admin = IntVar(value=1)

            if pnj2_infos == False:
                var_pnj2_admin = IntVar(value=0)
            else:
                var_pnj2_admin = IntVar(value=1)

            if pnj3_infos == False:
                var_pnj3_admin = IntVar(value=0)
            else:
                var_pnj3_admin = IntVar(value=1)

            if pnj4_infos == False:
                var_pnj4_admin = IntVar(value=0)
            else:
                var_pnj4_admin = IntVar(value=1)

            if pnj5_infos == False:
                var_pnj5_admin = IntVar(value=0)
            else:
                var_pnj5_admin = IntVar(value=1)

            if assemble_cle == False:
                var_cle_admin = IntVar(value=0)
            else:
                var_cle_admin = IntVar(value=1)

            #les check buttons
            Label_checkbutton_pnj1_admin = Checkbutton(Label_frame_gestion_perso_admin, text="item, cours : pnj1", variable = var_pnj1_admin)
            Label_checkbutton_pnj2_admin = Checkbutton(Label_frame_gestion_perso_admin, text="item, cours : pnj2", variable = var_pnj2_admin)
            Label_checkbutton_pnj3_admin = Checkbutton(Label_frame_gestion_perso_admin, text="item, cours : pnj3", variable = var_pnj3_admin)
            Label_checkbutton_pnj4_admin = Checkbutton(Label_frame_gestion_perso_admin, text="item, cours : pnj4", variable = var_pnj4_admin)
            Label_checkbutton_pnj5_admin = Checkbutton(Label_frame_gestion_perso_admin, text="item, cours : pnj5", variable = var_pnj5_admin)

            Label_checkbutton_assemble_cle_admin = Checkbutton(Label_frame_gestion_perso_admin, text="assemble_cle", variable = var_cle_admin)
            
            Label_checkbutton_pnj1_admin.pack(side=TOP, pady =2, padx = 5)
            Label_checkbutton_pnj2_admin.pack(side=TOP, pady =2, padx = 5)
            Label_checkbutton_pnj3_admin.pack(side=TOP, pady =2, padx = 5)
            Label_checkbutton_pnj4_admin.pack(side=TOP, pady =2, padx = 5)
            Label_checkbutton_pnj5_admin.pack(side=TOP, pady =2, padx = 5)

            Label_checkbutton_assemble_cle_admin.pack(side=TOP, pady =2, padx = 5)

            # désactivation des éléments quand il ne sont pas présents sur le niveau en question
            if Niveau ==0 or Niveau == 5: 
                Label_checkbutton_pnj4_admin.config(state=DISABLED)
                Label_checkbutton_pnj5_admin.config(state=DISABLED) 
            elif Niveau == 1 or Niveau==6:
                Label_checkbutton_pnj5_admin.config(state=DISABLED)
            elif Niveau ==4 or Niveau ==8:
                Label_checkbutton_pnj1_admin.config(state=DISABLED)
                Label_checkbutton_pnj2_admin.config(state=DISABLED)
                Label_checkbutton_pnj3_admin.config(state=DISABLED)
                Label_checkbutton_pnj4_admin.config(state=DISABLED)
                Label_checkbutton_pnj5_admin.config(state=DISABLED)
                Label_checkbutton_assemble_cle_admin.config(state=DISABLED)


            #sous - frame box btn des exo / boss (ouverture porte)
            Label_frame_exo_boss_porte_admin =  Frame(Label_frame_pack_admin, bg = "#99A6D0")
            Label_frame_exo_boss_porte_admin.pack(side = LEFT, expand=True, fill=BOTH, pady = 5, padx = 5)

            Label_btn_exo_boss_porte_admin = Button(Label_frame_exo_boss_porte_admin, text = "Exo / Boss : porte", command=lambda:check_command_admin('exo'))
            Label_btn_exo_boss_porte_admin.pack(pady = 5, padx = 5)

            #sous - frame checkkbutton type partie choix
            Label_frame_check_button_typepartie = Frame(Label_frame_pack_admin, bg = "#99A6D0")
            Label_frame_check_button_typepartie.pack(side = LEFT, expand=True, fill=BOTH, pady = 5, padx = 5)

            # en fonction du type des variables, on affiche le type de partie acuel (coché" / décoché)
            if type_partie =='seconde':
                type1_admin_game_intvar = IntVar(value = 1)
            else:
                type1_admin_game_intvar = IntVar(value = 0)

            if type_partie =='premiere':
                type2_admin_game_intvar = IntVar(value = 1)
            else:
                type2_admin_game_intvar = IntVar(value = 0)
            
            if type_partie == 'all':
                type3_admin_game_intvar = IntVar(value = 1)
            else:
                type3_admin_game_intvar = IntVar(value = 0)

            #les check buttons
            type1_admin_game_checkbutton = Checkbutton(Label_frame_check_button_typepartie, variable = type1_admin_game_intvar, text = "partie : seconde", command =check_type_partie_admin_checkbutton_1 )
            type2_admin_game_checkbutton = Checkbutton(Label_frame_check_button_typepartie, variable = type2_admin_game_intvar, text = "partie : premiere", command = check_type_partie_admin_checkbutton_2)
            type3_admin_game_checkbutton = Checkbutton(Label_frame_check_button_typepartie, variable = type3_admin_game_intvar, text = "partie : all", command =check_type_partie_admin_checkbutton_3)

            type1_admin_game_checkbutton.pack(side = TOP, pady = 2, padx = 5)
            type2_admin_game_checkbutton.pack(side = TOP, pady = 2, padx = 5)
            type3_admin_game_checkbutton.pack(side = TOP, pady = 2, padx = 5)

            # infos 
            Label_infos_text_btn_type_partie_admin = Label(Label_frame_check_button_typepartie, text = "Attention, ce bouton reset l'avancée au début du type sélectionné sauf pour 'all',", wraplength = 100)
            Label_infos_text_btn_type_partie_admin.pack(side =BOTTOM, padx = 4, pady = 5)

            Label_btn_valider_type_partie_special_admin = Button(Label_frame_check_button_typepartie, text="Valid Type", command=lambda:check_command_admin('game'), fg = 'red')
            Label_btn_valider_type_partie_special_admin.pack(side=BOTTOM, pady = 2, padx = 5)

            
            Label_valider_changements_admin = Button(new_window_admin, text="VALIDER", command=lambda:check_command_admin('autre'))
            Label_valider_changements_admin.pack(pady= 5, padx = 5)




            infos_label_admin = StringVar()
            label_widget_infos_admin = Label(new_window_admin, textvariable = infos_label_admin, fg = "red", wraplength = 250)
            label_widget_infos_admin.pack(side = BOTTOM, pady = 5, padx = 5)
            new_window_admin.mainloop()

    # Bind the key press event to the check_konami_code function
    Jeu.bind("<Key>", check_konami_code)






    #comparaison pour lancer les bon niveaux / résultats en fonction du type sélectionné
    if type_partie =='all':
        tours = 9
    elif type_partie =='seconde':
        tours = 5
    elif type_partie == 'premiere':
        tours = 9

    if Niveau < tours: # titre de la fenetre en fonction de l'avancée
        if Niveau==4 or Niveau ==8:
            Jeu.title(f"Maths-Quest | Niveau Boss       © PLADEAU Quentin LUBAN Théo")
        else:
            Jeu.title("Maths-Quest | Niveau Jeu       © PLADEAU Quentin LUBAN Théo")


        #On crée la map 
        longueur = 38
        largeur = 21
        L = labyrinthe.mapmaker(longueur,largeur) 

        #On custom la map avec les pnj, portes et joueurs...
        L = custom_labyrinthe.Custom_Map(L, longueur, largeur, Niveau)


        #On load les imgs pour pouvoir les afficher (img générale)

        porte = PhotoImage(file="Images/Autre/porte_petit.png")
        porte_moyen = PhotoImage(file="Images/Autre/porte_moyen.png")
        carre = PhotoImage(file="Images/Autre/CARRE.png")
        craft_table_petit = PhotoImage(file="Images/Autre/craft_petit.png")
        craft_table_moyen = PhotoImage(file="Images/Autre/craft_moyen.png")

        Perso = PhotoImage(file="Images/Autre/Perso_marche_1.png")
        Perso2 = PhotoImage(file="Images/Autre/Perso_marche_2.png")
        idee = PhotoImage(file="Images/Autre/idee.png")

        Volume_nv1 = PhotoImage(file="Images/Exercices/volume.png")
        exo_boss_portdesete = PhotoImage(file="Images/Exercices/boss_exo.png")
        exo_boss_briquedelait = PhotoImage(file="Images/Exercices/boss_exo2.png")
        indice2_boss2 = PhotoImage(file="Images/Exercices/indice2_boss2.png")

        #en fonction du niveau, on choisit les murs / les pnjs / les loots

        if Niveau ==0 or Niveau ==5:
                Grande_cle = PhotoImage(file="Images/Objets/Cle_1_repare.png")

                loot_vide_pnj1 = PhotoImage(file="Images/Objets/clepnj1_.png")
                loot_vide_pnj2 = PhotoImage(file="Images/Objets/clepnj2_.png")
                loot_vide_pnj3 = PhotoImage(file="Images/Objets/clepnj3_.png")

                loot_pnj1 = PhotoImage(file="Images/Objets/clepnj1.png")
                loot_pnj2 = PhotoImage(file="Images/Objets/clepnj2.png")
                loot_pnj3 = PhotoImage(file="Images/Objets/clepnj3.png")

        elif Niveau == 1 or Niveau==6:
                Grande_cle = PhotoImage(file="Images/Objets/Cle_2_repare.png")

                loot_vide_pnj1 = PhotoImage(file="Images/Objets/clepnj1_.png")
                loot_vide_pnj2 = PhotoImage(file="Images/Objets/clepnj2_.png")
                loot_vide_pnj3 = PhotoImage(file="Images/Objets/clepnj3_.png")
                loot_vide_pnj4 = PhotoImage(file="Images/Objets/Glue_Ombre.png")

                loot_pnj1 = PhotoImage(file="Images/Objets/clepnj1.png")
                loot_pnj2 = PhotoImage(file="Images/Objets/clepnj2.png")
                loot_pnj3 = PhotoImage(file="Images/Objets/clepnj3.png")
                loot_pnj4 = PhotoImage(file="Images/Objets/Glue.png")

        elif Niveau ==2 or Niveau ==3 or Niveau ==7:
                Grande_cle = PhotoImage(file="Images/Objets/Cle_3_repare.png")

                loot_vide_pnj1 = PhotoImage(file="Images/Objets/clepnj1_.png")
                loot_vide_pnj2 = PhotoImage(file="Images/Objets/clepnj2_.png")
                loot_vide_pnj3 = PhotoImage(file="Images/Objets/clepnj3_.png")
                loot_vide_pnj4 = PhotoImage(file="Images/Objets/Glue_Ombre.png")
                loot_vide_pnj5 = PhotoImage(file="Images/Objets/Kit_de_nettoyage_ombre.png")

                loot_pnj1 = PhotoImage(file="Images/Objets/clepnj1-.png")
                loot_pnj2 = PhotoImage(file="Images/Objets/clepnj2-.png")
                loot_pnj3 = PhotoImage(file="Images/Objets/clepnj3-.png")
                loot_pnj4 = PhotoImage(file="Images/Objets/Glue.png")
                loot_pnj5 = PhotoImage(file="Images/Objets/Kit_de_nettoyage.png")


        if Niveau ==0 or Niveau == 5:
            mur1 = PhotoImage(file="Images/Map/Water.png")
            mur2 = PhotoImage(file="Images/Map/Water_rock.png")
            mur3 = PhotoImage(file="Images/Map/Water_Lotus.png")

            pnj1 = PhotoImage(file = "Images/pnj/Leilegalite/Leilegalite_petit.png")
            pnj2 = PhotoImage(file = "Images/pnj/Iggy/Iggy_petit.png")
            pnj3 = PhotoImage(file = "Images/pnj/Mathemami/Mathemami_petit.png")

            pnj1_moyen = PhotoImage(file="Images/pnj/Leilegalite/Leilegalite_moyen.png")
            pnj2_moyen = PhotoImage(file="Images/pnj/Iggy/Iggy_moyen.png")
            pnj3_moyen = PhotoImage(file="Images/pnj/Mathemami/Mathemami_moyen.png")

            pnj1_grand = PhotoImage(file="Images/pnj/Leilegalite/Leilegalite_grand.png")
            pnj2_grand = PhotoImage(file="Images/pnj/Iggy/Iggy_grand.png")
            pnj3_grand = PhotoImage(file="Images/pnj/Mathemami/Mathemami_grand.png")

        elif Niveau ==1 or Niveau ==6:
            mur1 = PhotoImage(file="Images/Map/Arbre.png")
            mur2 = PhotoImage(file="Images/Map/Maison_1.png")
            mur3 = PhotoImage(file="Images/Map/Maison_2.png")

            pnj1 = PhotoImage(file = "Images/pnj/Papy/Papy_petit.png")
            pnj4 = PhotoImage(file = "Images/pnj/Titouan/Titouan_petit.png")

            if Niveau ==1:
                pnj2 = PhotoImage(file = "Images/pnj/Cecylindre/Cecylindre_petit.png")
                pnj3 = PhotoImage(file = "Images/pnj/MarchandDeGlace/Marchand_de_glace_petit.png")

                pnj2_moyen = PhotoImage(file="Images/pnj/Cecylindre/Cecylindre_moyen.png")
                pnj3_moyen = PhotoImage(file="Images/pnj/MarchandDeGlace/Marchand_de_glace_moyen.png")

                pnj2_grand = PhotoImage(file="Images/pnj/Cecylindre/Cecylindre_grand.png")
                pnj3_grand = PhotoImage(file="Images/pnj/MarchandDeGlace/Marchand_de_glace_grand.png")

            elif Niveau ==6:
                pnj2 = PhotoImage(file = "Images/pnj/MarchandDeGlace/Marchand_de_glace_petit.png")
                pnj3 = PhotoImage(file = "Images/pnj/Cecylindre/Cecylindre_petit.png")

                pnj2_moyen = PhotoImage(file="Images/pnj/MarchandDeGlace/Marchand_de_glace_moyen.png")
                pnj3_moyen = PhotoImage(file="Images/pnj/Cecylindre/Cecylindre_moyen.png")

                pnj2_grand = PhotoImage(file="Images/pnj/MarchandDeGlace/Marchand_de_glace_grand.png")
                pnj3_grand = PhotoImage(file="Images/pnj/Cecylindre/Cecylindre_grand.png")

           
            pnj1_moyen = PhotoImage(file="Images/pnj/Papy/Papy_moyen.png")
            pnj4_moyen = PhotoImage(file="Images/pnj/Titouan/Titouan_moyen.png")

            pnj1_grand = PhotoImage(file="Images/pnj/Papy/Papy_grand.png")
            pnj4_grand = PhotoImage(file="Images/pnj/Titouan/Titouan_grand.png")


        elif Niveau ==2 or Niveau ==3 or Niveau==7:
            mur1 = PhotoImage(file="Images/Map/Wall1.png")
            mur2 = PhotoImage(file="Images/Map/Wall2.png")
            mur3 = PhotoImage(file="Images/Map/Wall3.png")

            if Niveau ==2 or Niveau ==7:
                pnj1 = PhotoImage(file = "Images/pnj/Cana/Cana_petit.png")
                pnj1_moyen = PhotoImage(file="Images/pnj/Cana/Cana_moyen.png")
                pnj1_grand = PhotoImage(file="Images/pnj/Cana/Cana_grand.png")
            elif Niveau ==3:
                pnj1 = PhotoImage(file = "Images/pnj/Mathemami/Mathemami_petit.png")
                pnj1_moyen = PhotoImage(file="Images/pnj/Mathemami/Mathemami_moyen.png")
                pnj1_grand = PhotoImage(file="Images/pnj/Mathemami/Mathemami_grand.png")


            pnj2 = PhotoImage(file = "Images/pnj/HommeStrict/HommeStrict_petit.png")
            pnj3 = PhotoImage(file = "Images/pnj/MarchandDeTapis/Marchand_de_tapis_petit.png")
            pnj4 = PhotoImage(file = "Images/pnj/Delta/Delta_petit.png")
            pnj5 = PhotoImage(file = "Images/pnj/CapitaineDunNavire/Capitaine_dun_navire_petit.png")

            pnj2_moyen = PhotoImage(file="Images/pnj/HommeStrict/HommeStrict_moyen.png")
            pnj3_moyen = PhotoImage(file="Images/pnj/MarchandDeTapis/Marchand_de_tapis_moyen.png")
            pnj4_moyen = PhotoImage(file="Images/pnj/Delta/Delta_moyen.png")
            pnj5_moyen = PhotoImage(file="Images/pnj/CapitaineDunNavire/Capitaine_dun_navire_moyen.png")

            pnj2_grand = PhotoImage(file="Images/pnj/HommeStrict/HommeStrict_grand.png")
            pnj3_grand = PhotoImage(file="Images/pnj/MarchandDeTapis/Marchand_de_tapis_grand.png")
            pnj4_grand = PhotoImage(file="Images/pnj/Delta/Delta_grand.png")
            pnj5_grand = PhotoImage(file="Images/pnj/CapitaineDunNavire/Capitaine_dun_navire_grand.png")


        #les deux niveaux de boss
        elif Niveau==4 or Niveau ==8:
            mur1 = PhotoImage(file="Images/Map/Wall_red.png")
            mur2 = PhotoImage(file="Images/Map/Wall_red_with_symbols.png")
            mur3 = PhotoImage(file="Images/Map/Wall_red_flower.png")

            pnj_boss_ = PhotoImage(file = "Images/pnj/Boss/Boss_yoda.png")
            pnj_boss_moyen = PhotoImage(file = "Images/pnj/Boss/Boss_yoda_icon.png")


        
        #Fonction qui gère le déplacement du personnage; MAJ de la map tkinter, les interractions avec les pnj
        def deplacement(event): 
            
            global ordonne
            global abscisse
            global deplacement_perso

            touche = event.keysym # on recup la touche
            check = ["■" ,"\U0001F6AA", "¤", "boss"] #list de verif
            pnj_liste = ["pnj1", "pnj2", "pnj3", "pnj4", "pnj5"]


            #pour chaque touche, il y a des vérifs pour se déplacer, et check les actions possibles

            if touche == "Up":
                if ordonne-1 > 0 and L[ordonne-1][abscisse] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne-1][abscisse] in pnj_liste) and (L[ordonne-2][abscisse] not in check) and (L[ordonne-2][abscisse] not in pnj_liste):
                        ordonne-=2
                    elif L[ordonne-1][abscisse] in pnj_liste :
                        pass
                    else:
                        ordonne-=1
                    
                    L[ordonne][abscisse] = "○"

                    if deplacement_perso == True:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso2)
                        deplacement_perso = False
                    else:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                        deplacement_perso = True


                else :
                    pass


            elif touche=="Left" :
                if abscisse-1 > 0 and L[ordonne][abscisse-1] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne][abscisse-1] in pnj_liste) and (L[ordonne][abscisse-2] not in check ) and (L[ordonne][abscisse-2] not in pnj_liste):
                        abscisse-=2
                    elif L[ordonne][abscisse-1] in pnj_liste :
                        pass
                    else:
                        abscisse-=1

                    L[ordonne][abscisse] = "○"

                    if deplacement_perso == True:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso2)
                        deplacement_perso = False
                    else:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                        deplacement_perso = True
                else :
                    pass


            elif touche=="Down" :
                if ordonne+1 < len(L) and L[ordonne+1][abscisse] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne+1][abscisse] in pnj_liste) and (L[ordonne+2][abscisse] not in check) and (L[ordonne+2][abscisse] not in pnj_liste):
                        ordonne+=2
                    elif L[ordonne+1][abscisse] in pnj_liste :
                        pass
                    else:
                        ordonne+=1

                    L[ordonne][abscisse] = "○"

                    if deplacement_perso == True:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso2)
                        deplacement_perso = False
                    else:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                        deplacement_perso = True
                else :
                    pass


            elif touche=="Right" :
                if abscisse+1 < len(L[ordonne]) and L[ordonne][abscisse +1] not in check :
                    L[ordonne][abscisse] = " "
                    L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=carre)

                    #Si jamais les pnj sont sur la route
                    if (L[ordonne][abscisse+1] in pnj_liste) and (L[ordonne][abscisse+2] not in check) and (L[ordonne][abscisse+2] not in pnj_liste):
                        abscisse+=2
                    elif L[ordonne][abscisse+1] in pnj_liste :
                        pass
                    else:
                        abscisse+=1

                    L[ordonne][abscisse] = "○"

                    if deplacement_perso == True:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso2)
                        deplacement_perso = False
                    else:
                        L[ordonne][abscisse] = canvas.create_image(24*abscisse, 24*ordonne, anchor=NW, image=Perso)
                        deplacement_perso = True

                else :
                    pass

            # nettoyage
            canvas_infos_possibilite_discussion.delete('all')

            #verif si table de craft dispo et si oui on affiche le msg d'information
            if L[ordonne][abscisse-1] == "¤":
                Label_text_possibilite_strvar.set("Appuie sur 'c' pour assembler la grande Clé !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=craft_table_moyen)

            #check si c'est la porte et on met à jour les infos dans le cadre en bas à gauche
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
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj1_moyen)

                #PNJ 2
                elif (L[ordonne-1][abscisse] == pnj_liste[1] or L[ordonne+1][abscisse]== pnj_liste[1] or L[ordonne][abscisse-1]== pnj_liste[1] or L[ordonne][abscisse+1]== pnj_liste[1]):
                    Label_text_possibilite_strvar.set("Appuie sur 'espace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj2_moyen)

                #PNJ3
                elif (L[ordonne-1][abscisse] == pnj_liste[2] or L[ordonne+1][abscisse]== pnj_liste[2] or L[ordonne][abscisse-1]== pnj_liste[2] or L[ordonne][abscisse+1]== pnj_liste[2]):
                    Label_text_possibilite_strvar.set("Appuie sur 'espace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj3_moyen)

                #PNJ4
                elif (L[ordonne-1][abscisse] == pnj_liste[3] or L[ordonne+1][abscisse]== pnj_liste[3] or L[ordonne][abscisse-1]== pnj_liste[3] or L[ordonne][abscisse+1]== pnj_liste[3]):
                    Label_text_possibilite_strvar.set("Appuie sur 'escpace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj4_moyen)

                #PNJ5
                elif (L[ordonne-1][abscisse] == pnj_liste[4] or L[ordonne+1][abscisse]== pnj_liste[4] or L[ordonne][abscisse-1]== pnj_liste[4] or L[ordonne][abscisse+1]== pnj_liste[4]):
                    Label_text_possibilite_strvar.set("Appuie sur 'escpace' pour me parler !")
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj5_moyen)

            else:
                # affiche de l'aide possible en fonction de l'avancement du joueur
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


                #clear  + affiche l'image d'idée pour les indices pour l'avancement
                canvas_infos_possibilite_discussion.delete('all')
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image = idee)

                #on clear si jamais la personne s'en va
                canvas_tete_pnj_grand.delete("all")
                Label_text_nom_pnj_strvar.set("")
                Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)

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

            # on affiche la clé si la condition est respectée
            if assemble_cle == True:
                canvas_inv.delete("all")
                canvas_inv.config(width = 150, height = 50)
                canvas_inv.create_image(0,0, anchor = NW, image=Grande_cle)
            
            # on affiche le reste de l'inventaire en fonction de l'avancement et de ce que le joueur possède
            else:
                canvas_inv.delete("all")
                long_canvas_inv = 150
                if Niveau ==1 or Niveau ==6:
                    long_canvas_inv = 200
                elif Niveau == 2 or Niveau ==3 or Niveau ==7:
                    long_canvas_inv = 250

                canvas_inv.config(width = long_canvas_inv, height = 50)

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

                if Niveau !=4 and Niveau !=8:
                    if pnj1_infos == True:
                        canvas_inv.create_image(0,0, anchor = NW, image=loot_pnj1)
                    else:
                        canvas_inv.create_image(0,0, anchor = NW, image=loot_vide_pnj1)

                    if pnj2_infos == True:
                        canvas_inv.create_image(50,0, anchor = NW, image=loot_pnj2)
                    else:
                        canvas_inv.create_image(50,0, anchor = NW, image=loot_vide_pnj2)

                    if pnj3_infos == True:
                        canvas_inv.create_image(100,0, anchor = NW, image=loot_pnj3)
                    else:
                        canvas_inv.create_image(100,0, anchor = NW, image=loot_vide_pnj3)


                    if Niveau ==1 or Niveau ==6 or Niveau ==2 or Niveau ==3 or Niveau ==7:

                        if pnj4_infos == True:
                            canvas_inv.create_image(150,0, anchor = NW, image=loot_pnj4)
                        else:
                            canvas_inv.create_image(150,0, anchor = NW, image=loot_vide_pnj4)


                        if Niveau ==2 or Niveau ==3 or Niveau ==7:
                            if pnj5_infos == True:
                                canvas_inv.create_image(200,0, anchor = NW, image=loot_pnj5)
                            else:
                                canvas_inv.create_image(200,0, anchor = NW, image=loot_vide_pnj5)


        #fonction pour afficher le cours 
        def load_cours(Niveau, num_pnj):
            #full cours bloc
            Liste_cours = [
            "De façon intuitive, une égalité fonctionne un peu comme une balance à deux plateaux \u2696 : si on effectue une opération dans un des membres, il faut réaliser la même opération dans l’autre pour garder l'équilibre.",
            "Quelques propriétés : On peut ajouter (ou soustraire) un même nombre aux deux membres d'une égalité. \n    a = b équivaut à a + c = b + c\n    a = b  équivaut à a - c = b - c \nOn peut multiplier (ou diviser) les deux membres d'une égalité par un même nombre non nul. \n    a = b équivaut à a × c = b × c \n    a = b équivaut à   a/c = b/c(c ≠ 0) \nExemple :  \n5x + 2 = 17 \n5x + 2 - 2 = 17 - 2 \n5x/5 = 15/5 \nx = 3",
            "Si il y a des x dans les deux membres de l’équation il faut tout mettre dans le même. Exemple : \n                 3x + 2 = 5x + 3 \néquivaut à  3x + 2 - 5x = 5x + 3 - 5x \néquivaut à  -2x + 2 = 3 \net ainsi de suite", 
            


            "La formule de l’aire d’un disque est π x rayon², l’aire d’un triangle est ", 
            " et celle d’un carré ou d’un rectangle est longueur x largeur. Vidéo explicative de pi ici",

            "Le volume du cylindre est : base x hauteur soit π x rayon² x h. De manière plus générale une multitude de volume se calcule simplement par base x hauteur.",

            "Le volume du cône est celui du cylindre divisé par 3 soit ", 
            ". Le volume d’une pyramide est celui du prisme droit que l’on divise par 3 soit",

            "La formule pour calculer le volume d’un sphère est ",
            


            "L’équation d’une droite se présente sous la forme mx + p, avec m en tant que coefficient directeur et p l’ordonné à l’origine.",
            "Les droites parallèles à l’axe des ordonnées (“droite verticale”) ne se présentent pas sous la forme y = mx + p mais ont une équation de la forme x=c avec c un nombre par exemple x = 2 est une droite verticale qui passe par l’abscisse 2.",
            "Dans une équation sous forme mx + p, passant par les points A(xA;yA) et B(xB;yB), p est l’ordonnée à l’origine pour trouver p, on utilise les coordonnées d’un point de la droite par exemple avec le point A(xA; yA), on a p = yA - m.xA et pour trouver m on a",
            "Une fonction affine admet une expression algébrique de la forme f(x) = mx + p et sa représentation graphique est une droite.",
            "Pour trouver les coordonnées du point d’intersection de 2 droites il faut trouver quand l’équation réduite 1 est égale à l’équation réduite 2 soit mx + p = m’x + p’",



            "Il y a 2 manières pour résoudre un système à doubles inconnues, la fin est la même mais la réflexion n’est pas la même, il y a donc la résolution par substitution et la résolution par combinaisons linéaires, un système à double inconnues peut permettre de trouver les coordonnées d’un point d’intersection.",
            
            "La méthode de substitution consiste à isoler une des variables dans l'une des équations et à substituer cette expression dans l'autre équation. Cela permet de réduire le système à une seule équation avec une seule inconnue, qui peut alors être résolue.",
            
            "Exemple de résolution par substitution :",
            "1. Isoler une variable à l’aide d’une équation : \n    y = 5 - x \n2. Substituer y par c-x dans l’autre équation : \n    2x - (5 - x) = 1  \n3. Résoudre pour trouver x : \n    2x - 5 + x = 1  \n    3x - 5 = 1 \n    3x = 6 \n    x = 2 \n4. Remplacer x par 2 et trouver y : : \n    y = 5 - 2 = 3  \nSolution \n    x = 2, y = 3",
            
            "La méthode de combinaisons linéaires consiste à manipuler les équations pour éliminer l'une des variables. Cette manipulation se fait généralement en multipliant les équations par des coefficients appropriés afin d'obtenir des coefficients opposés pour une des variables, puis en additionnant ou soustrayant les équations.",
            
            "Exemple de résolution par combinaison linéaire :", 
            "1. Additionner les deux équations pour éliminer y  : \n    (2x + y) + (3x - y) = 5 + 4 \n     2x + 3x + y - y = 9 \n     5x = 9 \n     x = 9/5 \n2. Remplacer x par 9/5 dans la première équation pour trouver y : \n     2*(9/5) + y = 5 \n     18/5 + y = 5 \n      y = 5 - 18/5 \n      y = 25/5 - 18/5 \n      y = 7/5 \nSolution \n     x = 9/5, y = 7/5", 




            "Un polynôme du second degré admet comme forme développée : P(x)= ax² + bx + c avec a, b et c des coefficients et a \u2260 0. Chaque polynôme admet une forme canonique sous la forme\n",

            "Pour résoudre P(x) = 0 il faut déterminer le discriminant delta :",
            "Si le delta > 0, P(x) admet deux solutions distinctes :\n ",
            "Remarque : Il peut se factoriser par P(x)= a(x-x1)(x-x2)   \nSi delta = 0 alors il n’en admet qu’une unique dite double :",
            "Remarque : Il se factorise par",
            "Si delta < 0 il n’admet pas de solution et ne se factorise pas",

            "Pour déterminer le signe du polynôme P(x), on doit utiliser le discriminant delta et alpha. \nLorsque delta > 0 : \nP(x) est du signe de a à l'extérieur des racines x1 et x2; c'est-à-dire sur les intervalles",
            "il est du signe opposé à a entre les racines; c'est-à-dire sur l'intervalle",
            "Lorsque delta = 0 : \n     P(x)  est toujours du signe de a sur R excepté à x = alpha où il est nulle.\nLorsque delta < 0 : \n     P(x) est toujours du signe de a \nVariations : \n     Lorsque a est positif la courbe représentative de P(x) décroît jusqu’à x=alpha puis croît. \n     Lorsque a est négatif la courbe croît jusqu’à x=alpha puis décroît.",




            "Le taux de variation d’une fonction f en un point a est une mesure de la rapidité avec laquelle f change près de a. On dit que f est dérivable en a si la limite suivante existe : ",
            "Si cette limite existe, elle est appelée la dérivée de f en a et est notée f’(a)",

            "La dérivée d'une fonction en un point donne la pente de la tangente à la courbe de la fonction en ce point. Elle se calcule grâce la formule T : y = f’(a)(x - a) + f(a) avec a un point de la courbe.",
            
            "Dérivée d'une constante : Si",
            ", alors ",
            "Dérivée de",
            ", alors ",
            "Dérivée de",
            ", alors ",
            "Dérivée de",
            ", alors ",
            "Dérivée de",
            ", alors ",
            "Somme et Différence : Si",
            ", alors ",
            "Produit : Si",
            ", alors ",
            "Quotient : Si ",
            ", alors ",

            "Une dérivée peut servir à connaître les intervalles croissant et décroissant de la courbe, lorsque f’(x) > 0 alors f(x) est croissant et lorsque f’(x) < 0 alors f(x) est décroissant.", 
            




            "Une suite est une liste ordonnée de nombres, on la définit souvent par : une relation de récurrence avec le terme n+1 noté ",
            "en fonction du terme n noté ",
            "Avec l’expression de récurrence, il est nécessaire de connaître un terme de la suite (par exemple U0 ou U1 etc…) pour calculer les autres. Ou une formule explicite qui permet d’exprimer directement le terme ",
            "en fonction de l’indice n.",

            "Dans une suite arithmétique le terme ",
            "se calcule à l’aide du terme précédent ",
            "auquel on additionne ou on retranche une constante nommée raison, notée r.\nLa relation de récurrence de la suite se note : ",
            "avec U0 le premier terme de la suite. \nLa formule explicite de la suite se note : ",
            "Exemple de la suite ",
            "de premier terme U0 = 1 et de raison r =2 :\nForme de récurrence : ",
            "Formule explicite : ",

            "Dans une suite géométrique le terme ",
            "se calcule à l’aide du terme précédent ",
            "auquel on multiplie une constante (la raison), notée q. \nLa relation de récurrence de la suite se note :  ",
            "avec",
            "le premier terme de la suite. \nLa formule explicite de la suite se note : ",
            "Exemple de la suite ",
            " de premier terme V0 = 0.5 et de raison q =1,7: \nForme de récurrence : ",
            "Formule explicite : ",

            "Pour reconnaître si une suite est une suite arithmétique on peut vérifier si la différence ",
            "est constante pour tout entier naturel n, ce qui donnera la raison par la même occasion.",

            "La somme des n premiers termes d’une suite arithmétique se calcule avec la formule : ",
            "La somme des n premiers termes d’une suite géométrique se calcule avec la formule : ",

            ]

            def ajouter_element(Texte): # afficher le cours dans la box de cours
                global listbox
                element = Texte.strip()
                listbox.config(state=NORMAL)
                if element:
                    listbox.insert(END, element)

            def saut_2_lignes(): # fonction pour ajouter des espaces 
                global listbox
                listbox.insert(END, "\n")
                listbox.insert(END, "\n")

            



            #partie load du premier chargement
            if num_pnj ==0 or num_pnj==1:


                #chargement de toutes les fonction qui permettent d'afficher les niveau de cours
                def load_cours_1():
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")

                    for i in range(3):
                        ajouter_element(Liste_cours[i])
                        saut_2_lignes()
                                    
                    listbox.insert(END, "\n")


                def load_cours_2():
                    listbox.insert(END, "--Volume--" + "\n")
                    listbox.insert(END, "\n")

                    ajouter_element(Liste_cours[3])
                    formule_latex.make_formule(r"$ \frac{(longueur \times largeur)}{2}$",listbox, 14, 0) #element latex qui fait appel au ficher en question
                    ajouter_element(Liste_cours[4])
                    saut_2_lignes()

                    ajouter_element(Liste_cours[5])
                    saut_2_lignes()

                    ajouter_element(Liste_cours[6])
                    formule_latex.make_formule(r"$ \frac{(\pi \times rayon^2 \times \text{hauteur})}{3}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[7])
                    formule_latex.make_formule(r"$ \frac{V_{prisme}}{3}$",listbox, 14, 0) 
                    saut_2_lignes()

                    ajouter_element(Liste_cours[8])
                    formule_latex.make_formule(r"$ \frac{4}{(3\pi \times r^3)}$",listbox, 14, 0) 
                    ajouter_element("    ")
                    saut_2_lignes()

                    listbox.insert(END, "\n")


                def load_cours_3():

                    listbox.insert(END, "--Fonction Affine & Equation de Droite--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(9,14):
                        ajouter_element(Liste_cours[i])
                        if i == 11:
                            formule_latex.make_formule(r"$ m = \frac{yB - yA}{xB - xA}$",listbox, 14, 0) 
                            ajouter_element("   ")
                        saut_2_lignes()

                    listbox.insert(END, "\n")

                def load_cours_4():
                    listbox.insert(END, "--Equation à 2 inconnues--" + "\n")
                    listbox.insert(END, "\n")
                    for i in range(14,21):
                        if i !=17 and i!=20:
                            ajouter_element(Liste_cours[i])

                        if i ==16:
                            listbox.insert(END, "\n")
                            formule_latex.make_formule(r"$\left\{ \begin{array}{lr} x + y & = 5 \\ 2x - y & = 1 \end{array} \right.$",listbox, 14, 1) 
                            ajouter_element(Liste_cours[17])

                        elif i ==19:
                            listbox.insert(END, "\n")
                            formule_latex.make_formule(r"$\left\{ \begin{array}{lr} 2x + y & = 5 \\ 3x - y & = 4 \end{array} \right.$",listbox, 14, 1) 
                            ajouter_element(Liste_cours[20])
                        
                        if i!=17 and i!=20:
                            saut_2_lignes()

                    listbox.insert(END, "\n")


                def load_cours_5():
                    listbox.insert(END, "--Equation du second degré--" + "\n")
                    listbox.insert(END, "\n")

                    ajouter_element(Liste_cours[21])
                    listbox.insert(END, "\n")
                    formule_latex.make_formule(r"$ a( x - \alpha)^2 + \beta$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ \alpha = \frac{-b}{2a}$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ \beta = \frac{- \Delta}{4a}$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ \Delta = b^2 - 4ac$",listbox, 14, 2)
                    
                    saut_2_lignes()

                    ajouter_element(Liste_cours[22])
                    ajouter_element(Liste_cours[23])
                    listbox.insert(END, "\n")
                    formule_latex.make_formule(r"$ x1 = \frac{-b - \sqrt{\Delta}}{2a}$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ x2 = \frac{-b + \sqrt{\Delta}}{2a}$",listbox, 14, 1)
                    ajouter_element(Liste_cours[24])
                    formule_latex.make_formule(r"$ x = \alpha = \frac{-b}{2a}$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[25])     
                    formule_latex.make_formule(r"$ a(x-\alpha)^2$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[26])

                    saut_2_lignes()

                    ajouter_element(Liste_cours[27])
                    formule_latex.make_formule(r"$\left] -\infty, x1 \right[ \cup \left] x2, +\infty \right[.$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[28])
                    formule_latex.make_formule(r"$\left] x1, x2 \right[.$",listbox, 14, 0)
                    ajouter_element(Liste_cours[29])

                    listbox.config(state=NORMAL)

                    saut_2_lignes()
                    listbox.insert(END, "\n")



                def load_cours_6():
                    listbox.insert(END, "--Dérivation--" + "\n")
                    listbox.insert(END, "\n")

                    ajouter_element(Liste_cours[30])
                    formule_latex.make_formule(r"$ f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} $",listbox, 14, 1) 
                    ajouter_element(Liste_cours[31])
                    saut_2_lignes()

                    ajouter_element(Liste_cours[32])
                    saut_2_lignes()

                    ajouter_element(Liste_cours[33])
                    formule_latex.make_formule(r"$f(x) =c$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[34])
                    formule_latex.make_formule(r"$f'(x) = 0.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[35])
                    formule_latex.make_formule(r"$x^n : f(x) = x^n$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[36])
                    formule_latex.make_formule(r"$f'(x) = nx^{n-1}.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[37])
                    formule_latex.make_formule(r"$nx : f(x) = nx$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[38])
                    formule_latex.make_formule(r"$f'(x) = n. $",listbox, 14, 1)


                    ajouter_element(Liste_cours[39])
                    formule_latex.make_formule(r"$ \frac{1}{x} : f(x) = \frac{1}{x}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[40])
                    formule_latex.make_formule(r"$f'(x) = \frac{-1}{x^2}.$",listbox, 14, 1)


                    ajouter_element(Liste_cours[41])
                    formule_latex.make_formule(r"$ \sqrt{x} : f(x) = \sqrt{x}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[42])
                    formule_latex.make_formule(r"$f'(x) = \frac{1}{2 \sqrt{x}}.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[43])
                    formule_latex.make_formule(r"$f(x) = u+v$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[44])
                    formule_latex.make_formule(r"$f'(x) = u'+v'$",listbox, 14, 1)

                    ajouter_element(Liste_cours[45])
                    formule_latex.make_formule(r"$f(x) = uv$",listbox, 14, 0)
                    ajouter_element(Liste_cours[46])
                    formule_latex.make_formule(r"$fu'v + uv'.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[47])
                    formule_latex.make_formule(r"$f(x) = \frac{u}{v}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[48])
                    formule_latex.make_formule(r"$f'(x) = \frac{u'v - uv'}{v^2}$",listbox, 14, 2)

                    saut_2_lignes() 

                    ajouter_element(Liste_cours[49])
                    saut_2_lignes() 


                    listbox.insert(END, "\n")


                def load_cours_7():
                    listbox.insert(END, "--Suite--" + "\n")
                    listbox.insert(END, "\n")

                    ajouter_element(Liste_cours[50])
                    formule_latex.make_formule(r"$  U_{n+1}  $",listbox, 14, 0) 
                    ajouter_element(Liste_cours[51])
                    formule_latex.make_formule(r"$  U_{n}.$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[52])
                    formule_latex.make_formule(r"$  U_{n}.$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[53])
                    saut_2_lignes()

                    ajouter_element(Liste_cours[54])
                    formule_latex.make_formule(r"$  U_{n+1}  $",listbox, 14, 0) 
                    ajouter_element(Liste_cours[55])
                    formule_latex.make_formule(r"$  U_{n}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[56])
                    formule_latex.make_formule(r"$  U_{n+1} = U_{n} + r $",listbox, 14, 0) 
                    ajouter_element(Liste_cours[57])
                    formule_latex.make_formule(r"$  U_{n} = U_{0} + n \times r $",listbox, 14, 1) 
                    ajouter_element(Liste_cours[58])
                    formule_latex.make_formule(r"$  U_{n}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[59])
                    formule_latex.make_formule(r"$  U_{n+1} = U_{n} + 2$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[60])
                    formule_latex.make_formule(r"$  U_{n} = 1 + 2n$",listbox, 14, 0) 
                    ajouter_element(" ")
                    saut_2_lignes()

                    ajouter_element(Liste_cours[61])
                    formule_latex.make_formule(r"$V_{n+1}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[62])
                    formule_latex.make_formule(r"$V_{n}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[63])
                    formule_latex.make_formule(r"$V_{n+1} = V{n} \times q $",listbox, 14, 0)
                    ajouter_element(Liste_cours[64])
                    formule_latex.make_formule(r"$V_{0} $",listbox, 14, 0)
                    ajouter_element(Liste_cours[65])
                    formule_latex.make_formule(r"$V_{n} = V_{0} \times q^{n} $",listbox, 14, 1)
                    ajouter_element(Liste_cours[66])
                    formule_latex.make_formule(r"$V_{0}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[67])
                    formule_latex.make_formule(r"$V_{n+1} = V{n} \times 1.7 $",listbox, 14, 1)
                    ajouter_element(Liste_cours[68])
                    formule_latex.make_formule(r"$V_{n} = 0.5 \times 1.7^{n} $",listbox, 14, 0)
                    ajouter_element(" ")
                    saut_2_lignes()

                    ajouter_element(Liste_cours[69])
                    formule_latex.make_formule(r"$ U_{n+1} - U_{n}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[70])
                    saut_2_lignes() 

                    ajouter_element(Liste_cours[71])
                    formule_latex.make_formule(r"$S_{n} = \text{nombre de terme} \times \frac{\text{premier terme + dernier terme}}{2}$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[72])
                    formule_latex.make_formule(r"$S_{n} = \text{premier terme} \times \frac{1 - \text{raison}^{\text{nombre de termes}}}{1 - \text{raison}}$",listbox, 14, 0) 
                    ajouter_element(" ")
                    saut_2_lignes()



                if num_pnj==0:
                    global listbox

                    #creation de la box du cours
                    listbox = scrolledtext.ScrolledText(Label_Frame_Cours_Affiche, width =35,wrap="word",bg=None, font=("Arial",10))
                    listbox.pack(side=LEFT, fill=BOTH, expand=True)

                    # pour stocker les img latex pour le cours
                    listbox.images = []

                elif num_pnj==1:
                    #on clear la box
                    listbox.config(state=NORMAL)
                    listbox.delete(1.0,END)
                    listbox.config(state=DISABLED)



                #chargement pour le reload de la fonction global quand on change de niveau
                #pour eviter d'ecrire à deux fois le meme code de 200 ligne; des optimisation sont faite 
                #ces optimisations consistent en conditions  : 
                #    - pour reload au changement de niveau
                #    - pour reload et mettre en ordre le cours au moment de passer la porte
                listbox.config(state=NORMAL)


                #chargement du cours au reload / quand on passe à l'exo pour remettre dans l'ordre le cours 
                if (Niveau ==0 and num_pnj==0):
                    listbox.insert(END, "--Equation du 1er degré--" + "\n")
                    listbox.insert(END, "\n")

                elif (Niveau ==1 and num_pnj==0) or (Niveau==0 and num_pnj==1):
                    load_cours_1()

                    if num_pnj==0:
                        listbox.insert(END, "--Volume--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau ==2 and num_pnj==0) or (Niveau== 1 and num_pnj==1):
                    load_cours_1()
                    load_cours_2()

                    if num_pnj==0:
                        listbox.insert(END, "--Fonction Affine & Equation de Droite--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau ==3 and num_pnj==0) or (Niveau== 2 and num_pnj==1):
                    load_cours_1()
                    load_cours_2()
                    load_cours_3()

                    if num_pnj==0:
                        listbox.insert(END, "--Equation à 2 inconnues--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau ==4 and num_pnj==0) or (Niveau== 3 and num_pnj==1):
                    load_cours_1()
                    load_cours_2()
                    load_cours_3()
                    load_cours_4()



                elif (Niveau ==5 and num_pnj==0):
                    listbox.insert(END, "--Equation du second degré--" + "\n")
                    listbox.insert(END, "\n")

                elif (Niveau ==6 and num_pnj==0) or (Niveau== 5 and num_pnj==1):
                    load_cours_5()

                    if num_pnj==0:
                        listbox.insert(END, "--Dérivation--" + "\n")
                        listbox.insert(END, "\n")

                elif (Niveau==7 and num_pnj==0) or (Niveau== 6 and num_pnj==1):
                    load_cours_5()
                    load_cours_6()

                    if num_pnj==0:
                        listbox.insert(END, "--Suite--" + "\n")
                        listbox.insert(END, "\n")


                elif (Niveau==8 and num_pnj==0) or (Niveau== 7 and num_pnj==1):
                    load_cours_5()
                    load_cours_6()
                    load_cours_7()
                

                listbox.config(state=DISABLED)



            # Pour chaque pnj qui donnera son cours, on l'affiche : 
            listbox.config(state=NORMAL)

            if Niveau ==0:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[0])
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[1])
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[2])
                    saut_2_lignes()
            


            elif Niveau ==1:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[3])
                    formule_latex.make_formule(r"$ \frac{(longueur \times largeur)}{2}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[4])
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[5])
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[6])
                    formule_latex.make_formule(r"$ \frac{(\pi \times rayon^2 \times \text{hauteur})}{3}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[7])
                    formule_latex.make_formule(r"$ \frac{V_{prisme}}{3}$",listbox, 14, 0) 
                    ajouter_element("   ")
                    saut_2_lignes()


                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[8])
                    formule_latex.make_formule(r"$ \frac{4}{(3\pi \times r^3)}$",listbox, 14, 0) 
                    ajouter_element("   ")
                    saut_2_lignes()



            elif Niveau ==2:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[9])
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[10])
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[11]) 
                    formule_latex.make_formule(r"$ m = \frac{yB - yA}{xB - xA}$",listbox, 14, 2) 
                    saut_2_lignes()

                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[12]) 
                    saut_2_lignes()

                elif num_pnj=="pnj5":
                    ajouter_element(Liste_cours[13])
                    saut_2_lignes()



            elif Niveau ==3:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[14])
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[15])
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[16])
                    listbox.insert(END, "\n")
                    formule_latex.make_formule(r"$\left\{ \begin{array}{lr} x + y & = 5 \\ 2x - y & = 1 \end{array} \right.$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[17])
                    saut_2_lignes() 

                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[18])
                    saut_2_lignes()

                elif  num_pnj=="pnj5":
                    ajouter_element(Liste_cours[19])
                    listbox.insert(END, "\n")
                    formule_latex.make_formule(r"$\left\{ \begin{array}{lr} 2x + y & = 5 \\ 3x - y & = 4 \end{array} \right.$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[20])
                    saut_2_lignes() 




            elif Niveau ==5:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[21])
                    listbox.insert(END, "\n")
                    formule_latex.make_formule(r"$ a( x - \alpha)^2 + \beta$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ \alpha = \frac{-b}{2a}$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ \beta = \frac{- \Delta}{4a}$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ \Delta = b^2 - 4ac$",listbox, 14, 2)
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[22])
                    ajouter_element(Liste_cours[23])
                    listbox.insert(END, "\n")
                    formule_latex.make_formule(r"$ x1 = \frac{-b - \sqrt{\Delta}}{2a}$",listbox, 14, 1) 
                    formule_latex.make_formule(r"$ x2 = \frac{-b + \sqrt{\Delta}}{2a}$",listbox, 14, 1)
                    ajouter_element(Liste_cours[24])
                    formule_latex.make_formule(r"$ x = \alpha = \frac{-b}{2a}$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[25])     
                    formule_latex.make_formule(r"$ a(x-\alpha)^2$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[26])
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[27])
                    formule_latex.make_formule(r"$\left] -\infty, x1 \right[ \cup \left] x2, +\infty \right[.$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[28])
                    formule_latex.make_formule(r"$\left] x1, x2 \right[.$",listbox, 14, 2) 
                    listbox.insert(END, "   ")
                    ajouter_element(Liste_cours[29])


                    saut_2_lignes()

            elif Niveau ==6:
                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[30])
                    formule_latex.make_formule(r"$ f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} $",listbox, 14, 1) 
                    ajouter_element(Liste_cours[31])
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[32])
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[33])
                    formule_latex.make_formule(r"$f(x) =c$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[34])
                    formule_latex.make_formule(r"$f'(x) = 0.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[35])
                    formule_latex.make_formule(r"$x^n : f(x) = x^n$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[36])
                    formule_latex.make_formule(r"$f'(x) = nx^{n-1}.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[37])
                    formule_latex.make_formule(r"$nx : f(x) = nx$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[38])
                    formule_latex.make_formule(r"$f'(x) = n. $",listbox, 14, 1)

                    ajouter_element(Liste_cours[39])
                    formule_latex.make_formule(r"$ \frac{1}{x} : f(x) = \frac{1}{x}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[40])
                    formule_latex.make_formule(r"$f'(x) = \frac{-1}{x^2}.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[41])
                    formule_latex.make_formule(r"$ \sqrt{x} : f(x) = \sqrt{x}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[42])
                    formule_latex.make_formule(r"$f'(x) = \frac{1}{2 \sqrt{x}}.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[43])
                    formule_latex.make_formule(r"$f(x) = u+v$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[44])
                    formule_latex.make_formule(r"$f'(x) = u'+v'$",listbox, 14, 1)

                    ajouter_element(Liste_cours[45])
                    formule_latex.make_formule(r"$f(x) = uv$",listbox, 14, 0)
                    ajouter_element(Liste_cours[46])
                    formule_latex.make_formule(r"$fu'v + uv'.$",listbox, 14, 1)

                    ajouter_element(Liste_cours[47])
                    formule_latex.make_formule(r"$f(x) = \frac{u}{v}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[48])
                    formule_latex.make_formule(r"$f'(x) = \frac{u'v - uv'}{v^2}$",listbox, 14, 2)

                    saut_2_lignes() 

                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[43])
                    saut_2_lignes() 


            elif Niveau ==7: 

                if num_pnj=="pnj1":
                    ajouter_element(Liste_cours[50])
                    formule_latex.make_formule(r"$  U_{n+1}  $",listbox, 14, 0) 
                    ajouter_element(Liste_cours[51])
                    formule_latex.make_formule(r"$  U_{n}.$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[52])
                    formule_latex.make_formule(r"$  U_{n}.$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[53])
                    saut_2_lignes()

                elif num_pnj=="pnj2":
                    ajouter_element(Liste_cours[54])
                    formule_latex.make_formule(r"$  U_{n+1}  $",listbox, 14, 0) 
                    ajouter_element(Liste_cours[55])
                    formule_latex.make_formule(r"$  U_{n}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[56])
                    formule_latex.make_formule(r"$  U_{n+1} = U_{n} + r $",listbox, 14, 0) 
                    ajouter_element(Liste_cours[57])
                    formule_latex.make_formule(r"$  U_{n} = U_{0} + n \times r $",listbox, 14, 1) 
                    ajouter_element(Liste_cours[58])
                    formule_latex.make_formule(r"$  U_{n}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[59])
                    formule_latex.make_formule(r"$  U_{n+1} = U_{n} + 2$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[60])
                    formule_latex.make_formule(r"$  U_{n} = 1 + 2n$",listbox, 14, 0) 
                    ajouter_element(" ")
                    saut_2_lignes()

                elif num_pnj=="pnj3":
                    ajouter_element(Liste_cours[61])
                    formule_latex.make_formule(r"$V_{n+1}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[62])
                    formule_latex.make_formule(r"$V_{n}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[63])
                    formule_latex.make_formule(r"$V_{n+1} = V{n} \times q $",listbox, 14, 0)
                    ajouter_element(Liste_cours[64])
                    formule_latex.make_formule(r"$V_{0} $",listbox, 14, 0)
                    ajouter_element(Liste_cours[65])
                    formule_latex.make_formule(r"$V_{n} = V_{0} \times q^{n} $",listbox, 14, 1)
                    ajouter_element(Liste_cours[66])
                    formule_latex.make_formule(r"$V_{0}$",listbox, 14, 0)
                    ajouter_element(Liste_cours[67])
                    formule_latex.make_formule(r"$V_{n+1} = V{n} \times 1.7 $",listbox, 14, 1)
                    ajouter_element(Liste_cours[68])
                    formule_latex.make_formule(r"$V_{n} = 0.5 \times 1.7^{n} $",listbox, 14, 0)
                    ajouter_element(" ")
                    saut_2_lignes()

                elif num_pnj=="pnj4":
                    ajouter_element(Liste_cours[69])
                    formule_latex.make_formule(r"$ U_{n+1} - U_{n}$",listbox, 14, 0) 
                    ajouter_element(Liste_cours[70])
                    saut_2_lignes() 

                elif num_pnj=="pnj5":
                    ajouter_element(Liste_cours[71])
                    formule_latex.make_formule(r"$S_{n} = \text{nombre de terme} \times \frac{\text{premier terme + dernier terme}}{2}$",listbox, 14, 1) 
                    ajouter_element(Liste_cours[72])
                    formule_latex.make_formule(r"$S_{n} = \text{premier terme} \times \frac{1 - \text{raison}^{\text{nombre de termes}}}{1 - \text{raison}}$",listbox, 14, 0) 
                    ajouter_element(" ")
                    saut_2_lignes()



            

            if Niveau < 5:
                def open_url(event): # ouvrir le lien dans le navigateur
                    webbrowser.open_new(r"https://youtu.be/B9NMxapgHtg?si=jWGVV_Wq8NYmuMfT")

                #set un des lien nécessaire
                # Marquage du texte pour le lien
                start_index = "26.160"  # Position du début du lien dans le texte
                end_index = "26.163"   # Position de la fin du lien dans le texte

                # Application de la balise pour le lien
                listbox.tag_add("link", start_index, end_index)
                listbox.tag_config("link", foreground="blue", underline=1)
                listbox.tag_bind("link", "<Enter>", lambda e: listbox.config(cursor="hand2"))
                listbox.tag_bind("link", "<Leave>", lambda e: listbox.config(cursor=""))
                listbox.tag_bind("link", "<Button-1>", open_url)
                    
            listbox.config(state=DISABLED)


        # foncion pour la table de fabrication
        def table_craft(event):
            global pnj1_infos
            global pnj2_infos
            global pnj3_infos
            global pnj4_infos
            global pnj5_infos

            global assemble_cle

            # nettoyage
            canvas_infos_possibilite_discussion.delete('all')
            canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=idee)
            
            # on se trouve à coté de la table et si nous possédons tout les élements nécéssaire, nous pouvons fabriquer la clé
            if L[ordonne][abscisse-1] == "¤":

                if assemble_cle == False:
                    
                    #on affiche dans l'aide les infos si c'est déjà fabriqué ou non
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




        #fonction de gestion des dialogues avec les pnj
        def parler_pnj(event):

            # fonction pour afficher progressivement les dialogues
            def affiche_prog(pnj, pnj_infos, Niveau):


                def insert_text(text_complet):

                    Label_btn_suivant_discussion_pnj['state'] = DISABLED
                    for i in range(len(text_complet)):
                        Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL) 
                        text_partiel = text_complet[i]
                        Label_texte_parole_discussion_pnj_scrolltext.insert(END, f"{text_partiel}")
                        Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
                        Label_texte_parole_discussion_pnj_scrolltext.update()
                        time.sleep(0.01)
                    Label_btn_suivant_discussion_pnj['state'] = NORMAL



                global c
                c += 1

                Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
 
                # comme cette partie est commune; on l'affiche au debut si c'est le bon tour
                if pnj_infos == False:

                    # on fait en fonction du pnj parce que le cours est unique à chaque pnj
                    if pnj == "pnj1":
                        # et le cours est différent en fonction du niveau (map qui change)
                        if Niveau ==0:
                            if c==1:
                                insert_text("B’jour jeune aventurier, je pense que j’pourrais bien t’apprendre un truc aujourd’hui.")
                            elif c==2:
                                insert_text("De façon intuitive, une égalité fonctionne un peu comme une balance à deux plateaux \u2696 : si on effectue une opération dans un membre, il faut réaliser la même opération dans l’autre membre pour garder l'équilibre.")
                            elif c==3:
                                insert_text("Tiens voila pour m’avoir écouté; un fragment de clé que j’ai ramené lors de mon dernier voyage !")

                        elif Niveau ==1:
                            if c==1:
                                insert_text("Tiens je parie que tu as croisé ma femme toi ! Eh oui je reconnais cet objet il est à moi mais trêve de plaisanterie je pense que si tu es là jeune aventurier c’est pour continuer ton périple.")
                            elif c==2:
                                insert_text("Pour cela, il te faudra connaître la formule de l’aire d’un disque qui est π x rayon², je vais aussi t’apprendre l’aire d’un triangle est ")
                                formule_latex.make_formule(r"$ \frac{(longueur \times largeur)}{2}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(" et celle d’un carré ou d’un rectangle est longueur x largeur.")

                            elif c==3:
                                insert_text("Tiens voila pour la suite, un bout de quelque chose de l’ancien temps !")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Miaou, Miaou Meow ! Miaou miaou Meow, Miaou Meow. Meow, Miaou Miaou. (Votre Miaou français est encore plus rouillé que votre waf mais vous comprenez : “Salut grand petit être, moi c’est Cana et toi tu m’écoutes bien ! Je parie que tu ne sais pas comment déterminer une équation de droite.")
                            elif c==2:
                                insert_text("Les droites ont une équation de la forme y = mx + p sauf cas particulier, le coefficient m est le coefficient directeur ou pente de la droite et le coefficient p l’ordonné à l’origine.")
                            elif c==3:
                                insert_text("Oh mince tu m’as bien eu, prends ce jouet je le mérite plus.")
                        
                        elif Niveau ==3:
                            if c==1:
                                insert_text("Oh ! Je te connais toi dis donc ! Tu veux que je t’apprenne autre chose ?")
                            elif c==2:
                                insert_text("Eh bien sache qu’il y a 2 manières pour résoudre un système à doubles inconnues, la fin est la même mais la réflexion n’est pas la même, il y a donc la résolution par substitution et la résolution par combinaisons linéaires, d’ailleurs un système à double inconnues permet par exemple de trouver les coordonnées d’un point d’intersection, je parie que ça t’en bouche un coin.")
                            elif c==3:
                                insert_text("Tiens c’est une autre babiole de mon mari.")

                        elif Niveau ==5:
                            if c==1:
                                insert_text(" Salut ! Tu veux que je t’explique un truc vite fait ? Ça pourrait t’aider.")
                            elif c==2:
                                insert_text("Un polynôme du second degré admet comme forme développée : P(x)= ax² + bx + c avec a, b et c des coefficients et a \u2260 0. Chaque polynôme admet une forme canonique sous la forme\n")
                                formule_latex.make_formule(r"$ a( x - \alpha)^2 + \beta$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                formule_latex.make_formule(r"$ \alpha = \frac{-b}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                formule_latex.make_formule(r"$ \beta = \frac{- \Delta}{4a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                formule_latex.make_formule(r"$ \Delta = b^2 - 4ac$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                            elif c==3:
                                insert_text("Allez tiens merci de m’avoir écouté !")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Salut mon ptit jeune, t’as du croiser ma femme toi, je me trompe ? Mais trêve de mondanité je vais t’apprendre ce qu’est le taux de variation d’une fonction f en un point a, en réalité c’est une mesure de la rapidité avec laquelle f change près de a.")
                            elif c==2:
                                insert_text("On dit que f est dérivable en a si la limite suivante existe : ")
                                formule_latex.make_formule(r"$ f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("Si cette limite existe, elle est appelée la dérivée de f en a et est notée f’(a)")
                            elif c==3:
                                insert_text("Tiens prends ça tu m’as bien écouté, allez roulez jeunesse.")

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Miaou, Miaou Meow ! Miaou miaou Meow, Miaou Meow. Meow, Miaou Miaou. (Votre Miaou français est encore plus rouillé que votre waf mais vous comprenez : “Salut toi, tu voudrais que dans ma grande bonté je t’offre un renseignement ?")
                            elif c==2:
                                insert_text("Bon j’accepte alors écoute bien, une suite est une liste ordonnée de nombres, on la définit souvent par : une relation de récurrence avec le terme n+1 noté ")
                                formule_latex.make_formule(r"$  U_{n+1}  $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("en fonction du terme n noté ")
                                formule_latex.make_formule(r"$  U_{n}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("Avec l’expression de récurrence, il est nécessaire de connaître un terme de la suite (par exemple U0 ou U1 etc…) pour calculer les autres. Ou une formule explicite qui permet d’exprimer directement le terme ")
                                formule_latex.make_formule(r"$  U_{n}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(" en fonction de l’indice n.”)")
                            elif c==3:
                                insert_text("Un objet se trouvant par terre attire votre regard et vous le prenez.")

                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_text_nom_pnj_strvar.set("")
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                            Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
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
                                insert_text("Wouf Wouf, Wouf Wouf Wouf, Wouf Wouf Woaf ! Wouf ?(Votre waf français est un peu rouillé mais vous comprenez : “Salut moi c’est Iggy, retiens bien ce que je vais te dire !")
                            elif c==2:
                                insert_text("On peut ajouter (ou soustraire) un même nombre aux deux membres d'une égalité. \n    a = b équivaut à a + c = b + c \n    a = b  équivaut à a - c = b - c \nOn peut multiplier (ou diviser) les deux membres d'une égalité par un même nombre non nul. \n    a = b équivaut à a × c = b × c \n    a = b équivaut à   a/c = b/c(c ≠ 0) \npar exemple 5x + 2 = 17 donne 5x + 2 - 2 = 17 - 2 puis 5x/5 = 15/5 donc x = 3")
                            elif c==3:
                                insert_text("D’ailleurs t’aurais pas des croquettes contre mon os doré ?")
                                
                        elif Niveau ==1:
                            if c==1:
                                insert_text("Salut toi t’aurais pas envie de savoir calculer le volume d’un cylindre par hasard ? Nan ?")
                            elif c==2:
                                insert_text("Bon si jamais c’est la hauteur multipliée par l’aire de la base. D’ailleurs il est important de savoir que pour plein de volume il s’agit souvent de l’aire de la base x la hauteur, essaie avec un cube par exemple !")
                            elif c==3:
                                insert_text("Tiens je te passe ça comme t’as l’air sympa.")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Dit jeune homme, savais-tu que les droites parallèles à l’axe des ordonnées (“droites verticales”) ne se présentent pas sous la forme y = mx + p.")
                            elif c==2:
                                insert_text("Elles ont une équation de forme x=c sachant que c est un nombre par exemple x = 2 est une droite verticale qui passe par l’abscisse 2.")
                            elif c==3:
                                insert_text("Tiens mon brave prends cet objet.")
                        
                        elif Niveau ==3:
                            if c==1:
                                insert_text("Encore un jeune ! Mais tu as l’air curieux alors je vais t’apprendre quelque chose, dans un système la méthode de substitution consiste à isoler une des variables dans l'une des équations et à substituer cette expression dans l'autre équation.")
                            elif c==2:
                                insert_text("Cela permet de réduire le système à une seule équation avec une seule inconnue, qui peut alors être résolue.")
                            elif c==3:
                                insert_text("Allez tiens ce bout de clé te sera peut être utile s’il ne part pas en poussière avant.")

                        elif Niveau ==5:
                            if c==1:
                                insert_text("Wouf Wouf Wouf(x), Wouf Wouf Wouf Wouf ! Wouf(x) Wouf(x) Wouf(x) (Votre waf français est un peu rouillé mais vous comprenez : “Salut moi c’est Iggy ! Tu veux que je t’apprenne un truc qui vaut un tas de croquettes ? Apparemment pour résoudre P(x) = 0 il faudrait déterminer le discriminant delta, j’espère que tu connais la formule :")
                            elif c==2:
                                insert_text("On m’a dit dans le chenil que si le delta > 0, P(x) admet deux solutions distinctes :\nPour trouver la première c’est")
                                formule_latex.make_formule(r"$ x1 = \frac{-b - \sqrt{\Delta}}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("et la deuxième c’est") 
                                formule_latex.make_formule(r"$ x2 = \frac{-b + \sqrt{\Delta}}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Attention parce qu’il peut se factoriser par P(x)= a(x-x1)(x-x2)   \n\nPar contre si delta = 0 alors il n’en admet qu’une unique dite double : \net la solution c’est ")
                                formule_latex.make_formule(r"$ x = \alpha = \frac{-b}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Et la il se factorise par ")
                                formule_latex.make_formule(r"$ a(x-\alpha)^2$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Mais alors la surprise si delta < 0 il n’admet pas de solution et ne se factorise pas")

                            elif c==3:
                                insert_text("D’ailleurs t’aurais pas des croquettes contre mon os doré ?”)")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Il fait chaud aujourd’hui non ? Tu préfères une glace ou une leçon ?")
                            elif c==2:
                                insert_text("Alors va pour la leçon je vais t’apprendre que la dérivée d'une fonction en un point donne la pente de la tangente à la courbe de la fonction en ce point. Elle se calcule grâce la formule T : y = f’(a)(x - a) + f(a) avec a un point de la courbe.")
                            elif c==3:
                                insert_text("Allez prends ça c’est pas une glace mais ça fera l’affaire.")

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Bonjour la jeunesse, je vais t’expliquer un truc utile dans la vie, dans une suite arithmétique le terme ")
                                formule_latex.make_formule(r"$  U_{n+1}  $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("se calcule à l’aide du terme précédent ")
                                formule_latex.make_formule(r"$  U_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("auquel on additionne ou on retranche une constante nommée raison, notée r.")
                            elif c==2:
                                insert_text("La relation de récurrence de la suite se note : ")
                                formule_latex.make_formule(r"$  U_{n+1} = U_{n} + r $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("avec U0, le premier terme de la suite.\n\nLa formule explicite de la suite se note : ")
                                formule_latex.make_formule(r"$  U_{n} = U_{0} + n \times r $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                            elif c==3:
                                insert_text("Tiens un petit exemple avec la suite")
                                formule_latex.make_formule(r"$  U_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("de premier terme U0 = 1 et de raison r =2 : \nForme de récurrence :")
                                formule_latex.make_formule(r"$  U_{n+1} = U_{n} + 2$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Formule explicite :")
                                formule_latex.make_formule(r"$  U_{n} = 1 + 2n$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 

                                insert_text("Tiens mon bon, prends cet objet tu le mérites.")

                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_text_nom_pnj_strvar.set("")
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                            Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
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
                                insert_text("Qu’est ce tu dis ?! Que tu n’as pas parlé ? Autant pour moi mon petit mes oreilles ne fonctionnent plus aussi bien qu’avant, j’ai l’impression que t’essais d’aller en ville pour que tu puisses passer je vais te montrer un truc.")
                            elif c==2:
                                insert_text("Quand tu résous une équation s’il y a des x des deux côtés essaie de tout mettre du même côté ce sera plus simple tu verras ! Par exemple : \n                 3x + 2 = 5x + 3 \néquivaut à  3x + 2 - 5x = 5x + 3 - 5x \néquivaut à  -2x + 2 = 3 \net ainsi de suite")
                            elif c==3:
                                insert_text("Tiens avant de partir prends ce bidule il appartient à mon mari redonne lui si tu le vois en ville.")

                        elif Niveau ==1:
                            if c==1:
                                insert_text("Dis donc toi, il fait chaud aujourd’hui un petit rafraichissement ?")
                            elif c==2:
                                insert_text("D’ailleurs tu savais qu’un cône avait pour volume celui d’un cylindre divisé par 3. C’est un peu la même chose pour une pyramide mais dans ce cas la c’est le volume du prisme qui est divisé par 3.")
                            elif c==3:
                                insert_text("Allez tiens c’est pas une glace mais ça te sera utile je pense.")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Salut à toi jeune aventurier. Alors si aujourd'hui je me permets de te parler, c'est pour une raison très simple. Savais-tu que 95 % de la population détient 5 % des richesses ? Alors je ne te garantie pas d’en faire partie mais au moins de partir sur de vraies bases ! Il faut que tu te poses les bonnes questions.")
                            elif c==2:
                                insert_text("Il faut savoir que dans une équation sous forme mx + p, p est l’ordonnée à l’origine et qu’il se calcule avec p = yA - m.xA et")
                                formule_latex.make_formule(r"$ m = \frac{yB - yA}{xB - xA}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("il te faudra simplement les coordonnées des points A(xA;yA) et B(xB;yB) de la droite ou tu te fermera des portes toute ta vie !")
                            elif c==3:
                                insert_text("Moi je pense qu’il y a une conclusion. Alors soit tu m'écoutes, soit tu vas demander des écus à tes parents pour tenter de passer la porte. Avec moi c'est comme ça que ça marche, OK ? Fais le bon choix, je t’offre ça pour bien commencer ta vie.")
                        
                        elif Niveau ==3:
                            if c==1:
                                insert_text("Salut à toi jeune… ! Attends ! Je t’ai pas déjà fait le coup à toi ? Zut ! Bon bah tant pis… [PAUSE] Salut à toi jeune aventurier. Alors si aujourd'hui je me permets de te parler, c'est pour une raison très simple. Savais-tu que 95 % de la population détient 5 % des richesses ? Alors je ne te garantie pas d’en faire partie mais au moins de partir sur de vraies bases ! Il faut que tu te poses les bonnes questions.")
                            elif c==2:
                                insert_text("Il faut savoir résoudre un système à double inconnues, je te fais une démonstration : \nPrenons\n")
                                formule_latex.make_formule(r"$\left\{ \begin{array}{lr} x + y & = 5 \\ 2x - y & = 1 \end{array} \right.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("1. Tu isoles une variable à l’aide d’une équation : \n    y = 5 - x  \n2. Tu substitues y par c-x dans l’autre équation : \n   2x - (5 - x) = 1  \n3. Tu résous pour trouver x : \n   2x - 5 + x = 1  \n   3x - 5 = 1 \n   3x = 6 \n   x = 2 \n4. Et enfin tu remplaces par 2 et tu trouves y : \n    y = 5 - 2 = 3  \nEt paf ta solution \n   x = 2, y = 3 ")
                            elif c==3:
                                insert_text("Faut le savoir ou tu te fermera des portes toute ta vie ! Moi je pense qu’il y a une conclusion. Alors soit tu m'écoutes, soit tu vas demander des écus à tes parents pour tenter de passer la porte. Avec moi c'est comme ça que ça marche, OK ? Fais le bon choix, je t’offre ça pour bien commencer ta vie.")

                        elif Niveau ==5:
                            if c==1:
                                insert_text("Hein ?! Parle plus fort !! Oh bonjour mon petit jeunot, excuse moi je suis un peu dur d’oreille. Si tu comptes continuer tes voyages tu devrais te préparer à apprendre que pour déterminer le signe du polynôme P(x), on doit utiliser le discriminant delta et alpha.")
                            elif c==2:
                                insert_text("Quand delta > 0, P(x) est du signe de a à l'extérieur des racines x1 et x2, c'est-à-dire sur les intervalles")
                                formule_latex.make_formule(r"$\left] -\infty, x1 \right[ \cup \left] x2, +\infty \right[.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("et donc il est du signe opposé à a entre les racines, c'est-à-dire sur l'intervalle")
                                formule_latex.make_formule(r"$\left] x1, x2 \right[.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Mais quand delta = 0, P(x)  est toujours du signe de a sur R excepté à x = alpha où il est nulle. \n\nPar contre quand delta < 0, P(x) est toujours du signe de a\n\nAprès pour les variations c’est très simple, lorsque a est positif la courbe représentative de P(x) décroît jusqu’à x=alpha puis croît cependant lorsque a est négatif la courbe croît jusqu’à x=alpha puis décroît.")

                            elif c==3:
                                insert_text("Avant de partir prends ce petit truc de mon mari, je ne sais pas à quoi ça sert alors peut être que toi si.")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Salut toi, tu savais qu’il y avait des cas qui ne changent jamais et donc super simple à mémoriser, regarde pour la dérivée d'une constante : ")
                                formule_latex.make_formule(r"$f(x) =c$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("alors ")
                                formule_latex.make_formule(r"$f'(x) = 0.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)
                            elif c==2:
                                insert_text("Celle de ")
                                formule_latex.make_formule(r"$x^n : f(x) = x^n$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("alors ")
                                formule_latex.make_formule(r"$f'(x) = nx^{n-1}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)


                                insert_text("Aussi celle de ")
                                formule_latex.make_formule(r"$nx : f(x) = nx$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = n. $",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Ainsi que ")
                                formule_latex.make_formule(r"$ \frac{1}{x} : f(x) = \frac{1}{x}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = \frac{-1}{x^2}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)


                                insert_text("Même celle la ")
                                formule_latex.make_formule(r"$ \sqrt{x} : f(x) = \sqrt{x}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = \frac{1}{2 \sqrt{x}}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)


                            elif c==3:
                                insert_text("Alors qu’avec la somme et différence ça donne ceci : ")
                                formule_latex.make_formule(r"$f(x) = u+v$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = u'+v'$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Ensuite un produit : ")
                                formule_latex.make_formule(r"$f(x) = uv$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$fu'v + uv'.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Et finalement le quotient : ")
                                formule_latex.make_formule(r"$f(x) = \frac{u}{v}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = \frac{u'v - uv'}{v^2}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)


             

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Salut à toi jeune aventurier. Alors si aujourd'hui je me permets de te parler, c'est pour une raison très simple. Savais-tu que 95 % de la population détient 5 % des richesses ? Alors je ne te garantie pas d’en faire partie mais au moins de partir sur de vraies bases ! Il faut que tu te poses les bonnes questions. Il faut savoir que dans une suite géométrique le terme ")
                                formule_latex.make_formule(r"$V_{n+1}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("se calcule à l’aide du terme précédent ")
                                formule_latex.make_formule(r"$V_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("auquel on multiplie une constante (la raison), notée q.")
                            elif c==2:
                                insert_text("Donc la relation de récurrence de la suite se note : ")
                                formule_latex.make_formule(r"$V_{n+1} = V{n} \times q $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("avec V0 le premier terme de la suite.\nAprès la formule explicite de la suite se note : ")
                                formule_latex.make_formule(r"$V_{n} = V_{0} \times q^{n} $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1)
                                insert_text("Exemple de la suite Vn de premier terme ")
                                formule_latex.make_formule(r"$V_{0} = 0.5 $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("et de raison q = 1.7 : \nDu coup voila la forme de récurrence : ")
                                formule_latex.make_formule(r"$V_{n+1} = V{n} \times 1.7 $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1)
                                insert_text("Et la formule explicite : ")
                                formule_latex.make_formule(r"$V_{n} = 0.5 \times 1.7^{n} $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)

                            elif c==3:
                                insert_text("Oublie pas ou tu te fermera des portes toute ta vie !")


                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_text_nom_pnj_strvar.set("")
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                            Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
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
                                insert_text("Zalut monzieur dis tu zavais qu’il pozait des zénigmes à la porte ?")
                            elif c==2:
                                insert_text("Je zais pas ze qu’il y a là bas mais au cas où ze vais t’apprendre à calculer le volume d’une zphère. Il zuffit de faire .")
                                formule_latex.make_formule(r"$ \frac{4}{(3\pi \times r^3)}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                            elif c==3:
                                insert_text("Tient au fait z’arrête pas de m’en mettre partout.")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Salut moi c’est Delta.")
                            elif c==2:
                                insert_text("Tu savais qu’une fonction affine admettait une expression algébrique de la forme f(x) = mx + p et que sa représentation graphique est une droite ?")
                            elif c==3:
                                insert_text("Tiens je te passe ça j’en ai plus besoin.")
                        
                        elif Niveau ==3:
                            if c==1:
                                insert_text("Salut toi ! Une des deux méthodes de résolution d’un système à 2 inconnues, la combinaison linéaire consiste à manipuler les équations pour éliminer l'une des variables.")
                            elif c==2:
                                insert_text("Cette manipulation se fait généralement en multipliant les équations par des coefficients appropriés afin d'obtenir des coefficients opposés pour une des variables, puis en additionnant ou soustrayant les équations.")
                            elif c==3:
                                insert_text("Tiens prends cette colle elle ne me sert à rien.")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Zalut toi, dit tu zavais qu’une dérivée peut zervir à connaître les zintervalles croizant et décroizant.")
                            elif c==2:
                                insert_text("Lorzque f’(x) > 0 alors f(x) est croizant et lorzque f’(x) < 0 alors f(x) est décroizant.")
                            elif c==3:
                                insert_text("Tiens ze croyais que z’était de la glace et ze m’en zuis mis partout.")
                        
                        elif Niveau ==7:
                            if c==1:
                                insert_text("Salut toi, dit tu voudrais pas savoir reconnaître si une suite est arithmétique ou géométrique ? Alors écoute bien, pour reconnaître si une suite est une suite arithmétique on peut vérifier si la différence ")
                                formule_latex.make_formule(r"$ U_{n+1} - U_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("est constante pour tout entier naturel n, ce qui donnera la raison par la même occasion.")
                            elif c==2:
                                insert_text("Pour reconnaître si une suite est une suite géométrique on peut vérifier si le rapport")
                                formule_latex.make_formule(r"$ \frac{V_{n+1}}{U_{n}}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("est constant pour tout entier naturel n, ce qui donnera la raison par la même occasion.")
                            elif c==3:
                                insert_text("Tiens je te donne ça, c’est un peu inutile pour moi ^^.")

                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_text_nom_pnj_strvar.set("")
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                            Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
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
                                insert_text("Doucement moussaillon tu vas te mouiller ! Tu sais c’est vachement utile de connaître les coordonnées du point d’intersection de 2 droites, ça m’a sauvé plus jeune alors je vais t’apprendre.")
                            elif c==2:
                                insert_text("Quand tu as les 2 équations réduites tu t’amuses à faire une équation des 2 soit mx + p = m’x + p’.")
                            elif c==3:
                                insert_text("Tiens mon brave si tu as une barre à rafistoler ça t’aidera !")

                        elif Niveau ==3:
                            if c==1:
                                insert_text("Doucement moussaillon, tu vas te mouiller ! Tu sais, c’est vachement utile de savoir résoudre des systèmes d’équations, ça m’a sauvé plus jeune alors je vais t’apprendre.")
                            elif c==2:
                                insert_text("Un exemple c’est le mieux alors :\n")
                                formule_latex.make_formule(r"$\left\{ \begin{array}{lr} 2x + y & = 5 \\ 3x - y & = 4 \end{array} \right.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("1. On additionne les deux équations pour éliminer y  : \n   (2x + y) + (3x - y) = 5 + 4  \n    2x + 3x + y - y = 9 \n    5x = 9 \n    x = 9/5  \n2. Puis on remplace x par 9/5 dans la première équation pour trouver y : \n    2*(9/5) + y = 5 \n    18/5 + y = 5 \n    y = 5 - 18/5 \n    y = 25/5 - 18/5 \n    y = 7/5 \nEt comme par enchantement ta solution \n    x = 9/5, y = 7/5")
                            elif c==3:
                                insert_text("C’est aussi simple que ça. Tiens, mon brave, si tu as un pont à nettoyer, ça t’aidera !")

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Salut marin d’eau douce, je vais t’apprendre à calculer la somme des n premiers termes d’une suite. Alors pour la somme des n premiers termes d’une suite arithmétique il faut utiliser la formule : ")
                                formule_latex.make_formule(r"$S_{n} = \text{nombre de terme} \times \frac{\text{premier terme + dernier terme}}{2}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                            elif c==2:
                                insert_text("Pour la somme des n premiers termes d’une suite géométrique il faut la formule :")
                                formule_latex.make_formule(r"$S_{n} = \text{premier terme} \times \frac{1 - \text{raison}^{\text{nombre de termes}}}{1 - \text{raison}}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 

                            elif c==3:
                                insert_text("Tiens moussaillon ça t’apprendra à monter les échelons !")
                        
                        if c == 4:
                            canvas_tete_pnj_grand.delete("all")
                            Label_text_nom_pnj_strvar.set("")
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                            Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                            Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
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
                                insert_text("On s’recroise dit donc ! T’as oublié ce qu’j’ai dit ? Alors écoute bien j’vais répéter, de façon intuitive, une égalité fonctionne un peu comme une balance à deux plateaux \u2696: si on effectue une opération dans un membre, il faut réaliser la même opération dans l’autre membre pour garder l'équilibre.")
                            elif c==2:
                                insert_text("Je t'ai déjà donné mon fragment de clé; bon courage dans ta quête !")

                        elif Niveau ==1:
                            if c==1:
                                insert_text("Alors aussi mauvaise mémoire que ma femme ?")
                            elif c==2:
                                insert_text("Écoute bien cette fois; la formule de l’aire d’un disque est π x rayon², l’aire d’un triangle est ")
                                formule_latex.make_formule(r"$ \frac{(longueur \times largeur)}{2}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("et celle d’un carré ou d’un rectangle est longueur x largeur.")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Meow Miaou !! Meow, Miaou Meow Miaou Miaou. Miaou Miaou Meow. Meow… (Vous comprenez : “Comment j’ai pu le laisser partir avec mon jouet !! Oh tu es de retour, tu veux que je te répète que les droites ont une équation de la forme y = mx + p sauf cas particulier, le coefficient m est le coefficient directeur ou pente de la droite et le coefficient p l’ordonné à l’origine.")
                            elif c==2:
                                insert_text("D’accord mais alors tu me repasses mon jouet. Oh…")

                        elif Niveau ==3:
                            if c==1:
                                insert_text("Re Bonjour jeune homme ! Tu n’as pas bien compris et tu veux que je réexplique ?")
                            elif c==2:
                                insert_text("Je comprends, écoute bien, il y a 2 manières pour résoudre un système à doubles inconnues, la fin est la même mais la réflexion n’est pas la même, il y a donc la résolution par substitution et la résolution par combinaisons linéaires, d’ailleurs un système à double inconnues permet par exemple de trouver les coordonnées d’un point d’intersection.")

                        elif Niveau ==5:
                            if c==1:
                                insert_text("T’as oublié et tu veux que je répète ?")
                            elif c==2:
                                insert_text("Alors écoute bien cette fois, un polynôme du second degré admet comme forme développée : P(x)= ax² + bx + c avec a, b et c des coefficients et a \u2260 0. Chaque polynôme admet une forme canonique sous la forme\n")
                                formule_latex.make_formule(r"$ a( x - \alpha)^2 + \beta$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                formule_latex.make_formule(r"$ \alpha = \frac{-b}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                formule_latex.make_formule(r"$ \beta = \frac{- \Delta}{4a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                formule_latex.make_formule(r"$ \Delta = b^2 - 4ac$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Alors toi aussi tu as besoin d’un sonotone comme ma femme ? Bon je vais te réexpliquer ce qu’est le taux de variation d’une fonction f en un point a, en réalité c’est une mesure de la rapidité avec laquelle f change près de a.")
                            elif c==2:
                                insert_text("On dit que f est dérivable en a si la limite suivante existe : ")
                                formule_latex.make_formule(r"$ f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("Si cette limite existe, elle est appelée la dérivée de f en a et est notée f’(a).")
                        elif Niveau ==7:
                            if c==1:
                                insert_text("Meow Miaou !! Meow, Miaou Meow Miaou Miaou. Miaou Miaou Meow. Meow… (Vous comprenez : “Alors tu reviens me voir, pour abuser de ma bonté, mais je refuse cette fois ci de te redire qu’une suite est une liste ordonnée de nombres, on la définit souvent par : une relation de récurrence avec le terme n+1 noté ")
                                formule_latex.make_formule(r"$  U_{n+1}  $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("en fonction du terme n noté ")
                                formule_latex.make_formule(r"$  U_{n}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                            elif c==2:
                                insert_text("Avec l’expression de récurrence, il est nécessaire de connaître un terme de la suite (par exemple U0 ou U1 etc…) pour calculer les autres. Ou une formule explicite qui permet d’exprimer directement le terme ")
                                formule_latex.make_formule(r"$  U_{n}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(" en fonction de l’indice n.”)")


                    #pnj 2 alternatif
                    elif pnj == "pnj2":
                        if Niveau ==0:
                            if c==1:
                                insert_text("Wouf Wouf Wouf ? Wouf Wouf, Wouf. (Vous comprenez : “T’as oublié tout ce que j’ai dit ? Ça va te couter cher en croquettes mais je vais répéter, on peut ajouter (ou soustraire) un même nombre aux deux membres d'une égalité. \n    a = b équivaut à a + c = b + c \n    a = b  équivaut à a - c = b - c \nOn peut multiplier (ou diviser) les deux membres d'une égalité par un même nombre non nul. \n    a = b équivaut à a × c = b × c \n    a = b équivaut à   a/c = b/c(c ≠ 0) \npar exemple 5x + 2 = 17 donne 5x + 2 - 2 = 17 - 2 puis 5x/5 = 15/5 donc x = 3.")
                            elif c==2:
                                insert_text("Je n'ai plus d'os doré pour toi... Mais il te reste des croquettes ?")

                        elif Niveau ==1:
                            if c==1:
                                insert_text("Finalement t’as pas écouté et tu aurais dû ?")
                            elif c==2:
                                insert_text("Le volume du cylindre c’est la hauteur multipliée par l’aire de la base. D’ailleurs il est important de savoir que pour plein de volume il s’agit souvent de l’aire de la base x la hauteur, essaie avec un cube par exemple !")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Re Bonjour mon brave. Tu n’as pas écouté et tu voudrais que je répète ? Ah la jeunesse ce n’est plus ce que c’était, je vais te réexpliquer mais c’est la dernière fois.")
                            elif c==2:
                                insert_text("Les droites parallèles à l’axe des ordonnées (“droites verticales”) ne se présentent pas sous la forme y = mx + p. mais ont une équation de forme x=c sachant que c est un nombre par exemple x = 2 est une droite verticale qui passe par l’abscisse 2.")
        
                        elif Niveau ==3:
                            if c==1:
                                insert_text("Tu n’as pas compris ou pas écouté ? Je ne te l'expliquerai qu’une fois de plus alors attention la méthode de substitution consiste à isoler une des variables dans l'une des équations et à substituer cette expression dans l'autre équation.")
                            elif c==2:
                                insert_text("Cela permet de réduire le système à une seule équation avec une seule inconnue, qui peut alors être résolue.")

                        elif Niveau ==5:
                            if c==1:
                                insert_text("Wouf Wouf Wouf ? Wouf Wouf, Wouf. (Vous comprenez : “T’as oublié tout ce que j’ai dit ? Ça va te couter cher en croquettes mais je vais répéter, apparemment pour résoudre P(x) = 0 il faudrait déterminer le discriminant delta, j’espère que tu connais la formule :")
                            elif c==2:
                                insert_text("On m’a dit dans le chenil que si le delta > 0, P(x) admet deux solutions distinctes :\nPour trouver la première c’est")
                                formule_latex.make_formule(r"$ x1 = \frac{-b - \sqrt{\Delta}}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("et la deuxième c’est") 
                                formule_latex.make_formule(r"$ x2 = \frac{-b + \sqrt{\Delta}}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Attention parce qu’il peut se factoriser par P(x)= a(x-x1)(x-x2)   \n\nPar contre si delta = 0 alors il n’en admet qu’une unique dite double : \net la solution c’est ")
                                formule_latex.make_formule(r"$ x = \alpha = \frac{-b}{2a}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Et la il se factorise par ")
                                formule_latex.make_formule(r"$ a(x-\alpha)^2$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Mais alors la surprise si delta < 0 il n’admet pas de solution et ne se factorise pas")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Tu voulais une glace en fait, désolé mais les enfants m’ont tout pris. Je peux te réexpliquer si tu veux pour compenser.")
                            elif c==2:
                                insert_text("Alors écoute bien la dérivée d'une fonction en un point donne la pente de la tangente à la courbe de la fonction en ce point. Elle se calcule grâce la formule T : y = f’(a)(x - a) + f(a) avec a un point de la courbe.")

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Tu n’as pas bien écouté ?! Je suis déçu, je vais te réexpliquer mais attention il n’y aura pas de prochaine fois. Dans une suite arithmétique le terme ")
                                formule_latex.make_formule(r"$  U_{n+1}  $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("se calcule à l’aide du terme précédent ")
                                formule_latex.make_formule(r"$  U_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("auquel on additionne ou on retranche une constante nommée raison, notée r.")
                            elif c==2:
                                insert_text("La relation de récurrence de la suite se note : ")
                                formule_latex.make_formule(r"$  U_{n+1} = U_{n} + r $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("avec U0, le premier terme de la suite.\n\nLa formule explicite de la suite se note : ")
                                formule_latex.make_formule(r"$  U_{n} = U_{0} + n \times r $",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Tiens un petit exemple avec la suite")
                                formule_latex.make_formule(r"$  U_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("de premier terme U0 = 1 et de raison r =2 : \nForme de récurrence :")
                                formule_latex.make_formule(r"$  U_{n+1} = U_{n} + 2$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Formule explicite :")
                                formule_latex.make_formule(r"$  U_{n} = 1 + 2n$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 


                    #pnj 3 alternatif
                    elif pnj == "pnj3":
                        if Niveau ==0:
                            if c==1:
                                insert_text("ZzZ ZzZ… Ah ! Tu m’as fait peur, je suis vieille tu sais. Comment ? Tu veux que je réexplique ? Alors je vais te remontrer, quand tu résous une équation s’il y a des x des deux côtés essaie de tout mettre du même côté ce sera plus simple tu verras ! Par exemple : \n                3x + 2 = 5x + 3 \néquivaut à  3x + 2 - 5x = 5x + 3 - 5x \néquivaut à  -2x + 2 = 3 \net ainsi de suite")
                            elif c==2:
                                insert_text("Je n'ai plus rien à te donner, bonne journée !")

                        elif Niveau ==1:
                            if c==1:
                                insert_text("Tu veux une glace au final ? Désolé mais les enfants m’ont tout pris.")
                            elif c==2:
                                insert_text("Je te propose de réécouter mon histoire de cône, pour calculer le volume d’un cône c’est le volume du cylindre que tu divises par 3. C’est un peu la même chose pour une pyramide mais dans ce cas la c’est le volume du prisme qui est divisé par 3.")

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Alors jeune aventurier tu veux que je te réexplique comment la vie fonctionne ?")
                            elif c==2:
                                insert_text("Pour comprendre faut que tu saches que dans une équation sous forme mx + p, p est l’ordonnée à l’origine et qu’il se calcule avec p = yA - m.xA et ")
                                formule_latex.make_formule(r"$ m = \frac{yB - yA}{xB - xA}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("il te faudra simplement les coordonnées des points A(xA;yA) et B(xB;yB) de la droite, alors tu entrevois la vrai vie maintenant ?")

                        elif Niveau ==3:
                            if c==1:
                                insert_text("Alors jeune aventurier tu veux que je te réexplique comment la vie fonctionne ?")
                            elif c==2:
                                insert_text(" Il faut savoir résoudre un système à double inconnues, je te fais une démonstration : \nPrenons\n")
                                formule_latex.make_formule(r"$\left\{ \begin{array}{lr} x + y & = 5 \\ 2x - y & = 1 \end{array} \right.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                                insert_text("1. Tu isoles une variable à l’aide d’une équation : \n    y = 5 - x  \n2. Tu substitues y par c-x dans l’autre équation : \n    x - (5 - x) = 1 \n3. Tu résous pour trouver x : \n    2x - 5 + x = 1 \n    3x - 5 = 1 \n    3x = 6 \n    x = 2 \n4. Et enfin tu remplaces par 2 et tu trouves y : \n    y = 5 - 2 = 3 \nEt paf ta solution \n    x = 2, y = 3 , alors tu entrevois la vraie vie maintenant ?")

                        elif Niveau ==5:
                            if c==1:
                                insert_text("Comment ?! Encore toi ?! Tu veux que je réexplique ?! Alors cette fois retiens que pour déterminer le signe du polynôme P(x), on doit utiliser le discriminant delta et alpha.")
                            elif c==2:
                                insert_text("Quand delta > 0, P(x) est du signe de a à l'extérieur des racines x1 et x2, c'est-à-dire sur les intervalles")
                                formule_latex.make_formule(r"$\left] -\infty, x1 \right[ \cup \left] x2, +\infty \right[$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("et donc il est du signe opposé à a entre les racines, c'est-à-dire sur l'intervalle")
                                formule_latex.make_formule(r"$\left] x1, x2 \right[ $",Label_texte_parole_discussion_pnj_scrolltext, 14, 2) 
                                insert_text("Mais quand delta = 0, P(x)  est toujours du signe de a sur R excepté à x = alpha où il est nulle. \n\nPar contre quand delta < 0, P(x) est toujours du signe de a\n\nAprès pour les variations c’est très simple, lorsque a est positif la courbe représentative de P(x) décroît jusqu’à x=alpha puis croît cependant lorsque a est négatif la courbe croît jusqu’à x=alpha puis décroît.")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Tu veux que te réexplique tout ce que j’ai dis ? Bon, ok mais écoute mieux cette fois, pour la dérivée d'une constante :")
                                formule_latex.make_formule(r"$f(x) =c$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("alors ")
                                formule_latex.make_formule(r"$f'(x) = 0.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                            elif c==2:
                                insert_text("Celle de ")
                                formule_latex.make_formule(r"$x^n : f(x) = x^n$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("alors ")
                                formule_latex.make_formule(r"$f'(x) = nx^{n-1}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Aussi celle de ")
                                formule_latex.make_formule(r"$nx : f(x) = nx$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = n. $",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Ainsi que ")
                                formule_latex.make_formule(r"$ \frac{1}{x} : f(x) = \frac{1}{x}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = \frac{-1}{x^2}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)


                                insert_text("Même celle la ")
                                formule_latex.make_formule(r"$ \sqrt{x} : f(x) = \sqrt{x}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = \frac{1}{2 \sqrt{x}}.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Alors qu’avec la somme et différence ça donne ceci : ")
                                formule_latex.make_formule(r"$f(x) = u+v$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = u'+v'$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Ensuite un produit : ")
                                formule_latex.make_formule(r"$f(x) = uv$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$fu'v + uv'.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)

                                insert_text("Et finalement le quotient : ")
                                formule_latex.make_formule(r"$f(x) = \frac{u}{v}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text(", alors ")
                                formule_latex.make_formule(r"$f'(x) = \frac{u'v - uv'}{v^2}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 2)


                        elif Niveau ==7:
                            if c==1:
                                insert_text("Alors jeune aventurier tu veux que je te réexplique comment la vie fonctionne ? Pour comprendre faut que tu saches que dans une suite géométrique le terme ")
                                formule_latex.make_formule(r"$V_{n+1}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("se calcule à l’aide du terme précédent ")
                                formule_latex.make_formule(r"$V_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("auquel on multiplie une constante (la raison), notée q.")
                            elif c==2:
                                insert_text("Donc la relation de récurrence de la suite se note : ")
                                formule_latex.make_formule(r"$V_{n+1} = V{n} \times q $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("avec V0 le premier terme de la suite.\nAprès la formule explicite de la suite se note : ")
                                formule_latex.make_formule(r"$V_{n} = V_{0} \times q^{n} $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1)
                                insert_text("Exemple de la suite Vn de premier terme ")
                                formule_latex.make_formule(r"$V_{0} = 0.5 $",Label_texte_parole_discussion_pnj_scrolltext, 14, 0)
                                insert_text("et de raison q = 1.7 : \nDu coup voila la forme de récurrence : ")
                                formule_latex.make_formule(r"$V_{n+1} = V{n} \times 1.7 $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1)
                                insert_text("Et la formule explicite : ")
                                formule_latex.make_formule(r"$V_{n} = 0.5 \times 1.7^{n} $",Label_texte_parole_discussion_pnj_scrolltext, 14, 1)
                                insert_text("Alors tu entrevois la vraie vie maintenant ?")


                    #pnj 4 alternatif
                    elif pnj == "pnj4":
                        if Niveau ==1:
                            if c==1:
                                insert_text("T’as pas réussi à passer la porte ?")
                            elif c==2:
                                insert_text("Alors ze vais te réexpliquer, pour calculer le volume d’une zphère il zuffit de faire ")
                                formule_latex.make_formule(r"$ \frac{4}{(3\pi \times r^3)}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 

                        elif Niveau ==2:
                            if c==1:
                                insert_text("Tu te rappelles plus ce que j’ai dit ?")
                            elif c==2:
                                insert_text("Une fonction affine admet une expression algébrique de la forme f(x) = mx + p et sa représentation graphique est une droite.")

                        elif Niveau ==3:
                            if c==1:
                                insert_text("Rebonjour ! Tu voudrais que je te réexplique ? Pas de soucis, écoute bien : Une des deux méthodes de résolution d’un système à 2 inconnues, la combinaison linéaire consiste à manipuler les équations pour éliminer l'une des variables.")
                            elif c==2:
                                insert_text("Cette manipulation se fait généralement en multipliant les équations par des coefficients appropriés afin d'obtenir des coefficients opposés pour une des variables, puis en additionnant ou soustrayant les équations.")

                        elif Niveau ==6:
                            if c==1:
                                insert_text("Alors t’as rien n’écouté ? Ba ze vais te réexpliquer.")
                            elif c==2:
                                insert_text("Une dérivée peut zervir à connaître les zintervalles croizant et décroizant, lorzque f’(x) > 0 alors f(x) est croizant et lorzque f’(x) < 0 alors f(x) est décroizant.")

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Tu as oublié ? Je vais te réexpliquer alors écoute bien, pour reconnaître si une suite est une suite arithmétique on peut vérifier si la différence ")
                                formule_latex.make_formule(r"$ U_{n+1} - U_{n}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("est constante pour tout entier naturel n, ce qui donnera la raison par la même occasion.")
                            elif c==2:
                                insert_text("Pour reconnaître si une suite est une suite géométrique on peut vérifier si le rapport")
                                formule_latex.make_formule(r"$ \frac{V_{n+1}}{U_{n}}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 0) 
                                insert_text("est constant pour tout entier naturel n, ce qui donnera la raison par la même occasion.")


                    #pnj 5 alternatif
                    elif pnj == "pnj5":
                        if Niveau ==2:
                            if c==1:
                                insert_text("Alors, tombé à l’eau ? Je t’avais prévenu, écoute mieux cette fois.")
                            elif c==2:
                                insert_text("Quand tu as les 2 équations réduites tu t’amuses à faire une équation des 2 soit mx + p = m’x + p’.")

                        if Niveau ==3:
                            if c==1:
                                insert_text("Alors, tombé à l’eau ? Je t’avais prévenu, écoute mieux cette fois.")
                            elif c==2:
                                insert_text("Un exemple c’est le mieux alors :\n ")
                                formule_latex.make_formule(r"$\left\{ \begin{array}{lr} 2x + y & = 5 \\ 3x - y & = 4 \end{array} \right.$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1)  
                                insert_text("1. On additionne les deux équations pour éliminer y  : \n    (2x + y) + (3x - y) = 5 + 4 \n    2x + 3x + y - y = 9 \n    5x = 9 \n    x = 9/5 \n2. Puis on remplace x par 9/5 dans la première équation pour trouver y : \n    2*(9/5) + y = 5 \n    18/5 + y = 5 \n    y = 5 - 18/5 \n    y = 25/5 - 18/5 \n    y = 7/5 \nEt comme par enchantement ta solution \n    x = 9/5, y = 7/5 ")

                        elif Niveau ==7:
                            if c==1:
                                insert_text("Alors t’as le mal de mer pour oublier si vite ? Bon je vais te réexpliquer écoute bien cette fois, pour calculer la somme des n premiers termes d’une suite arithmétique il faut utiliser la formule : ")
                                formule_latex.make_formule(r"$S_{n} = \text{nombre de terme} \times \frac{\text{premier terme + dernier terme}}{2}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 
                            elif c==2:
                                insert_text("Pour la somme des n premiers termes d’une suite géométrique il faut la formule : ")
                                formule_latex.make_formule(r"$S_{n} = \text{premier terme} \times \frac{1 - \text{raison}^{\text{nombre de termes}}}{1 - \text{raison}}$",Label_texte_parole_discussion_pnj_scrolltext, 14, 1) 

                        
                    if c == 3 : 
                        #on clear si jamais la personne s'en va
                        canvas_tete_pnj_grand.delete("all")
                        Label_text_nom_pnj_strvar.set("")
                        Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                        Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                        Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
                        #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
                        if Label_btn_suivant_discussion_pnj is not None:
                            if Label_btn_suivant_discussion_pnj.winfo_exists():
                                Label_btn_suivant_discussion_pnj.destroy()
                        c = 0
                Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED) 




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
                #fonction pour afficher le nom du pnj
                def nom_pnj_actuel(pnj, Niveau):
                    if pnj == "pnj1":
                        if Niveau ==0:
                            nom_du_pnj = "Leilégalité :"
                        elif Niveau ==1:
                            nom_du_pnj = "Paπ :"          
                        elif Niveau ==2:
                            nom_du_pnj = "Cana :"
                        elif Niveau ==3:
                            nom_du_pnj = "Mathémami :"
                        elif Niveau ==5:
                            nom_du_pnj = "Leilégalité :"
                        elif Niveau ==6:
                            nom_du_pnj = "Paπ :"
                        elif Niveau ==7:
                            nom_du_pnj = "Cana :"

                    elif pnj == "pnj2":
                        if Niveau ==0:
                            nom_du_pnj = "Iggy :"
                        elif Niveau ==1:
                            nom_du_pnj = "Cécylindre :"          
                        elif Niveau ==2:
                            nom_du_pnj = "Homme strict :"
                        elif Niveau ==3:
                            nom_du_pnj = "Homme strict :"
                        elif Niveau ==5:
                            nom_du_pnj = "Iggy :"
                        elif Niveau ==6:
                            nom_du_pnj = "Marchand de glace :"
                        elif Niveau ==7:
                            nom_du_pnj = "Homme strict :"
                            
                       
                    elif pnj == "pnj3":
                        if Niveau ==0:
                            nom_du_pnj = "Mathémami :"
                        elif Niveau ==1:
                            nom_du_pnj = "Marchand de glace :"          
                        elif Niveau ==2:
                            nom_du_pnj = "Marchand de tapis :"
                        elif Niveau ==3:
                            nom_du_pnj = "Marchand de tapis :"
                        elif Niveau ==5:
                            nom_du_pnj = "Mathémami :"
                        elif Niveau ==6:
                            nom_du_pnj = "Cécilyndre :"
                        elif Niveau ==7:
                            nom_du_pnj = "Marchand de tapis :"
                           
                    elif pnj == "pnj4":

                        if Niveau ==1:
                            nom_du_pnj = "Titouan :"
                        elif Niveau ==2:
                            nom_du_pnj = "Delta :"  
                        elif Niveau ==3:
                            nom_du_pnj = "Delta :"                        
                        elif Niveau ==6:
                             nom_du_pnj = "Titouan :"                   
                        elif Niveau ==7:
                             nom_du_pnj = "Delta :"                       
                       
                    elif pnj == "pnj5":
                        if Niveau ==2:
                            nom_du_pnj = "Capitaine d’un navire :"
                        elif Niveau ==3:
                            nom_du_pnj = "Capitaine d’un navire :"
                        elif Niveau ==7:
                            nom_du_pnj = "Capitaine d’un navire : "

                    return nom_du_pnj
                    
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
                    canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj5_grand)


                global Label_btn_suivant_discussion_pnj

                if Label_btn_suivant_discussion_pnj is not None:
                    if Label_btn_suivant_discussion_pnj.winfo_exists():
                        Label_btn_suivant_discussion_pnj.destroy()
                #On crée le bouton pour faire discuter le pnj avec l'utilisateur et on set le texte de bienvenue
                Label_text_nom_pnj_strvar.set(nom_pnj_actuel(pnj_, Niveau))
                Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                Label_texte_parole_discussion_pnj_scrolltext.delete('1.0', END)
                Label_texte_parole_discussion_pnj_scrolltext.insert(END, "Salut ! Clique sur suivant !")
                Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)

                Label_btn_suivant_discussion_pnj = Button(Label_Frame_Discussion_pnj, text="Suivant", command=lambda: affiche_prog(pnj_, pnj_infos_, Niveau))
                Label_btn_suivant_discussion_pnj.pack(side=BOTTOM, anchor="e", pady=5, padx=2)
            
            # check s'il y a la porte à proximité
            elif (L[ordonne-1][abscisse] == "\U0001F6AA" or L[ordonne+1][abscisse]== "\U0001F6AA" or L[ordonne][abscisse-1]== "\U0001F6AA" or L[ordonne][abscisse+1]== "\U0001F6AA"):
                global assemble_cle
                if assemble_cle == True:
                    porte_enigme()
                    load_cours(Niveau, 1)
                else:
                    Label_text_possibilite_strvar.set("Vous devez d'abord assemblé votre Clé pour pouvoir ouvrir la porte !")
                    canvas_infos_possibilite_discussion.delete('all')
                    canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=idee)

            #check s'il y le boss à proximité :
            elif (L[ordonne-1][abscisse] == "boss" or L[ordonne+1][abscisse]== "boss" or L[ordonne][abscisse-1]== "boss" or L[ordonne][abscisse+1]== "boss"):
                boss_enigme()

            else:
                canvas_infos_possibilite_discussion.delete('all')
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=idee)
                Label_text_possibilite_strvar.set("Il n'y a personne autour de vous avec qui discuter !")
                #on clear si jamais la personne s'en va
                canvas_tete_pnj_grand.delete("all")
                Label_text_nom_pnj_strvar.set("")
                Label_texte_parole_discussion_pnj_scrolltext.config(state=NORMAL)
                Label_texte_parole_discussion_pnj_scrolltext.delete('1.0',END)
                Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)
                #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
                if Label_btn_suivant_discussion_pnj is not None:
                    if Label_btn_suivant_discussion_pnj.winfo_exists():
                        Label_btn_suivant_discussion_pnj.destroy()
                c = 0



        #Fonction de la porte avec verif nb fenetre et gestion de l'exo
        def porte_enigme():
            
            global second_window_probleme


            if not second_window_probleme or not second_window_probleme.winfo_exists():  # Vérifie si la deuxième fenêtre existe
                def affiche_consigne():
                    global Niveau
                    #fonction pour afficher le text progressivement
                    def insert_consignes_exo(text_complet_consignes):
                        Label_btn_suivant_second_window ['state'] = DISABLED
                        for i in range(len(text_complet_consignes)):
                            Label_scrollbox_consignes_exo.config(state=NORMAL)
                            Label_scrollbox_consignes_exo.delete('1.0', END)
                            text_partiel_second_window = text_complet_consignes[:i+1]
                            Label_scrollbox_consignes_exo.insert(END, f"{text_partiel_second_window}")
                            Label_scrollbox_consignes_exo.update()
                            Label_scrollbox_consignes_exo.config(state=DISABLED)

                            time.sleep(0.01)
                        Label_btn_suivant_second_window ['state'] = NORMAL


                    global erreur
                    global c_sw
                    c_sw  += 1
                    
                    #text global + text en fonction de l'exo
                    if c_sw==1:
                        insert_consignes_exo("Pour pouvoir tourner la clé et ainsi dévérouiller la porte, vous devez résoudre cette exercice ! ")
                    elif c_sw==2:
                        insert_consignes_exo("Toutes les parties du cours que vous avez collectées vous serviront pour répondre ! Vous pouvez les consulter ")
                    elif c_sw==3:
                        if Niveau ==0:
                            insert_consignes_exo("Vous devez résoudre cette équation du premier degré en trouvant la valeur de x. Après avoir résolu cette equation; selectionnez la bonne case et faites valider \n \n")
                            formule_latex.make_formule(Exo_correction[0],Label_scrollbox_consignes_exo, 15, 0)
                        elif Niveau ==1:
                            insert_consignes_exo(f"Vous devez résoudre ce calcul de volume, il vous faudra trouver le volume total; selectionnez la bonne case et faites valider. Attention; toutes les valeurs données sont en m et le résultat attendu en m cube. Données : a = {Exo_correction[5][0]}; b ={Exo_correction[5][1]}; c ={Exo_correction[5][2]}; d ={Exo_correction[5][3]}; e ={Exo_correction[5][4]}; f ={Exo_correction[5][5]}; r ={Exo_correction[5][6]}")
                        elif Niveau ==2:
                            insert_consignes_exo(f"Vous devez résoudre ce problème : A l'aide des coordonnées, déterminez l'équation réduite de (AB) et (CD). Voici les coordonnées des points : A = {Exo_correction[5][0]}; B ={Exo_correction[5][1]}; C ={Exo_correction[5][2]}; D ={Exo_correction[5][3]}")
                        elif Niveau==3:
                            insert_consignes_exo("Vous devez résoudre ce système à 2 inconnues en trouvant la valeur de x et y.")
                            formule_latex.make_formule(Exo_correction[0],Label_scrollbox_consignes_exo, 15, 0)
                        elif Niveau==5:
                            insert_consignes_exo("Vous devez trouver la ou les solutions possibles de f(x) = 0 si il y en a.")
                            formule_latex.make_formule(Exo_correction[0],Label_scrollbox_consignes_exo, 15, 0)
                        elif Niveau==6:
                            insert_consignes_exo(f"Vous devez dériver la fonction f(x) suivante. Puis trouver l'équation de tangente pour x = {Exo_correction[5]}")
                            formule_latex.make_formule(Exo_correction[0],Label_scrollbox_consignes_exo, 15, 0)
                        elif Niveau==7:
                            insert_consignes_exo(f"Vous devez trouver la raison de cette suite et calculer la somme des {Exo_correction[5][3]} premiers termes. Voici les valeurs Uo = {Exo_correction[5][0]}; U1 = {Exo_correction[5][1]}; U2 = {Exo_correction[5][2]} de la suite.")
        
                    elif c_sw==4:
                        Label_btn_suivant_second_window ['state'] = DISABLED
                        # on affiche les btns de réponses
                        Label_btn_result_possible_1 = Button(Label_Frame_Reponse_Verif_2, text=value_btn_1, command=lambda:verif_reponse_sw(value_btn_1,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                        Label_btn_result_possible_1.pack(side = LEFT, padx = 25, pady = 5)

                        Label_btn_result_possible_2 = Button(Label_Frame_Reponse_Verif_2, text=value_btn_2, command=lambda:verif_reponse_sw(value_btn_2,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                        Label_btn_result_possible_2.pack(side = LEFT, padx = 25, pady = 5)

                        Label_btn_result_possible_3 = Button(Label_Frame_Reponse_Verif_2, text=value_btn_3, command=lambda:verif_reponse_sw(value_btn_3,Exo_correction[1],Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3))
                        Label_btn_result_possible_3.pack(side = LEFT, padx= 25, pady = 5)

                    elif c_sw==5:
                        if erreur == 0:
                            insert_consignes_exo("Bravo ! Vous avez trouvé la bonne solution !")
                        else:
                            insert_consignes_exo("Vous n'avez pas trouvé la bonne solution, cliquez sur suivant pour recommencer !")

                    elif c_sw==6:
                        if erreur == 0:
                            if Niveau ==3 or Niveau==7:
                                insert_consignes_exo("Cliquez sur suivant pour passez au niveau du boss !")
                            else:
                                insert_consignes_exo("Cliquez sur suivant pour passez au niveau suppérieur !")

                        else:
                            second_window_probleme.destroy()

                    else:
                        
                        second_window_probleme.destroy()
                        global type_partie
                        Niveau +=1
                        Gestion_Jouer(Jeu, Niveau, type_partie)



                #fonction de verif qui donne la possibilité de passer au niveau suivant ou non 
                def verif_reponse_sw(reponse, correction,Label_btn_result_possible_1,Label_btn_result_possible_2,Label_btn_result_possible_3):
                    Label_btn_result_possible_1.destroy()
                    Label_btn_result_possible_2.destroy()
                    Label_btn_result_possible_3.destroy()
                    global erreur
                    erreur = 0
                    if reponse == correction:
                        affiche_consigne()
                    else:
                        erreur = 1
                        affiche_consigne()


                
                global c_sw
                c_sw = 0

                second_window_probleme = Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
                second_window_probleme.title("Maths-Quest | Porte Exercice       © PLADEAU Quentin LUBAN Théo")

                ####frame global de la fenetre
                Label_Frame_global_second_window = Frame(second_window_probleme, bg = "#BBC4E3")
                Label_Frame_global_second_window.pack(expand=True, fill="both")

                # nom de l'exo qui s'affichera sur la page de l'exo
                if Niveau ==0:
                    exo_nom = "Equation du premier degré"
                elif Niveau==1:
                    exo_nom = "Volumes"
                elif Niveau ==2:
                    exo_nom ="Fonctions affines & Equation de droite"
                elif Niveau==3:
                    exo_nom ="Système à 2 inconnues"
                elif Niveau ==5:
                    exo_nom ="Equation du second degré (polynôme)"
                elif Niveau==6:
                    exo_nom ="Dérivation"
                elif Niveau ==7:
                    exo_nom ="Suites"

                Label_text_infos_type_exo =Label(Label_Frame_global_second_window, text=exo_nom, font=('Arial',12), bg="#BBC4E3")
                Label_text_infos_type_exo.pack(anchor="nw",side= TOP, pady=5, padx=5)


                ###frame qui contiendra toutes les consignes / explications et le btn suivant
                Label_Frame_Canvas_consignes_explication_btn = Frame(Label_Frame_global_second_window, bg="#99A6D0")
                Label_Frame_Canvas_consignes_explication_btn.pack(side=TOP, expand=True, fill=BOTH, pady= 5, padx=5)

                #on load les elements de consignes
                Label_scrollbox_consignes_exo = scrolledtext.ScrolledText(Label_Frame_Canvas_consignes_explication_btn, wrap='word', font=("Arial", 10), height=4)
                Label_scrollbox_consignes_exo.pack(side=LEFT, fill=BOTH, expand=True, pady= 5, padx = 5)
                Label_scrollbox_consignes_exo.insert(END, 'Clique sur suivant !')
                Label_scrollbox_consignes_exo.images = [] # pour stocker les images latex 

                Label_btn_suivant_second_window = Button(Label_Frame_Canvas_consignes_explication_btn, text="Suivant !", command=affiche_consigne)
                Label_btn_suivant_second_window.pack(side=TOP, anchor="e", pady=5, padx=5)

                Label_Frame_Canvas_formule_exo = None

                if Niveau ==1 or Niveau ==2:
                    ### frame qui contient le canvas qui affichera une image si besoin
                    Label_Frame_Canvas_formule_exo = Frame(Label_Frame_global_second_window, bg="#99A6D0")
                    Label_Frame_Canvas_formule_exo.pack(side=TOP, fill='y', pady= 5, padx=5)

                    if Niveau ==1:
                        Label_canvas_img_sw = Canvas(Label_Frame_Canvas_formule_exo, width = 713, height = 487, bg = "#ffffff")
                        Label_canvas_img_sw.pack(padx=5,pady=5)
                        Label_canvas_img_sw.create_image(0,0,anchor=NW, image=Volume_nv1)


                # on recupère la formule et la correction
                Exo_correction = py_maths_exo.choix_exo_niveau(Niveau,Label_Frame_Canvas_formule_exo)



                ## Frame global de la frame qui contient les trois valeurs de réponse avec les cases à cocher et le bouton valider
                Label_Frame_Reponse_Verif = Frame(Label_Frame_global_second_window, bg= None)
                Label_Frame_Reponse_Verif.pack(side=TOP, fill='x', pady= 5, padx=5, )
                #Frame avec les 3 btn 
                Label_Frame_Reponse_Verif_2 = Frame(Label_Frame_Reponse_Verif, bg = None)
                Label_Frame_Reponse_Verif_2.pack(anchor=CENTER)
                # on définit les trois valeurs qui vont s'afficher dans les boutons
                value_btn_1 = Exo_correction[2]
                value_btn_2 = Exo_correction[3]
                value_btn_3 = Exo_correction[4]


                # Lit la fermeture de la fenêtre à la réinitialisation de second_window_probleme
                second_window_probleme.protocol("WM_DELETE_WINDOW", lambda: reset_second_window())
        
        #fonction pour fermer cette fenetre
        def reset_second_window():
            global second_window_probleme
            if second_window_probleme:
                second_window_probleme.destroy()  # Détruit la fenêtre
            second_window_probleme= None


        #Fonction qui gère les deux salles de boss
        def boss_enigme():
            global boss_window
            global Niveau

            if not boss_window or not boss_window.winfo_exists():  # Vérifie si la deuxième fenêtre existe

                #on reset le nombre d'indice donné si jamais il y a eu plusieurs tentatives
                global indices_give_1
                global indices_give_2
                if Niveau ==4:
                    indices_give_1 = 0
                elif Niveau ==8:
                    indices_give_2 = 0

                def affiche_consigne_boss():

                    #fonction de verif des réponses choisies par l'utilisateur
                    def verif_reponse_boss(correction1, correction2 ,Label_btn_result_possible_1_boss,Label_btn_result_possible_2_boss,Label_btn_result_possible_3_boss,Label_btn_result_possible_1_2_boss,Label_btn_result_possible_2_2_boss,Label_btn_result_possible_3_2_boss,Label_text_infos_selection_verif_boss , Label_btn_valider_boss_exo):

                        global erreur_boss
                        erreur_boss = 0
                        if get_value_boss_1.get() != "" and get_value_boss_2.get() !="":

                            Label_btn_result_possible_1_boss.destroy()
                            Label_btn_result_possible_2_boss.destroy()
                            Label_btn_result_possible_3_boss.destroy()
                            Label_btn_result_possible_1_2_boss.destroy()
                            Label_btn_result_possible_2_2_boss.destroy()
                            Label_btn_result_possible_3_2_boss.destroy()

                            if get_value_boss_1.get() == correction1 and get_value_boss_2.get() == correction2:
                                Label_text_infos_selection_verif_boss.destroy()
                                Label_btn_valider_boss_exo.destroy()
                                affiche_consigne_boss()
                            else:
                                erreur_boss = 1
                                Label_text_infos_selection_verif_boss.destroy()
                                Label_btn_valider_boss_exo.destroy()
                                affiche_consigne_boss()
                        else:
                            Label_str_var_btn_verif_boss_infos.set("Vous devez sélectionner 1 réponse par colonne !") # infos si ne seule réponse est sélectionné


                    global erreur_boss
                    global c_boss
                    global type_partie
                    global Niveau

                    c_boss  += 1

                    text_complet_consignes_boss = ""

                    #text des consignes pour le boss
                    if c_boss==1:
                            text_complet_consignes_boss = "Pour pouvoir tourner la clé et ainsi dévérouiller la porte, vous devez résoudre cette exercice ! "
                    elif c_boss==2:
                            text_complet_consignes_boss = "Toutes les parties du cours que vous avez collectées vous serviront pour répondre ! Vous pouvez les consulter "
                    elif c_boss==3:
                        if Niveau==4:
                            text_complet_consignes_boss = f"Un voilier se trouve dans le port de Sète et avant de partir un client veut connaître le volume d’huile que le navire peut transporter sachant qu’il possède une cargaison de 85 tonneaux de longueur :{Exo_correction_boss[8][4]} et de largeur :{Exo_correction_boss[8][5]} (nous affirmons que les tonneaux utilisés ont des côtés totalement droit et non arrondis. Après cela le bateau prend le large et reçoit des informations sur un autre bateau naviguant à la même vitesse, déterminer si les 2 bateaux se croiseront. De plus le bateau b1 est actuellement au point A et navigue selon la direction (AB). De même le bateau b2 est actuellement au point C et navigue selon la direction (CD). Coordonnées : A ={Exo_correction_boss[8][0]} ; B = {Exo_correction_boss[8][1]} ; C = {Exo_correction_boss[8][2]} ; D = {Exo_correction_boss[8][3]}"
                        elif Niveau ==8:
                            text_complet_consignes_boss = f"Un fabriquant envisage la production de briques de lait en carton. Au départ, il dispose d’une feuille carrée en carton dans laquelle on a retiré deux bandes de même largeur. Le côté de la feuille carrée mesure {Exo_correction_boss[8][0]} cm et on désigne par x la largeur des bandes découpées en centimètres. Trouver le volume en litre maximal dans cette brique à lait en fonction de x\n\nTrouver ensuite le prix de la brique au bout de {Exo_correction_boss[8][2]} ans sachant qu'il subit une inflation de {Exo_correction_boss[8][1]} % et que le prix d'origine était 1.20€ "
 
                    elif c_boss==4:
                        Label_btn_suivant_boss_window ['state'] = DISABLED
                        # on affiche les btns de réponses
                        get_value_boss_1 = StringVar()
                        Label_btn_result_possible_1_boss = Radiobutton(Label_Frame_Reponse_Verif_boss_2, text=value_btn_1_boss, value=value_btn_1_boss, variable=get_value_boss_1)
                        Label_btn_result_possible_1_boss.pack(side =TOP, padx = 5, pady = 5)

                        Label_btn_result_possible_2_boss = Radiobutton(Label_Frame_Reponse_Verif_boss_2, text=value_btn_2_boss, value=value_btn_2_boss, variable=get_value_boss_1)
                        Label_btn_result_possible_2_boss.pack(side =TOP, padx = 5, pady = 5)

                        Label_btn_result_possible_3_boss = Radiobutton(Label_Frame_Reponse_Verif_boss_2, text=value_btn_3_boss, value=value_btn_3_boss, variable=get_value_boss_1)
                        Label_btn_result_possible_3_boss.pack(side =TOP, padx= 5, pady = 5)


                        get_value_boss_2 = StringVar()
                        Label_btn_result_possible_1_2_boss = Radiobutton(Label_Frame_Reponse_Verif_boss_2_2, text=value_btn_1_2_boss, value = value_btn_1_2_boss, variable=get_value_boss_2)
                        Label_btn_result_possible_1_2_boss.pack(side =TOP, padx = 5, pady = 5)

                        Label_btn_result_possible_2_2_boss = Radiobutton(Label_Frame_Reponse_Verif_boss_2_2, text=value_btn_2_2_boss, value = value_btn_2_2_boss, variable=get_value_boss_2)
                        Label_btn_result_possible_2_2_boss.pack(side =TOP, padx = 5, pady = 5)

                        Label_btn_result_possible_3_2_boss = Radiobutton(Label_Frame_Reponse_Verif_boss_2_2, text=value_btn_3_2_boss, value = value_btn_3_2_boss, variable=get_value_boss_2)
                        Label_btn_result_possible_3_2_boss.pack(side =TOP, padx= 5, pady = 5)


                        #label du text infos
                        Label_str_var_btn_verif_boss_infos = StringVar()
                        Label_text_infos_selection_verif_boss = Label(Label_Frame_Reponse_Verif_boss, textvariable=Label_str_var_btn_verif_boss_infos, fg = "#9A0004", wraplength=150)
                        Label_text_infos_selection_verif_boss.pack(side = BOTTOM, pady = 2)

                        #bouton de validation
                        Label_btn_valider_boss_exo = Button(Label_Frame_Reponse_Verif_boss, text="Valider", command=lambda:verif_reponse_boss(Exo_correction_boss[0],Exo_correction_boss[1],Label_btn_result_possible_1_boss,Label_btn_result_possible_2_boss,Label_btn_result_possible_3_boss,Label_btn_result_possible_1_2_boss,Label_btn_result_possible_2_2_boss,Label_btn_result_possible_3_2_boss,Label_text_infos_selection_verif_boss , Label_btn_valider_boss_exo))
                        Label_btn_valider_boss_exo.pack(side=BOTTOM, pady=5)


                    elif c_boss==5:
                        if erreur_boss == 0:
                            text_complet_consignes_boss = "Bravo ! Vous avez trouvé la bonne solution !"
                        else:
                            text_complet_consignes_boss = "Vous n'avez pas trouvé la bonne solution, cliquez sur suivant pour recommencer !"

                    elif c_boss==6:
                        if erreur_boss == 0:
                            if Niveau ==4 and type_partie=='all':
                                text_complet_consignes_boss ="Cliquez sur suivant pour passez au niveau suppérieur !"
                            else:
                                text_complet_consignes_boss ="Cliquez sur suivant pour obtenir vos résultats et terminer le jeu !"

                        else:
                            boss_window.destroy()

                    else:
                        boss_window.destroy()
                        Niveau +=1
                        Gestion_Jouer(Jeu, Niveau, type_partie)

                    
                    if  4 > c_boss  or 5 <= c_boss <7:

                        Label_btn_suivant_boss_window ['state'] = DISABLED

                        Label_scrollbox_consignes_boss.config(state = NORMAL)
                        Label_scrollbox_consignes_boss.delete('1.0', END)
                        Label_scrollbox_consignes_boss.config(state = DISABLED)

                        for i in range(len(text_complet_consignes_boss)):
                            Label_scrollbox_consignes_boss.config(state = NORMAL)
                            text_partiel_boss = text_complet_consignes_boss[i]
                            Label_scrollbox_consignes_boss.insert(END, f"{text_partiel_boss}")
                            Label_scrollbox_consignes_boss.update()
                            Label_scrollbox_consignes_boss.config(state = DISABLED)
                            time.sleep(0.01)
                        Label_btn_suivant_boss_window ['state'] = NORMAL
    

   
                
                #fonction pour donner les indices et les compter
                def Give_indices_boss(Niveau):
                    
                    def ajouter_element_indices(Texte_): # ajout des indices dans la box des indices sur demande
                        global listbox_indices
                        element_ = Texte_.strip()
                        listbox_indices.config(state=NORMAL)
                        if element_:
                            listbox_indices.insert(END, element_ + "\n")
                        listbox_indices.insert(END, "\n")
                        listbox_indices.config(state=DISABLED)


                    global indices_give_1 # on recup les valeurs
                    global indices_give_2


                    #box des indices en stock
                    L_indices_1 = [
                        "Indice 1 : Je te rappelle qu’un litre vaut 1dm3",
                        "Indice 2 : Il faut commencer par déterminer les équations des droites (AB) et (CD) puis déterminer les coordonnées du point d’intersection entre ces deux droites.",
                        "Indice 3 : Si les bateaux voguent à la même vitesse, ils parcourent donc la même distance en un temps donné. \nPour trouver la longueur d’un segment il faut utiliser la formule ",
                        "Vous avez utilisé tout les indices !"
                        ]
                    L_indices_2 = [
                        "Indices 1 : Essayez de trouver la fonction du volume de la brique. \nRappel : Le volume se calcule avec la formule aire de la base x hauteur",
                        "Indices 2 : ",
                        "Indices 3 : Pensez à dériver votre fonction !",
                        "Vous avez utilisé tout les indices !"
                        ]

                    #en fonction du niveau, on donne les indices
                    if Niveau ==4:
                        if indices_give_1 < 3:
                            ajouter_element_indices(L_indices_1[indices_give_1])
                            if indices_give_1==2:
                                formule_latex.make_formule(r"$ \sqrt{(xB-xA)^2 + (yB-yA)^2}$",listbox_indices, 14, 0)
                            indices_give_1 +=1

                        elif indices_give_1 == 3:
                            ajouter_element_indices(L_indices_1[indices_give_1])
                            Label_btn_get_indices.destroy()



                    elif Niveau == 8:
                        if indices_give_2 < 3:
                            ajouter_element_indices(L_indices_2[indices_give_2])
                            if indices_give_2==1:
                                listbox_indices.config(state=NORMAL)
                                listbox_indices.image_create(END, image=indice2_boss2)
                                listbox_indices.config(state=DISABLED)
                            indices_give_2 +=1
                        elif indices_give_2 ==3:
                            ajouter_element_indices(L_indices_2[indices_give_2])
                            Label_btn_get_indices.destroy()




                global c_boss
                c_boss = 0


                boss_window = Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
                boss_window.title("Maths-Quest | Boss Exercices       © PLADEAU Quentin LUBAN Théo")


                #####frame global de la fenetre
                Label_Frame_global_boss = Frame(boss_window, bg = "#BBC4E3")
                Label_Frame_global_boss.pack(expand=True, fill="both")

                #### frame globale des elements de droite / des indices
                Label_frame_indices_boss = Frame(Label_Frame_global_boss, bg ="#99A6D0", width= 100)
                Label_frame_indices_boss.pack(expand=True, fill = 'both', side=RIGHT)

                ###frame box de la listbox des indices
                Label_Frame_box_listbox_indices_boss = Frame(Label_frame_indices_boss, bg = None)
                Label_Frame_box_listbox_indices_boss.pack(side =TOP,expand=True, fill='y', pady= 5, padx = 5)
                #on crée la box pour les indices s'il sont demandés par l'utilisateur
                global listbox_indices
                listbox_indices = scrolledtext.ScrolledText(Label_Frame_box_listbox_indices_boss, wrap='word', font=("Arial", 10), height=4, width=35)
                listbox_indices.pack(side=LEFT, fill=BOTH, expand=True)

                #on ajoute le titre de la box des indices
                listbox_indices.insert(END, "--Indices--" + "\n")
                listbox_indices.insert(END, "\n")
                listbox_indices.config(state=DISABLED)
                listbox_indices.images = []


                Label_btn_get_indices = Button(Label_frame_indices_boss,text="Obtenir un indice", command=lambda:Give_indices_boss(Niveau))
                Label_btn_get_indices.pack(pady=10, side=TOP)

                ###frame global des éléments de gauche
                Label_frame_global_element_gauche_boss = Frame(Label_Frame_global_boss, bg = "#99A6D0")
                Label_frame_global_element_gauche_boss.pack(expand=True, fill=BOTH, side=LEFT)

                ###frame qui contiendra toutes les consignes / explications et le btn suivant
                Label_Frame_Canvas_consignes_explication_btn_boss = Frame(Label_frame_global_element_gauche_boss, bg=None)
                Label_Frame_Canvas_consignes_explication_btn_boss.pack(side=TOP,expand=True, fill = BOTH, pady= 5, padx=5)

                #on load les elements de consignes
                Label_scrollbox_consignes_boss = scrolledtext.ScrolledText(Label_Frame_Canvas_consignes_explication_btn_boss, wrap='word', font=("Arial", 10), height=4)
                Label_scrollbox_consignes_boss.pack(side=LEFT, fill=BOTH, expand=True, pady= 5, padx = 5)
                Label_scrollbox_consignes_boss.insert(END, 'Clique sur suivant !')
                Label_scrollbox_consignes_boss.images = []

                Label_scrollbox_consignes_boss.config(state = DISABLED)

                Label_btn_suivant_boss_window = Button(Label_Frame_Canvas_consignes_explication_btn_boss, text="Suivant !", command=affiche_consigne_boss)
                Label_btn_suivant_boss_window.pack(side=TOP, anchor="e", pady=5, padx=5)

                ### frame qui contient le canvas qui affichera la formule
                Label_Frame_Canvas_formule_boss = Frame(Label_frame_global_element_gauche_boss, bg="#99A6D0")
                Label_Frame_Canvas_formule_boss.pack(side=TOP, fill='y', pady= 5, padx=5)

                #canvas avec l'image
                Label_canvas_boss_image = Canvas(Label_Frame_Canvas_formule_boss, )
                Label_canvas_boss_image.pack()

                # on recupère la correction et les valeurs nécéssaires à la consigne
                Exo_correction_boss = py_maths_boss.choix_exo_niveau_boss(Niveau)
                if Niveau ==4:
                    #on affiche l'image du problème
                    Label_canvas_boss_image.configure(width = 400, height = 283)
                    Label_canvas_boss_image.create_image(0,0,anchor=NW, image = exo_boss_portdesete)


                elif Niveau==8:
                    #on affiche l'image du problème
                    Label_canvas_boss_image.configure(width = 400, height = 171)
                    Label_canvas_boss_image.create_image(0,0,anchor=NW, image = exo_boss_briquedelait)   



                # on définit les trois valeurs qui vont s'afficher dans les boutons
                value_btn_1_boss = Exo_correction_boss[2]
                value_btn_2_boss = Exo_correction_boss[3]
                value_btn_3_boss = Exo_correction_boss[4]

                value_btn_1_2_boss = Exo_correction_boss[5]
                value_btn_2_2_boss = Exo_correction_boss[6]
                value_btn_3_2_boss = Exo_correction_boss[7]

                ## Frame global qui contient la frame ave les trois valeurs de réponse avec les cases à cocher et le bouton valider
                Label_Frame_Reponse_Verif_boss = Frame(Label_frame_global_element_gauche_boss, bg= None)
                Label_Frame_Reponse_Verif_boss.pack(side=TOP, fill='x', pady= 5, padx=5, anchor=CENTER)

                ##sous frame de cette frame principal qui contient les frames btn
                Label_Frame_box_2_frame_btn = Frame(Label_Frame_Reponse_Verif_boss, bg = None)
                Label_Frame_box_2_frame_btn.pack(side=TOP, fill = BOTH, expand=True)
                
                #Frame avec les btn
                Label_Frame_Reponse_Verif_boss_2 = Frame(Label_Frame_box_2_frame_btn, bg=None)
                Label_Frame_Reponse_Verif_boss_2.pack(anchor = CENTER, side=LEFT, padx = 5)

                #Frame avec les btn
                Label_Frame_Reponse_Verif_boss_2_2 = Frame(Label_Frame_box_2_frame_btn, bg = None)
                Label_Frame_Reponse_Verif_boss_2_2.pack(anchor=CENTER, side=RIGHT, padx = 5)

                # Lit la fermeture de la fenêtre à la réinitialisation de boss_window
                boss_window.protocol("WM_DELETE_WINDOW", lambda: reset_boss_window())

        def reset_boss_window():
            global boss_window
            if boss_window:
                boss_window.destroy()  # Détruit la fenêtre
            boss_window= None



        #fenetre avec les règles
        def regle_infos_jeu(event):
            global Regle 

            if not Regle  or not Regle.winfo_exists():  # Vérifie si la deuxième fenêtre existe

                Regle = Toplevel()
                Regle.config(bg = "#BBC4E3")
                Regle.title("Maths-Quest | Règles & Aide       © PLADEAU Quentin LUBAN Théo")

                Label_titre_regle = Label(Regle, text="Maths-Quest : Règles & Aide", font=("Arial", 12), bg = "#BBC4E3").pack(pady=5)

                Label_Frame_Touche = Frame(Regle, bg = "#BBC4E3")
                Label_Frame_Touche.pack(expand=True, fill="both")

                Label_frame_1 = Frame(Label_Frame_Touche, bg = "#99A6D0", width=250)
                Label_frame_1.pack(fill='y', side=LEFT, pady=5, padx=5)

                scroll_text_touche_help = scrolledtext.ScrolledText(Label_frame_1, wrap=WORD,width = 35, font=("Arial", 10))
                scroll_text_touche_help.pack(expand=True, fill='both', pady = 5, padx = 5)

                text_touche_help = """
    Les déplacements :
        Haut --> Touche '↑'
        Bas --> Touche '↓'
        Gauche --> Touche '←'
        Droite --> Touche '→'

    Parler :
        Parler aux pnj --> Touche 'espace'
        Affronter le boss --> Touche 'espace'

    Autre :
        Fabriquer --> Touche 'c'
        Obtenir de l'aide --> 'echap'
"""

                scroll_text_touche_help.insert(END, text_touche_help)
                scroll_text_touche_help.config(state=DISABLED)


                Label_frame_2= Frame(Label_Frame_Touche, bg = "#99A6D0", width=250)
                Label_frame_2.pack(fill='y', side ='right', pady=5, padx=5)

                scroll_text_regles_help = scrolledtext.ScrolledText(Label_frame_2, wrap=WORD,width = 60, font=("Arial", 10))
                scroll_text_regles_help.pack(expand=True, fill='both', pady = 5, padx = 5)

                text_regles_help = """
    But du jeu
Vous devez vous déplacer sur la carte pour rencontrer les différents personnages. Chaque personnage est unique, il est donc nécessaire de discuter avec chacun d'entre eux pour obtenir divers objets. Ces objets, une fois assemblés, vous permettront de déverrouiller la porte présente sur la carte.

Lorsque vous atteindrez la porte, un problème en rapport avec le cours que vous avez suivi à ce niveau vous sera posé. Vous devrez le résoudre pour avancer.

Une fois que vous aurez passé tous les niveaux, vous atteindrez le niveau "boss". Dans ce niveau, vous devrez résoudre un exercice récapitulatif couvrant les cours que vous avez suivis précédemment. Vous aurez à votre disposition le cours et trois indices.
Attention, chaque indice utilisé affectera votre résultat final !

Exemple de PNJ :

"""

                scroll_text_regles_help.insert(END, text_regles_help)

                image__0 = PhotoImage(file="Images/pnj/Iggy/Iggy_petit.png") 
                image__1 = PhotoImage(file="Images/pnj/MarchandDeGlace/Marchand_de_glace_petit.png")
                image__2 = PhotoImage(file="Images/pnj/CapitaineDunNavire/Capitaine_dun_navire_petit.png")
                
                scroll_text_regles_help.image_create(END, image=image__0)
                scroll_text_regles_help.image_create(END, image=image__1)
                scroll_text_regles_help.image_create(END, image=image__2)

                text_regles_help2 = """


Pour plus de renseignements : https://github.com/Gandalf0207/Maths-Quest
"""

                scroll_text_regles_help.insert(END, text_regles_help2)
                scroll_text_regles_help.config(state=DISABLED)

                close_btn = Button(Regle, command=Regle.destroy, text="Fermer").pack(side=BOTTOM, pady = 5)
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

        # affichage de l'element fabriqué

        global assemble_cle
        assemble_cle = False





        ######On place tous les elements sur la fenetre#####

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
                    canvas.create_image(24*y, 24*x, anchor=NW, image=pnj5)
                elif L[x][y] == "\U0001F6AA":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=porte)
                elif L[x][y] == "○":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=Perso)
                elif L[x][y] == "¤":
                    canvas.create_image(24*y, 24*x, anchor=NW, image=craft_table_petit)
                    
        if Niveau==4 or Niveau==8:
            canvas.create_image(24*16, 24*7, anchor=NW, image=pnj_boss_)

        canvas.pack(side="top",padx=5, pady=0)

        ###Frame gauche bas pour clé + pouvoir parler infos
        Label_Frame_pnj_Text = Frame(Label_Frame_Jeu_Inv, bg="#99A6D0")
        Label_Frame_pnj_Text.pack(side=TOP, fill=BOTH,padx=5, pady=5, expand=True)

        ##Frame affiche le texte si on peut parler à un pnj ou faire une action
        Label_Frame_Text_Info_Discussion_pnj = Frame(Label_Frame_pnj_Text, bg= None)
        Label_Frame_Text_Info_Discussion_pnj.pack(fill='y', padx=5, pady=0, side='left')

        #On load les elements pour afficher les msg de possibilités de discussion 
        canvas_infos_possibilite_discussion = Canvas(Label_Frame_Text_Info_Discussion_pnj, bg=None, height=50, width=50)
        canvas_infos_possibilite_discussion.pack(anchor="c", side=LEFT, padx=15)
        Label_text_possibilite_strvar = StringVar()
        canvas_infos_possibilite_discussion.create_image(0,0, anchor=NW, image=idee)

        #set de la base de l'objectif au changement
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
        Label_Frame_Discussion_pnj.pack(expand=True, fill=BOTH, padx=5, pady=0, side='right')

        #On load les elements qui serviront aux boites de discussion des pnjs
        canvas_tete_pnj_grand = Canvas(Label_Frame_Discussion_pnj, bg=None, height=100, width=100)
        canvas_tete_pnj_grand.pack(anchor="nw", padx=10,pady=5, side=LEFT)
        
        #petite frame pour avoir le dialogue et le nom du pnj en question
        Label_frame_nompnj_dialoguepnj = Frame(Label_Frame_Discussion_pnj, bg=None)
        Label_frame_nompnj_dialoguepnj.pack(expand=True, fill=BOTH)

        Label_text_nom_pnj_strvar = StringVar()
        Label_text_nom_pnj_widget = Label(Label_frame_nompnj_dialoguepnj, textvariable=Label_text_nom_pnj_strvar, font=('Arial 10 bold'))
        Label_text_nom_pnj_widget.pack(side=TOP, anchor='nw')
        Label_texte_parole_discussion_pnj_scrolltext = scrolledtext.ScrolledText(Label_frame_nompnj_dialoguepnj, wrap='word', width=40, height=5, font=('Arial', 10))
        Label_texte_parole_discussion_pnj_scrolltext.pack(anchor="c",side=TOP, pady= 0, padx=5, fill=BOTH, expand=True)
        Label_texte_parole_discussion_pnj_scrolltext.config(state=DISABLED)

        Label_texte_parole_discussion_pnj_scrolltext.images = []

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

        canvas_inv = Canvas(Label_Frame_Inv_Cle, height=50, bg = "#7786BA")
        canvas_inv.pack(pady=10)

        #on load l'inv de base
        load_inv(Niveau)




        #deplacements
        Jeu.focus_set()

        Jeu.bind("<KeyPress-Up>", deplacement)
        Jeu.bind("<KeyPress-Down>", deplacement)
        Jeu.bind("<KeyPress-Left>", deplacement)
        Jeu.bind("<KeyPress-Right>", deplacement)

        Jeu.bind("<space>", parler_pnj)

        Jeu.bind("<KeyPress-c>", table_craft)

        Jeu.bind("<Escape>", regle_infos_jeu)






    elif Niveau == tours:
        #fenetre des médailles / résultats
        def text_choix_medaille(type_partie_ , nb_check):

            #text de victoire
            L_Text_resultat_medaille = [
                "Bravo, vous n'avez utilisé aucun indices, vous obtenez la médaille de diamant !",
                "Très bien, vous n'avez utilisé qu'un indices, vous obtenez la médaille d'or !",
                "Bien, vous avez utilisé deux indices, vous obtenez la médaille d'argent !",
                "Merci d'avoir participé, vous avez utilisé tous les indices, vous obtenez la médaille de bronze !",
            ]

            #On affiche la ligne qui correspond aux elements
            if type_partie_=='seconde':
                text_medaille.set(L_Text_resultat_medaille[indices_give_1])
            elif type_partie_=='premiere':
                text_medaille.set(L_Text_resultat_medaille[indices_give_2])
            else:
                if nb_check==0:
                    text_medaille.set(L_Text_resultat_medaille[indices_give_1])
                elif nb_check ==1:
                    text2_medaille.set(L_Text_resultat_medaille[indices_give_2])

        #def qui fait acceder au crédits, avec un reload
        def acces_credits():
            global Niveau
            Niveau +=1
            Gestion_Jouer(Jeu,Niveau,type_partie)

        #en fonction du type de partie et du nombres d'indices utilisés, on load les elements qui correspondent
        if type_partie=='seconde':
            if indices_give_1 ==0:
                img_resultat =  PhotoImage(file="Images/Medailles/diamond.png") 
            elif indices_give_1 ==1:
                img_resultat = PhotoImage(file = "Images/Medailles/gold.png")
            elif indices_give_1 ==2:
                img_resultat = PhotoImage(file = "Images/Medailles/silver.png")
            elif indices_give_1 ==3:
                img_resultat = PhotoImage(file = "Images/Medailles/bronze.png")

        if type_partie=='premiere':
            if indices_give_2 ==0:
                img_resultat = PhotoImage(file="Images/Medailles/diamond.png") 
            elif indices_give_2 ==1:
                img_resultat = PhotoImage(file = "Images/Medailles/gold.png")
            elif indices_give_2 ==2:
                img_resultat = PhotoImage(file = "Images/Medailles/silver.png")
            elif indices_give_2 ==3:
                img_resultat = PhotoImage(file = "Images/Medailles/bronze.png")

        if type_partie =='all':
            if indices_give_1 ==0:
                img_resultat = PhotoImage(file="Images/Medailles/diamond.png") 
            elif indices_give_1 ==1:
                img_resultat = PhotoImage(file = "Images/Medailles/gold.png")
            elif indices_give_1 ==2:
                img_resultat = PhotoImage(file = "Images/Medailles/silver.png")
            elif indices_give_1 ==3:
                img_resultat = PhotoImage(file = "Images/Medailles/bronze.png") 

            if indices_give_2 ==0:
                img_resultat2 = PhotoImage(file="Images/Medailles/diamond.png") 
            elif indices_give_2 ==1:
                img_resultat2 = PhotoImage(file = "Images/Medailles/gold.png")
            elif indices_give_2 ==2:
                img_resultat2 = PhotoImage(file = "Images/Medailles/silver.png")
            elif indices_give_2 ==3:
                img_resultat2 = PhotoImage(file = "Images/Medailles/bronze.png") 


        #titre de la fenetre (haut)
        Jeu.title("Maths-Quest | Résultats       © PLADEAU Quentin LUBAN Théo")
        Label_titre_resultat_partie = Label(Jeu, text = 'Résultats',bg = '#BBC4E3')
        Label_titre_resultat_partie.pack(pady=10)

        #Frame global pour afficher les éléments des résultats
        Label_Frame_global_resultat = Frame(Jeu, bg = '#BBC4E3')
        Label_Frame_global_resultat.pack(expand=True, fill=BOTH, pady= 5, padx = 5)

        Label_btn_suivant = Button(Jeu,text="Crédits", command=acces_credits) # btn, pour passer aux crédits
        Label_btn_suivant.pack(side=BOTTOM, pady=5)

        Jeu.protocol("WM_DELETE_WINDOW", acces_credits) #quand la fenetre est fermée par la croix on passe au crédits

        if type_partie !='all':
            #Frame avec les elements des resulats (sous frame)
            Label_Frame_resultat_titre_elements = Frame(Label_Frame_global_resultat, bg = '#99A6D0')
            Label_Frame_resultat_titre_elements.pack(expand=True, fill=BOTH, pady=5, padx=5)

            Label_titre_type_partie_resultat = Label(Label_Frame_resultat_titre_elements, text = type_partie, anchor = NW, bg='#99A6D0')
            Label_titre_type_partie_resultat.pack(pady=5, padx=5, side=TOP)

            #frame avec le canvas de la médaille en fonction des indices et du text correspondant de félicitation(sous-sous frame)
            Label_Frame_resultat_canvas_text = Frame(Label_Frame_resultat_titre_elements, bg='#99A6D0')
            Label_Frame_resultat_canvas_text.pack(side=TOP, pady=5, padx=5)

            Label_canvas_medailles = Canvas(Label_Frame_resultat_canvas_text, width=75, height=75, bg = None)
            Label_canvas_medailles.pack(side=LEFT, pady=5, padx=5)

            text_medaille= StringVar()
            Label_text_resultat = Label(Label_Frame_resultat_canvas_text, textvariable=text_medaille, bg='#99A6D0')
            Label_text_resultat.pack(side=RIGHT, pady=5, padx=5)

            text_choix_medaille(type_partie, -1)
            Label_canvas_medailles.create_image(0,0,anchor=NW, image=img_resultat)

        else:
            ### ELEMENT POUR LA PARTIE SECONDE
            #Frame avec les elements des resulats (sous frame)
            
            Label_Frame_resultat_titre_elements = Frame(Label_Frame_global_resultat, bg = '#99A6D0')
            Label_Frame_resultat_titre_elements.pack(expand=True, fill=BOTH, pady=5, padx=5)

            Label_titre_type_partie_resultat = Label(Label_Frame_resultat_titre_elements, text = "seconde", anchor = NW, bg='#99A6D0')
            Label_titre_type_partie_resultat.pack(pady=5, padx=5, side=TOP)

            #frame avec le canvas de la médaille en fonction des indices est du text correspondant de félicitation(sous-sous frame)
            Label_Frame_resultat_canvas_text = Frame(Label_Frame_resultat_titre_elements, bg='#99A6D0')
            Label_Frame_resultat_canvas_text.pack(side=TOP, pady=5, padx=5)

            Label_canvas_medailles = Canvas(Label_Frame_resultat_canvas_text, width=75, height=75, bg='#99A6D0')
            Label_canvas_medailles.pack(side=LEFT, pady=5, padx=5)

            text_medaille= StringVar()
            Label_text_resultat = Label(Label_Frame_resultat_canvas_text, textvariable=text_medaille, bg='#99A6D0')
            Label_text_resultat.pack(side=RIGHT, pady=5, padx=5)

            text_choix_medaille(type_partie, 0)
            Label_canvas_medailles.create_image(0,0,anchor=NW, image=img_resultat)



            #### ELEMENT POUR LA PARTIE PREMIERE
            #Frame avec les elements des resulats (sous frame)
            Label_Frame_resultat_titre_elements2 = Frame(Label_Frame_global_resultat, bg='#99A6D0')
            Label_Frame_resultat_titre_elements2.pack(expand=True, fill=BOTH, pady=5, padx=5)

            Label_titre_type_partie_resultat2 = Label(Label_Frame_resultat_titre_elements2, text = "premiere", anchor = NW,bg='#99A6D0')
            Label_titre_type_partie_resultat2.pack(pady=5, padx=5, side=TOP)

            #frame avec le canvas de la médaille en fonction des indices et du text correspondant de félicitation(sous-sous frame)
            Label_Frame_resultat_canvas_text2 = Frame(Label_Frame_resultat_titre_elements2,bg='#99A6D0')
            Label_Frame_resultat_canvas_text2.pack(side=TOP, pady=5, padx=5)

            Label_canvas_medailles2 = Canvas(Label_Frame_resultat_canvas_text2, width=75, height=75,bg='#99A6D0')
            Label_canvas_medailles2.pack(side=LEFT, pady=5, padx=5)

            text2_medaille= StringVar()
            Label_text_resultat2 = Label(Label_Frame_resultat_canvas_text2, textvariable=text2_medaille,bg='#99A6D0')
            Label_text_resultat2.pack(side=RIGHT, pady=5, padx=5)

            text_choix_medaille(type_partie, 1)
            Label_canvas_medailles2.create_image(0,0,anchor=NW, image=img_resultat2)




    else:

        # titre de la fenetre quand on passe sur les crédits
        Jeu.title("Maths-Quest | Crédits  © PLADEAU Quentin LUBAN Théo")

        Label_Titre_Credits = Label(Jeu, text = "Crédits", font=("Arial", 15), bg = '#BBC4E3')
        Label_Titre_Credits.pack(pady=15)


        frame_credits = Frame(Jeu)
        frame_credits.pack(expand=True, fill='both', padx=20, pady=20)
        
        scroll_text_credits = scrolledtext.ScrolledText(frame_credits, wrap=WORD, width=60, height=20, font=("Arial", 10))
        scroll_text_credits.pack(expand=True, fill='both')

        #texte des crédits
        text_credits = """
        Maths-Quest

        Merci beaucoup d'avoir joué à Maths-Quest ! Nous espérons que ce jeu vous a plu et vous a permis d'acquérir de nouvelles connaissances.

        Ce projet a nécessité pas moins de 300 heures de travail, de réflexion et de développement. N'hésitez pas à nous faire part de vos avis concernant ce projet !

        Pour soutenir le projet / obtenir des informations : https://github.com/Gandalf0207/Maths-Quest

        
        
        Projet créé par Théo LUBAN et Quentin PLADEAU

        Une idée originale de Théo LUBAN 

        Développé par Quentin PLADEAU

        Designé par Théo LUBAN
        avec l'aide de Kaylan TROUHILLET

        Sous les conseils de Cédric ESCOUTE



            """

        text_credits2 = """

            Maths-Quest
            
            © Tous droits réservés 2024

            by LUBAN Théo & PLADEAU Quentin

        """

        # Ajout de texte avec différentes polices
        normal_font = ('Arial', 12)
        italic_font = ('Arial', 10, 'italic')

        scroll_text_credits.insert(END, text_credits, 'normal')
        scroll_text_credits.insert(END, text_credits2, 'italic')

        # Configuration des tags de police
        scroll_text_credits.tag_configure('normal', font=normal_font)
        scroll_text_credits.tag_configure('italic', font=italic_font)


        btn_fin = Button(Jeu, text="Fermer", command=Jeu.destroy)
        btn_fin.pack(pady=5)
    

    Jeu.mainloop() # loop de la fenetre




#################################################
#ACCUEIL#


global Niveau
Niveau = 0

#fonction parametre pour choix du type de partie
def parametre(Lancement, Label_Frame_courverture): 

    #chek avant de lancer le jeu + indication si le lancement n'est pas possible
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

    #mise à jour des check_button accessible ou non en fonction de ce que le joueur choisit comme type de partie
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

    #mise à jour des check_button accessible ou non en fonction de ce que le joueur choisit comme type de partie
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

    #fonction de check sur les consignes et termes d'utilisation pour activer /désactiver le btn pour jouer
    def check(btn):

        global check_btn
        if check_btn == False:
            btn.config(state=NORMAL)
            check_btn = True
        else:
            btn.config(state=DISABLED)
            check_btn = False

    global check_btn 
    check_btn = False
    
    #fonction qui ouvre la fenetre des consignes et termes d'utilisation
    def condition_generale_utilisation():
    
        global f
        if not f or not f.winfo_exists(): #check si la fenetre est deja existante pour eviter d'en ouvrir plusieurs à la fois
            #elements de la fenetre
            f = Toplevel()
            f.title("Maths-Quest | Termes et Conditons d'Utilisation      © PLADEAU Quentin LUBAN Théo")



            Label_titre = Label(f, text="Maths-Quest", fg = "#01548d", font=("Arial", 25))

            Label_titre.pack(pady=10)


            frame = Frame(f)
            frame.pack(expand=True, fill='both', padx=20, pady=20)
            
            scroll_text = scrolledtext.ScrolledText(frame, wrap=WORD, width=60, height=20, font=("Arial", 10))
            scroll_text.pack(expand=True, fill='both')

            text_condition = """
                    Termes et Conditions d'Utilisation

                Merci d'utiliser ce jeu Python Maths-Quest, un projet créé avec passion pour l'amour des mathématiques et du partage de connaissances. Avant de continuer à utiliser ce logiciel, veuillez lire attentivement les conditions suivantes :

                1. Droit d'auteur : Ce jeu est protégé par les lois sur le droit d'auteur et est la propriété intellectuelle de LUBAN Théo & PLADEAU Quentin. Tous les droits qui ne sont pas expressément accordés dans ces conditions sont réservés.

                2. Utilisation personnelle : Ce jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.

                3. Règlementation française : En utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.

                4. Librairies open source : Ce jeu utilise des librairies open source telles que Python, Tkinter, Matplotlib, LaTeX, et d'autres. Nous reconnaissons et apprécions le travail des développeurs de ces librairies, et nous nous engageons à respecter les termes de leurs licences respectives. Les informations sur ces licences sont disponibles dans les fichiers correspondants du projet.
                
                5. Crédits : Nous tenons à remercier LUBAN Théo & PLADEAU Quentin pour leur contribution à ce projet. Leurs efforts ont été essentiels pour créer ce jeu. Nous apprécions également le soutien de ESCOUTE Cédric, qui a rendu ce projet possible.

                6. Cadre de réalisation : Ce jeu a été développé dans le cadre du cours de NSI de première. Nous sommes reconnaissants envers ESCOUTE Cédric pour son soutien et l'enseignement de connaissances ayant servie au projet.

                En utilisant ce jeu, vous acceptez ces termes et conditions. Si vous n'acceptez pas ces termes, veuillez ne pas utiliser ce logiciel. Ces termes et conditions peuvent être modifiés à tout moment sans préavis.

                Pour toute question ou préoccupation concernant ces termes et conditions, veuillez contacter votre enseignant vous ayant transmit une copie du projet ou bien vous référer à la liscence disponible sur le dépots GitHub du projet : https://github.com/Gandalf0207/Maths-Quest .      
                
    © Tous droits réservé 2024
    PLADEAU Quentin & LUBAN Théo
                """
            scroll_text.insert(END, text_condition)
            close_btn_f = Button(f, command=f.destroy, text="Fermer").pack(side=BOTTOM, pady = 5)
            f.mainloop()


    #Fonction de mise en page au survol du text pour le souligner (text des consignes d'utilisation) 
    def surligne(event):
        Label_text_check_button_condition.config(font=(label_font_family, label_font_size, "underline"))

    def desurligne(event):
        Label_text_check_button_condition.config(font=(label_font_family, label_font_size))





    #on détruit la couverture, pour pouvoir afficher les elements suivants
    Label_Frame_courverture.destroy()
    

    #elements de parametres
    Lancement.title("Maths-Quest | Menu      © PLADEAU Quentin LUBAN Théo")


    Label_titre_lancement = Label(Lancement, text="Maths-Quest",fg = "#01548d", font=("Arial", 25),bg = "#BBC4E3")
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
    Frame_.pack(expand=True, fill=BOTH, side=BOTTOM)
    

    #btn jour pour lancer la partie
    btn = Button(Frame_, text="Jouer !",command=verif_lancement, state=DISABLED)
    btn.pack( pady=20)

    text_erreur_lancement = StringVar()
    Label_text_erreur_lancement = Label(Frame_, textvariable=text_erreur_lancement,bg = "#99A6D0", wraplength = 200, justify='center', fg='#9A0004')
    Label_text_erreur_lancement.pack()

    # frame check button condition + text du check button en label pour pouvoir le cliquer
    Label_frame_check_button_conditon_utilisation = Frame(Lancement,bg = "#99A6D0")
    Label_frame_check_button_conditon_utilisation.pack(side = TOP, pady= 5 , padx = 5)
    # Récupérer la police par défaut du Label_check_button_conditon
    label_font = font.nametofont("TkDefaultFont")
    label_font_family = label_font.actual()["family"]
    label_font_size = label_font.actual()["size"]

    Label_check_button_conditon = Checkbutton(Label_frame_check_button_conditon_utilisation, command=lambda:check(btn),  bg ="#99A6D0", cursor="hand2")
    Label_check_button_conditon.pack(pady= 5,padx = 5, side = LEFT, anchor = N)

    Label_text_check_button_condition = Label(Label_frame_check_button_conditon_utilisation,text = "J'ai pris connaissance et j'accepte les conditions et termes général d'utilisation du jeu Maths-Quest créé par LUBAN Théo & PLADEAU Quentin",wraplength=300,bg="#99A6D0", cursor="hand2",justify=LEFT,  )
    Label_text_check_button_condition.pack(side = RIGHT, pady = 5, padx=5, anchor = N)
    Label_text_check_button_condition.bind("<Button-1>", lambda e: condition_generale_utilisation())
    Label_text_check_button_condition.bind("<Enter>", surligne)
    Label_text_check_button_condition.bind("<Leave>", desurligne)



#toute première fenetre pour ouvrir la fenetre du jeu, avec les infos sur le jeu + couverture
Lancement = Tk()
Lancement.title("Maths-Quest | Lancement      © PLADEAU Quentin LUBAN Théo")
# Lancement.geometry("350x400")
Lancement.config(bg = "#BBC4E3")
couverture = PhotoImage(file="Images/Autre/couverture.png")

### frame qui contient le canva de la couverture
Label_Frame_courverture = Frame(Lancement, bg = "#99A6D0" )
Label_Frame_courverture.pack(expand=True)

##canva de la courverture
Label_canvas_courverture = Canvas(Label_Frame_courverture,width = 463, height = 652, bg = None)
Label_canvas_courverture.pack(expand=True)

Label_canvas_courverture.create_image(0,0,anchor =NW, image = couverture)

Label_btn_lancement_config = Button(Label_Frame_courverture, text="Menu", command=lambda:parametre(Lancement, Label_Frame_courverture))
Label_btn_lancement_config.pack(side= BOTTOM, pady=3)


Lancement.mainloop()

##################################################################################################



# FIN main # 



#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################