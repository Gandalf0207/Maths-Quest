import tkinter as tk
 
fenetre = tk.Tk()
 
##Création du canva
canva = tk.Canvas(fenetre, width=100, height=100, bg='red')
canva.pack()
 
## Création du bouton
button1 = tk.Button(canva, text='Testing', bg='blue')
 
## Insertion du bouton dans le canva.
canva.create_window(50, 50, window=button1)
 
fenetre.mainloop()