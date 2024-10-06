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

saveBtn = Button(manageframe,text="Save",)


window.resizable(False,False)
window.mainloop()
