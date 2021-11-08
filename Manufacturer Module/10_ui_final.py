import manufacturer
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

# Method when button 'Add Manufacturer' clicked
def clickedAdd():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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
    frame = Frame(window, width=screen_width, height=screen_height, bg=white)
    frame.grid(column=0, row=0, columnspan=2, rowspan=10)
    btnTest = Button(frame, text="GO", font=('Arial', 18), command=clickedAdd)
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
manufacturer.create_manufacturer_PHPDB()
manufacturer.create_manufacturer_table("sql/PHPDB_Manufacturer.sql")

# Testing purpose button
btnTest = Button(window, text="GO", font=('Arial', 18), command=clickedAdd)
btnTest.grid(column=0, row=0)
  
window.mainloop()
