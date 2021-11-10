import authentication as auth
import database as db
from tkinter import messagebox
from tkinter import *
from tkinter.font import BOLD

config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "PHPDB"
        }

auth_db_conn = db.create_db_connection(config)

loginUserID = 0

# Color code
blue = "#344955"
white = "#ffffff"
orange = "#fb8000"

# Function to show login page
def loginPage():
    # Left Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
    leftFrame.grid(column=0, row=0, rowspan=10)
    leftFrame.grid_propagate(0)

    # Company 
    companyName = Label(master=leftFrame, text="People\nHealth\nPharmacy\n(PHP)\nInc.", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    companyName.place(x=120, y=140, anchor=CENTER)

    # Line
    lineLabel = Label(leftFrame, bg=orange)
    lineLabel.place(x=120, y=300, anchor="center", width=195, height=3)

    # Software Name
    appName = Label(master=leftFrame, text="Sales\nReporting\nand\nPrediction\nSystem", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    appName.place(x=120, y=450, anchor=CENTER)

    # On Login function
    def OnLogin():
        # Check if all fields are filled
        if(len(usernameEntry.get()) != 0 and len(passwordEntry.get()) != 0):
            username = usernameEntry.get()
            password = passwordEntry.get()
            if (auth.login(auth_db_conn, username, password)):
                global loginUserID
                loginUserID = auth.get_userID(auth_db_conn, username)
                messagebox.showinfo('', "Login successfully")
                changePasswordPage()
            else:
                messagebox.showerror('Error', 'Username or password is false')
            # Go dashboard if correct credential
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')
    
    # Main frame 
    mainFrame = Frame(window, width=screen_width-240, height=screen_height)
    mainFrame.grid(column=1, row=0, rowspan=10, sticky="ns")

    # Login page title
    title = Label(master=mainFrame, text="Login Page", fg=blue, font=("Arial", 30, BOLD))
    title.place(x=(screen_width-240)/2, y=70, anchor='center')

    # Username field
    usernameLabel = Label(master=mainFrame, text="Username:", fg=blue, font=("Arial", 24))
    usernameEntry = Entry(master=mainFrame, bg=blue, fg=white, font=("Arial", 24))
    usernameLabel.place(x=x_offset, y=270, anchor="e")
    usernameEntry.place(x=x_offset+10, y=270, anchor="w", height=50)

    # Password field
    passwordLabel = Label(master=mainFrame, text="Password:", fg=blue, font=("Arial", 24))
    passwordEntry = Entry(master=mainFrame, bg=blue, fg=white, font=("Arial", 24))
    passwordLabel.place(x=x_offset, y=370, anchor="e")
    passwordEntry.place(x=x_offset+10, y=370, anchor="w", height=50)

    # Login button
    loginBtn = Button(mainFrame, text="Login", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=30, pady=5, command=OnLogin)
    loginBtn.place(x=(screen_width-240)/2, y=500, anchor="center")

# Function to show Register Account Page
def registerAccountPage():
    # Left Navigation Frame
    navFrame = Frame(window, bg=blue, width=240, height=screen_height)
    navFrame.grid(column=0, row=0, rowspan=10)
    navFrame.grid_propagate(0)

    # Module Name
    moduleName = Label(master=navFrame, text="Account\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor=CENTER)
    # Line
    lineLabel = Label(navFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)

    # Buttons for changing module
    changePwdBtn = Button(navFrame, text="Change\nPassword", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, 
    command=changePasswordPage)
    changePwdBtn.place(x=120, y=260, anchor="center", width=160, height=100)

    registerAccBtn = Button(navFrame, text="Register\nAccount", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white,
    command=registerAccountPage)
    registerAccBtn.place(x=120, y=400, anchor="center", width=160, height=100)

    deleteAccBtn = Button(navFrame, text="Delete\nAccount", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, 
    command=deleteAccountPage)
    deleteAccBtn.place(x=120, y=540, anchor="center", width=160, height=100)

    # On register button button clicked
    def onRegister():
        if (len(fNameEntry.get()) != 0 and len(lNameEntry.get()) != 0 and len(usernameEntry.get()) != 0 and len(pwdEntry.get()) != 0 and len(roleSelected.get()) != 0):
            fName = fNameEntry.get()
            lName = lNameEntry.get()
            username = usernameEntry.get()
            pwd = pwdEntry.get()
            
            if (roleSelected.get() == "Manager"):
                role = 2
            elif (roleSelected.get() == "Cashier"):
                role = 3

            if (auth.add_account(auth_db_conn, username, pwd, fName, lName, role)):
                messagebox.showinfo('', 'Account added successfully!')
                registerAccountPage()
            else:
                messagebox.showerror('Error', 'Process failed!')
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')

    # Register Account Form
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")

    # Register Account Title
    labelTitle = Label(inputFrame, text="Register Account", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')

    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=20, pady=5,
    command=loginPage)
    btnBack.place(x=50, y=70, anchor='w')

    # First Name
    fNameLabel = Label(inputFrame, text="First Name :", font=('Arial', 24), fg=blue)
    fNameLabel.place(x=x_offset, y=270, anchor="e")
    fNameEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    fNameEntry.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)

    # Last Name
    lNameLabel = Label(inputFrame, text="Last Name :", font=('Arial', 24), fg=blue)
    lNameLabel.place(x=x_offset, y=370, anchor="e")
    lNameEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    lNameEntry.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)

    # Username
    usernameLabel = Label(inputFrame, text="Username :", font=('Arial', 24), fg=blue)
    usernameLabel.place(x=x_offset, y=470, anchor="e")
    usernameEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    usernameEntry.place(x=x_offset+10, y=470, anchor="w", width=entry_width, height=50)

    # Password
    pwdLabel = Label(inputFrame, text="Password :", font=('Arial', 24), fg=blue)
    pwdLabel.place(x=x_offset, y=570, anchor="e")
    pwdEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    pwdEntry.place(x=x_offset+10, y=570, anchor="w", width=entry_width, height=50)

    # Role
    options = ["Manager", "Cashier"]
    roleSelected = StringVar()

    roleLabel = Label(inputFrame, text="Roles :", font=('Arial', 24), fg=blue)
    roleLabel.place(x=x_offset, y=670, anchor="e")
    roleEntry = OptionMenu(inputFrame, roleSelected, *options)
    roleEntry["font"] = "Arial 24"
    roleEntry["background"] = blue
    roleEntry["foreground"] = white
    roleEntry["menu"]["background"] = blue
    roleEntry["menu"]["foreground"] = white
    roleEntry["menu"]["font"] = "Arial 24"
    roleEntry.place(x=x_offset+10, y=670, anchor="w", width=entry_width, height=50)

    # Register button
    btnSubmit = Button(inputFrame, text="Register", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=30, pady=5,
    command=onRegister)
    btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

# Function to show change password page
def changePasswordPage():
    # Left Navigation Frame
    navFrame = Frame(window, bg=blue, width=240, height=screen_height)
    navFrame.grid(column=0, row=0, rowspan=10)
    navFrame.grid_propagate(0)

    # Module Name
    moduleName = Label(master=navFrame, text="Account\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor=CENTER)
    # Line
    lineLabel = Label(navFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)

    # Buttons for changing module
    changePwdBtn = Button(navFrame, text="Change\nPassword", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, 
    command=changePasswordPage)
    changePwdBtn.place(x=120, y=260, anchor="center", width=160, height=100)

    registerAccBtn = Button(navFrame, text="Register\nAccount", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white,
    command=registerAccountPage)
    registerAccBtn.place(x=120, y=400, anchor="center", width=160, height=100)

    deleteAccBtn = Button(navFrame, text="Delete\nAccount", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, 
    command=deleteAccountPage)
    deleteAccBtn.place(x=120, y=540, anchor="center", width=160, height=100)

    # On change password button event
    def onChangePwd():
        if (len(changePwdEntry.get()) != 0 and len(confirmPwdEntry.get()) != 0):
            global loginUserID
            pwd = changePwdEntry.get()
            pwdConfirm = confirmPwdEntry.get()
            if (pwd == pwdConfirm):
                if (auth.password_change(auth_db_conn, loginUserID, pwd)):
                    messagebox.showinfo('', "Password changed successfully!")
                    changePasswordPage()
                else:
                    messagebox.showerror('Error', 'Process failed!')
            else:
                messagebox.showerror('Error', 'Passwords do not match!')
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')

    # Change Password Form
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")

    # Change Passowrd Title
    labelTitle = Label(inputFrame, text="Change Password", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')

    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=20, pady=5,
    command=loginPage)
    btnBack.place(x=50, y=70, anchor='w')

    # New Password
    changePwdLabel = Label(inputFrame, text="New Password :", font=('Arial', 24), fg=blue)
    changePwdLabel.place(x=x_offset, y=270, anchor="e")
    changePwdEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    changePwdEntry.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)

    # Confirm Password
    confirmPwdLabel = Label(inputFrame, text="Confirm Password :", font=('Arial', 24), fg=blue)
    confirmPwdLabel.place(x=x_offset, y=370, anchor="e")
    confirmPwdEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    confirmPwdEntry.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)

    # Change Password button
    btnSubmit = Button(inputFrame, text="Change Password", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=30, pady=5,
    command=onChangePwd)
    btnSubmit.place(x=(screen_width-240)/2, y=600, anchor='center')

# Function to show Delete Account Page
def deleteAccountPage():
    # Left Navigation Frame
    navFrame = Frame(window, bg=blue, width=240, height=screen_height)
    navFrame.grid(column=0, row=0, rowspan=10)
    navFrame.grid_propagate(0)

    # Module Name
    moduleName = Label(master=navFrame, text="Account\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor=CENTER)
    # Line
    lineLabel = Label(navFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
    
    # Buttons for changing module
    changePwdBtn = Button(navFrame, text="Change\nPassword", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, 
    command=changePasswordPage)
    changePwdBtn.place(x=120, y=260, anchor="center", width=160, height=100)

    registerAccBtn = Button(navFrame, text="Register\nAccount", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white,
    command=registerAccountPage)
    registerAccBtn.place(x=120, y=400, anchor="center", width=160, height=100)

    deleteAccBtn = Button(navFrame, text="Delete\nAccount", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, 
    command=deleteAccountPage)
    deleteAccBtn.place(x=120, y=540, anchor="center", width=160, height=100)

    # Delete Account Form
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")

    # Delete Account Title
    labelTitle = Label(inputFrame, text="Delete Account", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')

    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=20, pady=5,
    command=loginPage)
    btnBack.place(x=50, y=70, anchor='w')

    # Delete Account on click
    def onDelete():
        if (len(accSelected.get()) != 0 and len(pwdEntry.get()) != 0):
            global loginUserID
            userID = int(accSelected.get()[0:accSelected.get().index(":")])
            pwd = pwdEntry.get()
            if userID == loginUserID:
                messagebox.showerror('Error', 'Cannot delete current account!')
            else:
                if (auth.delete_account(auth_db_conn, userID) and pwd == auth.getPassword(auth_db_conn, loginUserID)):
                    messagebox.showinfo('', "Account deleted successfully!")
                    deleteAccountPage()
                else:
                    messagebox.showerror('Error', "Process failed!")
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')

    # Accounts
    accounts = auth.getUserList(auth_db_conn)
    options = []
    for acc in accounts:
        options.append(str(acc[0]) + " : " + acc[1])

    accSelected = StringVar()

    roleLabel = Label(inputFrame, text="Account :", font=('Arial', 24), fg=blue)
    roleLabel.place(x=x_offset, y=270, anchor="e")
    roleEntry = OptionMenu(inputFrame, accSelected, *options)
    roleEntry["font"] = "Arial 24"
    roleEntry["background"] = blue
    roleEntry["foreground"] = white
    roleEntry["menu"]["background"] = blue
    roleEntry["menu"]["foreground"] = white
    roleEntry["menu"]["font"] = "Arial 24"
    roleEntry.place(x=x_offset+10, y=270, anchor="w", width=entry_width, height=50)

    # Password
    pwdLabel = Label(inputFrame, text="Password :", font=('Arial', 24), fg=blue)
    pwdLabel.place(x=x_offset, y=370, anchor="e")
    pwdEntry = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    pwdEntry.place(x=x_offset+10, y=370, anchor="w", width=entry_width, height=50)

    # Delete button
    btnSubmit = Button(inputFrame, text="Delete", font=('Arial', 18), bg=orange, fg=white, relief='flat', activebackground='#FB5F00', activeforeground=white, padx=30, pady=5, 
    command=onDelete)
    btnSubmit.place(x=(screen_width-240)/2, y=600, anchor='center')

window = Tk()

window.geometry("1440x1024")

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

loginPage()

window.mainloop()