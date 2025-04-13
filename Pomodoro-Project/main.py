from tkinter import *
import math

# -------------------------- CONSTANTS ---------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# -------------------------- TIMER RESET --------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canva.itemconfig(time_filter, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if it's in 8th rep
        timer_label.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        # if it's in 2/4/6
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        #if it's in 1/3/5/7 reps
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    count_min = math.floor(time / 60)
    count_sec = time % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(time_filter, text=f"{count_min}:{count_sec}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        start_timer()
        marks = ""
        work_seasions = math.floor(reps / 2)
        for _ in range(work_seasions):
            marks += "✔"
        check_mark.config(text=marks)

# -------------------------- UI SETUP ----------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,)


timer_label = Label(text="Timer",bg=YELLOW, font=(FONT_NAME, 35, "bold"),fg=GREEN)
timer_label.grid(column=1, row=0)

canva = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(100,113, image= tomato_img)
time_filter = canva.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canva.grid(column=1,row=1)

button1 = Button(text="Start", highlightthickness=0,command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column= 1, row= 3)

window.mainloop()
