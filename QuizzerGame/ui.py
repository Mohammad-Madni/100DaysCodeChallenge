from tkinter import *


THEME_COLOR = "#375362"
class QuizzerInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score = 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)


        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="some question text",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0, columnspan=2, pady= 50)

        false_image = PhotoImage(file="images/false.png")
        self.

        true_image = PhotoImage(file="images/true.png")





        self.window.mainloop()
