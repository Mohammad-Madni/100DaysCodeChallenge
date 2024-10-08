from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = Tk()
window.title("Stock Management System")
my_tree = ttk.Treeview(window,show="headings",height=20)
window.geometry("720x640")

placeholderArray = ['','','','','']

for i in range(0,5):
    placeholderArray[i] = tkinter.StringVar()

frame = tkinter.Frame(window,bg="#02577A")
frame.pack()

btnColor = "#196E78"

manageframe = tkinter.LabelFrame(frame,text="Manage",borderwidth=5)
manageframe.grid(row=0,column=0,sticky="w",padx=[10,200],pady=20,ipadx=[6])

saveBtn = Button(manageframe,text="SAVE",width=10,borderwidth=3,bg=btnColor,fg="white")
updateBtn = Button(manageframe,text="UPDATE",width=10,borderwidth=3,bg=btnColor,fg="white")
deleteBtn = Button(manageframe,text="DELETE",width=10,borderwidth=3,bg=btnColor,fg="white")
selectBtn = Button(manageframe,text="SELECT",width=10,borderwidth=3,bg=btnColor,fg="white")
findBtn = Button(manageframe,text="FIND",width=10,borderwidth=3,bg=btnColor,fg="white")
clearBtn = Button(manageframe,text="CLEAR",width=10,borderwidth=3,bg=btnColor,fg="white")
exportBtn = Button(manageframe,text="EXPORT",width=10,borderwidth=3,bg=btnColor,fg="white")

saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn.grid(row=0,column=4,padx=5,pady=5)
clearBtn.grid(row=0,column=5,padx=5,pady=5)
exportBtn.grid(row=0,column=6,padx=5,pady=5)


entriesframe = tkinter.LabelFrame(frame,text="Form",borderwidth=5)
entriesframe.grid(row=0,column=0,sticky="w",padx=[10,200],pady=20,ipadx=[6])


window.resizable(False,False)
window.mainloop()
