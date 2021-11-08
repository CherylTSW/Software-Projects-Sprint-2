import manufacturer
import mysql.connector

# Method to get the manufacturer details by ID
def report_toCSV():
    try:
        connection = manufacturer.connect_manufacturer_PHPDB()

        cursor = connection.cursor()
        sql_select_query = """select * from MANUFACTURER"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        for i in range(len(records)):
            for j in range(len(records[i])):
                print (records[i][j])

    except mysql.connector.Error as error:
        print("Unable to convert report to CSV: {}".format(error))
        return False

report_toCSV()