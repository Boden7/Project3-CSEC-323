# admin.py
# Date: 9/11/24
# Name: Brenden Shelton
# Program for an admin to create user accounts on the system

# use module getpass and crypt
# mksalt(crypt.METHOD_SHA512)

import getpass, bcrypt, re, uuid

# prompt the user to enter a username, full name, and password that meets the policies
def main():
    # open the user_innformation.txt and password.txt files for writing
    account_file = open("C:/Users/Br3nd/OneDrive - Randolph-Macon College/Comp Science/System Security/HW1/account.txt", "a")
    account_info_file = open("C:/Users/Br3nd/OneDrive - Randolph-Macon College/Comp Science/System Security/HW1/account_info.txt", "a")
    
    # acount.txt file path for checking userid uniqness
    account_file_path = "C:/Users/Br3nd/OneDrive - Randolph-Macon College/Comp Science/System Security/HW1/account.txt"
    # load exisitng userids from the file
    existing_user_ids = load_existing_user_ids(account_file_path)
    # generate a random userid for the user being created
    user_id = generate_unique_user_id(existing_user_ids)


    # ask the user for a Username, full name, and password
    username = input("Enter a Username: ")
    full_name = input("Full Name: ")
    print("""
    # Password Policy
    # 1. The password must be at least 8 characters long
    # 2. The password must contain upper- and lower-case letters
    # 3. The password must contain a number
    # 4. The password must contain a non-alphanumeric character
    """)
    password = getpass.getpass("Password: ")
    # check to make sure the password entered fits the criterea
    if password_check(password) != True:
        print("Invalid password")
        print("""
        # Password Policy
        # 1. The password must be at least 8 characters long
        # 2. The password must contain upper- and lower-case letters
        # 3. The password must contain a number
        # 4. The password must contain a non-alphanumeric character
        """)
        exit(0)

    # create the salt value and hash the given password to be stored in the account.txt file
    # Unix version
    # salt = crypt.mksalt(METHOD_SHA512)
    # hashed_password = crypt.crypt(password, salt)
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt) # convert password to bytes

    # add userid and hashed password to account.txt file
    account_file.write(f"{user_id},{salt.decode()},{hashed_password.decode()}\n") # must decode the bytes into string and add newline character

    # add account information to the account_info.txt file
    account_info_file.write(f"{user_id},{username},{full_name}\n") # have to manually add newline character when writing to a file

    # close the files
    account_file.close()
    account_info_file.close()


    


# checks to see if a given string meets the password requirements
def password_check(password):
    # password policy
    # 1. The password must be at least 8 characters long
    # 2. The password must contain upper- and lower-case letters
    # 3. The password must contain a number
    # 4. The password must contain a non-alphanumeric character

    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains both upper- and lower-case letters
    elif not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains a number
    elif not re.search(r'[0-9]', password):
        return False
    
    # Check if the password contains a non-alphanumeric character
    elif not re.search(r'[\W_]', password): 
        return False

    else:
        return True
    
# loads userids from the given file into a set
def load_existing_user_ids(file_path):
    existing_ids = set()
    with open(file_path, 'r') as file:
        for line in file:
            user_id, salt, password = line.strip().split(',', 2)
            existing_ids.add(user_id)
    return existing_ids

# checks the given userids for uniqueness
def generate_unique_user_id(existing_ids):
    if len(existing_ids) > 0:
        new_id = int(max(existing_ids)) + 1 
    else:
        new_id = 10000000  
    return new_id



main()
    

