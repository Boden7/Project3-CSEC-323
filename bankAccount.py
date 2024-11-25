""" 
This module defines the BankAccount class.
@author: Hunter Peacock, Boden Kahn, and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a Bank Account
"""

# Import statements
from transaction import Transaction
from abc import ABC, abstractmethod

class BankAccount:
    # A private class variable that holds the number of the next account value
    _nextAccountVal = 1000
    
    # A private class variable that holds the interest rates in decimal form 
    _intRates = {'checking': 0.015, 'savings': 0.04}

    # Constructs a BankAccount object.
    #
    #  @param balanceIn: The starting balance of the Bank Account (Floating point; default is $0)
    #  @param account_type: The account type of the Bank Account (String; default is 'checking')
    #
    #  @require: balanceIn is a floating-point type and is positive
    #  @require: account_type must be either 'checking' or 'savings'    
    #
    #  @ensure BankAccount object successfully created    
    # Hunter 
    def __init__(self, balanceIn = 0.0, account_type = 'checking'):
        # Assert statements for preconditions
        assert isinstance(balanceIn, float), "The balance must be a floating-point value."
        assert balanceIn >= 0.0, "The balance must be a positive value." 
        assert account_type in ['checking', 'savings'], "Invalid account type."

        # Sets the instance variables
        self._accountNum = BankAccount._nextAccountVal
        # Updates the next account value
        BankAccount._nextAccountVal += 1
        self._accountTransactions = []  # Container to store all transactions on an account
        self._balance = balanceIn
        self._accountType = account_type

    @abstractmethod
    # Deposits money into the bank account if the transaction is valid and records the transaction
    #
    #  @param amount: The amount to be deposited
    #
    # Abstract method to be implemented in subclasses
    def deposit(self, amount):
        pass
    
    @abstractmethod
    # Withdraws money from the account if the transaction is valid and records the transaction
    #
    #  @param amount: The amount to be withdrawn    
    #
    # Abstract method to be implemented in subclasses    
    def withdraw(self, amount):
        pass
     
    @abstractmethod
    # Transfers an amount of money from one account to another if the transfer is valid
    #
    #  @param amount: The amount being transferred to the other account  
    #  @param otherAccount: The account being transferred money to, if possible
    #
    # Abstract method to be implemented in subclasses
    def transfer(self, amount, otherAccount):
        pass

    @abstractmethod
    # Calculate the interest to add to an account based on the balance and account type
    #
    # Abstract method to be implemented in subclasses 
    def calcInterest(self):
        pass

    # Accessor/getter to retrieve the account type of an account
    #
    #  @return: The account type associated with the Bank Account (String)    
    # Boden
    def getAccountType(self):
        return self._accountType
        
    # Accessor/getter to retrieve the balance of an account
    #
    #  @return: The balance associated with the Bank Account (floating-point)    
    # Anna 
    def getBalance(self):
        return self._balance

    # Accessor/getter to retrieve the account number
    #
    #  @return: The account number associated with the Bank Account (integer)    
    # Anna 
    def getAccountNumber(self):
        return self._accountNum

    # An accessor/getter method for the next available account value
    #
    #  @return: The next available bank account value (integer)   
    # Hunter 
    def getNextAccountNumber(self):
        return BankAccount._nextAccountVal
    
    # An accessor/getter method for the interest rate
    #
    #  @return: The bank account's interest rate (float)
    # Boden
    def getInterestRate(self):
        return BankAccount._intRates[self.getAccountType()]   

    # Returns a String representation of the transactions for a Bank Account object
    #
    # @return: A String representation of the transactions stored within a Bank Account object (String)
    # Anna
    def printTransactionList(self):
        # If the transaction list is empty
        if(len(self._accountTransactions) == 0):
            return("There are no valid transactions to display.")
      
        # If there is at least one transaction in the transaction list to display
        # Creates a String variable to hold the list of transactions
        transList = ""
        
        # Loops through every transaction in the list
        for transIndex in range(len(self._accountTransactions)):
            
            # If the transaction is the last one in the list
            if(transIndex == (len(self._accountTransactions) - 1)):
                # Adds the String representation of the transaction to transList (without a new line)
                transList = transList + str(self._accountTransactions[transIndex])
                
            # If the transaction is not the last one in the list
            else:
                # Adds the String representation of the transaction to transList (with a new line)
                transList = transList + str(self._accountTransactions[transIndex]) + "\n"
      
        # Returns the full amount of transactions as a String
        return(transList)
   
    @abstractmethod
    # Write all bank account transactions to a local file
    #
    # Abstract method to be implemented in subclasses     
    def _writeTransaction(self):
        pass

    @abstractmethod
    # Read all bank account transactions from a local file
    #
    # Abstract method to be implemented in subclasses     
    def _readTransactions(self):
        pass

    @abstractmethod
    # Returns a String representation of a Bank Account object
    #
    # Abstract method to be implemented in subclasses    
    def __repr__(self):
        pass

    # Compares two Bank Accounts to see if they are the same
    #
    #  @param other: The account to compare the original Bank Account (self) to
    #
    #  @require: other must be a BankAccount instance    
    #
    #  @return: True if the two Bank Accounts are equal, False if not
    # Hunter 
    def __eq__(self, other):
        assert(isinstance(other, BankAccount)), "Comparison must be between two BankAccount instances."
        return (self._accountNum == other._accountNum and
                self._accountType == other._accountType)