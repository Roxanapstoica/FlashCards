import pandas
from tkinter import *
import random


def generate_random_word():
    # random_dict = list_data[random.randint(0, len(list_data)-1)]

    random_dict = random.choice(list_data)

    random_french_word = random_dict['French']
    global title_english
    title_english = list(random_dict.keys())[1]
    global translation
    translation = random_dict['English']
    canvas.itemconfig(french_image, image=my_image)
    canvas.itemconfigure(card_title, text=f"{list(random_dict.keys())[0]}", fill="black")
    canvas.itemconfig(card_word, text=f"{random_french_word}", fill="black")
    # print(translation)

    return list(random_dict.keys())[0], random_french_word, list(random_dict.keys())[1], translation

def flip_card():
    # title = generate_random_word()[2]
    # word = generate_random_word()[3]
    canvas.itemconfig(french_image, image=new_image)
    canvas.itemconfig(card_title, text=f"{title_english}", fill="white")
    canvas.itemconfig(card_word, text=f"{translation}", fill="white")
    global flip
    flip = window.after(3000, flip_card)


data = pandas.read_csv("data/french_words.csv")
list_data = data.to_dict(orient="records")
# print(list_data)

# title_english = ''
# translation = ''

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
icon = PhotoImage("images/France-Flag-icon.ico")
window.iconbitmap(icon)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
french_image = canvas.create_image(400, 263, image=my_image)
card_title = canvas.create_text(400, 150, text="", font=("calibri", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("calibri", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

generate_random_word()

button_image_wrong = PhotoImage(file="images/wrong.png")
button_image_right = PhotoImage(file="images/corect.png")
button_wrong = Button(image=button_image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word)
button_wrong.grid(row=1, column=0)
button_right = Button(image=button_image_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word)
button_right.grid(row=1, column=1)

flip = window.after(3000, flip_card)

window.mainloop()
