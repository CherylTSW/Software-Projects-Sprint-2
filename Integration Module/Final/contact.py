import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter.font import BOLD

# This is to create the database PHPDB
def create_database():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")

    #This is to create a cursor object using the cursor() method
    cursor = connection.cursor()

    #This will drop the database if it already exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS PHPDB")

    #This is to retrieve the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

    #This is to close the connection
    cursor.close()

# This is to connect to the database PHPDB
def connect_contact_db():
    try:
        connection = mysql.connector.connect(
        host="localhost",
        database="PHPDB",
        user="root",
        password="")
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server Version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record) 
        return connection   

    except Error:
        print("Error while connecting to MySQL", Error)

# This is to create a new table named CONTACTMODULE in the database
def create_contact_table(filename):
    try:
        connection = connect_contact_db()

        file = open(filename, 'r')
        sqlCode = file.read().split(';')
        file.close()
       
        cursor = connection.cursor()
        for code in sqlCode:
            cursor.execute(code)

        print("Contact Module Table created successfully")
        
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

# This is to insert a new row of information in the CONTACTMODULE with the user input        
def insert_contact(orderId: int, orderDate: str, manufacturerId: int, productId: int, quantity: int, totalPrice: float):
    try:
        connection = connect_contact_db()

        mySql_insert_query = f"INSERT INTO CONTACTMODULE (orderId, orderDate, manufacturerId, productId, quantity, totalPrice) VALUES (%s, %s, %s, %s, %s, %s) "

        information = (orderId, orderDate, manufacturerId, productId, quantity, totalPrice)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, information)
        connection.commit()

        result = cursor.rowcount
        print(result, "Record inserted successfully into Contact table")
        
        #If the row affected > 0, the insertion is successful. True is returned if success, otherwise return false
        toReturn = False
        if(result > 0):
            toReturn = True

        cursor.close()
        return toReturn

    except mysql.connector.Error as error:
        print("Failed to insert record into Contact table {}".format(error))
        return False

# This is to delete the row of information based on the user input
def delete_contact(orderId: int):
    try:
        connection = connect_contact_db()
        myCursor = connection.cursor()

        # Delete a record
        deleting = f"Delete from CONTACTMODULE where orderId = " + str(orderId)
        myCursor.execute(deleting)
        connection.commit()

        # This is to count the number of rows affected
        result = myCursor.rowcount
        print('Number of rows deleted: ', result)

        #This is to verify using select query
        myCursor.execute(deleting)
        records = myCursor.fetchall()
        if len(records) == 0:
            print("Record has been deleted successfully")
        return True

    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
        return False

#This is to retreieve the contact details by ID
def get_contact_by_ID(orderID: int):
    try:
        connection = connect_contact_db()
        myCursor = connection.cursor()
        
        selecting = f"Select * from CONTACTMODULE where orderId = " + str(orderID)
        myCursor.execute(selecting)
        records = myCursor.fetchall()
        print(records)

        return records

    except mysql.connector.Error as error:
        print("Failed to display record from table: {}".format(error))
        return False

#This is to display the contact details for the user to see
def display_contact(frame: Tk, startX: int, startY: int, contact):
    
    #This is to declare the fields(used as table headings) and fieldsWidth(used for setting the width of each column)
    fields = ["Order ID" , "Order Date", "ManufacturerID", "Product ID", "Quantity", "Total Price"]
    fieldsWidth = [150, 150, 200, 200, 150, 200]
    fieldsXPos = [0, 150, 300, 500, 700, 850, 1050]

    #This is to obtain the number of rows and columns
    noOfRow = len(contact)
    noOfColumn = len(contact[0])

    #This is to create the Label()
    for x in range(noOfRow):
        for y in range(noOfColumn):
            heading = Label(frame, font=('Arial', 16, BOLD), text=fields[y], borderwidth=2, relief="ridge", bg='#344955', fg='#ffffff')
            heading.place(x=startX+fieldsXPos[y], y=startY, anchor="w", width=fieldsWidth[y], height=40)
            heading.config(highlightbackground='#ffffff')
            data = Label(frame, font=('Arial', 14), text=contact[x][y], borderwidth=2, relief="ridge", bg='#344955', fg='#ffffff')
            data.config(highlightbackground='#ffffff')
            data.place(x=startX+fieldsXPos[y], y=startY+(x+1)*40, anchor="w", width=fieldsWidth[y], height=40)