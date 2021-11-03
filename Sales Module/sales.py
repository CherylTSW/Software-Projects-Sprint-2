import mysql.connector
from mysql.connector import Error

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