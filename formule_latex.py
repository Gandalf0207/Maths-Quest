from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO


plt.rcParams['text.usetex'] = True

def make_formule(eqt, label_de_la_box):
    def render_latex(text):
        # Create a matplotlib figure with a tight layout
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        fontsize=25
        
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
        
        return ImageTk.PhotoImage(image)

        
    # Render and insert LaTeX text with font size 10
    latex_text = eqt
    latex_image = render_latex(latex_text)
    label_de_la_box.config(state=NORMAL)
    label_de_la_box.image_create(END, image=latex_image)
    label_de_la_box.config(state=DISABLED)
    # Keep a reference to the image to prevent garbage collection
    label_de_la_box.image = latex_image




