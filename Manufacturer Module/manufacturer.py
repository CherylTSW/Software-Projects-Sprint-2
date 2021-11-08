from tkinter.font import BOLD
import mysql.connector
from tkinter import *
from mysql.connector import Error

# Method to create the PHPDB database
def create_manufacturer_PHPDB():
    # Establishing the connection
    conn = mysql.connector.connect(user='root', password='', host='localhost')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping PHPDB database if already exists.
    cursor.execute("CREATE DATABASE IF NOT EXISTS PHPDB")

    # Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

    # Closing the connection
    conn.close()

# Method to connect to the PHPDB database
def connect_manufacturer_PHPDB():
    try:
        connection = mysql.connector.connect(host="localhost", database="PHPDB", user="root", password="")

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

# Method to create the Manufacturer table
def create_manufacturer_table(filename):
    try:
        connection = connect_manufacturer_PHPDB()

        file = open(filename, 'r')
        sqlCode = file.read().split(';')
        file.close()

        cursor = connection.cursor()

        for code in sqlCode:
            cursor.execute(code)

        print("Manufacturer Table created successfully ")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

# Method to add the manufacturer details
def add_manufacturer(ManufacturerID: int, ManufacturerFirstName: str, ManufacturerLastName: str, ManufacturerItem: str, ManufacturerStreetAddress: str, ManufacturerPhoneNumber: str):
    try:
        connection = connect_manufacturer_PHPDB()

        mySql_insert_query = """INSERT INTO MANUFACTURER (ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber) 
                            VALUES 
                            (%s, %s, %s, %s, %s, %s) """

        data = (ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()

        result = cursor.rowcount
        print(result, "Record inserted successfully into Manufacturer table")

        # If row affected > 0, the insertion is successful. Return True on success, else return false
        toReturn = False
        if(result > 0):
            toReturn = True

        cursor.close()

        return toReturn

    except mysql.connector.Error as error:
        print("Failed to insert record into Manufacturer table {}".format(error))
        return False

# Method to remove the manufacturer details
def remove_manufacturer(ManufacturerID: int):
    try:
        connection = connect_manufacturer_PHPDB()

        cursor = connection.cursor()
        print("Manufacturer table before deleting a row")
        sql_select_query = """select * from MANUFACTURER where ManufacturerID = """ + str(ManufacturerID)
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)

        # Delete a record
        sql_Delete_query = """Delete from MANUFACTURER where ManufacturerID = """ + str(ManufacturerID)
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('number of rows deleted', cursor.rowcount)

        # Verify using select query
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        if len(records) == 0:
            print("Record Deleted successfully ")

        return True

    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
        return False

# Method to get the manufacturer details by ID
def get_manufacturer_by_id(ManufacturerID: int):
    try:
        connection = connect_manufacturer_PHPDB()

        cursor = connection.cursor()
        sql_select_query = """select * from MANUFACTURER where ManufacturerID = """ + str(ManufacturerID)
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print(records)

        return records

    except mysql.connector.Error as error:
        print("Failed to display record from table: {}".format(error))
        return False

# Method to display the manufacturer details
def display_manufacturer(frame: Tk, startX: int, startY: int, manufacturers):
    # Declaring fields(used as table headings) and fieldsWidth(used to set width of each column)
    fields = ["Manufacturer ID", "First Name", "Last Name", "Manufacturer Item", "Manufacturer Street Address", "Phone Number"]
    fieldsWidth = [200, 200, 200, 200, 300, 200]
    fieldsXPos = [0, 200, 400, 600, 800, 1100, 1300]

    # Get the number of rows and columns
    numberOfRow = len(manufacturers)
    numberOfColumn = len(manufacturers[0])

    # loop to create the Label()
    for x in range(numberOfRow):
        for y in range(numberOfColumn):
            heading = Label(frame, font=('Arial', 16, BOLD), text=fields[y], borderwidth=2, relief="ridge", bg='#344955', fg='#ffffff')
            heading.place(x=startX+fieldsXPos[y], y=startY, anchor="w", width=fieldsWidth[y], height=40)
            heading.config(highlightbackground='#ffffff')
            data = Label(frame, font=('Arial', 14), text=manufacturers[x][y], borderwidth=2, relief="ridge", bg='#344955', fg='#ffffff')
            data.config(highlightbackground='#ffffff')
            data.place(x=startX+fieldsXPos[y], y=startY+(x+1)*40, anchor="w", width=fieldsWidth[y], height=40)
