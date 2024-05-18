import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Vos coordonnées de points (x, y)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Créez une fenêtre Tkinter
root = tk.Tk()

# Créez un canvas Tkinter pour afficher le graphique
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Créez un graphique Matplotlib
fig, ax = plt.subplots()  # Ajoutez "ax" ici
for x, y in points:
    ax.scatter(x, y, color='blue', marker='o', label=f"({x}, {y})")
    ax.text(x, y, f"({x}, {y})", ha='center', va='bottom')  # Ajoutez l'étiquette

# Supprimez les axes
ax.axis('off')  # Ajoutez cette ligne pour masquer les axes

# Affichez le graphique dans le canvas Tkinter
canvas_widget = FigureCanvasTkAgg(fig, master=canvas)
canvas_widget.draw()
canvas_widget.get_tk_widget().pack()

# Exécutez la boucle principale Tkinter
root.mainloop()
