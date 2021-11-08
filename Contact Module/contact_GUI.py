import contact
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

#This is for when the "Add Contact" button is clicked
def clickedAddContact():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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

def clickedBack():
    frame = Frame(window, width=screen_width, height=screen_height, bg=white)
    frame.grid(column=0, row=0, columnspan=2, rowspan=10)
    btnTest = Button(frame, text="GO", font=('Arial', 18), command=clickedAddContact)
    btnTest.grid(column=0, row=0, in_=frame)
    frame.grid_propagate(0)
    frame.lift()

# Color code
blue = "#344955"
white = "#ffffff"
orange = "#fb8000"

# Create window
window = Tk()
window.attributes('-fullscreen', True)
screen_width = window.winfo_screenwidth()        
screen_height = window.winfo_screenheight()

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
contact.create_contact_table("sql/ContactDB.sql")

# Testing purpose button
btnTest = Button(window, text="GO", font=('Arial', 18), command=clickedAddContact)
btnTest.grid(column=0, row=0)
  
window.mainloop()