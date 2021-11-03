import authentication as auth
import database as db

config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "SPRINT1"
        }

auth_db_conn = db.create_db_connection(config)

# Add an account 
auth.add_account(auth_db_conn, "test", "123", "pol", "tato", 1)

# Login
print(auth.login(auth_db_conn, "test", "123"))

# Change password
# auth.password_change(auth_db_conn, auth.get_userID(auth_db_conn, "abc"), "456")

# Delete an account with userID
auth.delete_account(auth_db_conn, auth.get_userID(auth_db_conn, "test"))