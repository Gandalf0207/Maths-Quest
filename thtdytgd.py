import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO

plt.rcParams['text.usetex'] = True

def render_latex(text, fontsize=10):
    # Create a matplotlib figure with a tight layout
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    
    # Render the LaTeX text with the specified fontsize
    ax.text(0.5, 0.5, text, fontsize=fontsize, ha='center', va='center', wrap=True)
    
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

def main():
    root = tk.Tk()
    root.title("Text with LaTeX")

    # Create a Text widget with a scrollbar
    text_widget = scrolledtext.ScrolledText(root, wrap='word')
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Insert normal text
    text_widget.insert(tk.END, "Voici du texte normal.\n\n")

    # Render and insert LaTeX text with font size 10
    latex_text = r"$\left\{ \begin{array}{lr} %sx + %sy & = %s \\ %sx - %sy & = %s \end{array} \right.$"%(1,2,3,4,5,6)
    latex_image = render_latex(latex_text, fontsize=10)
    text_widget.image_create(tk.END, image=latex_image)
    
    # Keep a reference to the image to prevent garbage collection
    text_widget.image = latex_image

    # Insert more text
    text_widget.insert(tk.END, "\n\nMerci beaucoup d'avoir joué à Maths-Quest !")
    text_widget.config(state=tk.DISABLED)
    root.mainloop()

if __name__ == "__main__":
    main()
