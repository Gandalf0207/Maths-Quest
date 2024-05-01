from tkinter import *

# Créez la fenêtre racine
Jeu = Tk()

# Chargez l'image après avoir créé la fenêtre racine
sorcier1 = PhotoImage(file="fichiers test/sorcier1.png")

# Variable pour suivre l'état de la deuxième fenêtre pour les problèmes de la porte
second_window_probleme= None

def deff(event=None):
    global second_window_probleme
    
    def deffff():
        Label_text_infos.configure(text="hehehe")

    if not second_window_probleme or not second_window_probleme.winfo_exists():  # Vérifie si la deuxième fenêtre existe
        second_window_probleme= Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
        canva_discussion = Canvas(second_window_probleme, width=300, height=260, bg="black")
        canva_discussion.create_image(0, 0, anchor=NW, image=sorcier1)
        canva_discussion.pack()

        Label_text_infos = Label(second_window_probleme, text="infos1")
        Label_text_infos.pack(pady=20)

        btn_suivant = Button(second_window_probleme, text="Suivant", command=deffff)
        btn_suivant.pack()

        # Lie la fermeture de la fenêtre à la réinitialisation de second_window_probleme
        second_window_probleme.protocol("WM_DELETE_WINDOW", lambda: reset_second_window())

def reset_second_window():
    global second_window_probleme
    if second_window_probleme:
        second_window_probleme.destroy()  # Détruit la fenêtre
    second_window_probleme= None

# Lie l'appui sur la touche "a" à la fonction deff
Jeu.bind("<KeyPress-a>", deff)

Jeu.mainloop()
