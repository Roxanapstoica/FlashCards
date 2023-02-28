import pandas
from tkinter import *
import random


def generate_random_word():
    word = list_data[random.randint(0, len(list_data)-1)]['French']
    canvas.itemconfig(french_word, text=f"{word}")
    print(word)
    return word


data = pandas.read_csv("data/french_words.csv")
list_data = data.to_dict(orient="records")
first_french_word = list_data[random.randint(0, len(list_data)-1)]['French']

print(list_data)
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
icon = PhotoImage("images/France-Flag-icon.ico")
window.iconbitmap(icon)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=my_image)
french = canvas.create_text(400, 150, text="French", font=("calibri", 40, "italic"))
french_word = canvas.create_text(400, 263, text=f"{first_french_word}", font=("calibri", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button_image_wrong = PhotoImage(file="images/wrong.png")
button_image_right = PhotoImage(file="images/corect.png")
button_wrong = Button(image=button_image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word)
button_wrong.grid(row=1, column=0)
button_right = Button(image=button_image_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word)
button_right.grid(row=1, column=1)

window.mainloop()
