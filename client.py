""" 
This module defines the Client class.
@author: Hunter Peacock, Boden Kahn, Brenden Shelton, and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a Client
"""

# Import statements
from name import Name
from address import Address
from phoneNumber import PhoneNumber
from bankAccount import BankAccount
from password import Password
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount
from AES_CBC import encrypt_AES_CBC
import os
import hashlib

# Hunter
class Client:

   # Declares the class variables
   PEPPER = "SHELBY_MADE"
   clientCounter = 100 # client number set to monotonically increase
   
   # Constructs a Client object.
   #
   #  @param name: The name of the Client (Name)
   #  @param address: The address of the Client (Address)
   #  @param phoneNumber: The phone number of the Client (PhoneNumber)
   #  @param accountType: The account type of the first account to be opened for the Client (String)
   #
   #  @require name is an instance of the Name class
   #  @require address is an instance of the Address class
   #  @require phoneNumber is an instance of the PhoneNumber class
   #  @require accountType is in the type list supplied
   #
   #  @ensure Client object successfully created   
   def __init__(self, name: Name, address: Address, phoneNumber: PhoneNumber, accountType: str, password: Password):
      
      # Assert statements
      assert isinstance(name, Name), "The name must be of the Name type."
      assert isinstance(address, Address), "The address must be of the Address type."
      assert isinstance(phoneNumber, PhoneNumber), "The phone number must be of the PhoneNumber type."
      assert accountType in ['checking', 'savings'], "The account type must be either checking or savings."
      assert isinstance(password, Password), "The password must be of the Password type."
      
      self._clientNumber = Client.clientCounter
      Client.clientCounter += 1 # monotonically increase client number with each new instance of a client

      self._name = name 
      self._address = address
      self._phoneNumber = phoneNumber

      # A private class variable that holds the number of the next account value
      self._nextAccountVal = 1001
      
      # Initializes the list of bank accounts as empty
      self._bankAccounts = []
      
      # Initializes the client's random salt value
      self._salt = os.urandom(16)      
      
      # Initializes the client's hashed password (stored in the variable, but
      # not saved as an instance variable)
      hashVal = self._createSecureHash(password)
      
      # Writes the hashed password value to its own file
      # TO BE DONE
      
      # Creates an empty (balance = 0) banking account instance of the account type passed in
      if accountType == 'checking':
         self.newCheck = CheckingAccount(1000, self._clientNumber, 0.0, 'checking')
         
         self._bankAccounts.append(self.newCheck)
      else:
         self.newSave = SavingsAccount(1000, self._clientNumber, 0.0, 'savings')
         
         self._bankAccounts.append(self.newSave)
   
   # A private method to securely hash the password.
   #
   #  @parameter: The password to hash
   #
   #  @require: 8 <= len(password) <=  16
   #  @require: password does not contain "/", "\\", "<", ">", "|"
   def _createSecureHash(self, password):
      # Assert statements
      assert isinstance(password, Password), "The password must be of the Password type."
      
      # Hashes the password based on the salt value, pepper value, hash algorithm,
      # and number of iterations to go through
      self._iterations = 100_000
      self._hash_algo = 'sha256'
      hash_value = hashlib.pbkdf2_hmac(
           self._hash_algo,
           password._password.encode('utf-8') + Client.PEPPER.encode('utf-8'),  
           self._salt,
           self._iterations
       ) 
      
      # Returns the hash value
      return hash_value
   
   # A method to allow the user to change their password. The user must first
   # enter their old password, then enter a valid new password twice.
   def changePassword(self):
      pass
    
   # Method to write and store client passwords for their accounts to a file
   # Data is encrypted first
   #  @param password: The password to be written to the file
   # Hunter 
   def _WritePasswordToFile(self, password):
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
      with open("", "wb") as outfile:
         # Convert transaction to string, then encrypt
         password_str = str(password)
         # Encrypt the transaction data
         encrypted_data = encrypt_AES_CBC(password_str, key, iv)
         # Write the length of the encrypted data to the file
         outfile.write(str(len(encrypted_data)).encode())
         outfile.write(b"\n")
         # Write the encrypted data to the file
         outfile.write(encrypted_data)
         outfile.write(b"\n")

      if DEBUG:
         print("Password written to "".")



   # Opens a new client bank account
   #
   #  @param account: The new account to be added to the Client (BankAccount)
   #
   #  @require accountType is in the type list supplied
   #   
   #  @return account: the account that was created
   # Anna
   def openBankAccount(self, accountType, balanceIn = 0.0):
      assert accountType in ['checking', 'savings'], "The account type must be either checking or savings."
      
      # Creates either a new checking or savings account
      if (accountType == 'checking'):
         account = CheckingAccount(self._nextAccountVal, self._clientNumber, balanceIn, 'checking')
      else:
         account = SavingsAccount(self._nextAccountVal, self._clientNumber, balanceIn, 'savings')
      
      # Adds the new account to the client's list of accounts and update the next account number
      self._bankAccounts.append(account)
      self._nextAccountVal += 1
      return account

    # Closes a client's already existing bank account
   #
   #  @param account: The account to be deleted from the Client (BankAccount object)
   #
   #  @require The account passed in must be a valid BankAccount type (checking or savings)
   #  @require The list of bank accounts must be greater than 1 to close an account   
   #  @require BankAccount object associated with the account number must already be stored in the client account
   # Anna
   def closeBankAccount(self, account: BankAccount):
      # Assert statements
      assert isinstance(account, BankAccount), "Must pass in a valid bank account to delete."
      assert account in self._bankAccounts, "The bank account must exist in the client's account list."
      assert len(self._bankAccounts) > 1, "Cannot delete a client's only account."
      
      # Withdraw all funds and remove the account: 
      print(f"Withdrawing all funds from account: {account.getAccountNumber()}.")
      
      # Withdraws the full account balance from the account
      account.withdraw(account.getBalance())
      
      print(f"Account {account.getAccountNumber()} closed.")
      
      # Removes the account from the list and dereferences it
      self._bankAccounts.remove(account)
      account = None

   # Returns a list of the client's bank accounts
   #
   #  @return: The list associated with the client's bank accounts (List)   
   def getClientAccounts(self):
      return self._bankAccounts
   
   # Returns the client number associated with a particular client
   #
   #  @return: The client number of a particular client (int)  
   def getClientNumber(self):
      return self._clientNumber
   
   # Returns the next available client number
   #
   #  @return: The next available client number (int)  
   def getNextClientNumber(self):
      return Client.clientCounter
   
   # An accessor/getter method for the next available account value
   #
   #  @return: The next available bank account value (integer)   
   # Hunter
   def getNextAccountNumber(self):
      return self._nextAccountVal
   
   # Accessor/getter method for the first name of the client
   #
   #  @return: The first name of the client (String)   
   def getFirstName(self):
      return self._name.getFirstName()
   
   # Accessor/getter method for the last name of the client
   #
   #  @return: The last name of the client (String)   
   def getLastName(self):
      return self._name.getLastName()
   
   # Accessor/getter method for the street of the client
   #
   #  @return: The street of the client (String)   
   def getStreet(self):
      return self._address.getStreet()
   
   # Returns the city of the client
   #
   #  @return: The city of the client (String)   
   def getCity(self):
      return self._address.getCity()
   
   # Accessor/getter method for the state of the client
   #
   #  @return: The state of the client (String)   
   def getState(self):
      return self._address.getState()   
   
   # Accessor/getter method for the phone number of the client
   #
   #  @return: The phone number of the client (String)   
   def getPhoneNumber(self):
      return self._phoneNumber.getPhoneNumber()
   
   # Mutator/setter method for the first name of the client  
   def setFirstName(self, firstIn):
      self._name.setFirstName(firstIn)
      
   # Mutator/setter method for the last name of the client  
   def setLastName(self, lastIn):
      self._name.setLastName(lastIn)
   
   # Mutator/setter method for the street of the client  
   def setStreet(self, streetIn):
      self._address.setStreet(streetIn)
      
   # Mutator/setter method for the city of the client  
   def setCity(self, cityIn):
      self._address.setCity(cityIn)
   
   # Mutator/setter method for the state of the client  
   def setState(self, stateIn):
      self._address.setState(stateIn)
   
   # Mutator/setter method for the phone number of the client  
   def setPhoneNumber(self, numberIn):
      self._phoneNumber.setPhoneNumber(numberIn)   
   
   # Repr method for string representation of a particular client
   #
   #  @return: A String representation of the Client object (String)   
   def __repr__(self): 
      details = (
      f"Client Number: {self.getClientNumber()}\n"
      f"Name: {self._name.__repr__()}\n"
      f"Phone Number: {self._phoneNumber.__repr__()}\n"
      f"Address: {self._address.__repr__()}\n"
      )
      if len(self._bankAccounts) == 0:
         details += f"There are no bank accounts associated with client {self.getClientNumber()}\n"
      else:
         details += "Bank Accounts: \n"
         for account in self._bankAccounts:
            details += (f"{account.__repr__()}\n")
      return(details)

   # Compares two Clients to see if they are the same
   #
   # @param other: The client to compare the original client (self) to
   #
   # @require: other must be a Client instance
   #
   # @return: True if the two Clients are equal, False if not
   # Brenden
   def __eq__(self, other):
      # Check if other is an instance of Client
      assert(isinstance(other, Client)), "Comparison must be between two Client instances."
      
      # Compare immutable variables
      return (self._clientNumber == other._clientNumber)
