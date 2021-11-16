import database

# Function to add account to database
def add_account(conn, username: str, pwd: str, firstName: str, lastName: str, role: int):
    # Add user into users table
    userQuery = f"""INSERT INTO Users (username, firstName, lastName, role, password) VALUES 
    ('{username}', '{firstName}', '{lastName}', {role}, '{pwd}');"""
    exec1 = database.execute_query(conn, userQuery)
    
    return exec1

# Function to delete account from database
def delete_account(conn, userID:int):
    # Delete the entry from users table
    deleteUserQuery = f"""DELETE FROM Users WHERE userID={userID};"""

    exec1 = database.execute_query(conn, deleteUserQuery)
    
    return exec1
    
# Function to get userID from username
def get_userID(conn, username:str):
    findQuery = f"""SELECT userID FROM Users WHERE username='{username}'"""
    result = database.read_query(conn, findQuery)
    userID = result[0][0]

    return userID

# Function to edit password of a user
def password_change(conn, userID:int, password:str):
    # Change password in users table
    pwdChangeQuery = f"""UPDATE Users SET password='{password}' WHERE userID={userID}"""
    
    exec1 = database.execute_query(conn, pwdChangeQuery)

    return exec1 

# Function to check whether credentials is correct and return the role
def login(conn, username:str, pwd:str):
    # Query to find whether the account exists
    findUserQuery = f"""
    SELECT EXISTS (SELECT * FROM Users WHERE username='{username}' AND password='{pwd}')
    """
    
    content = database.read_query(conn, findUserQuery)

    status = content[0][0]

    return status == 1
    """
    if (status == 1):
        # If account is found, login successful, get role and userID
        getUserInfo = f
        SELECT * FROM Users WHERE username='{username}' AND password='{pwd}'
        
        result = database.read_query(conn, getUserInfo)
        print("Login successfully")
        return True
        # return result[0][0], result[0][4]
    else:
        print("Login failed, username or password not found.")
        return False
        """

# Function to return a list of userID and username
def getUserList(conn):
    findUsersQuery = f"""
    SELECT userID, username FROM Users
    """

    result = database.read_query(conn, findUsersQuery)

    return result

# Function to get password
def getPassword(conn, userID:int):
    findPwdQuery = f"""
    SELECT password FROM Users WHERE userID={userID}
    """

    result = database.read_query(conn, findPwdQuery)

    return result[0][0]