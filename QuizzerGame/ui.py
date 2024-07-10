from tkinter import *


THEME_COLOR = "#375362"
class QuizzerInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.question_label = self.Label(text=f"{}", bg="white", font=("arial", 20, "italic"))
        self.question_label.grid(column=1, row=1)


        


        self.window.mainloop()
