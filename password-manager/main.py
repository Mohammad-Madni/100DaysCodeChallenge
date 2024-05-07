from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk("Welcome to Password Manager")
canvas = Canvas(height=200, width=200)
photo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=39)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"madnikorejo9@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons
generate_password_button = Button(text="Generate Password",)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add", width=34)
add_button.grid(row=4, column=1,columnspan=2)

window.config(pady=50, padx=50)
window.mainloop()
