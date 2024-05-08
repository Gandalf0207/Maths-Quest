import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

# Fonction pour générer aléatoirement les coefficients des droites
def generate_random_coeffs():
    a1, b1 = random.randint(-10, 10), random.randint(-10, 10)
    a2, b2 = random.randint(-10, 10), random.randint(-10, 10)
    return a1, b1, a2, b2

# Fonction pour calculer l'intersection des droites
def calculate_intersection(a1, b1, a2, b2):
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Intersection de deux droites")

# Génération aléatoire des coefficients des droites et calcul de l'intersection
a1, b1, a2, b2 = generate_random_coeffs()
x_intersect, y_intersect = calculate_intersection(a1, b1, a2, b2)

# Création d'une figure Matplotlib
fig, ax = plt.subplots()
x_values = range(-10, 11)
y1_values = [a1 * x + b1 for x in x_values]
y2_values = [a2 * x + b2 for x in x_values]
ax.plot(x_values, y1_values, label=f"Droite 1: y = {a1}x + {b1}")
ax.plot(x_values, y2_values, label=f"Droite 2: y = {a2}x + {b2}")
ax.scatter(x_intersect, y_intersect, color='red', label=f'Intersection: ({x_intersect:.2f}, {y_intersect:.2f})')
ax.legend()

# Création d'un canvas Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Boucle principale Tkinter
tk.mainloop()
