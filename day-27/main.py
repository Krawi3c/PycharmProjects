from tkinter import *
import playground


def button_clicked():
    my_label.config(text=user_input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=100)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "new_text"
my_label.config(text="new_text", padx=20, pady=100)
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

button = Button(text="Click Me 2", command=button_clicked)
button.grid(column=1, row=1)

user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
