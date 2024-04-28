from tkinter import *

# Variable pour suivre l'état de la deuxième fenêtre
second_window = None

def parler_pnj(event):
    global ordonne, abscisse, second_window

    # Listes des PNJ et des images correspondantes
    pnj_List = ["pnj1", "pnj2", "pnj3", "pnj4"]
    sorciers = {
        "pnj1": "image/sorcier1.png",
        "pnj2": "image/sorcier2.png",
        "pnj3": "image/sorcier3.png",
        "pnj4": "image/sorcier4.png"
    }

    # Vérifie si un PNJ est présent autour du joueur
    if any(L[ordonne + i][abscisse + j] in pnj_List for i in [-1, 0, 1] for j in [-1, 0, 1]):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if L[ordonne + i][abscisse + j] in pnj_List:
                    pnj_ = L[ordonne + i][abscisse + j]
                    pnj_infos_ = globals()[f"{pnj_}_infos"]
                    sorcier_ = PhotoImage(file=sorciers[pnj_])

                    if not second_window or not second_window.winfo_exists():
                        second_window = Toplevel()
                        canva_discussion = Canvas(second_window, width=450, height=260, bg="white")
                        canva_discussion.pack()
                        canva_discussion.create_image(0, 0, anchor=NW, image=sorcier_)

                        Label_text_infos = Label(canva_discussion, text="Clique sur Suivant !", wraplength=180, justify="left")
                        Label_text_infos.pack(pady=20)
                        canva_discussion.create_window(350, 30, window=Label_text_infos)

                        btn_suivant = Button(second_window, text="Suivant", command=lambda: affiche_prog(pnj_, pnj_infos_, Niveau))
                        btn_suivant.pack()

                        second_window.protocol("WM_DELETE_WINDOW", reset_second_window)

def reset_second_window():
    global second_window
    if second_window:
        second_window.destroy()
    second_window = None
