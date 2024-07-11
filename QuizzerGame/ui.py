from tkinter import *


THEME_COLOR = "#375362"
class QuizzerInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        
        canvas = Canvas(width=300, height=250)
        canvas.create_text(text="",font=("Arial", 20, "italic"),fill="white")
        canvas.grid(row=1,column=1)


        false_image = PhotoImage(file="images/false.png")





        self.window.mainloop()
