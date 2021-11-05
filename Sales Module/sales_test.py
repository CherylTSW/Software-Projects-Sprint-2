import unittest
from tkinter import *
import sales

class TestInventory(unittest.TestCase):

    # Test case to test if Sales Table is created successfully
    def test_create_table(self):
        sales.execute_sql_file("SalesTable.sql")
        mydb = sales.connect_db()

        # Iterate through the cursor to obtain the tables present in database
        myCursor = mydb.cursor()
        myCursor.execute("SHOW TABLES")
        result = ""
        for table in myCursor:
            result += str(table)
        print(result)

        # If SQL code from file executed successfully, table should be created and result != ""
        self.assertNotEqual(result, "")
    
    # Test case to test if add_sales() INSERT sales record into the table successfully
    def test_add_sales(self):
        result = sales.add_sales("Panadol", 300.00)

        # result = False if error occurs while adding sales record
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()