import sales
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

# Method when button 'Add Inventory' clicked
def clickedAdd():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
        if(len(entrySalesItem.get()) != 0 and len(entrySalesAmount.get()) != 0):
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
            messagebox.showerror('Error', 'Please fill in all the fields')
    
    # Frame
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
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
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
    leftFrame.grid(column=0, row=0, rowspan=10)
    leftFrame.grid_propagate(0)
    # Label
    moduleName = Label(leftFrame, text="Sales\nModule", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor="center")
    # Show as line
    lineLabel = Label(leftFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
    # Button
    btnAdd = Button(leftFrame, text="Add Sales", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white)
    btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
    btnDelete = Button(leftFrame, text="Delete\nSales", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
    # Title of the page
    labelTitle = Label(inputFrame, text="Display Sales", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')

    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=tempDashboard, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
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
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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

# Main program
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
# Create table
sales.execute_sql_file("sql/InventoryDB.sql")
# Testing purpose button
btnTest = Button(window, text="GO", font=('Arial', 18), command=clickedAdd)
btnTest.grid(column=0, row=0)
  
window.mainloop()