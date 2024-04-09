from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# Import Files
try:
    words = pandas.read_csv("data/to_learn.csv")
    words_dict = words.to_dict(orient="records")
    print("tolearn")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
    words_dict = words.to_dict(orient="records")
    print("normal")

try:
    french = list(words["French"])
    english = list(words["English"])
except KeyError:
    messagebox.askokcancel(title="No Data", message="Do you want to study from beginning?")
else:
    pass



# New Card
def next_card(is_known):
    if len(french) != 0:
        global flip_timer
        window.after_cancel(flip_timer)
        current_word = random.choice(french)
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_word, fill="black")
        canvas.itemconfig(side, image=card_front)
        flip_timer = window.after(3000, flip_card)
        if is_known:
            delete()


# Delete Card
def delete():
    english_word = english[french.index(canvas.itemcget(card_word, 'text'))]
    french_word = canvas.itemcget(card_word, 'text')
    if len(french) != 0:
        french.remove(french_word)
        english.remove(english_word)
        words_to_learn = []

        for word in french:
            english_word = english[french.index(word)]
            words_to_learn.append({
                "French": word,
                "English": english_word
            })
        create_new_file(words_to_learn)
        next_card(False)


# Create New File
def create_new_file(dict):
    new_data = pandas.DataFrame(dict)
    new_data.to_csv("data/to_learn.csv")


# Flip Card
def flip_card():
    translation = english[french.index(canvas.itemcget(card_word, 'text'))]
    canvas.itemconfig(side, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(card_word, text=translation, fill="white")


# Window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")


# Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
side = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=lambda:[next_card(False)])
wrong.grid(row=1, column=0)
right = Button(image=right_image, highlightthickness=0, borderwidth=0, command=lambda:[next_card(True)])
right.grid(row=1, column=1)

# Functions
flip_timer = window.after(3000, flip_card)
next_card(False)



window.mainloop()