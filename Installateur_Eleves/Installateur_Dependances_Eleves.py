#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

#############################################################################################################################



# DEBUT Installeur_Dependances_Eleves # 



# Ce script est a éxécuter en seconde partie. Ce script est utilisé uniquement par les déteneurs du dossier élèves du projet.
# Ce script installe, toutes les dépendances nécéssaire au bon fonctionnement du jeu.

# Importation des modules nécessaire
import subprocess # Module de gestion 
from tkinter import * # Module de GUI
from tkinter import scrolledtext # Module de GUI


# Fonction d'installation 
def installateur():
    # Récupérer le jeu sur github
    subprocess.run("git clone https://github.com/Gandalf0207/Maths-Quest.git", shell=True, text=True)

    # Installer pip.
    subprocess.run(["python", "-m", "ensurepip"], shell=True)
    # Installer les bibliothèques requises
    subprocess.run(["pip", "install", "matplotlib"], shell=True)

    # Installer dépendances Latex nécéssaires
    subprocess.run(["mpm", "--install", "type1cm"], shell=True)
    subprocess.run(["mpm", "--install", "cm-super"], shell=True)
    subprocess.run(["mpm", "--install", "geometry"], shell=True)
    subprocess.run(["mpm", "--install", "underscore"], shell=True)
    subprocess.run(["mpm", "--install", "zhmetrics"], shell=True)


# Fonction de vérification d'acceptation des Termes et Consignes d'utilisation
def check():
    global btn
    if btn == False:
        Label_btn_lancer.config(state=NORMAL) # Bouton cliquable
        btn = True
    else:
        Label_btn_lancer.config(state=DISABLED) # Bouton non cliquable
        btn = False

# Set de la valeur initiale du bouton (non cliquable)
global btn 
btn = False


# Lancement de la fenêtre principal du script
if __name__ == "__main__":

    f = Tk() # Initialisation de la fenêtre
    f.title("Maths-Quest | Termes et conditions d'utilisation      © PLADEAU Quentin LUBAN Théo") # Titre (haut) de la fenêtre

    Label_titre = Label(f, text="Maths-Quest", fg = "#01548d", font=("Arial", 25)) # Titre principal de la fenetre
    Label_titre.pack(pady=10)
    
    frame = Frame(f) # Bloc frame qui contient tout les éléments
    frame.pack(expand=True, fill='both', padx=20, pady=20)
    
    scroll_text = scrolledtext.ScrolledText(frame, wrap=WORD, width=60, height=20, font=("Arial", 10)) # Boite où sont affichés les les Termes et consignes d'utilisation
    scroll_text.pack(expand=True, fill='both')

    # Consignes et Termes d'utilisation
    text = """
                Termes et Conditions d'Utilisation

            Merci d'utiliser ce jeu Python Maths-Quest, un projet créé avec passion pour l'amour des mathématiques et du partage de connaissances. Avant de continuer à utiliser ce logiciel, veuillez lire attentivement les conditions suivantes :

            1. Droit d'auteur : Ce jeu est protégé par les lois sur le droit d'auteur et est la propriété intellectuelle de LUBAN Théo & PLADEAU Quentin. Tous les droits qui ne sont pas expressément accordés dans ces conditions sont réservés.

            2. Utilisation personnelle : Ce jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.

            3. Règlementation française : En utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.

            4. Librairies open source : Ce jeu utilise des librairies open source telles que Python, Tkinter, Matplotlib, LaTeX, et d'autres. Nous reconnaissons et apprécions le travail des développeurs de ces librairies, et nous nous engageons à respecter les termes de leurs licences respectives. Les informations sur ces licences sont disponibles dans les fichiers correspondants du projet.
            
            5. Crédits : Nous tenons à remercier LUBAN Théo & PLADEAU Quentin pour leur contribution à ce projet. Leurs efforts ont été essentiels pour créer ce jeu. Nous apprécions également le soutien de ESCOUTE Cédric, qui a rendu ce projet possible.

            6. Cadre de réalisation : Ce jeu a été développé dans le cadre du cours de NSI de première. Nous sommes reconnaissants envers ESCOUTE Cédric pour son soutien et l'enseignement de connaissances ayant servie au projet.

            En utilisant ce jeu, vous acceptez ces termes et conditions. Si vous n'acceptez pas ces termes, veuillez ne pas utiliser ce logiciel. Ces termes et conditions peuvent être modifiés à tout moment sans préavis.

            Pour toute question ou préoccupation concernant ces termes et conditions, veuillez contacter votre enseignant vous ayant transmit une copie du projet ou bien vous référer à la liscence disponible sur le dépots GitHub du projet : https://github.com/Gandalf0207/Maths-Quest .      
            
    © Tous droits réservé 2024
    PLADEAU Quentin & LUBAN Théo

    """
    scroll_text.insert(END, text) # Insertion des Consignes et Termes d'utilisation dans la boite 

    Label_cases_coche = Checkbutton(f, command=check) # Case avec érification d'acceptation de ces Termes et Consignes d'utilisation
    Label_cases_coche.pack()


    Label_btn_lancer = Button(f, command=installateur, text="Installer") # Bouton permetant l'execution du script d'installation
    Label_btn_lancer.config(state=DISABLED) # Set initial du bouton (non cliquable)
    Label_btn_lancer.pack()


    f.mainloop() # Loop de lafenêtre pour la faire fonctionner



# FIN Installeur_Dependances_Eleves # 


#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

#############################################################################################################################