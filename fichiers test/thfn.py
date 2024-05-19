from tkinter import *

def ac():
    if intt.get() == 1:
        inttt.set(0)
    elif inttt.get() == 1:
        intt.set(0)

j = Tk()

intt = IntVar()
b = Checkbutton(j, text="aaa", variable=intt, command=ac)
b.pack()

inttt = IntVar()
c = Checkbutton(j, text="aaa", variable=inttt, command=ac)
c.pack()

j.mainloop()
