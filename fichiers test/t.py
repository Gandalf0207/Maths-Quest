import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application principale")
        
        self.bind("<KeyPress-a>", self.open_second_window)  # Lie l'appui sur la touche "a" à la fonction open_second_window
        
        self.second_window_opened = False  # Variable pour suivre l'état de la deuxième fenêtre
        
    def open_second_window(self, event=None):
        if not self.second_window_opened:  # Vérifie si la deuxième fenêtre est déjà ouverte
            self.second_window = SecondWindow(self)
            self.second_window_opened = True

class SecondWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Deuxième fenêtre")

        self.protocol("WM_DELETE_WINDOW", self.on_close)  # Gère la fermeture de la fenêtre via la croix en haut à droite
        
        self.label = tk.Label(self, text="Deuxième fenêtre ouverte")
        self.label.pack(padx=20, pady=20)

    def on_close(self):
        self.master.second_window_opened = False
        self.destroy()  # Détruit la fenêtre lorsque l'événement WM_DELETE_WINDOW est déclenché

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
