from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO

plt.rcParams['text.usetex'] = True

def make_formule(eqt, scrolled_text, fontsize):
    def render_latex(text):
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
        
        return ImageTk.PhotoImage(image)
    
    # Render and insert LaTeX text with specified fontsize
    latex_text = eqt
    latex_image = render_latex(latex_text)
    scrolled_text.config(state=NORMAL)
    scrolled_text.image_create(END, image=latex_image)
    scrolled_text.config(state=DISABLED)
    
    # Keep a reference to the image to prevent garbage collection
    scrolled_text.images.append(latex_image)


# Create a Tkinter window
root = Tk()
root.title("Scrolltext avec images")

# Create a scrolledtext widget
scrolled_text = scrolledtext.ScrolledText(root)
scrolled_text.pack(expand=True, fill=BOTH)

# Add a list to store images
scrolled_text.images = []

# Example equations
equations = [
    r'$\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$',
    r'$F(s)=\int_{0}^{\infty} e^{-st} f(t) dt$'
]

# Make images for each equation
for eq in equations:
    make_formule(eq, scrolled_text, fontsize=12)

root.mainloop()
