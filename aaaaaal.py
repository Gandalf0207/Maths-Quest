from tkinter import *

# Créez la fenêtre racine
Jeu = Tk()

# Chargez l'image après avoir créé la fenêtre racine
sorcier1 = PhotoImage(file="fichiers test/sorcier1.png")

def deff():
    def deffff():
        Label_text_infos.configure(text="hehehe")

    ok = Toplevel()  # Utiliser Toplevel au lieu de Tk pour une nouvelle fenêtre indépendante
    canva_discussion = Canvas(ok, width=300, height=260, bg="black")
    canva_discussion.create_image(0, 0, anchor=NW, image=sorcier1)
    canva_discussion.pack()

    Label_text_infos = Label(ok, text="infos1")
    Label_text_infos.pack(pady=20)

    btn_suivant = Button(ok, text="Suivant", command=deffff)
    btn_suivant.pack()

btn_suivant = Button(Jeu, text="Suivant", command=deff)
btn_suivant.pack()

Jeu.mainloop()
