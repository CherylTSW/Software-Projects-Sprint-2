import manufacturer
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD


import manufacturer
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

from report_module import report_toCSV


# Method when button 'Display Manufacturer' clicked
def clickedDisplay():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
    leftFrame.grid(column=0, row=0, rowspan=10)
    leftFrame.grid_propagate(0)
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
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
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
    frame = Frame(window, width=screen_width, height=screen_height, bg=white)
    frame.grid(column=0, row=0, columnspan=2, rowspan=10)
    btnTest = Button(frame, text="GO", font=('Arial', 18), command=clickedDisplay)
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


# Testing purpose button
btnTest = Button(window, text="GO", font=('Arial', 18), command=clickedDisplay)
btnTest.grid(column=0, row=0)
  
window.mainloop()