import tkinter as tk
import time

def afficher_progressivement(texte_complet):
    for i in range(len(texte_complet)):
        texte_partiel = texte_complet[:i+1]
        label.configure(text=texte_partiel)
        fenetre.update()
        time.sleep(0.1)  # Attente de 100 millisecondes entre chaque caractère

fenetre = tk.Tk()
fenetre.geometry('300x100')

texte_initial = "Bienvenue sur WayToLearnX !"
label = tk.Label(fenetre, text=texte_initial)
label.pack(pady=20)

# Remplacez le texte ci-dessous par ce que vous souhaitez afficher progressivement
texte_cible = "Voici un exemple de texte progressif."

bouton = tk.Button(fenetre, text="Afficher progressivement", command=lambda: afficher_progressivement(texte_cible))
bouton.pack()

fenetre.mainloop()
