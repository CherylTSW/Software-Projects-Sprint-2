from tkinter.font import BOLD
import mysql.connector
from tkinter import *
from mysql.connector import Error

# Method to create the database PHPDB
def create_inventory_db():
    # Create the database PHPDB if it does not exist
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
    )
    mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS PHPDB")
    mydb.close()

# Method to connect to database PHPDB. 
# Return the connection object if successful, else return False
def connect_inventory_db():
    # Create connection to database
    try:
        # If connection created successfully, return the connection object
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "PHPDB"
        )
        return mydb
    except Error:
        # If error occurs, return False
        return False

# Method to execute SQL code from file
def execute_sql_file(filename):
    mydb = connect_inventory_db()

    # Open file to read, then split the content with ';' as delimiter to form mSQL code that can be executed
    file = open(filename, 'r')
    sqlCode = file.read().split(';')
    file.close()

    # Execute the code
    myCursor = mydb.cursor()
    for code in sqlCode:
        myCursor.execute(code)

    mydb.close()

# Method to add an inventory item using the itemName, itemPrice, and itemQuantity received as parameters.
# Return True if successful, else return False
def add_inventory(itemName: str, itemPrice: float, itemQuantity: int):
    try:
        # Create the INSERT code to be executed
        sqlInsert = f"INSERT INTO Items (itemName, itemPrice, itemQuantity) VALUES (%s, %s, %s)"
        data = (itemName, itemPrice, itemQuantity)

        # Connect to database and execute the command
        mydb = connect_inventory_db()
        myCursor = mydb.cursor()
        myCursor.execute(sqlInsert, data)
        mydb.commit()

        # Obtain the count of row affected
        result = myCursor.rowcount
        mydb.close()
        
        toReturn = False
        # If row affected > 0, the insertion is successful. Return True on success, else return false
        if(result > 0):
            toReturn = True

        return toReturn
        
    # If there is error, return False        
    except Error:
        return False

# Method to get all inventory item from the database
# Return the records if successful, else return False
def get_all_inventory():
    try:
        # try selecting all records from table Items, and return the result(the records)
        mydb = connect_inventory_db()
        query = "SELECT * FROM Items"
        myCursor = mydb.cursor()
        myCursor.execute(query)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to get inventory item by ID of the item
# Return the records if successful, else return False
def get_inventory_by_id(id: int):
    try:
        # try selecting all records from table Items with itemID matching the parameter 'id', and return the result(the records)
        mydb = connect_inventory_db()
        query = f"SELECT * FROM Items WHERE itemID = %s"
        itemID = (id,)
        myCursor = mydb.cursor()
        myCursor.execute(query, itemID)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to get inventory item by name of the item
# Return the records if successful, else return False
def get_inventory_by_name(name: str):
    try:
        # try selecting all records from table Items with itemName matching the parameter 'name', and return the result(the records)
        mydb = connect_inventory_db()
        query = f"SELECT * FROM Items WHERE itemName = %s"
        itemID = (name,)
        myCursor = mydb.cursor()
        myCursor.execute(query, itemID)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to edit the information of an inventory item with itemID = id(parameter) by replacing its itemName, itemPrice and itemQuantity with the parameter newName, newPrice and newQuantity.
# Return True if item is edited successfully, else return False
def edit_inventory(newName: str, newPrice: float, newQuantity: int, id: int):
    if(get_inventory_by_id(id)):
        # try updating the table Items by setting itemName = newName, itemPrice = newPrice, itemQuantity = newQuantity. Return True
        mydb = connect_inventory_db()
        query = f"Update Items SET itemName = %s, itemPrice = %s, itemQuantity = %s WHERE itemID = %s"
        itemID = (newName, newPrice, newQuantity, id)
        myCursor = mydb.cursor()
        myCursor.execute(query, itemID)
        mydb.commit()
        mydb.close()
        return True
    else:
        # return False if error occurs
        return False

# Method to display the items retrieved from database in a table form
def display_inventory(frame: Tk, startX: int, startY: int, items):
    # Declaring fields(used as table headings) and fieldsWidth(used to set width of each column)
    fields = ["ID", "Item Name", "Price(RM)", "Quantity"]
    fieldsWidth = [100, 600, 150, 150]
    fieldsXPos = [0, 100, 700, 850]

    # Get the number of rows and columns
    numberOfRow = len(items)
    numberOfColumn = len(items[0])

    # loop to create the Label()
    for x in range(numberOfRow):
        for y in range(numberOfColumn):
            heading = Label(frame, font=('Arial', 16, BOLD), text=fields[y], borderwidth=2, relief="ridge", bg='#344955', fg='#ffffff')
            heading.place(x=startX+fieldsXPos[y], y=startY, anchor="w", width=fieldsWidth[y], height=40)
            heading.config(highlightbackground='#ffffff')
            data = Label(frame, font=('Arial', 14), text=items[x][y], borderwidth=2, relief="ridge", bg='#344955', fg='#ffffff')
            data.config(highlightbackground='#ffffff')
            data.place(x=startX+fieldsXPos[y], y=startY+(x+1)*40, anchor="w", width=fieldsWidth[y], height=40)