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

    # Test case to test if add_sales() INSERT sales record into the table successfully
    def test_delete_sales(self):
        result = sales.delete_sales(1)

        # result = False if error occurs while adding sales record
        self.assertTrue(result)

    # Test case to test if get_all_sales() retrieve items from the database successfully
    def test_get_all_sales(self):
        # Call the method and print the rows of the table if result != False
        result = sales.get_all_sales()
        if(result):
            for row in result:
                print(row)
        
        # result = False if error occurs while getting the sales
        self.assertTrue(result)

    # Test case to test if get_sales_by_id() retrieve correct items from the database successfully
    def test_get_sales_by_id(self):
        # Call the method and print the record retrieved to see if expected item is retrieved
        result = sales.get_sales_by_id(1)
        if(result):
            for row in result:
                print(row)

        # result = False if error occurs while getting the inventory
        self.assertTrue(result)

    # Test case to test if get_sales_by_name() retrieve correct items from the database successfully
    def test_get_sales_by_name(self):
        # Call the method and print the record retrieved to see if expected item is retrieved
        result = sales.get_sales_by_name("Paracetamol 10 Tablets")
        if(result):
            for row in result:
                print(row)

        # result = False if error occurs while getting the inventory
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()