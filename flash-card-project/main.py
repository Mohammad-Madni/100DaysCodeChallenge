from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
learn = data.to_dict(orient="records")


def nextcard():
    current_choice = random.choice(learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_choice["French"])

# --------------------------UI---------------------------


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=nextcard)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=nextcard)
right_button.grid(row=1, column=1)

nextcard()

window.mainloop()
