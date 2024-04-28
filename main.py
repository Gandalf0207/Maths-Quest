### EN FONCTION DU NIVEAU IL FAUT SET UP LA GENERATION / CUSTOM / TEXT DES PNJ ET ITEMS ###

from tkinter import *
from tkinter import ttk
import time 
import labyrinthe
import custom_labyrinthe


# Variable pour suivre l'état de la deuxième fenêtre ################################### CODE IA
second_window = None ################################### CODE IA
# Déclarez les variables globales pour stocker les images
sorcier1_image = None
sorcier2_image = None
sorcier3_image = None
sorcier4_image = None

def Gestion_Jouer(fenetre, Niveau):
    

    #Pour cette comparaison, le "fenetre" correspond à la fenetre tk qui est en cours de loop
    # Le permir passage se sera la fenetre 'Lancement', puis les autres tours se sera les fenetres de 'Jeu'
    # Ce fonctionnement permet de faire tourner le programme pour le nombre de niveaux disponible !
    if Niveau ==0:
        #Nettoyage de la page
        fenetre.destroy()
    else:
        fenetre.destroy()

    Jeu = Tk()

    #On crée la map 
    longueur = int(Label_Longueur_Map.get())
    largeur = int(Label_Largeur_Map.get())
    L = labyrinthe.mapmaker(longueur,largeur) 

    #On custom la map avec les pnj, portes et joueur....
    L = custom_labyrinthe.Custom_Map(L, longueur, largeur, Niveau)


    #On load les img pour pouvoir les afficher
    Perso = PhotoImage(file="image/perso.png")
    Arbre = PhotoImage(file="image/okok.png")
    pnj1 = PhotoImage(file = "image/pnj1.png")
    pnj2 = PhotoImage(file = "image/pnj2.png")
    pnj3 = PhotoImage(file = "image/pnj3.png")
    pnj4 = PhotoImage(file = "image/pnj4.png")
    porte = PhotoImage(file="image/porte.png")
    carre = PhotoImage(file="image/CARRE.png")
    Frag2 = PhotoImage(file="image/frag_cle2.png")
    Frag_cle = PhotoImage(file="image/frag_cle.png")



    #On affiche dans le terminal pour check
    for i in range(len(L)):
        print(*L[i], sep=" ")
        
    #Fonction qui gère le déplacement du personnage; MAJ de la map tkinter, les interractions avec les pnj
    def deplacement(event):
        
        global ordonne
        global abscisse

        touche = event.keysym
        check = ["■" ,"\U0001F6AA"]
        pnj_liste = ["pnj1", "pnj2", "pnj3", "pnj4"]


        if touche == "z":
            if ordonne-1 > 0 and L[ordonne-1][abscisse] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)

                #Si jamais les pnj sont sur la route
                if (L[ordonne-1][abscisse] in pnj_liste) and (L[ordonne-2][abscisse] not in check):
                    ordonne-=2
                elif L[ordonne-1][abscisse] in pnj_liste :
                    print("C'est un PNJ")
                else:
                    ordonne-=1
                
                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")


        elif touche=="q" :
            if abscisse-1 > 0 and L[ordonne][abscisse-1] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)

                #Si jamais les pnj sont sur la route
                if (L[ordonne][abscisse-1] in pnj_liste) and (L[ordonne][abscisse-2] not in check):
                    abscisse-=2
                elif L[ordonne][abscisse-1] in pnj_liste :
                    print("C'est un PNJ")
                else:
                    abscisse-=1

                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")


        elif touche=="s" :
            if ordonne+1 < len(L) and L[ordonne+1][abscisse] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)

                #Si jamais les pnj sont sur la route
                if (L[ordonne+1][abscisse] in pnj_liste) and (L[ordonne+2][abscisse] not in check):
                    ordonne+=2
                elif L[ordonne+1][abscisse] in pnj_liste :
                    print("C'est un PNJ")
                else:
                    ordonne+=1

                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
            else :
                print("C'est un mur !")


        elif touche=="d" :
            if abscisse+1 < len(L[ordonne]) and L[ordonne][abscisse +1] not in check :
                L[ordonne][abscisse] = " "
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=carre)

                #Si jamais les pnj sont sur la route
                if (L[ordonne][abscisse+1] in pnj_liste) and (L[ordonne][abscisse+2] not in check):
                    abscisse+=2
                elif L[ordonne][abscisse+1] in pnj_liste :
                    print("C'est un PNJ")
                else:
                    abscisse+=1

                L[ordonne][abscisse] = "○"
                L[ordonne][abscisse] = canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)

            else :
                print("C'est un mur !")

        else:
            print("suite des fonctionnalités pas encore faites")

        print("Abscisse : ", abscisse)
        print("Ordonne : ", ordonne)


    #Fonction de MAJ et affichage de l'inventaire du joueur ### pas terminé , manque les crafts possible !
    def load_inv(nb_frag_cle):
        if nb_frag_cle == 0:
            canvas_inv.create_image(0,0, anchor = NW, image=Frag_cle)
            canvas_inv.create_image(60,0, anchor = NW, image=Frag_cle)
            canvas_inv.create_image(120,0, anchor = NW, image=Frag_cle)
            text_nb_cle.set(f"Fragments de clé {nb_frag_cle}/3")
        if nb_frag_cle == 1:
            canvas_inv.create_image(0,0, anchor = NW, image=Frag2)
            text_nb_cle.set(f"Fragments de clé {nb_frag_cle}/3")
        elif nb_frag_cle == 2:
            canvas_inv.create_image(60,0, anchor = NW, image=Frag2)
            text_nb_cle.set(f"Fragments de clé {nb_frag_cle}/3")
        elif nb_frag_cle == 3:
            canvas_inv.create_image(120,0, anchor = NW, image=Frag2)
            text_nb_cle.set(f"Fragments de clé {nb_frag_cle}/3")


    def parler_pnj(event):

        def affiche_prog(pnj, pnj_infos, Niveau):
            global c
            c += 1
            text_complet = ""
            # comme cette partie est commune; on l'affiche au debut si c'est le bon tour
            if pnj_infos == False:
                if c == 1:
                    text_complet = "Bravo ! Vous avez obtenu 1 fragment de clé !" 
                elif c == 2 :
                    text_complet = "Vous obtenez également une partie du cours !"

                # on fait en fonction du pnj parce que le cours est unique à chaque pnj
                elif pnj == "pnj1":
                    # et le cours est différent en fonction du niveau (map qui change)
                    if Niveau == 0:
                        if c == 3 : 
                            text_complet = "insérer le cours !"
                        elif c == 4:
                            second_window.destroy()

                            global pnj1_infos
                            pnj1_infos = True

                            global nb_frag_cle
                            nb_frag_cle +=1
                            load_inv(nb_frag_cle)

                elif pnj == "pnj2":
                    if Niveau == 0:
                        if c == 3 : 
                            text_complet = "insérer le cours !"
                        elif c == 4:
                            second_window.destroy()
                            global pnj2_infos
                            pnj2_infos = True

                elif pnj == "pnj3":
                    if Niveau == 0:
                        if c == 3 : 
                            text_complet = "insérer le cours !"
                        elif c == 4:
                            second_window.destroy()
                            global pnj3_infos
                            pnj3_infos = True

                elif pnj == "pnj4":
                    if Niveau == 0:
                        if c == 3 : 
                            text_complet = "insérer le cours !"
                        elif c == 4:
                            second_window.destroy()
                            global pnj4_infos
                            pnj4_infos = True


            #de nouveau une partie commune mais cette fois quand on a déjà vu le pnj
            else:
                if c ==1:
                    text_complet = "Vous avez déjà obtenu le fragment de clé de ce sorcier !" 
                elif c == 2 :
                    text_complet = "Vous pouvez consulter la partie du cours obtenue dans la page 'cours'.'"
                elif c == 3 : 
                    second_window.destroy()



            if (c < 4 and pnj_infos == False) or (c < 3 and pnj_infos == True):

                for i in range(len(text_complet)):
                    text_partiel = text_complet[:i+1]
                    Label_text_infos.configure(text = text_partiel)
                    second_window.update()
                    time.sleep(0.1)

        global pnj1_infos
        global pnj2_infos
        global pnj3_infos
        global pnj4_infos  
        global nb_frag_cle

        pnj_List = ["pnj1" , "pnj2" ,"pnj3" ,"pnj4"]

        global c
        c = 0

        global sorcier1_image, sorcier2_image, sorcier3_image, sorcier4_image


        # check avant de lancer la fenetre si jamais un sorcier n'est pas présent quand la touche 'a' est pressée   
        if   (L[ordonne-1][abscisse] in pnj_List or L[ordonne+1][abscisse] in pnj_List or L[ordonne][abscisse-1] in pnj_List or L[ordonne][abscisse+1] in pnj_List ):
            


            global second_window################################### CODE IA

            if not second_window or not second_window.winfo_exists():  # Vérifie si la deuxième fenêtre existe################################### CODE IA
                #PNJ 1
                if (L[ordonne-1][abscisse] == pnj_List[0] or L[ordonne+1][abscisse]== pnj_List[0] or L[ordonne][abscisse-1]== pnj_List[0] or L[ordonne][abscisse+1]== pnj_List[0]):
                    pnj_ = "pnj1"
                    pnj_infos_ = pnj1_infos

                #PNJ 2
                elif (L[ordonne-1][abscisse] == pnj_List[1] or L[ordonne+1][abscisse]== pnj_List[1] or L[ordonne][abscisse-1]== pnj_List[1] or L[ordonne][abscisse+1]== pnj_List[1]):
                    pnj_ = "pnj2"
                    pnj_infos_ = pnj2_infos

                #PNJ3
                elif (L[ordonne-1][abscisse] == pnj_List[2] or L[ordonne+1][abscisse]== pnj_List[2] or L[ordonne][abscisse-1]== pnj_List[2] or L[ordonne][abscisse+1]== pnj_List[2]):
                    pnj_ = "pnj3"
                    pnj_infos_ = pnj3_infos

                #PNJ4
                elif (L[ordonne-1][abscisse] == pnj_List[3] or L[ordonne+1][abscisse]== pnj_List[3] or L[ordonne][abscisse-1]== pnj_List[3] or L[ordonne][abscisse+1]== pnj_List[3]):
                    pnj_ = "pnj4"
                    pnj_infos_ = pnj4_infos
                

                second_window = Toplevel()  
                canva_discussion = Canvas(second_window, width=450, height=260, bg="white")
                canva_discussion.pack()

                if pnj_ == "pnj1":
                    sorcier1_image = PhotoImage(file="image/sorcier1.png")
                    canva_discussion.create_image(0, 0, anchor=NW, image=sorcier1_image)
                elif pnj_ == "pnj2":
                    sorcier2_image = PhotoImage(file="image/sorcier2.png")
                    canva_discussion.create_image(0, 0, anchor=NW, image=sorcier2_image)
                elif pnj_ == "pnj3":
                    sorcier3_image = PhotoImage(file="image/sorcier3.png")
                    canva_discussion.create_image(0, 0, anchor=NW, image=sorcier3_image)
                elif pnj_ == "pnj4":
                    sorcier4_image = PhotoImage(file="image/sorcier4.png")
                    canva_discussion.create_image(0, 0, anchor=NW, image=sorcier4_image)
                                
                Label_text_infos = Label(canva_discussion, text="Clique sur Suivant !", wraplength=180, justify="left")
                Label_text_infos.pack(pady=20)


                canva_discussion.create_window(350, 30, window=Label_text_infos)

                btn_suivant = Button(second_window, text="Suivant", command=lambda: affiche_prog(pnj_, pnj_infos_, Niveau))
                btn_suivant.pack()

                second_window.protocol("WM_DELETE_WINDOW", lambda: reset_second_window())
    
    def reset_second_window(): #code i
        global second_window, sorcier1_image, sorcier2_image, sorcier3_image, sorcier4_image
        if sorcier1_image:
            canva_discussion.create_image(0, 0, anchor=NW, image=sorcier1_image)
        elif sorcier2_image:
            canva_discussion.create_image(0, 0, anchor=NW, image=sorcier2_image)
        elif sorcier3_image:
            canva_discussion.create_image(0, 0, anchor=NW, image=sorcier3_image)       
        elif sorcier4_image:
            canva_discussion.create_image(0, 0, anchor=NW, image=sorcier4_image)

        global second_window
        if second_window:
            second_window.destroy()  # Détruit la fenêtre
        second_window = None






    #Fonction de boucle pour les niveaux, il faut faire les conditions pour la boucle dcp
    def porte_enigme(event):

        global Niveau
        touche = event.keysym
        if touche == "b":
            question = int(input("cc"))
            if question == 1:
                Niveau +=1
                Gestion_Jouer(Jeu, Niveau)
        




    global ordonne
    global abscisse
    global nb_frag_cle
    global craft
    global pnj1_infos
    global pnj2_infos
    global pnj3_infos
    global pnj4_infos    

    abscisse = 1
    ordonne = 1
    nb_frag_cle = 0
    craft = 0
    pnj1_infos = False
    pnj2_infos = False
    pnj3_infos = False
    pnj4_infos = False
    


    long_c = len(L[0])*16
    larg_c = len(L)*16

    canvas = Canvas(Jeu, width=long_c, height=larg_c, bg= "white")

    #On affiche dans tkinter
    for x in range(len(L)):
        for y in range(len(L[x])):
            if L[x][y] == "■":
                canvas.create_image(16*y, 16*x, anchor=NW, image=Arbre)
            elif L[x][y] == "pnj1":
                canvas.create_image(16*y, 16*x, anchor=NW, image=pnj1)
            elif L[x][y] == "pnj2":
                canvas.create_image(16*y, 16*x, anchor=NW, image=pnj2)
            elif L[x][y] == "pnj3":
                canvas.create_image(16*y, 16*x, anchor=NW, image=pnj3)
            elif L[x][y] == "pnj4":
                canvas.create_image(16*y, 16*x, anchor=NW, image=pnj4)
            elif L[x][y] == "\U0001F6AA":
                canvas.create_image(16*y, 16*x, anchor=NW, image=porte)
    
    #On affiche le joueur
    canvas.create_image(16*abscisse, 16*ordonne, anchor=NW, image=Perso)
    L[1][1] = "○"

    Jeu.focus_set()
    Jeu.bind("<KeyPress-z>", deplacement)
    Jeu.bind("<KeyPress-q>", deplacement)
    Jeu.bind("<KeyPress-s>", deplacement)
    Jeu.bind("<KeyPress-d>", deplacement)
    Jeu.bind("<KeyPress-a>", parler_pnj)
    Jeu.bind("<KeyPress-b>", porte_enigme)

    canvas.pack()

    #On load l'inventaire de base 
    Label_Titre = Label(Jeu, text="Inventaire").pack()
    text_nb_cle = StringVar()
    text_nb_cle.set(f"Fragments de clé {nb_frag_cle}/3")
    Label_Titre_Cle = Label(Jeu, textvariable=text_nb_cle).pack(pady=20)

    canvas_inv = Canvas(Jeu, width=170, height=60, bg = "black")
    canvas_inv.create_image(0,0,anchor=NW, image = Frag_cle)
    canvas_inv.create_image(60,0,anchor=NW, image = Frag_cle)
    canvas_inv.create_image(120,0,anchor=NW, image = Frag_cle)

    canvas_inv.pack()

    Jeu.mainloop()


    
    




    





##################################################################################################
#ACCUEIL#

global Niveau
Niveau = 0

Lancement = Tk()
Lancement.title("RPG : Lanncement  Théo | Quentin")

Lancement.geometry("350x400")

Frame = ttk.Frame(Lancement, bg = None)

Label_Longueur_Map = StringVar()
Label_Longueur_Map.set(45)
Lmap = Scale(Frame, variable=Label_Longueur_Map, orient=HORIZONTAL, from_=30, to=70).pack()

Label_Largeur_Map = StringVar()
Label_Largeur_Map.set(20)
lmap = Scale(Frame, variable=Label_Largeur_Map, from_=10, to=30).pack()

btn = ttk.Button(Frame, text="Jouer !",command=lambda:Gestion_Jouer(Lancement, Niveau)).pack( pady=20)
Frame.pack()

Lancement.mainloop()
##################################################################################################






