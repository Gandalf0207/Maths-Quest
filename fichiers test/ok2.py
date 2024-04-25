from tkinter import *
from tkinter import ttk

def set_default_theme():
    style.theme_use("default")

def set_custom_theme():
    style.theme_use("mytheme")

Jeu = Tk()
Jeu.geometry("350x400")
Jeu.title("RPG Théo | Quentin")

Frame = ttk.Frame(Jeu)

style = ttk.Style()
style.theme_create("mytheme")
# Configurez le thème par défaut
style.theme_settings("mytheme", {
    "TButton": {
        "configure": {"padding": 10},
        "map": {
            "background": [("active", "#2C7BF2"), ("!disabled", "#ACB2F4")],
            "foreground": [("focus", "#090B15"), ("!disabled", "#090B15")],
        },
    },
    "TLabel": {"foreground": {"color": "#BA3FAF"}},
})

# Créez les boutons
btn_default = ttk.Button(Frame, text="Thème par défaut", command=set_default_theme)
btn_custom = ttk.Button(Frame, text="Thème personnalisé", command=set_custom_theme)
label_test = ttk.Label(Frame, text="ok test")

label_test.pack(pady=20)
btn_default.pack(pady=20)
btn_custom.pack(pady=60)

Frame.pack()

Jeu.mainloop()



# style.theme_create("mytheme")





# style.theme_use("mytheme", "default")

# style.theme_settings("mytheme", {
#     "TButton" : {
#             "configure" : { "padding" : 10},
#             "map" : {
#                 "background" : [("active", "#2C7BF2"),
#                                 ("!disabled", "#ACB2F4")],
#                 "foreground" : [("focus" , "#090B15"),
#                                 ("!disabled", "#090B15")]
#                     }
#                 },

#     "TLabel" : {
#             "foreground" : {"color" : "#BA3FAF"}
#                 }
#     }
# )
