### EN FONCTION DU NIVEAU IL FAUT SET UP LA GENERATION / CUSTOM / TEXT DES PNJ ET ITEMS ###

from tkinter import *
from tkinter import ttk
import random
import time 
import labyrinthe
import custom_labyrinthe

### Pour avoir une certaine sécurité lors de la récupération des fragements de clé; il a fallut faire en sorte
# de ne pourvoir ouvrir qu'une seule fenetre à la fois pour eviter de donner plus de fragments de clé que prévus
# nous avons donc utilisé l'ia pour apprendre et comprendre comment fonctionne le protocole utilisé... ###

### C'est pourquoi il est possible de voir des commentaires : #code ia
# Cela signifie que cette partie du code n'a pas été réalisée uniquement par nous meme....
global Label_btn_suivant_discussion_pnj
Label_btn_suivant_discussion_pnj = None


def Gestion_Jouer(fenetre, Niveau):

    global Label_btn_suivant_discussion_pnj
    Label_btn_suivant_discussion_pnj = None
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
    Frag2 = PhotoImage(file="image/frag_cle2.png")
    Frag_cle = PhotoImage(file="image/frag_cle.png")
    glue2 = PhotoImage(file="image/glue.png")
    glue = PhotoImage(file="image/glue0.png")
    craft_table_ = PhotoImage(file="image/craft.png")

    Perso = PhotoImage(file="image/perso.png")

    pnj1 = PhotoImage(file = "image/pnj1.png")
    pnj2 = PhotoImage(file = "image/pnj2.png")
    pnj3 = PhotoImage(file = "image/pnj3.png")
    pnj4 = PhotoImage(file = "image/pnj4.png")

    pnj1_grand = PhotoImage(file="image/sorcier1.png")
    pnj2_grand = PhotoImage(file="image/sorcier2.png")
    pnj3_grand = PhotoImage(file="image/sorcier3.png")
    pnj4_grand = PhotoImage(file="image/sorcier4.png")

    Cle_full = PhotoImage(file="image/cle.png")
    clepnj1 = PhotoImage(file="image/clepnj1.png")
    clepnj2 = PhotoImage(file="image/clepnj2.png")
    clepnj3 = PhotoImage(file="image/clepnj3.png")

    mur1 = PhotoImage(file="image/Wall1.png")
    mur2 = PhotoImage(file="image/Wall2.png")
    mur3 = PhotoImage(file="image/Wall3.gif")



    #On affiche dans le terminal pour check
    for i in range(len(L)):
        print(*L[i], sep=" ")
        
    #Fonction qui gère le déplacement du personnage; MAJ de la map tkinter, les interractions avec les pnj
    def deplacement(event):
        
        global ordonne
        global abscisse

        touche = event.keysym
        check = ["■" ,"\U0001F6AA", "¤"]
        pnj_liste = ["pnj1", "pnj2", "pnj3", "pnj4"]


        if touche == "z":
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


        elif touche=="q" :
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


        elif touche=="s" :
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


        elif touche=="d" :
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

        #Script permettant d'afficher si une discution est possible avec les pnj ou non
        if (L[ordonne-1][abscisse] in pnj_liste or L[ordonne+1][abscisse] in pnj_liste or L[ordonne][abscisse-1] in pnj_liste or L[ordonne][abscisse+1] in pnj_liste):
            #PNJ 1
            if (L[ordonne-1][abscisse] == pnj_liste[0] or L[ordonne+1][abscisse]== pnj_liste[0] or L[ordonne][abscisse-1]== pnj_liste[0] or L[ordonne][abscisse+1]== pnj_liste[0]):
                Label_text_possibilite_strvar.set("Appuie sur 'E' pour me parler !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj1)

            #PNJ 2
            elif (L[ordonne-1][abscisse] == pnj_liste[1] or L[ordonne+1][abscisse]== pnj_liste[1] or L[ordonne][abscisse-1]== pnj_liste[1] or L[ordonne][abscisse+1]== pnj_liste[1]):
                Label_text_possibilite_strvar.set("Appuie sur 'E' pour me parler !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj2)

            #PNJ3
            elif (L[ordonne-1][abscisse] == pnj_liste[2] or L[ordonne+1][abscisse]== pnj_liste[2] or L[ordonne][abscisse-1]== pnj_liste[2] or L[ordonne][abscisse+1]== pnj_liste[2]):
                Label_text_possibilite_strvar.set("Appuie sur 'E' pour me parler !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj3)

            #PNJ4
            elif (L[ordonne-1][abscisse] == pnj_liste[3] or L[ordonne+1][abscisse]== pnj_liste[3] or L[ordonne][abscisse-1]== pnj_liste[3] or L[ordonne][abscisse+1]== pnj_liste[3]):
                Label_text_possibilite_strvar.set("Appuie sur 'E' pour me parler !")
                canvas_infos_possibilite_discussion.create_image(0,0,anchor=NW, image=pnj4)

        else:
            Label_text_possibilite_strvar.set("Aucun personnage n'est présent aux alentours ! ")
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

        # if craft ==1:
        #     if nb_frag_cle !=0:
        #         canvas_inv.delete("all")
        #         nb_frag_cle = 0
        #         nb_glue = 0
        #         nb_cle += 1

        #     text_nb_cle.set(f"Clé : {nb_cle}/1")


        #     if Niveau == 0:
        #         canvas_inv.create_image(60,0, anchor = NW, image = Cle_full)

        #     elif Niveau == 1 :
        #         canvas_inv.create_image(110,0, anchor = NW, image = Cle_full)
        #         text_nb_glue.destroy()


        if pnj1_infos == False and pnj2_infos == False and pnj3_infos == False and pnj4_infos == False :
            canvas_inv.create_image(0,0, anchor = NW, image=clepnj1)
            canvas_inv.create_image(60,0, anchor = NW, image=clepnj2)
            canvas_inv.create_image(120,0, anchor = NW, image=clepnj3)
            if Niveau == 1:
                canvas_inv.create_image(170,0, anchor = NW, image=glue)

        if pnj1_infos == True:
            canvas_inv.create_image(0,0, anchor = NW, image=Cle_full)

        if pnj2_infos == True:
            canvas_inv.create_image(60,0, anchor = NW, image=Cle_full)

        if pnj3_infos == True:
            canvas_inv.create_image(120,0, anchor = NW, image=Cle_full)
        
        if pnj4_infos == True:
            canvas_inv.create_image(180,0, anchor = NW, image=glue2)



    def table_craft(event):
        global craft, nb_frag_cle, nb_glue
        
        if L[ordonne][abscisse-1] == "¤":
            if Niveau ==0:
                if nb_frag_cle ==3:
                    craft +=1
                    load_inv()
                else:
                    print("vous n'avez pas assez de frags clé !")

            elif Niveau == 1:
                if nb_frag_cle ==3 and nb_glue ==1:
                    craft+=1
                    load_inv()
                else:
                    print("vous n'avez pas assez de colle ou de frags de clé !")
        else:
            print("Il n'y a pas de tableau de craft près de vous pour fabriquer votre objet !")




    def parler_pnj(event):

        def affiche_prog(pnj, pnj_infos, Niveau):
            global c
            # global nb_frag_cle
            # global nb_glue
            # global craft

            c += 1
            text_complet = ""
            # comme cette partie est commune; on l'affiche au debut si c'est le bon tour
            if pnj_infos == False:
                if c == 1 :
                    if pnj != "pnj4":
                        text_complet = "Bravo ! Vous avez obtenu 1 fragment de clé !" 
                    else:
                        text_complet = "Bravo ! Vous avez obtenue un bâton de colle !"

                elif c == 2:
                    text_complet = "Vous obtenez également une partie du cours !"

                # on fait en fonction du pnj parce que le cours est unique à chaque pnj
                elif pnj == "pnj1":
                    # et le cours est différent en fonction du niveau (map qui change)
                    if c == 3 :
                        if Niveau == 0: 
                            text_complet = "insérer le cours !"
                        elif Niveau == 1:
                            text_complet = "insérer le cours !"

                    elif c == 4:
                        canvas_tete_pnj_grand.delete("all")
                        Label_texte_parole_discussion_pnj_strvar.set("")
                        Label_btn_suivant_discussion_pnj.destroy()

                        global pnj1_infos
                        pnj1_infos = True

                        load_inv(Niveau)

                elif pnj == "pnj2":
                    if c == 3 :
                        if Niveau == 0: 
                            text_complet = "insérer le cours !"
                        elif Niveau == 1:
                            text_complet = "insérer le cours !"

                    elif c == 4:
                        canvas_tete_pnj_grand.delete("all")
                        Label_texte_parole_discussion_pnj_strvar.set("")
                        Label_btn_suivant_discussion_pnj.destroy()


                        global pnj2_infos
                        pnj2_infos = True

                        load_inv(Niveau)

                elif pnj == "pnj3":
                    if c == 3 :
                        if Niveau == 0: 
                            text_complet = "insérer le cours !"
                        elif Niveau == 1:
                            text_complet = "insérer le cours !"

                    elif c == 4:
                        canvas_tete_pnj_grand.delete("all")
                        Label_texte_parole_discussion_pnj_strvar.set("")
                        Label_btn_suivant_discussion_pnj.destroy()

                        global pnj3_infos
                        pnj3_infos = True

                        load_inv(Niveau)

                elif pnj == "pnj4":
                    if c == 3 :
                        if Niveau == 1:
                            text_complet = "insérer le cours !"

                    elif c == 4:
                        canvas_tete_pnj_grand.delete("all")
                        Label_texte_parole_discussion_pnj_strvar.set("")
                        Label_btn_suivant_discussion_pnj.destroy()

                        global pnj4_infos
                        pnj4_infos = True

                        load_inv(Niveau)



            #de nouveau une partie commune mais cette fois quand on a déjà vu le pnj
            else:
                if c ==1:
                    if pnj=="pnj4":
                        text_complet = "Vous avez déjà obtenu le bâton de colle de ce sorcier !" 
                    else:
                        text_complet = "Vous avez déjà obtenu le fragment de clé de ce sorcier !" 
                elif c == 2 :
                    text_complet = "Vous pouvez consulter la partie du cours obtenue dans la page 'cours'.'"
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

                for i in range(len(text_complet)):
                    text_partiel = text_complet[:i+1]
                    Label_texte_parole_discussion_pnj_strvar.set(f"{text_partiel}")
                    Label_texte_parole_discussion_pnj_widget.update()
                    time.sleep(0.03)



        global pnj1_infos
        global pnj2_infos
        global pnj3_infos
        global pnj4_infos  

        pnj_List = ["pnj1" , "pnj2" ,"pnj3" ,"pnj4"]

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
                    canvas_tete_pnj_grand.create_image(0, 0, anchor=NW, image=pnj1_grand)

            
                global Label_btn_suivant_discussion_pnj

                if Label_btn_suivant_discussion_pnj is not None:
                    if Label_btn_suivant_discussion_pnj.winfo_exists():
                        Label_btn_suivant_discussion_pnj.destroy()
                #On crée le bouton pour faire discuter le pnj avec l'utilisateur et on set le texte de bienvenue          
                Label_texte_parole_discussion_pnj_strvar.set("Salut ! Clique sur suivant !")
                Label_btn_suivant_discussion_pnj = Button(Label_Frame_Discussion_pnj, text="Suivant", command=lambda: affiche_prog(pnj_, pnj_infos_, Niveau))
                Label_btn_suivant_discussion_pnj.pack(side=BOTTOM, anchor="c", pady=5)
        else:
            #on clear si jamais la personne s'en va
            canvas_tete_pnj_grand.delete("all")
            Label_texte_parole_discussion_pnj_strvar.set("")
            #fonction de check pour delete btn (winfo : true/false) et première ligne pour eviter les erreurs (double verif)
            if Label_btn_suivant_discussion_pnj is not None:
                if Label_btn_suivant_discussion_pnj.winfo_exists():
                    Label_btn_suivant_discussion_pnj.destroy()
            c = 0



    #Fonction de boucle pour les niveaux, il faut faire les conditions pour la boucle dcp
    def porte_enigme(event):

        global Niveau
        touche = event.keysym
        if touche == "b":
            question = int(input("cc"))
            if question == 1:
                Niveau +=1
                Gestion_Jouer(Jeu, Niveau)
        



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
    pnj1_infos = False
    pnj2_infos = False
    pnj3_infos = False
    pnj4_infos = False   

    # 

    global craft
    global nb_cle

    nb_cle = 0
    craft = 0

    # 



    Jeu.geometry("1300x700")
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
    Label_text_possibilite_strvar.set("Aucun personnage n'est présent aux alentours ! ")
    Label_text_possibilite_widget = Label(Label_Frame_Text_Info_Discussion_pnj, textvariable=Label_text_possibilite_strvar, wraplength=200, justify="left")
    Label_text_possibilite_widget.pack(side="left", pady=5, padx=5)
   
    ## Frame de box de discussion avec les pnj
    Label_Frame_Discussion_pnj = Frame(Label_Frame_pnj_Text, bg="blue")
    Label_Frame_Discussion_pnj.pack(expand=True, fill=BOTH, padx=5, pady=5, side='right')

    #On load les element qui serviron aux boites de discussion des pnjs
    canvas_tete_pnj_grand = Canvas(Label_Frame_Discussion_pnj, bg='white', height=100, width=200)
    canvas_tete_pnj_grand.pack(anchor="c", padx=10,pady=5, side=LEFT)
    Label_texte_parole_discussion_pnj_strvar = StringVar()
    Label_texte_parole_discussion_pnj_widget = Label(Label_Frame_Discussion_pnj, textvariable=Label_texte_parole_discussion_pnj_strvar, wraplength=500, justify="left")
    Label_texte_parole_discussion_pnj_widget.pack(side=LEFT, padx=5, pady=5)



    ####Partie Droite : 
    Label_Frame_Cours_cle = Frame(Label_Frame_Global, bg="#000000")
    Label_Frame_Cours_cle.pack(side='right', expand=True, fill="both", padx=5, pady=5)

    ##Frame qui affiche le cours actuel
    Label_Frame_Cours_Affiche = Frame(Label_Frame_Cours_cle,bg='white')
    Label_Frame_Cours_Affiche.pack(side='top', expand=True, fill="both", padx=5, pady=5)
    
    ##Frame affiche l'inventaire (clé(s))
    Label_Frame_Inv_Cle = Frame(Label_Frame_Cours_cle, bg='white')
    Label_Frame_Inv_Cle.pack(side='bottom', padx=5, pady=5, fill='x')

    #On load l'inventaire de base 
    long_canvas_inv = 170
    if Niveau ==1:
        long_canvas_inv = 230

    canvas_inv = Canvas(Label_Frame_Inv_Cle, width=long_canvas_inv, height=50, bg = "black")
    canvas_inv.create_image(0,0,anchor=NW, image = clepnj1)
    canvas_inv.create_image(60,0,anchor=NW, image = clepnj2)
    canvas_inv.create_image(120,0,anchor=NW, image = clepnj3)
    if Niveau == 1:
        canvas_inv.create_image(180,0,anchor=NW, image = glue)

    canvas_inv.pack(pady=10)





#deplacement
    Jeu.focus_set()
    Jeu.bind("<KeyPress-z>", deplacement)
    Jeu.bind("<KeyPress-q>", deplacement)
    Jeu.bind("<KeyPress-s>", deplacement)
    Jeu.bind("<KeyPress-d>", deplacement)
    Jeu.bind("<KeyPress-a>", parler_pnj)
    Jeu.bind("<KeyPress-b>", porte_enigme)
    Jeu.bind("<KeyPress-c>", table_craft)


    Jeu.mainloop()






##################################################################################################
#ACCUEIL#

global Niveau
Niveau = 0

Lancement = Tk()
Lancement.title("RPG : Lanncement  Théo | Quentin")

Lancement.geometry("350x400")

Frame_ = ttk.Frame(Lancement, bg = None)


btn = ttk.Button(Frame_, text="Jouer !",command=lambda:Gestion_Jouer(Lancement, Niveau)).pack( pady=20)
Frame_.pack()

Lancement.mainloop()
##################################################################################################






