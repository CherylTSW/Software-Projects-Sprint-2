import manufacturer
import mysql.connector
import pandas as pd

# Method to get the manufacturer details by ID
def report_toCSV():
    try:
        connection = manufacturer.connect_manufacturer_PHPDB()

        cursor = connection.cursor()
        sql_select_query = """select * from MANUFACTURER"""

        # Testing
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        for i in range(len(records)):
            print("\nRow Number", i)
            for j in range(len(records[i])):
                print (records[i][j])

        # Put the data into a dataframe
        df = pd.read_sql(sql_select_query, connection)
        print(df)

        # Convert to CSV file format
        df.to_csv("SalesReport.csv", index = False, header=True)

    except mysql.connector.Error as error:
        print("Unable to convert report to CSV: {}".format(error))
        return False

# Runs the Report Module
report_toCSV()
