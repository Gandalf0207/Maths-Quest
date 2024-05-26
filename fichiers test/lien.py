import tkinter as tk
from tkinter import scrolledtext
import webbrowser

def open_url(event):
    webbrowser.open_new(r"http://www.example.com")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple de ScrollText avec Lien Cliquable")

# Création du widget ScrolledText
scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
scroll_text.pack(padx=10, pady=10)

# Insertion de texte dans le widget ScrolledText
scroll_text.insert(tk.END, "Cliquez ici pour visiter Example.com")

# Marquage du texte pour le lien
start_index = "1.7"  # Position du début du lien dans le texte
end_index = "1.36"   # Position de la fin du lien dans le texte

# Application de la balise pour le lien
scroll_text.tag_add("link", start_index, end_index)
scroll_text.tag_config("link", foreground="blue", underline=1)
scroll_text.tag_bind("link", "<Enter>", lambda e: scroll_text.config(cursor="hand2"))
scroll_text.tag_bind("link", "<Leave>", lambda e: scroll_text.config(cursor=""))
scroll_text.tag_bind("link", "<Button-1>", open_url)

# Désactivation de l'édition pour éviter les modifications accidentelles
scroll_text.config(state=tk.DISABLED)

# Lancement de la boucle principale
root.mainloop()
