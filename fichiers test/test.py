import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import random

def afficher_formule_math():
    nb1 = random.randint(2, 20)
    nb2 = random.randint(2, 20)
    nb3 = random.randint(2, 20)
    nb4 = random.randint(2, 20)

    # Formater la formule avec les nombres aléatoires
    formule = r'$\Leftrightarrow %sx - %s = %s + %sx$' % (nb1, nb2, nb3, nb4)

    # Créer une figure matplotlib sans légendes et sans box
    fig = Figure(figsize=(5, 2), dpi=100, frameon=False)  # Taille initiale de la figure sans boîte englobante
    # Ajouter un sous-graphique
    ax = fig.add_subplot(111)
    # Supprimer les légendes et la boîte englobante
    ax.axis('off')
    # Ajouter la formule mathématique
    ax.text(0.5, 0.5, formule, fontsize=20, ha='center')
    # Obtenir les limites de la boîte englobante de la formule
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    # Redimensionner la figure en fonction de la taille de la formule
    fig.set_size_inches(5, bbox.height)
    # Créer un canvas Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    # Afficher le canvas
    canvas.get_tk_widget().pack(padx=5, pady=5)
    
    
# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Affichage d'une formule mathématique")

# Ajouter un bouton pour afficher la formule mathématique
btn_afficher = tk.Button(window, text="Afficher la formule mathématique", command=afficher_formule_math)
btn_afficher.pack()

# Lancer la boucle principale Tkinter
window.mainloop()
