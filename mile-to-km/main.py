from tkinter import *

def clicked():
    miles = float(miles_input.get())
    km = miles*1.609344
    km_output.config(text=km)

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=300)

miles_input = Entry()

miles = Label(text="Miles")

equal = Label(text="is equal to")

km_output = Label(text=0)

km_text = Label(text="Kilometers")

calculate = Button(text="Calculate", command=clicked)

miles_input.grid(column=1, row=0)
miles.grid(column=2, row=0)
equal.grid(column=0, row=1)
km_output.grid(column=1, row=1)
km_text.grid(column=2, row=1)
calculate.grid(column=1, row=2)



window.mainloop()