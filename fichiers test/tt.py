from tkinter import *

def ajouter_element():
    element = entry.get().strip()
    if element:
        listbox.insert(END, element + "\n")
        entry.delete(0, END)

root = Tk()
root.title("Liste avec Scrollbar")

frame = Frame(root)
frame.pack(pady=10)

listbox = Text(frame, width=50, height=10, wrap="word")
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)

entry = Entry(root, width=50)
entry.pack()

ajouter_button = Button(root, text="Ajouter", command=ajouter_element)
ajouter_button.pack()

root.mainloop()
