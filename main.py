from tkinter import *
import csv
import random


def generate_random_word():
    with open("data/french_words.csv", "r") as data_file:
        data_file_content = csv.reader(data_file)
        text = random.choice(list(data_file_content))
        if french_word != '':
            canvas.itemconfigure(french_word, text=f"{text[0]}")
        return text

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
icon = PhotoImage("images/France-Flag-icon.ico")
window.iconbitmap(icon)

with open("data/french_words.csv", "r") as data_file:
    content = csv.reader(data_file)
    french_word_text = random.choice(list(content))

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=my_image)
french = canvas.create_text(400, 150, text="French", font=("calibri", 40, "italic"))
french_word = canvas.create_text(400, 263, text=f"{french_word_text[0]}", font=("calibri", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button_image_wrong = PhotoImage(file="images/wrong.png")
button_image_right = PhotoImage(file="images/corect.png")
button_wrong = Button(image=button_image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word)
button_wrong.grid(row=1, column=0)
button_right = Button(image=button_image_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word)
button_right.grid(row=1, column=1)

window.mainloop()
