# Ce script est a éxécuter en première partie
# Ce script permet de lancer les 3.exe nécessaire au bon fonctionnement du jeu 
# Ce script permet donc de rendre la machine de l'utilisateur aux normes pour accueillir le projet jeu

import subprocess
from tkinter import *
from tkinter import scrolledtext


def installateur():
    #Installation du module git
    subprocess.run("Git-2.45.1-64-bit.exe", shell=True)

    # Installation de pytohn 3.12.3
    python_installer = "python-3.12.3-amd64.exe"
    subprocess.call(python_installer, shell=True)

    # Installation miktek : compilateur latex
    subprocess.run("basic-miktex-24.1-x64.exe", shell=True)

    # Installation visual c++ x64 : script c
    subprocess.run("VC_redist.x64.exe", shell=True)
    
def check():

    global btn
    if btn == False:
        Label_btn_lancer.config(state=NORMAL)
        btn = True
    else:
        Label_btn_lancer.config(state=DISABLED)
        btn = False

global btn 
btn = False



if __name__ == "__main__":



    f = Tk()
    f.title("Termes et conditions d'utilisation | Installation")



    Label_titre = Label(f, text="Math-Quest", fg = "#01548d", font=("Arial", 25))

    Label_titre.pack(pady=10)
    


    frame = Frame(f)
    frame.pack(expand=True, fill='both', padx=20, pady=20)
    
    scroll_text = scrolledtext.ScrolledText(frame, wrap=WORD, width=60, height=20, font=("Arial", 10))
    scroll_text.pack(expand=True, fill='both')

    text = """
            Termes et Conditions d'Utilisation

        Merci d'utiliser ce jeu Python Math-Quest, un projet créé avec passion pour l'amour des mathématiques et du partage de connaissances. Avant de continuer à utiliser ce logiciel, veuillez lire attentivement les conditions suivantes :

        1. Droit d'auteur : Ce jeu est protégé par les lois sur le droit d'auteur et est la propriété intellectuelle de LUBAN Théo & PLADEAU Quentin. Tous les droits qui ne sont pas expressément accordés dans ces conditions sont réservés.

        2. Utilisation personnelle : Ce jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.

        3. Règlementation française : En utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.

        4. Librairies open source : Ce jeu utilise des librairies open source telles que Python, Tkinter, Matplotlib, LaTeX, et d'autres. Nous reconnaissons et apprécions le travail des développeurs de ces librairies, et nous nous engageons à respecter les termes de leurs licences respectives. Les informations sur ces licences sont disponibles dans les fichiers correspondants du projet.
        
        5. Crédits : Nous tenons à remercier LUBAN Théo & PLADEAU Quentin pour leur contribution à ce projet. Leurs efforts ont été essentiels pour créer ce jeu. Nous apprécions également le soutien de ESCOUTE Cédric, qui a rendu ce projet possible.

        6. Cadre de réalisation : Ce jeu a été développé dans le cadre [du cours de NSI de première]. Nous sommes reconnaissants envers ESCOUTE Cédric pour son soutien et l'enseignement de connaissances ayant servie au projet.

        En utilisant ce jeu, vous acceptez ces termes et conditions. Si vous n'acceptez pas ces termes, veuillez ne pas utiliser ce logiciel. Ces termes et conditions peuvent être modifiés à tout moment sans préavis.

        Pour toute question ou préoccupation concernant ces termes et conditions, veuillez contacter votre enseignant vous ayant transmit une copie du projet.      
        """
    scroll_text.insert(END, text)


    Label_cases_coche = Checkbutton(f, command=check)
    Label_cases_coche.pack()


    Label_btn_lancer = Button(f, command=installateur, text="Installer")
    Label_btn_lancer.config(state=DISABLED)
    Label_btn_lancer.pack()


    f.mainloop()