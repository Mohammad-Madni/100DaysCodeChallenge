from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import random
import pymysql
import csv
from datetime import datetime
import numpy as np
from unicodedata import category

window = Tk()
window.title("Stock Management System")
window.geometry("720x640")
my_tree = ttk.Treeview(window,show="headings",height=20)
style = ttk.Style()

placeholderArray = ['','','','','']
numeric = '1234567890'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def Connection():
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="stockmanagementsystem"
    )
    return con

con = Connection()
cursor = con.cursor()

for i in range(0,5):
    placeholderArray[i] = tkinter.StringVar()

def read():
    cursor.connection.ping()
    sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks ORDER BY 'id' DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    con.commit()
    con.close()
    return results

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent="",index='end',iid=array,text="",values=(array),tags="orow")
    my_tree.tag_configure("orow",background="#EEEEEE")
    my_tree.pack()


def setph(word,num):
    for ph in range(0,5):
        if ph == num:
            placeholderArray[ph].set(word)


def generateRand():
    itemId=''
    for i in range(0,3):
        randno = random.randrange(0,(len(numeric)-1))
        itemId = itemId+str(numeric[randno])
    randno = random.randrange(0,len(alpha)-1)
    itemId = itemId+'-'+str(alpha[randno])
    setph(itemId,0)


def save():
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    qnt = str(qntEntry.get())
    cat = str(categoryCombo.get())

    # Check for blanks
    if not (itemId and itemId.strip()) or not (name and name.strip()) or not (price and price.strip()) or not (
            qnt and qnt.strip()) or not (cat and cat.strip()):
        messagebox.showwarning("", "Please Fill up all blanks")
        return

    # Validate Item ID
    if len(itemId) < 5:
        messagebox.showwarning("", "Invalid Item Id")
        return
    if itemId[3] != "-":
        messagebox.showwarning("", "Invalid Item Id format, expecting 'XXX-...'.")
        return

    valid = True
    for i in range(0, 3):
        if itemId[i] not in numeric:
            valid = False
            break
    if itemId[4] not in alpha:
        valid = False

    if not valid:
        messagebox.showwarning("", "Invalid Item Id")
        return

    try:
        cursor.connection.ping()  # Ensure the connection is alive

        # Secure query using parameters
        sql = "SELECT * FROM stocks WHERE item_id = %s"
        cursor.execute(sql, (itemId,))
        checkItemNo = cursor.fetchall()

        if len(checkItemNo) > 0:
            messagebox.showwarning("", "Item Id already used")
            return
        else:
            # Inserting data securely
            sql = "INSERT INTO stocks (item_id, name, price, quantity, category) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (itemId, name, price, qnt, cat))
            con.commit()

        refreshTable()  # Refresh the table to show new data

    except Exception as e:
        messagebox.showwarning("", f"Error while saving: {str(e)}")
        return
    finally:
        if con.is_connected():
            con.close()  # Closing the connection safely




frame = tkinter.Frame(window,bg="#02577A")
frame.pack()

btnColor = "#196E78"

manageframe = tkinter.LabelFrame(frame,text="Manage",borderwidth=5)
manageframe.grid(row=0,column=0,sticky="w",padx=[10,200],pady=20,ipadx=[6])

saveBtn = Button(manageframe,text="SAVE",width=10,borderwidth=3,bg=btnColor,fg="white",command=save)
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

categoryArray = ["Networking Tools", "Computer Parts","Repair Tools","Gadgets"]

itemIdEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[0])
nameEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[1])
priceEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[2])
qntEntry = Entry(entriesframe,width=50,textvariable=placeholderArray[3])
categoryCombo = ttk.Combobox(entriesframe,width=47,textvariable=placeholderArray[4],values=categoryArray)

itemIdEntry.grid(row=0,column=2,padx=5,pady=5)
nameEntry.grid(row=1,column=2,padx=5,pady=5)
priceEntry.grid(row=2,column=2,padx=5,pady=5)
qntEntry.grid(row=3,column=2,padx=5,pady=5)
categoryCombo.grid(row=4,column=2,padx=5,pady=5)

generateIdBtn = Button(entriesframe,text="GENERATE ID",borderwidth=3,bg=btnColor,fg="white",command=generateRand)
generateIdBtn.grid(row=0,column=3,padx=5,pady=5)

style.configure(window)

my_tree["columns"] = ("Item Id","Name","Price","Quantity","Category","Date")

my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Item Id",anchor=W,width=70)
my_tree.column("Name",anchor=W,width=125)
my_tree.column("Price",anchor=W,width=125)
my_tree.column("Quantity",anchor=W,width=100)
my_tree.column("Category",anchor=W,width=150)
my_tree.column("Date",anchor=W,width=150)

my_tree.heading("Item Id",text="Item Id",anchor=W)
my_tree.heading("Name",text="Name",anchor=W)
my_tree.heading("Price",text="Price",anchor=W)
my_tree.heading("Quantity",text="Quantity",anchor=W)
my_tree.heading("Category",text="Category",anchor=W)
my_tree.heading("Date",text="Date",anchor=W)

my_tree.tag_configure("orow",background="#EEEEEE")
my_tree.pack()

refreshTable()

window.resizable(False,False)
window.mainloop()
