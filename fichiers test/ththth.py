import tkinter as tk
from tkinter import messagebox

def on_closing():
    # Cette fonction sera appelée lorsque l'utilisateur appuie sur la croix de la fenêtre
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
        # Si l'utilisateur confirme, nous fermons la fenêtre
        root.destroy()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Exemple de fermeture")

# Configurer la taille de la fenêtre
root.geometry("300x200")

# Associer la fonction de fermeture à l'événement de clic sur la croix
root.protocol("WM_DELETE_WINDOW", on_closing)

# Lancer la boucle principale de l'interface Tkinter
root.mainloop()
