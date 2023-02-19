from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file="images\card_front.png")
canvas.create_image(400, 263, image=my_image)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

button_image_wrong = PhotoImage(file="images\wrong.png")
button_image_right = PhotoImage(file="images\corect.png")
button_wrong = Button(image=button_image_wrong, highlightthickness=0)
button_wrong.grid(row=2, column=0)
button_right = Button(image=button_image_right, highlightthickness=0)
button_right.grid(row=2, column=1)

window.mainloop()
