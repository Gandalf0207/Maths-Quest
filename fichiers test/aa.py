from tkinter import *

def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=400, height=600, background='white')
    frame.pack_propagate(0)    
    frame.pack()
    img = PhotoImage(file='image/arbre.png')
    make_label(frame, img)

    root.mainloop()