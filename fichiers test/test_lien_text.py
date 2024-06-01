import tkinter as tk
from tkinter import Toplevel, font

def ouvrir_fenetre():
    nouvelle_fenetre = Toplevel(root)
    nouvelle_fenetre.title("Nouvelle Fenêtre")
    Label_check_button_conditon = tk.Label(nouvelle_fenetre, text="Ceci est une nouvelle fenêtre")
    Label_check_button_conditon.pack()

def surligne(event):
    Label_check_button_conditon.config(font=(label_font_family, label_font_size, "underline"))

def desurligne(event):
    Label_check_button_conditon.config(font=(label_font_family, label_font_size))

root = tk.Tk()
root.title("Fenêtre Principale")

# Récupérer la police par défaut du Label_check_button_conditon
label_font = tk.font.nametofont("TkDefaultFont")
label_font_family = label_font.actual()["family"]
label_font_size = label_font.actual()["size"]

Label_check_button_conditon = tk.Label(root, text="Cliquez ici pour ouvrir une nouvelle fenêtre", fg="blue", cursor="hand2")
Label_check_button_conditon.pack(pady=20)

Label_check_button_conditon.bind("<Button-1>", lambda e: ouvrir_fenetre())
Label_check_button_conditon.bind("<Enter>", surligne)
Label_check_button_conditon.bind("<Leave>", desurligne)

root.mainloop()
