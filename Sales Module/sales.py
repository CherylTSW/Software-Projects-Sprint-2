import mysql.connector
from mysql.connector import Error
from tkinter import *

# Method to connect to database SPRINT1. 
# Return the connection object if successful, else return False
def connect_db():
    # Create connection to database
    try:
        # If connection created successfully, return the connection object
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "SPRINT1"
        )
        return mydb
    except Error:
        # If error occurs, return False
        return False

# Method to execute SQL code from file
def execute_sql_file(filename):
    mydb = connect_db()

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
def add_sales(salesItem: str, salesAmount: float):
    try:
        # Create the INSERT code to be executed
        sqlInsert = f"INSERT INTO Sales (salesItem, salesAmount) VALUES (%s, %s)"
        data = (salesItem, salesAmount)

        # Connect to database and execute the command
        mydb = connect_db()
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

# Function to return sales from table
def get_all_sales():
    try:
        # SQL command to get the list of sales
        salesQuery = """
        SELECT * FROM Sales
        """
        # Connect to database and execute the command
        mydb = connect_db()
        myCursor = mydb.cursor()
        myCursor.execute(salesQuery)
        result = myCursor.fetchall()
        mydb.close()
        # Return the list of sales
        # Expected output [(salesID, salesItem, salesAmount/Price), ...]
        return result

    # If there is error, return false
    except Error:
        return False

# Method to get sales item by ID of the sales
# Return the records if successful, else return False
def get_sales_by_id(id: int):
    try:
        # Get sales item where sales ID == given id
        mydb = connect_db()
        query = f"SELECT * FROM Sales WHERE salesID={id}"
        myCursor = mydb.cursor()
        myCursor.execute(query)
        result = myCursor.fetchall()
        mydb.close()
        # Expected output [(salesID, salesItem, salesAmount/Price)]
        return result
    except Error:
        # return False if error occurs
        return False

# Method to get sales item by name of the item
# Return the records if successful, else return False
def get_sales_by_name(item: str):
    try:
        # Get sales item where sales item == item
        mydb = connect_db()
        query = f"SELECT * FROM Sales WHERE salesItem='{item}'"
        myCursor = mydb.cursor()
        myCursor.execute(query)
        result = myCursor.fetchall()
        mydb.close()
        return result
    except Error:
        # return False if error occurs
        return False

# Method to delete the items retrieved from database in a table form
def delete_sales(salesID: int):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        if(get_sales_by_id(salesID)):
            print("Table before deleting a row")
            sql_select_query = f"SELECT * FROM sales WHERE salesID = %s"
            formatString = (salesID,)
            cursor.execute(sql_select_query, formatString)
            record = cursor.fetchone()
            print(record)

            # Delete a record
            sql_Delete_query = f"DELETE FROM sales WHERE salesID = %s"
            formatString = (salesID,)
            cursor.execute(sql_Delete_query, formatString)
            connection.commit()
            print('number of rows deleted', cursor.rowcount)

            # Verify using select query (optional)
            cursor.execute(sql_select_query, formatString)
            records = cursor.fetchall()
            if len(records) == 0:
                print("Sales Record Deleted successfully ")
                return True

        else:
            return False

    except mysql.connector.Error as error:
        print("Failed to delete sales record from table: {}".format(error))
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Method to display the items retrieved from database in a table form
def display_sales(window: Tk, startColumn: int, startRow: int, items):
    # Declaring fields(used as table headings) and fieldsWidth(used to set width of each column)
    fields = ["ID", "Sales", "Price"]
    fieldsWidth = [10, 30, 15]

    # Get the number of rows and columns
    numberOfRow = len(items)
    numberOfColumn = len(items[0])

    # loop to create the Label()
    for x in range(numberOfRow):
        for y in range(numberOfColumn):
            heading = Label(window, font=('Arial', 12), text=fields[y], width=fieldsWidth[y], borderwidth=2, relief="ridge")
            heading.grid(column=startColumn+y, row=startRow)
            data = Label(window, font=('Arial', 12), text=items[x][y], width=fieldsWidth[y], borderwidth=2, relief="ridge")
            data.grid(column=startColumn+y, row=startRow+x+1)