import tkinter as tk

def supprimer_label():
    label.destroy()

# Créer une fenêtre tkinter
fenetre = tk.Tk()

# Créer un label text
label = tk.Label(fenetre, text="Label à supprimer")
label.pack()

# Créer un bouton pour supprimer le label
bouton_supprimer = tk.Button(fenetre, text="Supprimer le label", command=supprimer_label)
bouton_supprimer.pack()

# Lancer la boucle principale de la fenêtre tkinter
fenetre.mainloop()
