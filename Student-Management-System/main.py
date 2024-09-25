#import Modules
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk



#Connection
def Connection():
    con = pymysql.connect(
        host="localhost",user="root",password="",db="student_db"
    )
    return con

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent="",index="end",id=array,text="",values=(array),tag="orow")
    my_tree.tag_configure("orow",background="#EEEEEE",font=("Arial",12))
    my_tree.grid(row=8,column=0,columnspan=5,rowspan=11,padx=10,pady=20)


#GUI

root = Tk()
root.title("Student Management System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

#Function

#placeholders
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#set placeholders the values
def setph(word,num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
         ph3.set(word)
    if num == 4:
         ph4.set(word)
    if num == 5:
         ph5.set(word)



def read():
    conn = Connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def add():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    phone = str(phoneEntry.get())
    address = str(addressEntry.get())

    if (studid == "" or studid == "") or (fname == "" or fname == "") or (lname == "" or lname == "") or (address == "" or address == "") or (phone == "" or phone == ""):
        messagebox.showinfo("Error!", "Please Fill up the blanks")
        return
    else:
        try:
            conn = Connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES ('"+studid+"','"+fname+"','"+lname+"','"+address+"','"+phone+"')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error!", "StudID already exits")
            return
    refreshTable()

def reset():
    desicion = messagebox.askquestion("Warning!!", "Delete All Data").lower()
    if desicion != "yes":
        return
    else:
        try:
            conn = Connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error!", "Sorry an error occured")
            return
    refreshTable()


def delete():
    desicion = messagebox.askquestion("Warning!!", "Delete Selected Data?").lower()
    if desicion != "yes":
        return
    else:
        selected_data = my_tree.selection()[0]
        delete_data = str(my_tree.item(selected_data)["values"][0])
        try:
            conn = Connection()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM students WHERE STUDID={delete_data}")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error!", "Sorry an error occured")
            return
    refreshTable()


def select():
        try:
            selected_data = my_tree.selection()[0]
            studid = str(my_tree.item(selected_data)["values"][0])
            fname = str(my_tree.item(selected_data)["values"][1])
            lname = str(my_tree.item(selected_data)["values"][2])
            phone = str(my_tree.item(selected_data)["values"][3])
            address = str(my_tree.item(selected_data)["values"][4])

            setph(studid,1)
            setph(fname,2)
            setph(lname,3)
            setph(phone,4)
            setph(address,5)
        except:
            messagebox.showinfo("Error!", "Please Select a Data Row")


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

studidEntry = Entry(root,width=55,bd=5,font=("Arial",15),textvariable=ph1)
fnameEntry = Entry(root,width=55,bd=5,font=("Arial",15),textvariable=ph2)
lnameEntry = Entry(root,width=55,bd=5,font=("Arial",15),textvariable=ph3)
phoneEntry = Entry(root,width=55,bd=5,font=("Arial",15),textvariable=ph4)
addressEntry = Entry(root,width=55,bd=5,font=("Arial",15),textvariable=ph5)

studidEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
fnameEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
lnameEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
phoneEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
addressEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)

#Command later
addButton = Button(
    root,text="Add",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#84F894",command=add
)
updateButton = Button(
    root,text="Update",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#84E8F8"
)
deleteButton = Button(
    root,text="Delete",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#FF9999",command=delete
)
searchButton = Button(
    root,text="Search",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#F4FE82"
)
resetButton = Button(
    root,text="Reset",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#F398FF",command=reset
)
selectButton = Button(
    root,text="Select",padx=65,pady=15,width=10,bd=5,font=("Arial",15),bg="#EEEEEE",command=select
)

addButton.grid(row=3,column=5,columnspan=1,rowspan=2)
updateButton.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteButton.grid(row=7,column=5,columnspan=1,rowspan=2)
searchButton.grid(row=9,column=5,columnspan=1,rowspan=2)
resetButton.grid(row=11,column=5,columnspan=1,rowspan=2)
selectButton.grid(row=13,column=5,columnspan=1,rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading",font=("Arial Bold",15))

my_tree["columns"] = ("Student ID","First Name","Last Name","Phone","Address")
my_tree.column("#0",width=0,stretch=NO)

my_tree.column("Student ID",anchor=W,width=170)
my_tree.column("First Name",anchor=W,width=150)
my_tree.column("Last Name",anchor=W,width=150)
my_tree.column("Phone",anchor=W,width=150)
my_tree.column("Address",anchor=W,width=165)

my_tree.heading("Student ID",text="Student ID",anchor=W)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("Last Name",text="Last Name",anchor=W)
my_tree.heading("Phone",text="Phone",anchor=W)
my_tree.heading("Address",text="Address",anchor=W)

refreshTable()

root.mainloop()
