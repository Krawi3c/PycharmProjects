from tkinter import *

window = Tk()

def create_new_routine(name):
    new = Label(text=name)
    new.grid(row=0, column=1)


window.mainloop()