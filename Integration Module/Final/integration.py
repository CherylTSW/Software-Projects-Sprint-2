from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import datetime as dt
import time
import os
import sys
import manufacturer
import contact
from report import report_toCSV
import sales
import inventory
from tkinter.font import BOLD

#--------------WINDOW------------------#
root = Tk()
root.attributes('-fullscreen', True)
root.title("PHP-SREPS MENU")
root.configure(background='white')
root.resizable(False, False)
# Get window size
screen_width = root.winfo_screenwidth()        
screen_height = root.winfo_screenheight()

#-----------------COMMANDFUNCTIONS------------#
def calllogin():
    os.system('authentication.py')

def callmanufacturer():
    # Color code
    blue = "#344955"
    white = "#ffffff"
    orange = "#fb8000"

    # Entry width calculation (wider width on bigger screen)
    entry_width = 470
    if(screen_width > 1750):
        entry_width = 670

    # X offset calculation
    x_offset = int((screen_width-240-780)/2 + 200)

    if(screen_width > 1750):
        x_offset = int((screen_width-240-980)/2 + 200)

    # Create database and table
    manufacturer.create_manufacturer_PHPDB()
    manufacturer.create_manufacturer_table("sql/PHPDB_Manufacturer.sql")

    # Method when button 'Add Manufacturer' clicked
    def clickedAdd():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        leftFrame.lift()
        # Label
        moduleName = Label(leftFrame, text="Manufacturer\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Delete\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDelete, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function

        # Method when button 'Submit' clicked
        def clickedSubmit():
            if(len(entryManufacturerID.get()) != 0 and len(entryManufacturerFirstName.get()) != 0 and len(entryManufacturerLastName.get()) != 0 and len(entryManufacturerItem.get()) != 0 and len(entryManufacturerStreetAddress.get()) != 0 and len(entryManufacturerPhoneNumber.get()) != 0):
                ManufacturerID = int(entryManufacturerID.get())
                ManufacturerFirstName = entryManufacturerFirstName.get()
                ManufacturerLastName = entryManufacturerLastName.get()
                ManufacturerItem = entryManufacturerItem.get()
                ManufacturerStreetAddress = entryManufacturerStreetAddress.get()
                ManufacturerPhoneNumber = int(entryManufacturerPhoneNumber.get())

                if(manufacturer.add_manufacturer(ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber)):
                    entryManufacturerID.delete(0, 'end')
                    entryManufacturerFirstName.delete(0, 'end')
                    entryManufacturerLastName.delete(0, 'end')
                    entryManufacturerItem.delete(0, 'end')
                    entryManufacturerStreetAddress.delete(0, 'end')
                    entryManufacturerPhoneNumber.delete(0, 'end')
                    messagebox.showinfo('', 'Manufacturer details were added successfully!')
                else:
                    messagebox.showerror('Error', 'An error occured while trying to add the manufacturer details')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields')
        
        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Add Manufacturer", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelManufacturerID = Label(inputFrame, text="Manufacturer ID :", font=('Arial', 24), fg=blue)
        labelManufacturerID.place(x=x_offset, y=270, anchor="e")
        labelManufacturerFirstName = Label(inputFrame, text="First Name :", font=('Arial', 24), fg=blue)
        labelManufacturerFirstName.place(x=x_offset, y=350, anchor="e")
        labelManufacturerLastName = Label(inputFrame, text="Last Name :", font=('Arial', 24), fg=blue)
        labelManufacturerLastName.place(x=x_offset, y=430, anchor="e")
        labelManufacturerItem = Label(inputFrame, text="Manufacturer Item :", font=('Arial', 24), fg=blue)
        labelManufacturerItem.place(x=x_offset, y=510, anchor="e")
        labelManufacturerStreetAddress = Label(inputFrame, text="Street Address :", font=('Arial', 24), fg=blue)
        labelManufacturerStreetAddress.place(x=x_offset, y=590, anchor="e")
        labelManufacturerPhoneNumber = Label(inputFrame, text="Phone Number :", font=('Arial', 24), fg=blue)
        labelManufacturerPhoneNumber.place(x=x_offset, y=670, anchor="e")
        # Entry
        entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerID.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        entryManufacturerFirstName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerFirstName.place(x=x_offset+10, y=350, anchor="w", width=entry_width, height=50)
        entryManufacturerLastName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerLastName.place(x=x_offset+10, y=430, anchor="w", width=entry_width, height=50)
        entryManufacturerItem = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerItem.place(x=x_offset+10, y=510, anchor="w", width=entry_width, height=50)
        entryManufacturerStreetAddress = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerStreetAddress.place(x=x_offset+10, y=590, anchor="w", width=entry_width, height=50)
        entryManufacturerPhoneNumber = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerPhoneNumber.place(x=x_offset+10, y=670, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Delete Manufacturer' clicked
    def clickedDelete():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Manufacturer\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Delete\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDelete, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function

        # Method when button 'Submit' clicked
        def clickedSubmit():
            if( len(entryManufacturerID.get()) != 0):
                ManufacturerID = int(entryManufacturerID.get())
                
                if(manufacturer.remove_manufacturer(ManufacturerID)):
                    entryManufacturerID.delete(0, 'end')
                    messagebox.showinfo('', 'Manufacturer details were deleted successfully!')
                else:
                    messagebox.showerror('Error', 'An error occured while trying to delete the manufacturer details')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Delete Manufacturer", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelManufacturerID = Label(inputFrame, text="Manufacturer ID :", font=('Arial', 24), fg=blue)
        labelManufacturerID.place(x=x_offset, y=270, anchor="e")
        # Entry
        entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerID.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Display Manufacturer' clicked
    def clickedDisplay():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Manufacturer\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Delete\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDelete, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function
        
        # Method when button 'Submit' clicked
        def clickedSubmit():
            if( len(entryManufacturerID.get()) != 0 ): 
                manufacturerID = int(entryManufacturerID.get())
                result = manufacturer.get_manufacturer_by_id(manufacturerID)
                if(result):
                    manufacturer.display_manufacturer(inputFrame, 150, 500, result)
                else:
                    messagebox.showerror('Match not found', 'No match can be found')
            else:
                messagebox.showerror('Error', 'Please fill in the Manufacturer ID to be searched')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Display Manufacturer", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelManufacturerID = Label(inputFrame, text="Manufacturer ID :", font=('Arial', 24), fg=blue)
        labelManufacturerID.place(x=x_offset, y=270, anchor="e")
        # Entry
        entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerID.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Search", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Back' clicked
    def clickedBack():
        Dashboard()

    clickedAdd()

def callorder():
    # Color code
    blue = "#344955"
    white = "#ffffff"
    orange = "#fb8000"

    # Entry width calculation (wider width on bigger screen)
    entry_width = 470
    if(screen_width > 1750):
        entry_width = 670

    # X offset calculation
    x_offset = int((screen_width-240-780)/2 + 200)

    if(screen_width > 1750):
        x_offset = int((screen_width-240-980)/2 + 200)

    # Create database and table
    contact.create_database()
    contact.create_contact_table("sql/PHPDB_Contact.sql")

    #This is for when the "Add Contact" button is clicked
    def clickedAddContact():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        leftFrame.lift()
        # Label
        moduleName = Label(leftFrame, text="Contact\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAddContact, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Delete\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDeleteContact, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplayContact, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        #This is the main function
        #This is for when the "Submit" button is clicked
        def clickedSubmitContact():
            if(len(entryOrderID.get()) !=0 and len(entryPrice.get()) !=0 and len(entryQuantity.get()) !=0 and len(entryOrderDate.get()) !=0 and len(entryManufacturerID.get()) !=0 and len(entryProductID.get()) !=0):
                orderId = int(entryOrderID.get())
                price = float(entryPrice.get())
                quantity = int(entryQuantity.get())
                orderDate = entryOrderDate.get()
                manufacturerId = int(entryManufacturerID.get())
                productId = int(entryProductID.get())

                if(contact.insert_contact(orderId, orderDate, manufacturerId, productId, quantity, price)):
                    entryOrderID.delete(0, 'end')
                    entryPrice.delete(0, 'end')
                    entryQuantity.delete(0, 'end')
                    entryOrderDate.delete(0, 'end')
                    entryManufacturerID.delete(0, 'end')
                    entryProductID.delete(0, 'end')
                    messagebox.showinfo('', 'Contact details were added successfully!')
                else:
                    messagebox.showerror('Error', 'An error has occured while trying to add the contact details.')

            else:
                messagebox.showerror('Error', 'Please fill in all the fields.')

        #Frame
        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")

        # Title of the page
        labelTitle = Label(inputFrame, text="Add Contact", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')

        # Label
        labelOrderId = Label(inputFrame, text="Order ID :", font=('Arial', 24), fg=blue)
        labelOrderId.place(x=x_offset, y=270, anchor="e")
        labelOrderDate = Label(inputFrame, text="Order Date :", font=('Arial', 24), fg=blue)
        labelOrderDate.place(x=x_offset, y=350, anchor="e")
        labelManufacturerId = Label(inputFrame, text="Manufacturer ID :", font=('Arial', 24), fg=blue)
        labelManufacturerId.place(x=x_offset, y=430, anchor="e")
        labelProductId = Label(inputFrame, text="Product ID :", font=('Arial', 24), fg=blue)
        labelProductId.place(x=x_offset, y=510, anchor="e")
        labelQuantity = Label(inputFrame, text="Quantity :", font=('Arial', 24), fg=blue)
        labelQuantity.place(x=x_offset, y=590, anchor="e")
        labelPrice = Label(inputFrame, text="Total Price :", font=('Arial', 24), fg=blue)
        labelPrice.place(x=x_offset, y=670, anchor="e")

        # Entry
        entryOrderID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryOrderID.place(x=x_offset+10, y=270, anchor="w", width=470, height=50)
        entryOrderDate = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryOrderDate.place(x=x_offset+10, y=350, anchor="w", width=470, height=50)
        entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryManufacturerID.place(x=x_offset+10, y=430, anchor="w", width=470, height=50)
        entryProductID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryProductID.place(x=x_offset+10, y=510, anchor="w", width=470, height=50)
        entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryQuantity.place(x=x_offset+10, y=590, anchor="w", width=470, height=50)
        entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryPrice.place(x=x_offset+10, y=670, anchor="w", width=470, height=50)

        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmitContact, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    #This is for when the "Delete Contact" button is clicked
    def clickedDeleteContact():
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Contact\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAddContact, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Delete\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDeleteContact, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplayContact, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        #This is the main function

        #This is for when the "Submit" button is clicked
        def clickedSubmitContact():
            if( len(entryOrderID.get()) != 0):
                orderID = int(entryOrderID.get())
                
                if(contact.delete_contact(orderID)):
                    entryOrderID.delete(0, 'end')
                    messagebox.showinfo('', 'Contact details were deleted successfully!')
                else:
                    messagebox.showerror('Error', 'An error occured while trying to delete the manufacturer details')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Delete Contact", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelOrderId = Label(inputFrame, text="Order ID :", font=('Arial', 24), fg=blue)
        labelOrderId.place(x=x_offset, y=270, anchor="e")
        # Entry
        entryOrderID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryOrderID.place(x=x_offset+10, y=270, anchor="w", width=470, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmitContact, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    #This is for when the "Dsiplay Contact" button is clicked
    def clickedDisplayContact():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Contact\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAddContact, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Delete\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDeleteContact, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nContact", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplayContact, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        #This is the main function

        #This is for when the "Submit" button is clicked
        def clickedSubmitContact():
            if( len(entryOrderID.get()) != 0):
                orderID = int(entryOrderID.get())
                result = contact.get_contact_by_ID(orderID)
                if(result):
                    contact.display_contact(inputFrame, 150, 500, result)
                else:
                    messagebox.showerror('Match not found', 'No match can be found')
            else:
                messagebox.showerror('Error', 'Please fill in the Order ID to search')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Display Contact", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelOrderId = Label(inputFrame, text="Order ID :", font=('Arial', 24), fg=blue)
        labelOrderId.place(x=x_offset, y=270, anchor="e")
        # Entry
        entryOrderID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryOrderID.place(x=x_offset+10, y=270, anchor="w", width=470, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Search", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmitContact, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Back' clicked
    def clickedBack():
        Dashboard()

    clickedAddContact()

def callreport():
    # Color code
    blue = "#344955"
    white = "#ffffff"
    orange = "#fb8000"

    # X offset calculation
    x_offset = int((screen_width-240-780)/2 + 200)

    if(screen_width > 1750):
        x_offset = int((screen_width-240-980)/2 + 200)

    # Method when button 'Generate Report' clicked
    def clickedDisplay():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        leftFrame.lift()
        # Label
        moduleName = Label(leftFrame, text="Report\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnDisplay = Button(leftFrame, text="Generate\nReport", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=260, anchor="center", width=160, height=100)

        # Main function
        
        # Method when button 'Submit' clicked
        def clickedDownload():
            report_toCSV()
            messagebox.showinfo('', 'You have successfully downloaded the report!')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Generate Report", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelManufacturerID = Label(inputFrame, text="Click on the button below to download the report", font=('Arial', 24), fg=blue)
        labelManufacturerID.place(x=x_offset+520, y=270, anchor="e")
        # Submit button
        btnSubmit = Button(inputFrame, text="Download", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDownload, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=350, anchor='center')
    
    # Method when button 'Back' clicked
    def clickedBack():
        Dashboard()

    clickedDisplay()

def callsales():
    # Color code
    blue = "#344955"
    white = "#ffffff"
    orange = "#fb8000"

    # Entry width calculation (wider width on bigger screen)
    entry_width = 470

    if(screen_width > 1750):
        entry_width = 670

    # X offset calculation
    x_offset = int((screen_width-240-780)/2 + 200)

    if(screen_width > 1750):
        x_offset = int((screen_width-240-980)/2 + 200)

    # Create table
    sales.execute_sql_file("sql/PHPDB_Sales.sql")
    
    # Method when button 'Add Inventory' clicked
    def clickedAdd():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        leftFrame.lift()
        # Label
        moduleName = Label(leftFrame, text="Sales\nModule", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add Sales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnDelete = Button(leftFrame, text="Delete\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDelete, activebackground='#FB5F00', activeforeground=white)
        btnDelete.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function

        # Method when button 'Submit' clicked
        def clickedSubmit():
            if(len(entrySalesItem.get()) != 0 and len(entrySalesAmount.get()) != 0):
                if(len(entrySalesItem.get()) < 255 or len(entrySalesAmount.get()) < 20):
                    salesItem = entrySalesItem.get()
                    if(entrySalesAmount.get().isdigit()):
                        amount = float(entrySalesAmount.get())

                        if(sales.add_sales(salesItem, amount)):
                            entrySalesItem.delete(0, 'end')
                            entrySalesAmount.delete(0, 'end')
                            messagebox.showinfo('', 'Sales record added into database successfully !')
                        else:
                            messagebox.showerror('Error', 'An error occured while trying to add the sales record into database')
                    else:
                        messagebox.showerror('Error', 'Please enter a valid number in the "Amount" field')
                else:
                    messagebox.showerror('Error', 'fields too long')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields')
        
        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        inputFrame.lift()
        # Title of the page
        labelTitle = Label(inputFrame, text="Add Sales", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelSalesItem = Label(inputFrame, text="Sales Item :", font=('Arial', 24), fg=blue)
        labelSalesItem.place(x=x_offset, y=270, anchor="e")
        labelSalesAmount = Label(inputFrame, text="Amount(RM) :", font=('Arial', 24), fg=blue)
        labelSalesAmount.place(x=x_offset, y=370, anchor="e")
        # Entry
        entrySalesItem = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entrySalesItem.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        entrySalesAmount = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entrySalesAmount.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Display Sales' clicked
    def clickedDisplay():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Sales\nModule", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add Sales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnDelete = Button(leftFrame, text="Delete\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDelete, activebackground='#FB5F00', activeforeground=white)
        btnDelete.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function
        
        # Method when button 'Submit' clicked
        def clickedSubmit():
            if( len(salesIDEntry.get()) != 0 ): 
                itemID = int(salesIDEntry.get())
                result = sales.get_sales_by_id(itemID)
                if(result):
                    sales.display_sales(inputFrame, 150, 500, result, screen_width, screen_height)
                    #150 500
                else:
                    messagebox.showerror('Match not found', 'No match can be found')
                
            # elif(len(entryItemName.get()) != 0):
            #     itemName = entryItemName.get()
            #     result = inventory.get_inventory_by_name(itemName)
            #     if(result):
            #         inventory.display_inventory(inputFrame, (screen_width-240-1000)/2, 500, result)
            #     else:
            #         messagebox.showerror('Match not found', 'No match can be found')
            else:
                messagebox.showerror('Error', 'Please fill in the Item ID or Item Name to be searched')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Display Sales", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')

        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')

        # Sales ID 
        salesIDLabel = Label(inputFrame, text="Sales ID :", font=('Arial', 24), fg=blue)
        salesIDLabel.place(x=x_offset, y=270, anchor="e")
        salesIDEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        salesIDEntry.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)

        # Sales Name
        # salesNameLabel = Label(inputFrame, text="Item Name :", font=('Arial', 24), fg=blue)
        # salesNameLabel.place(x=x_offset, y=370, anchor="e")
        # salesNameEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        # salesNameEntry.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)

        # Submit button
        btnSubmit = Button(inputFrame, text="Search", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Empty method just to avoid error in the code
    def clickedDelete():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Sales\nModule", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add Sales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnDelete = Button(leftFrame, text="Delete\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDelete, activebackground='#FB5F00', activeforeground=white)
        btnDelete.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Method when button 'Submit' clicked
        def clickedSubmit():
            if( len(entryOrderID.get()) != 0 ):
                salesID = int(entryOrderID.get())
                if(sales.delete_sales(salesID)):
                    entryOrderID.delete(0, 'end')
                    messagebox.showinfo('', 'Sales record deleted from database successfully !')
                else:
                    messagebox.showerror('Error', 'An error occured while trying to delete the sales record')
            else:
                messagebox.showerror('Error', 'Please fill in the Sales ID to be deleted')
            
        # Main function 
        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Delete Sales", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelOrderId = Label(inputFrame, text="Sales ID :", font=('Arial', 24), fg=blue)
        labelOrderId.place(x=x_offset, y=270, anchor="e")
        # Entry
        entryOrderID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryOrderID.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Back' clicked
    def clickedBack():
        Dashboard()

    clickedAdd()

def callinventory():
    # Color code
    blue = "#344955"
    white = "#ffffff"
    orange = "#fb8000"

    # Entry width calculation (wider width on bigger screen)
    entry_width = 470
    if(screen_width > 1750):
        entry_width = 670

    # X offset calculation
    x_offset = int((screen_width-240-780)/2 + 200)

    if(screen_width > 1750):
        x_offset = int((screen_width-240-980)/2 + 200)

    # Create database and table
    inventory.create_inventory_db()
    inventory.execute_sql_file("sql/PHPDB_Inventory.sql")

    # Method when button 'Add Inventory' clicked
    def clickedAdd():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        leftFrame.lift()
        # Label
        moduleName = Label(leftFrame, text="Inventory\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Edit\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function
        
        # Method when button 'Submit' clicked
        def clickedSubmit():
            if(len(entryItemName.get()) != 0 and len(entryPrice.get()) != 0 and len(entryQuantity.get()) != 0):
                itemName = entryItemName.get()
                price = float(entryPrice.get())
                quantity = int(entryQuantity.get())

                if(inventory.add_inventory(itemName, price, quantity)):
                    entryItemName.delete(0, 'end')
                    entryPrice.delete(0, 'end')
                    entryQuantity.delete(0, 'end')
                    messagebox.showinfo('', 'Item added into inventory successfully !')
                else:
                    messagebox.showerror('Error', 'An error occured while trying to add the item into inventory')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields')
        
        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Add Inventory", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelItemName = Label(inputFrame, text="Item Name :", font=('Arial', 24), fg=blue)
        labelItemName.place(x=x_offset, y=270, anchor="e")
        labelPrice = Label(inputFrame, text="Price(RM) :", font=('Arial', 24), fg=blue)
        labelPrice.place(x=x_offset, y=370, anchor="e")
        labelQuantity = Label(inputFrame, text="Quantity :", font=('Arial', 24), fg=blue)
        labelQuantity.place(x=x_offset, y=470, anchor="e")
        # Entry
        entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryItemName.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryPrice.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)
        entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryQuantity.place(x=x_offset+10, y=470, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Edit Inventory' clicked
    def clickedEdit():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Inventory\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Edit\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function

        # Method when button 'Submit' clicked
        def clickedSubmit():
            if( len(entryItemID.get()) != 0 and len(entryItemName.get()) != 0 and len(entryPrice.get()) != 0 and len(entryQuantity.get()) != 0):
                itemID = int(entryItemID.get())
                itemName = entryItemName.get()
                price = float(entryPrice.get())
                quantity = int(entryQuantity.get())
                
                if(inventory.edit_inventory(itemName, price, quantity, itemID)):
                    entryItemID.delete(0, 'end')
                    entryItemName.delete(0, 'end')
                    entryPrice.delete(0, 'end')
                    entryQuantity.delete(0, 'end')
                    messagebox.showinfo('', 'Item Edited successfully !')
                else:
                    messagebox.showerror('Error', 'An error occured while trying to edit the item')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Edit Inventory", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelItemID = Label(inputFrame, text="Item ID :", font=('Arial', 24), fg=blue)
        labelItemID.place(x=x_offset, y=270, anchor="e")
        labelItemName = Label(inputFrame, text="New Item Name :", font=('Arial', 24), fg=blue)
        labelItemName.place(x=x_offset, y=370, anchor="e")
        labelPrice = Label(inputFrame, text="New Price(RM) :", font=('Arial', 24), fg=blue)
        labelPrice.place(x=x_offset, y=470, anchor="e")
        labelQuantity = Label(inputFrame, text="New Quantity :", font=('Arial', 24), fg=blue)
        labelQuantity.place(x=x_offset, y=570, anchor="e")
        # Entry
        entryItemID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryItemID.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryItemName.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)
        entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryPrice.place(x=x_offset+10, y=470, anchor="w", width=entry_width, height=50)
        entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryQuantity.place(x=x_offset+10, y=570, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Display Inventory' clicked
    def clickedDisplay():
        # The left navigation panel
        # Frame
        leftFrame = Frame(root, bg=blue, width=240, height=screen_height)
        leftFrame.grid(column=0, row=0, rowspan=10)
        leftFrame.grid_propagate(0)
        # Label
        moduleName = Label(leftFrame, text="Inventory\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
        moduleName.place(x=120, y=80, anchor="center")
        # Show as line
        lineLabel = Label(leftFrame, bg=orange)
        lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
        # Button
        btnAdd = Button(leftFrame, text="Add\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
        btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
        btnEdit = Button(leftFrame, text="Edit\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
        btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
        btnDisplay = Button(leftFrame, text="Display\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
        btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

        # Main function
        
        # Method when button 'Submit' clicked
        def clickedSubmit():
            if( len(entryItemID.get()) != 0 ): 
                itemID = int(entryItemID.get())
                result = inventory.get_inventory_by_id(itemID)
                if(result):
                    inventory.display_inventory(inputFrame, 150, 500, result)
                else:
                    messagebox.showerror('Match not found', 'No match can be found')
                
            elif(len(entryItemName.get()) != 0):
                itemName = entryItemName.get()
                result = inventory.get_inventory_by_name(itemName)
                if(result):
                    inventory.display_inventory(inputFrame, (screen_width-240-1000)/2, 500, result)
                else:
                    messagebox.showerror('Match not found', 'No match can be found')
            else:
                messagebox.showerror('Error', 'Please fill in the Item ID or Item Name to be searched')

        # Frame
        inputFrame = Frame(root, width=screen_width-240, height=screen_height)
        inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
        # Title of the page
        labelTitle = Label(inputFrame, text="Display Inventory", font=('Arial', 30, BOLD), fg=blue)
        labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
        # Back button
        btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
        btnBack.place(x=50, y=70, anchor='w')
        # Label
        labelItemID = Label(inputFrame, text="Item ID :", font=('Arial', 24), fg=blue)
        labelItemID.place(x=x_offset, y=270, anchor="e")
        labelItemName = Label(inputFrame, text="Item Name :", font=('Arial', 24), fg=blue)
        labelItemName.place(x=x_offset, y=370, anchor="e")
        # Entry
        entryItemID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryItemID.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)
        entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
        entryItemName.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)
        # Submit button
        btnSubmit = Button(inputFrame, text="Search", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
        btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

    # Method when button 'Back' clicked
    def clickedBack():
        Dashboard()

    clickedAdd()

def callaccount():
    os.system('account.py')

def Dashboard():
    date = dt.datetime.now()
    #-----------------FRAME--------------------------
    f1=Frame(root,width=240,height=screen_height,bg='#324856')
    f1.grid(column=0, row=0, rowspan=10)
    f1.lift()
    f2=Frame(root,width=screen_width-240,height=screen_height,bg='white')
    f2.grid(column=1, row=0, rowspan=10, sticky="ns")
    f2.lift()

    #------------------TITLE------------------------
    lbl=Label(root, text="PHP-SRePS", fg='white', bg='#324856', font=("arial", 40))
    lbl.place(x=155, y=280)
    lbl2=Label(root, text="______________________", fg='orange', bg='#324856', font=("arial", 30))
    lbl2.place(x=60, y=340)
    # clock = Label (root, text=time1, font=('arial', 20, 'bold'), fg='white', bg='#324856')
    # clock.place(x=200, y=610)
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
    salesbtn=Button(root, text="Sales",fg ='white',bg='orange', command=callsales, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
    salesbtn.place(x=1050, y=400, anchor="center", width=180, height=90)
    accbtn=Button(root, text="Account \nManagement",fg ='white',bg='orange', command=callaccount, font=("arial",20), activebackground='#FB5F00', activeforeground='white')
    accbtn.place(x=1050, y=600, anchor="center", width=180, height=90)
    
    '''
    #-------------------TIME---------------------
    def tick():
        global time1
        time2 = time.strftime ('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text="Time: " + time2)
        clock.after(200,tick)

    tick()
    '''

Dashboard()
root.mainloop()