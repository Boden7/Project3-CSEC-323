""" 
This module defines the CheckingAccount class.
@author: Hunter Peacock, Boden Kahn, Brenden Shelton, and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a CheckingAccount
This class is inherited from the BankAccount superclass
"""

# Import statements
from bankAccount import BankAccount
from transaction import Transaction
from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC

# Hunter 
class CheckingAccount(BankAccount):

    # Constructs a CheckingAccount object.
    #
    #  @param balanceIn: The starting balance of the CHecking Account (Floating point)
    #
    #  @ensure CheckingAccount object successfully created
    def __init__(self, accountNum, clientNum, balanceIn = 0.0, accountType = 'checking'):
        super().__init__(accountNum, clientNum, balanceIn, accountType)

    # Deposits money into the account if the transaction is valid and records the transaction
    #
    #  @param amount: the amount to be deposited
    #
    #  @require amount must be a positive, floating-point value
    #
    #  @return The success or failure of the deposit
    # Boden
    def deposit(self, amount):
        # Make sure the amount to deposit a float is not negative
        assert(isinstance(amount, float))
        assert(amount > 0)
        # Process the transaction and update necessary variables
        depositTransaction = Transaction("deposit", self.getNextTransactionNum(), amount)
        # add deposit to list of transactions
        self._accountTransactions.append(depositTransaction)
        self._writeTransaction(depositTransaction)
        self._balance += amount
        return True

    # Withdraws money from the account if the transaction is valid and records the transaction
    #
    #  @param amount: the amount to be withdrawn
    #
    #  @require amount must be a positive, floating-point value
    #
    #  @return The success or failure of the withdrawal
    # Boden
    def withdraw(self, amount):
        assert(isinstance(amount, float))
        assert(amount > 0)
        assert self._balance >= amount, "Withdrawal denied: insufficient funds."
        # Process the transaction and update necessary variables
        withdrawalTransaction = Transaction("withdrawal", self.getNextTransactionNum(), amount)
        # add withdrawal to list of transactions
        self._accountTransactions.append(withdrawalTransaction)
        self._writeTransaction(withdrawalTransaction)
        self._balance -= amount
        return True

    # Transfer an amount of money from one account to another
    #
    #  @param amount: The amount being transferred to the other account
    #  @param otherAccount: The account that is being transferred the money (if possible)
    #
    #  @return: True if the money was able to be transferred and False if not
    # Boden
    def transfer(self, amount, otherAccount: BankAccount):
        assert self.withdraw(amount)
        otherAccount.deposit(amount)
        transaction = Transaction("transfer", self.getNextTransactionNum(), amount)
        # add transfer to list of transactions
        self._accountTransactions.append(transaction)
        self._writeTransaction(transaction)
        return True

    # Calculates the interest payment for a checking account, adds a new interest transaction
    # to the account, and updates the account balance
    #
    #  @require balance > 0
    #
    #  @return if the interest was added or not    
    # Hunter
    def calcInterest(self):
        assert(self._balance > 0), "No interest can be added to an account with a negative balance."
        interestAmount = self._balance * BankAccount._intRates['checking']
        transaction = Transaction("interest", self.getNextTransactionNum(), interestAmount)
        # add interest to list of transactions
        self._accountTransactions.append(transaction)
        self._writeTransaction(transaction)
        self.deposit(interestAmount)
        return True
    
    # Prints a String representation of all transactions for a Checking Account object   
    # Hunter
    def printTransactionList(self):
        print("Checking Account Transactions:")
        print(super().printTransactionList())

    # Method to write all transactions made on a checking account to the checking.txt
    # file
    # Data is encrypted first
    #
    #  @param transaction: The transaction to be written to the file
    # Hunter, fixed by Boden
    def _writeTransaction(self, transaction: Transaction):
        # Set the Debug Flag
        DEBUG = False
        # Encryption key (Ensure the key is 16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
        key = b'MySuperSecretKey1222222222222222'
        # Initialization vector (Ensure the IV is 16 bytes)
        iv = b'MySuperSecretIV1'

        if DEBUG:
            print("The length of the key is %d bytes" % len(key))
            print("The length of the Initialization Vector is %d bytes" % len(iv))

        # Open the file to write the data
        fileName = f"checking-{self._clientNum}-{self._accountNum}.txt"
        with open(fileName, "wb") as outfile:
            # Convert transaction to string, then encrypt
            transaction_str = str(transaction)
            # Encrypt the transaction data
            encrypted_data = encrypt_AES_CBC(transaction_str, key, iv)
            # Write the length of the encrypted data to the file
            outfile.write(str(len(encrypted_data)).encode())
            outfile.write(b"\n")
            # Write the encrypted data to the file
            outfile.write(encrypted_data)
            outfile.write(b"\n")

        self._nextTransaction += 1

        if DEBUG:
            print(f"Transactions written to checking-{self._clientNum}-{self._accountNum}.txt.")

    # Method to read all transactions made on a checking account to the checking.txt
    # file
    # Data is decrypted first
    # Hunter
    def _readTransactions(self):
        # Set the Debug Flag
        DEBUG = False
        key = b'MySuperSecretKey1222222222222222'
        iv = b'MySuperSecretIV1'

        # Open the file to read the data
        fileName = f"checking-{self._clientNum}-{self._accountNum}.txt"
        with open(fileName, "rb") as infile:
            length = infile.readline().rstrip().decode()

            while length != "":
                length = int(length)
                if DEBUG:
                    print("Length: ", length)
                data = infile.read(length)
                data = decrypt_AES_CBC(data, key, iv)
                # process the decrypted data: 
                print("Decrypted transaction:", data)
                infile.readline()  # Skip the newline
                length = infile.readline().rstrip().decode()


    # Returns a String representation of a Checking Account object
    #
    # @return: A String representation of the Checking Account object (String)    
    def __repr__(self):
        details = (f"Account Number: {self._accountNum}\n"
                    f"Balance: {self._balance:.2f}\n"
                    f"Account Type: '{super().getAccountType()}'\n"
                    f"Transactions:\n{super().printTransactionList()}")
        return (details)
