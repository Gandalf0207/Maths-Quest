import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Styles Prédéfinis et Personnalisés')

        # Créez un bouton sans spécifier de style (utilisera le style prédéfini TButton)
        ttk.Button(self, text='Bouton par défaut').pack(pady=10)

        # Créez un style personnalisé
        self.style = ttk.Style(self)
        self.style.configure('MyCustom.TButton', font=('Helvetica', 12), foreground='red')

        # Créez un bouton avec le style personnalisé
        ttk.Button(self, text='Mon Bouton Personnalisé', style='MyCustom.TButton').pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
