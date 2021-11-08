from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import datetime as dt
import time
import os
import sys

#--------------WINDOW------------------#
root = Tk()
root.geometry("1200x800")
root.title("PHP-SREPS MENU")
root.configure(background='white')
root.resizable(False, False)

#-----------------COMMANDFUNCTIONS------------#
def calllogin():
    os.system('authentication.py')

def callmanufacturer():
    os.system('manufacturer.py')

def callorder():
    os.system('contact.py')

def callreport():
    os.system('report.py')

def calsales():
    os.system('sales.py')

def callinventory():
    os.system('inventory.py')

def callaccount():
    os.system('account.py')

time1 = ''
date = dt.datetime.now()

#-----------------FRAME--------------------------
f1=Frame(root,width=600,height=800,bg='#324856')
f1.pack(side=LEFT)
f2=Frame(root,width=600,height=800,bg='white')
f2.pack(side=RIGHT)

#------------------TITLE------------------------
lbl=Label(root, text="PHP-SRePS", fg='white', bg='#324856', font=("arial", 40))
lbl.place(x=155, y=280)
lbl2=Label(root, text="______________________", fg='orange', bg='#324856', font=("arial", 30))
lbl2.place(x=60, y=340)
clock = Label (root, text=time1, font=('arial', 20, 'bold'), fg='white', bg='#324856')
clock.place(x=200, y=610)
date = Label (root, text=f"{date:%A, %B %d, %Y}", font=('arial', 20, 'bold'), fg='white', bg='#324856')
date.place(x=110, y=550)

#------------------LEFTBUTTON-----------------------
lgnbtn=Button(root, text="Logout",fg ='white',bg='orange', command=calllogin, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
lgnbtn.place(x=300, y=500, anchor="center", width=300, height=50)
#------------------RIGHTBUTTON
manubtn=Button(root, text="Manufacturer",fg ='white',bg='orange', command=callmanufacturer, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
manubtn.place(x=800, y=200, anchor="center", width=180, height=90)
repobtn=Button(root, text="Report",fg ='white',bg='orange', command=callreport, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
repobtn.place(x=800, y=400, anchor="center", width=180, height=90)
invbtn=Button(root, text="Inventory",fg ='white',bg='orange', command=callinventory, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
invbtn.place(x=800, y=600, anchor="center", width=180, height=90)
ordbtn=Button(root, text="Order",fg ='white',bg='orange', command=callorder, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
ordbtn.place(x=1050, y=200, anchor="center", width=180, height=90)
salesbtn=Button(root, text="Sales",fg ='white',bg='orange', command=calsales, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
salesbtn.place(x=1050, y=400, anchor="center", width=180, height=90)
accbtn=Button(root, text="Account \nManagement",fg ='white',bg='orange', command=calsales, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
accbtn.place(x=1050, y=600, anchor="center", width=180, height=90)
#-------------------TIME---------------------

def tick():
    global time1
    time2 = time.strftime ('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text="Time: " + time2)
    clock.after(200,tick)

tick()





root.mainloop()