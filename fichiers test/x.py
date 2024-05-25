import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.title("Texte défilant avec différentes polices")

# Cadre contenant le canvas et la scrollbar
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Canvas pour le texte défilant
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Scrollbar verticale
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configuration de la scrollbar pour le canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Cadre interne pour contenir le widget Text
text_frame = tk.Frame(canvas)
canvas.create_window((0,0), window=text_frame, anchor='nw')

# Widget Text
text_widget = tk.Text(text_frame, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=1)




# Ajout de texte avec différentes polices
normal_font = ('Arial', 12)
italic_font = ('Arial', 12, 'italic')

text_widget.insert(tk.END, "Texte en police normale.\n", 'normal')
text_widget.insert(tk.END, "Texte en police italique.\n", 'italic')

# Configuration des tags de police
text_widget.tag_configure('normal', font=normal_font)
text_widget.tag_configure('italic', font=italic_font)

# Configuration du canvas pour s'adapter aux modifications du widget Text
# text_frame.bind('<Configure>', on_configure)

# # Déplacement du canvas pour suivre le texte
# text_widget.bind('<1>', lambda event: canvas.bind_all('<MouseWheel>', on_mouse_wheel))
# text_widget.bind('<Leave>', lambda event: canvas.unbind_all('<MouseWheel>'))

# def on_mouse_wheel(event):
#     canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root.mainloop()
