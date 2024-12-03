# user.py
# Date: 9/15/24
# Name: Brenden Shelton
# Program for authenticating users and allowing password changes

import sys
import getpass
import bcrypt
import re

# File paths (use same ones as admin.py)
ACCOUNT_FILE = "C:/Users/Br3nd/OneDrive - Randolph-Macon College/Comp Science/System Security/HW1/account.txt"
ACCOUNT_INFO_FILE = "C:/Users/Br3nd/OneDrive - Randolph-Macon College/Comp Science/System Security/HW1/account_info.txt"

# Function to authenticate user
def authenticate_user(username):
    user_id = get_user_id(username)
    if user_id:
        account_data = load_account_data()
        if user_id in account_data:
            user_id, salt, stored_password = account_data[user_id]
            entered_password = getpass.getpass("Enter password: ")
            hashed_entered_password = bcrypt.hashpw(entered_password.encode(), salt.encode())
            
            if hashed_entered_password.decode() == stored_password:
                print("Success!! authentication valid.")
            else:
                print("Error!! authentication failed due to an invalid password.")
        else:
            print(f"Error: User {username} not found in account data.")
    else:
        print(f"Error: User {username} not found in account info.")

# Function to change password
def change_password(username):
    user_id = get_user_id(username)
    if user_id:
        account_data = load_account_data()
        if user_id in account_data:
            user_id, salt, stored_password = account_data[user_id]
            print(f"Changing password for user {username}")
            
            current_password = getpass.getpass("Current password: ")
            hashed_current_password = bcrypt.hashpw(current_password.encode(), salt.encode())
            
            if hashed_current_password.decode() == stored_password:
                new_password = get_new_password()
                if new_password:
                    # Generate a new salt for the new password
                    new_salt = bcrypt.gensalt()
                    
                    # Hash the new password with the new salt
                    new_hashed_password = bcrypt.hashpw(new_password.encode(), new_salt).decode()
                    
                    # Update the account file with the new salt and new hashed password
                    update_account_file(user_id, new_salt.decode(), new_hashed_password)
                    print("Password changed successfully!")
            else:
                print("Error: Incorrect current password.")
        else:
            print(f"Error: User {username} not found in account data.")
    else:
        print(f"Error: User {username} not found in account info.")


# Function to prompt and validate new password
def get_new_password():
    while True:
        new_password = getpass.getpass("New Password: ")
        if password_check(new_password):
            reentered_password = getpass.getpass("Re-enter new password: ")
            if new_password == reentered_password:
                return new_password
            else:
                print("Error: Passwords do not match.")
        else:
            print("Invalid password. Please follow the password policy.")

# Function to get user_id from username using account_info.txt
def get_user_id(username):
    with open(ACCOUNT_INFO_FILE, 'r') as file:
        for line in file:
            user_id, stored_username, full_name = line.strip().split(',')
            if stored_username == username:
                return user_id
    return None

# Function to load account data from account.txt
def load_account_data():
    account_data = {}
    with open(ACCOUNT_FILE, 'r') as file:
        for line in file:
            user_id, salt, hashed_password = line.strip().split(',')
            account_data[user_id] = (user_id, salt, hashed_password)
    return account_data

# Function to update account file with new password
def update_account_file(user_id, salt, new_password):
    account_data = load_account_data()
    account_data[user_id] = (user_id, salt, new_password)

    with open(ACCOUNT_FILE, 'w') as file:
        for user, (user_id, salt, password) in account_data.items():
            file.write(f"{user_id},{salt},{password}\n")

# Password policy check
def password_check(password):
    if len(password) < 8:
        return False
    elif not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    elif not re.search(r'[0-9]', password):
        return False
    elif not re.search(r'[\W_]', password): 
        return False
    else:
        return True

# Main function
def main():
    # Check for command-line arguments using sys.argv
    if len(sys.argv) < 2:
        print("Usage: user.py [-p] username")
        sys.exit(1)

    # Extract the username and optional -p flag from sys.argv
    if '-p' in sys.argv:
        if len(sys.argv) == 3:
            username = sys.argv[2]
            change_password(username)
        else:
            print("Usage: user.py -p username")
            sys.exit(1)
    else:
        if len(sys.argv) == 2:
            username = sys.argv[1]
            authenticate_user(username)
        else:
            print("Usage: user.py username")
            sys.exit(1)

main()