BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

# --------------------------UI---------------------------
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)

bg_img = PhotoImage(file="images/card_back.png")
label = Label(image=bg_img)
label.grid(row=0,column=0)

#Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img,highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

window.mainloop()
