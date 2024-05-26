import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO

plt.rcParams['text.usetex'] = True

# LaTeX rendering function
def make_formule(eqt, label_de_la_box, fontsize):
    def render_latex(text):
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        
        ax.text(0, 0, text, fontsize=fontsize, ha='center', va='center', wrap=True)
        
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
        buf.seek(0)
        
        image = Image.open(buf)
        bbox = image.getbbox()
        image = image.crop(bbox)
        
        return ImageTk.PhotoImage(image)

    latex_text = eqt
    latex_image = render_latex(latex_text)
    label_de_la_box.config(state=tk.NORMAL)
    label_de_la_box.image_create(tk.END, image=latex_image)
    label_de_la_box.insert(tk.END, "\n\n")  # Ajoutez deux retours à la ligne ici
    label_de_la_box.config(state=tk.DISABLED)
    label_de_la_box.images.append(latex_image)

# Function to add elements to the scrolled text box
def ajouter_element(Texte):
    global listbox
    element = Texte.strip()
    listbox.config(state=tk.NORMAL)
    if element:
        listbox.insert(tk.END, element)

# Function to insert two new lines
def saut_2_lignes():
    global listbox
    listbox.insert(tk.END, "\n")
    listbox.insert(tk.END, "\n")

# Main part of the code
if __name__ == "__main__":
    # Initialize the main window
    root = tk.Tk()
    root.title("Cours")

    # Create a scrolled text widget
    listbox = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
    listbox.pack(padx=10, pady=10)

    # Adding an images attribute to keep references to images
    listbox.images = []

    # Define the list of courses
    Liste_cours = [
        "De façon intuitive, une égalité fonctionne un peu comme une balance à deux plateaux \u2696 : si on effectue une opération d'un côté, il faut réaliser la même opération de l'autre côté pour garder l'équilibre.",
        "Quelques propriétés : On peut ajouter (ou soustraire) un même nombre aux deux membres d'une égalité. \n a = b équivaut à a + c = b + c \n a = b  équivaut à a - c = b - c \n On peut multiplier (ou diviser) les deux membres d'une égalité par un même nombre non nul. \n a = b équivaut à a × c = b × c \n a = b équivaut à   a/c = b/c(c ≠ 0) \n Exemple :  \n 5x + 2 = 17 \n 5x + 2 - 2 = 17 - 2 \n 5x/5 = 15/5 \n x = 3",
        "Si il y a des x dans les deux membres de l’équation il faut tout mettre dans le même. Exemple : \n 3x + 2 = 5x + 3 \n équivaut à  3x + 2 - 5x = 5x + 3 - 5x \n équivaut à  -2x + 2 = 3 \n et ainsi de suite", 
        "La formule de l’aire de la base d’un disque qui est π x rayon², l’aire d’un triangle est ", 
        " et celle d’un carré ou d’un rectangle est longueur x largeur. Vidéo explicative de pi ici",
        "Le volume du cylindre est : base x hauteur soit π x rayon² x h. De manière plus générale une multitude de volume se calcule simplement par base x hauteur.",
        "Le volume du cône est celui du cylindre divisé par 3 soit ", 
        ". Le volume d’une pyramide est celui du prisme droit que l’on divise par 3 soit",
        "La formule pour calculer le volume d’un sphère est ",
        "Une droite se présente sous la forme mx + p, avec m en tant que coefficient directeur et p l’ordonné à l’origine.",
        "Les droites parallèles à l’axe des ordonnées (“droite verticale”) ont une équation de la forme x=c avec c un nombre par exemple x = 2 est une droite verticale qui passe par l’abscisse 2.",
        "Dans une équation sous forme mx + p, passant par les points A(xA;yA) et B(xB;yB), p est l’ordonnée à l’origine pour trouver p, on utilise les coordonnées d’un point de la droite par exemple avec le point A(xA; yA), on a p = yA - m.xA et pour trouver m on a",
        "Une fonction affine admet une expression algébrique de la forme f(x) = mx + p et sa représentation graphique est une droite. [Ptet image de droite du coup]",
        "Pour trouver le point d’intersection de 2 droites il faut trouver quand l’équation réduite 1 est égale à l’équation réduite 2 soit mx + p = m’x + p",
        "Il y a 2 manières pour résoudre un système à doubles inconnues, la fin est la même mais la réflexion n’est pas la même, il y a donc la résolution par substitution et la résolution par combinaisons linéaires.",
        "La méthode de substitution consiste à isoler une des variables dans l'une des équations et à substituer cette expression dans l'autre équation. Cela permet de réduire le système à une seule équation avec une seule inconnue, qui peut alors être résolue.",
        "Exemple de résolution par substitution :",
        "1. Isoler une variable : \n    y = 5 - x \n2. Substituer : \n    2x - (5 - x) = 1  \n3. Résoudre : \n    2x - 5 + x = 1  \n    3x - 5 = 1 \n    3x = 6 \n    x = 2 \n4. Remplacer et résoudre : \n    y = 5 - 2 = 3  \nSolution \n    x = 2, y = 3",
        "La méthode de combinaisons linéaires consiste à manipuler les équations pour éliminer l'une des variables. Cette manipulation se fait généralement en multipliant les équations par des coefficients appropriés afin d'obtenir des coefficients opposés pour une des variables, puis en additionnant ou soustrayant les équations.",
        "Exemple de résolution par combinaison linéaire :",
        "1. Additionner les deux équations pour éliminer y  : \n (2x + y) + (3x - y) = 5 + 4 \n 2x + 3x + y - y = 9 \n 5x = 9 \n x = 9/5 \n 2. Substituer x dans la première équation pour trouver y  : \n 2*(9/5) + y = 5 \n 18/5 + y = 5 \n y = 5 - 18/5 \n y = 25/5 - 18/5 \n y = 7/5 \n Solution \n x = 9/5, y = 7/5", 
        "cours 1 nv5",
        "cours 2 nv5",
        "cours 3 nv5",
        "cours 1 nv6",
        "cours 2 nv6",
        "cours 3 nv6",
        "cours 4 nv6", 
        "cours 1 nv7",
        "cours 2 nv7",
        "cours 3 nv7",
        "cours 4 nv7",
        "cours 5 nv7"
    ]

    # Sample level and PNJ numbers to demonstrate functionality
    Niveau = 3
    num_pnj = "pnj3"

    if Niveau == 3:
        if num_pnj == "pnj1":
            ajouter_element(Liste_cours[14])
            saut_2_lignes()
        elif num_pnj == "pnj2":
            ajouter_element(Liste_cours[15])
            saut_2_lignes()
        elif num_pnj == "pnj3":
            ajouter_element(Liste_cours[16])
            listbox.insert(tk.END, "\n")
            make_formule(r"$\left\{ \begin{array}{lr} x + y & = 5 \\ 2x - y & = 1 \end{array} \right.$", listbox, 11)
            listbox.insert(tk.END, "\n\n")  # Ajoutez deux retours à la ligne ici
            ajouter_element(Liste_cours[17])
            saut_2_lignes()

    listbox.config(state=tk.DISABLED)

    # Run the main loop
    root.mainloop()
