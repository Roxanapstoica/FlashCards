import pandas
from tkinter import *
import random
import os

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(french_image, image=card_front_img)
    canvas.itemconfigure(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(french_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    global finish
    try:
        to_learn.remove(current_card)
        print(len(to_learn))
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    except IndexError:
        canvas.itemconfigure(card_title, text="Congratulations!", fill="black")
        canvas.itemconfig(card_word, text="You have learned all the words!", fill="black", font=("calibri", 30, "bold"))
        button_wrong.destroy()
        button_right.destroy()
        os.remove("data/words_to_learn.csv")

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
icon = PhotoImage("images/France-Flag-icon.ico")
window.iconbitmap(icon)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
french_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("calibri", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("calibri", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

next_card()

button_image_wrong = PhotoImage(file="images/wrong.png")
button_image_right = PhotoImage(file="images/corect.png")
button_image_exit = PhotoImage(file="images/exit.png")

button_wrong = Button(image=button_image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(row=1, column=0)
button_right = Button(image=button_image_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
button_right.grid(row=1, column=1)
# button_exit = Button(image=button_image_exit, highlightthickness=0, bg=BACKGROUND_COLOR, command=quit)
# button_exit.grid(row=1, column=2)

window.mainloop()
