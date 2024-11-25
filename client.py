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
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount

# Hunter
class Client:
   
   client_counter = 100 # client number set to monotonically increase
   
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
   def __init__(self, name: Name, address: Address, phoneNumber: PhoneNumber, accountType: str):
      
      # Assert statements
      assert isinstance(name, Name), "The name must be of the Name type."
      assert isinstance(address, Address), "The address must be of the Address type."
      assert isinstance(phoneNumber, PhoneNumber), "The phone number must be of the PhoneNumber type."
      assert accountType in ['checking', 'savings'], "The account type must be either checking or savings."
      
      self._clientNumber = Client.client_counter
      Client.client_counter += 1 # monotonically increase client number with each new instance of a client

      self._name = name 
      self._address = address
      self._phoneNumber = phoneNumber

      # A private class variable that holds the number of the next account value
      self._nextAccountVal = 1000
      
      # Initializes the list of bank accounts as empty
      self._bankAccounts = []
      
      # Creates an empty (balance = 0) banking account instance of the account type passed in
      if accountType == 'checking':
         newCheck = CheckingAccount(0.0)
         
         self._bankAccounts.append(newCheck)
      else:
         newSave = SavingsAccount(0.0)
         
         self._bankAccounts.append(newSave)

   # Opens a new client bank account
   #
   #  @param account: The new account to be added to the Client (BankAccount)
   #
   #  @require accountType is in the type list supplied  
   # Anna
   def openBankAccount(self, accountType, balanceIn = 0.0):
      assert accountType in ['checking', 'savings'], "The account type must be either checking or savings."
      
      # Creates either a new checking or savings account
      if (accountType == 'checking'):
         account = CheckingAccount(balanceIn, 'checking', self._nextAccountVal)
      else:
         account = SavingsAccount(balanceIn, 'savings', self._nextAccountVal)
      
      # Adds the new account to the client's list of accounts and update the next account number
      self._bankAccounts.append(account)
      self._nextAccountVal += 1

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
      return Client.client_counter
   
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
   
