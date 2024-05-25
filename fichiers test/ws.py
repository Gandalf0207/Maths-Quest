import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

# Créer la frame qui peut changer de taille
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Créer le widget ScrolledText avec des dimensions initiales
scrolled_text = ScrolledText(frame, width=50, height=50)
scrolled_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
