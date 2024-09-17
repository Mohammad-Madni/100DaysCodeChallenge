#import Modules
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


#Connection


#GUI

root = Tk()
root.title("Student Management System")
root.geometry("1080x720")
mt_tree = ttk.Treeview(root)

#Function

#GUI
label = Label(root,text="Student Management System (CRUD MATRIX)",font=("Arial Bold",30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

studidlabel = Label(root,text="Student ID",font=("Arial",15))
fnamelabel = Label(root,text="First Name",font=("Arial",15))
lnamelabel = Label(root,text="Last Name",font=("Arial",15))
phonelabel = Label(root,text="Phone",font=("Arial",15))
addresslabel = Label(root,text="Address",font=("Arial",15))

studidlabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
fnamelabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
lnamelabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
phonelabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
addresslabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

studidEntry = Entry(root,width=55,bd=5,font=("Arial",15))
fnameEntry = Entry(root,width=55,bd=5,font=("Arial",15))
lnameEntry = Entry(root,width=55,bd=5,font=("Arial",15))
phoneEntry = Entry(root,width=55,bd=5,font=("Arial",15))
addressEntry = Entry(root,width=55,bd=5,font=("Arial",15))

studidEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
fnameEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
lnameEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
phoneEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
addressEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)

#Command later
addButton = Button(
    root,text="Add",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#84F894"
)
updateButton = Button(
    root,text="Update",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#84E8F8"
)
deleteButton = Button(
    root,text="Delete",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#FF9999"
)
searchButton = Button(
    root,text="Search",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#F4FE82"
)
resetButton = Button(
    root,text="Reset",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#F398FF"
)
selectButton = Button(
    root,text="Select",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#EEEEEE"
)

addButton.grid(row=3,column=5,columnspan=1,rowspan=2)
updateButton.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteButton.grid(row=7,column=5,columnspan=1,rowspan=2)
searchButton.grid(row=9,column=5,columnspan=1,rowspan=2)
resetButton.grid(row=11,column=5,columnspan=1,rowspan=2)
selectButton.grid(row=13,column=5,columnspan=1,rowspan=2)


root.mainloop()
