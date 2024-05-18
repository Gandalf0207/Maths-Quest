import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()

# Création de la Frame
frame = tk.Frame(root)
frame.pack()

# Création d'une sous-Frame pour centrer les boutons horizontalement
button_frame = tk.Frame(frame)
button_frame.pack(anchor=tk.CENTER)

# Création des boutons et leur ajout à la sous-Frame
button1 = tk.Button(button_frame, text="Button 1")
button1.pack(side=tk.LEFT)

button2 = tk.Button(button_frame, text="Button 2")
button2.pack(side=tk.LEFT)

button3 = tk.Button(button_frame, text="Button 3")
button3.pack(side=tk.LEFT)

# Lancement de la boucle principale
root.mainloop()
