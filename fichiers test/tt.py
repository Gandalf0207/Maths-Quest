import tkinter as tk
from tkinter import Scrollbar

def ajouter_element():
    element = entry.get().strip()
    if element:
        listbox.insert(tk.END, element + "\n")
        entry.delete(0, tk.END)

def effacer_liste():
    listbox.delete(1.0, tk.END)

root = tk.Tk()
root.title("Liste avec Scrollbar")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Text(frame, width=50, height=10, wrap="word")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=50)
entry.pack()

ajouter_button = tk.Button(root, text="Ajouter", command=ajouter_element)
ajouter_button.pack()

clear_button = tk.Button(root, text="Effacer la liste", command=effacer_liste)
clear_button.pack()

root.mainloop()
