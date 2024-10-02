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

