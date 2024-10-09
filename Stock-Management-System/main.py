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
entriesframe.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[6])

itemIdLabel = Label(entriesframe,text="ITEM ID",anchor='e',width=10)
nameLabel = Label(entriesframe,text="NAME",anchor='e',width=10)
priceLabel = Label(entriesframe,text="PRICE",anchor='e',width=10)
qntLabel = Label(entriesframe,text="QNT",anchor='e',width=10)
categoryLabel = Label(entriesframe,text="CATEGORY",anchor='e',width=10)

itemIdLabel.grid(row=0,column=0,padx=10)
nameLabel.grid(row=1,column=0,padx=10)
priceLabel.grid(row=2,column=0,padx=10)
qntLabel.grid(row=3,column=0,padx=10)
categoryLabel.grid(row=4,column=0,padx=10)

itemIdEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[0])
nameEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[1])
priceEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[2])
qntEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[3])
categoryCombo = ttk.Combobox(entriesframe,width=50,textvariable=placeholderArray[4])

itemIdEntry.grid(row=0,column=2,padx=5,pady=5)
nameEntry.grid(row=1,column=2,padx=5,pady=5)
priceEntry.grid(row=2,column=2,padx=5,pady=5)
qntEntry.grid(row=3,column=2,padx=5,pady=5)
categoryCombo.grid(row=4,column=2,padx=5,pady=5)

window.resizable(False,False)
window.mainloop()
