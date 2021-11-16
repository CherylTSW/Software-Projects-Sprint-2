import mysql.connector
from mysql.connector import Error

# Function to connect to DB
def create_db_connection(config):
    connection = None
    try:
        connection = mysql.connector.connect(**config)
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to execute query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except Error as err:
        print(f"Error: '{err}'")
        return False

# Function for read query, e.g. SELECT
def read_query(connection, query):
    cursor = connection.cursor()
    results = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        content = [] 

        for result in results:
            content.append(result)
        
        return content
    except Error as err:
        print(f"Error: '{err}'")

# Function to connect to server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Method to execute SQL code from file
def execute_sql_file(filename):
    conn = create_server_connection("localhost", "root", "")
    # Open file to read, then split the content with ';' as delimiter to form mSQL code that can be executed
    file = open(filename, 'r')
    sqlCode = file.read().split(';')
    file.close()

    for code in sqlCode:
        execute_query(conn, code)