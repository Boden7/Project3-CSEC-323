---------------------------- README --------------------------- 

** Bank Account and Client Management System Overview **

* This project allows you to manage clients and their bank accounts. 
* Each client will create a password for their account, which can later be changed if desired. 
* A client can have one or more bank accounts, with the possibility to create, 
    display, transfer, deposit, and withdraw funds from checking or savings accounts. 
* The system also includes functionality for handling overdrafts, interest calculations, and account transaction histories. 
* Additionally, all client details, including name,
    phone number, and address, are validated to ensure accuracy and conformity.

---------------------------- FEATURES --------------------------
* Client Class: Manage client information, including name, phone number, address, password, and associated bank accounts.
* Bank Account Class: Base class for managing both checking and savings accounts.
* Checking Account: Inherits from BankAccount and supports specific checking account operations (e.g., interest calculation, withdrawals, transfers).
* Savings Account: Inherits from BankAccount and includes overdraft handling and interest calculation.

Setup Instructions: 
Prerequisites
Python 3+ 
Required libraries: unittest, os, cryptography (for encryption/decryption of transaction data files)
(pip install cryptography)

------------------------------ USAGE --------------------------
Downloading the project:
Files needed: AES_CBC.py, address.py, bankAccount.py, checkingAccount.py, client.py, name.py, phoneNumber.py, savingsAccount.py, transaction.py, password.py
Download the files from the project's repository: https://github.com/Boden7/Project2-CSEC-323

Files needed for testing: test_address.py, test_checking.py, test_client.py, test_name.py, test_password.py, test_phoneNumber.py, test_savings.py, test_transaction.py

Creating and Managing Clients:
To create a new client and assign them a bank account, you can follow this example:

from Client import Client
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount

# Create a new client
client1 = Client(Name("First", "Last"), Address("100 Street", "City", "VA"), PhoneNumber("8041234567"), "checking", Password("Tester123!"))

# Display client information
client1.__repr__()

# Open a checking account
checking_account = CheckingAccount(accountNum from Client, clientNum from Client, balanceIn = 500.0)

# Open a savings account
savings_account = SavingsAccount(accountNum from Client, clientNum from Client, balanceIn = 1000.0)

# Add accounts to the client
client1.openBankAccount(checking_account)
client1.openBankAccount(savings_account)

# Display accounts and transactions
client1.printTransactionList()

# Close an account by withdrawing all funds
client1.closeBankAccount(checking_account)

---------------------------- Client Class Details -----------------------------
* The Client class includes:

Attributes: 
name (first and last names, validated for length and format)
phone (must be a valid 10 digit phone number)
address (street, city, valid state abbreviation)
password (client password, validated for length and no special characters)
_clientCounter (unique, starting from 100 and incrementing upon each new client creation)
A list of associated bank accounts.

Methods:
__init__(): Initializes the client with valid details.
__repr__(): Displays the client's information, excluding their password.
openBankAccount(account): Adds a bank account to the client's list, if the account does not already exist.
closeBankAccount(account): Withdraws all funds from the specified account and removes it from the list of accounts.
changePassword(password): Changes the password of a Client.
__eq__(): Compares two clients to see if they are the same. 

----------------------- Bank Account Classes ----------------------
The BankAccount class is abstract and provides shared functionality, 
    such as deposit, withdrawal, and transfer methods. The actual logic for 
        each account type (checking or savings) is implemented in the respective subclasses.

* Checking Account: 
The CheckingAccount class inherits from BankAccount and adds functionality specific to checking accounts:

Interest Calculation: 1.5% interest rate.
Withdrawals: Can only withdraw funds if there are enough funds available.
Transfers: Can transfer funds to another account.
Transactions: Supports printing, reading, and writing transactions to a file (with encryption/decryption).
File Storage: Transaction details are saved in the file checking.txt with encrypted data.


* Savings Account: 
The SavingsAccount class also inherits from BankAccount and adds features specific to savings accounts:

Interest Calculation: 4.0% interest rate.
Overdraft Handling: Allows a maximum of three overdrafts, with different fees for each occurrence.
Transaction Limits: Similar to checking accounts, but with additional restrictions on withdrawals after overdraft incidents.
File Storage: Transaction details are saved in the file savings.txt with encrypted data.

Validation
The system performs several validations to ensure correct data entry:

Client Name: The first name can be up to 25 characters, and the last name can be up to 40 characters. 
    Special characters are not allowed.
Phone Number: Must be a String that contains a 10-digit number and cannot start with 0.
Address: (street, city, valid state abbreviation)
   Street: Cannot be empty, max of 30 characters, no special characters.
   City: Cannot be empty, max of 30 characters, no special characters.
   State: Must be a valid state abbreviation: VA, MD, NJ, PA, DE, NC, WV, DC
Password: Must be a String between 8 and 16 characters in length inclusive that does not contain blank characters
or explicitly specified special characters shown in the password parameters.
