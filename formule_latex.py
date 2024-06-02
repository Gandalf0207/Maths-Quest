#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################



# DEBUT formule_latex #



# Ce script permet de généré, à partir de formule latex, une image ayant l'affichage des formule 'jolie', ce qui est le but du latex

# Importation des modules nécessaire
from tkinter import * # Module de GUI
from tkinter import scrolledtext # Module de GUI
from PIL import Image, ImageTk # Module de gestion d'images
import matplotlib.pyplot as plt # Module mathématiques / graphiques
from io import BytesIO # Module de conversion des images

# Elément permetant, l'utilisation des dépendances latex, nécéssaires  à la création de ces images avec le bon affichage
plt.rcParams['text.usetex'] = True

#Fonction principal de gestion (appelé depuis le script principal)
def make_formule(eqt, label_de_la_box, fontsize, space): # Paramètres : la formules, l'endroit ou l'image doit etre ajoutée, la taille de police, si un retour à la ligne est nécéssaire 

    def render_latex(text): # Script généré par IA puis adapté, il permet la conversion en igmage de la taille de la formule le tout sans bords d'images
        
        # Create a matplotlib figure with a tight layout
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        
        # Render the LaTeX text with the specified fontsize
        ax.text(0, 0, text, fontsize=fontsize, ha='center', va='center', wrap=True)
        
        # Save the figure to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
        buf.seek(0)
        
        # Load the image from the BytesIO object
        image = Image.open(buf)
        
        # Crop the image to the bounding box of the content
        bbox = image.getbbox()
        image = image.crop(bbox)
        plt.close(fig) 
        
        return ImageTk.PhotoImage(image)

        
    # Render and insert LaTeX text with font size 10
    latex_text = eqt
    latex_image = render_latex(latex_text)

    label_de_la_box.config(state=NORMAL) # On rend la box accessible à l'écriture
    label_de_la_box.image_create(END, image=latex_image) # On écrit 
    if space==1: # Si des espace sont demandé , on en rajoute
        label_de_la_box.insert(END, "\n")
    elif space==2:
        label_de_la_box.insert(END, "\n\n")
    label_de_la_box.config(state=DISABLED) #On rend la box non modifiables par l'utilisateur 

    # Keep a reference to the image to prevent garbage collection
    label_de_la_box.images.append(latex_image)



# FIN formule_latex #



#############################################################################################################################

### MATHS-QUEST ###
# Pour toutes informations, veillez vous référer au dépot GitHub : https://github.com/Gandalf0207/Maths-Quest

# © Tous droits réservé 2024
#   PLADEAU Quentin & LUBAN Théo

############################################################################################################################