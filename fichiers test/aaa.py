import tkinter as tk
from tkinter import scrolledtext

class TermsAndConditionsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Terms and Conditions")
        
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.scroll_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
        self.scroll_text.pack(expand=True, fill='both')
        
        self.add_text()

    def add_text(self):
        text = """
        **Termes et Conditions d'Utilisation**

        Merci d'utiliser ce jeu Python, un projet créé avec passion pour l'amour des mathématiques et du partage de connaissances. Avant de continuer à utiliser ce logiciel, veuillez lire attentivement les conditions suivantes :

        1. {bold}Droit d'auteur :{\bold} Ce jeu est protégé par les lois sur le droit d'auteur et est la propriété intellectuelle de [Ton Nom / Nom du Projet]. Tous les droits qui ne sont pas expressément accordés dans ces conditions sont réservés.

        2. {bold}Utilisation personnelle :{bold} Ce jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.

        3. {bold}Règlementation française :{bold} En utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.

        4. {bold}Librairies open source :{bold} Ce jeu utilise des librairies open source telles que Python, Tkinter, Matplotlib, LaTeX, et d'autres. Nous reconnaissons et apprécions le travail des développeurs de ces librairies, et nous nous engageons à respecter les termes de leurs licences respectives. Les informations sur ces licences sont disponibles dans les fichiers correspondants du projet.

        5. {bold}Crédits :{bold} Nous tenons à remercier [Liste des contributeurs / Collaborateurs] pour leur contribution à ce projet. Leurs efforts ont été essentiels pour créer ce jeu. Nous apprécions également le soutien de [Organisation / Sponsor], qui a rendu ce projet possible.

        6. {bold}Cadre de réalisation :{bold} Ce jeu a été développé dans le cadre de [Description du cadre de réalisation du projet]. Nous sommes reconnaissants envers [Organisation / Institution] pour son soutien financier / logistique / académique / autre.

        En utilisant ce jeu, vous acceptez ces termes et conditions. Si vous n'acceptez pas ces termes, veuillez ne pas utiliser ce logiciel. Ces termes et conditions peuvent être modifiés à tout moment sans préavis.

        Pour toute question ou préoccupation concernant ces termes et conditions, veuillez nous contacter à [adresse e-mail de contact].
        """
        self.scroll_text.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TermsAndConditionsWindow(root)
    root.mainloop()
