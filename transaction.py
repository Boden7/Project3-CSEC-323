""" 
Implementation of the Transaction class
@author: John McManus
Edited by Anna Pitt and Boden Kahn
@date: October 11, 2024

This module defines the Transaction class.
A class to represent the data elements and methods required to implement a back account transaction.
"""

# import the datetime class used to get today's date
import datetime

class Transaction:
   
   _nextTransaction = 100 # A private class variable that hold the number of the next transaction
   DEBUG = False # A class constant that turns debugging printing on and off
   RESET_TNUMBER = False # Ensures that transaction numbers don't reset each call
   _typeSet = {"deposit", "withdrawal", "interest", "transfer", "penalty"}
   
   # Constructs a transaction.
   #  @param tType: the type of this transaction (String)
   #  @param amount: the amount of this transaction (Floating point: default is 0.0, must be a positive float)
   #  @ensure self._amount >= 0
   #  @ensure tType is in the set {"deposit", "withdrawl", "interest", "transfer", "penalty"}
   #  @ensure date is a valid date
   # Boden
   def __init__(self, tType, amount = 0.0) :
      # Assert statements for preconditions
      assert(isinstance(amount, float)), "The amount must be a floating-point value."
      assert amount >= 0, "The amount must be a positive numerical value."
      assert(isinstance(tType, str)), "The transaction type must be a String value."
      assert tType in Transaction._typeSet, "The transaction type must be a valid type."
      
      if Transaction.DEBUG:
         print ("Creating a new transaction")
         
      if Transaction.RESET_TNUMBER:
         Transaction._nextTransaction = 100 
         
      # Set the transaction number and increment the next transaction class variable
      self._tNumber = Transaction._nextTransaction
      Transaction._nextTransaction = Transaction._nextTransaction + 1      
      
      # Set the tType 
      self._tType = tType

      # set the amount
      self._amount = amount
   
      # Set the date to today's date
      self._setDate()

      return

   # Define the Special Methods Needed

   # Checks an transaction to see if it is equal to the second transaction.
   #  @param other: the transaction you are comparing the first transaction with
   #  @return result: True if the two transaction have the same amount, date, and tNumber and False if not
   def __eq__(self, other) :
      # Compares the immutable values of the transactions to check for equality
      result = (self._amount == other._amount) and (self._date == other._date) and (self._tNumber == other._tNumber)
      return result 
    
   # Checks a transaction to see if it is not equal to the second transaction.
   #  @param other: the transaction you are comparing the first transaction with
   #  @return result: True if these two transactions do not have the same amount, dates, and tNumber and False if they do
   def __ne__(self, other) :
    # Compares the immutable values of the transactions to check inequality
      result = (self._amount != other._amount) or (self._date != other._date) or (self._tNumber != other._tNumber)
      return result 
  
   # adds an transaction to the second transaction.
   #  @param other: the transaction your are adding the first transaction to
   #  @return result: the sum of the two transaction prices
   def __add__(self, other) :
      # Adds the two transaction amounts and returns the resulting floating-point value
      return (self._amount + other._amount)
   
   #  Subtracts a second transaction from the first transaction
   #  @param other: the transaction you are subtracting from the first transaction
   #  @return result: the subtraction of the two transaction amounts
   def __sub__(self, other) :
      # Subtracts the floating-point value of other from self and returns the resulting floating-point value
      return (self._amount - other._amount)

   # implements the sum() function that will sum a list of the Transactions
   #  @param other: the transaction your are adding to the sum
   #  @return: the sum of the transaction amounts in the list
   def __radd__(self, other):
      # Adds each amount to a running total in succession
      return other + self._amount

   # Define the accessor methods
   
   # getDay returns the day of the transaction.
   # @return: The day of the transaction
   def getDay(self):
      return self._day

   # getMonth returns the month of the transaction.
   # @return: The month of the transaction
   def getMonth(self):
      return self._month
   
   # getYear returns the year of the transaction.
   # @return: The year of the transaction
   def getYear(self):
      return self._year

   # getAmount returns the amount of the transaction.
   # @return: The amount of the transaction 
   def getAmount(self) :
      return self._amount

   # getDate returns the date of the transaction.
   # @return: The date of the transaction
   def getDate(self) :
      return self._date

   # getTNumber returns the transaction number of the transaction.
   # @return: The transaction number of the transaction
   def getTNumber(self) :
      return self._tNumber

   # getTType returns the transaction type of the transaction.
   # @return: The transaction type of the transaction
   def getTType(self) :
      return self._tType

   # Anna
   # Returns the next available transaction number
   # @return: The next available transaction number
   def getNextTNumber(self):
       return Transaction._nextTransaction
   
   # Prints all of the transaction instance variables.
   def printTransaction(self):
      print("Transaction # %d, amount $%.2f, date %s type: %s" % (self._tNumber, self._amount, self._date, self._tType))

   # Prints all of the transaction instance variables.
   # @return: The formatted, human readable string of the transaction   
   def __str__ (self):
      return ("Transaction # %d, amount = $%.2f, date %s, type: %s" % (self._tNumber, self._amount, self._date, self._tType))

   # Prints all of the transaction instance variables.
   # @return: The formatted, machine readable string of the transaction   
   def __repr__ (self):
      return ("Transaction(tNumber = %d, amount = $%.2f, date = %s, tType = %s)" % (self._tNumber, self._amount, self._date, self._tType))

   # Define the mutator methods
   # @require year: Must be greater than or equal to 2024
   # @require month: Must be between 1 and 12 inclusive
   # @require day: Must be between 1 and 31 inclusive
   # Helper method that sets the date for a transaction
   def _setDate(self):
      date = str(datetime.date.today())
      self._date = date
      date = date.split("-")
      assert(int(date[0]) >= 2024)
      assert(int(date[1]) >= 1)
      assert(int(date[1]) <= 12)
      assert(int(date[2]) >= 1)
      assert(int(date[2]) <= 31)
      self._year = date[0]
      self._month = date[1]
      self._day = date[2]
      return 