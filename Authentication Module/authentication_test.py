import unittest

import authentication as auth
import database as db

test_config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "Test"
        }

# Create test tables in database
create_table_query = """
CREATE TABLE Users (
    userID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    role INT(3) NOT NULL,
    password VARCHAR(30) NOT NULL
);"""

class TestAuthentication(unittest.TestCase):
    def test_add_account(self):
        """
        Test that whether account is added successfully
        """
        
        # Create test database
        first_connection = db.create_server_connection("localhost", "root", "")
        start_fresh_queries = ["DROP DATABASE IF EXISTS Test;", "CREATE DATABASE Test;"]

        for query in start_fresh_queries:
            db.execute_query(first_connection, query)

        conn = db.create_db_connection(test_config)

        db.execute_query(conn, create_table_query)

        self.assertTrue(auth.add_account(conn, "test", "test", "test", "test", 1))

    def test_delete_account(self):
        """
        Test that whether account is deleted successfully
        """
        
        # Create test database
        first_connection = db.create_server_connection("localhost", "root", "")
        start_fresh_queries = ["DROP DATABASE IF EXISTS Test;", "CREATE DATABASE Test;"]

        for query in start_fresh_queries:
            db.execute_query(first_connection, query)

        conn = db.create_db_connection(test_config)

        db.execute_query(conn, create_table_query)

        auth.add_account(conn, "test", "test", "test", "test", 1)

        self.assertTrue(auth.delete_account(conn, auth.get_userID(conn, "test")))

    def test_change_password(self):
        """
        Test that whether account password is changed successfully
        """  

        # Create test database
        first_connection = db.create_server_connection("localhost", "root", "")
        start_fresh_queries = ["DROP DATABASE IF EXISTS Test;", "CREATE DATABASE Test;"]

        for query in start_fresh_queries:
            db.execute_query(first_connection, query)

        conn = db.create_db_connection(test_config)

        db.execute_query(conn, create_table_query)

        auth.add_account(conn, "test", "test", "test", "test", 1)

        self.assertTrue(auth.password_change(conn, auth.get_userID(conn, "test"), "new pwd"))

if __name__ == '__main__':
    unittest.main()