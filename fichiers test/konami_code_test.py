import tkinter as tk

# Initialiser la fenêtre principale
root = tk.Tk()
root.title("Konami Code Example")

# La séquence de touches pour le code 'admin'
konami_code = ['a', 'd', 'm', 'i', 'n']
current_input = []

def check_konami_code(event):
    # Ajouter la touche pressée à la séquence actuelle
    current_input.append(event.char)
    
    # Vérifier si la séquence actuelle dépasse la longueur du Konami Code
    if len(current_input) > len(konami_code):
        current_input.pop(0)
    
    # Vérifier si la séquence actuelle correspond au Konami Code
    if current_input == konami_code:
        open_new_window()

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="Vous avez entré le Konami Code 'admin'!")
    label.pack(pady=20, padx=20)

# Bind the key press event to the check_konami_code function
root.bind("<Key>", check_konami_code)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
