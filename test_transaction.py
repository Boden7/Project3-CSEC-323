""" 
Simple Unit Test Example using Python's unittest module and assertions
@author: John McManus
Edited by Anna Pitt
@date: October 11, 2024

Import the unittest module and the Transaction module
Test each method with at least one unit test
"""

import unittest
from unittest.mock import patch
from datetime import datetime
from transaction import Transaction

""" Define test testTransaction class by extending the unittest.TestCase class"""

class TestTransaction(unittest.TestCase):
    
    # Determines the current day to compare transactions to
    now = datetime.now()
    currentDate = now.strftime("%Y-%m-%d")
    
    DEPOSIT = 2000.00   # Expected Deposit amount
    WITHDRAWL = 500.00  # Expected Withdrawal amount
    FIRST = 100      # Expected first transaction number
    TYPE = "deposit" # Expected Deposit transaction type
    
    # The setup method creates three transactions
    def setUp(self):
        # Resets the transaction number each time
        Transaction._nextTransaction = 100
        
        self.transaction1 = Transaction("deposit", TestTransaction.DEPOSIT)
        self.transaction2 = Transaction("withdrawal", TestTransaction.WITHDRAWL)
        self.transaction3 = Transaction("interest")
        self.transaction4 = Transaction("deposit")
        self.transaction5 = Transaction("transfer", 500.00)

    # The test_constructor method tests the constructor 
    def test_constructor(self):
        print("\nTesting the constructor") 
        self.assertEqual(self.transaction1.getAmount(), TestTransaction.DEPOSIT)
        self.assertEqual(self.transaction1.getTNumber(), TestTransaction.FIRST)
        self.assertEqual(self.transaction1.getTType(), TestTransaction.TYPE)
        print("The first transaction: ", self.transaction1)
        print(repr(self.transaction1))
    
    def test_constructorNoBalance(self):
        print("\nTesting the constructor without a balance parameter") 
        self.assertEqual(self.transaction4.getAmount(), 0)
        self.assertEqual(self.transaction4.getTNumber(), 103)
        self.assertEqual(self.transaction4.getTType(), "deposit")
        print("The transaction with no balance: ", self.transaction4)
        print(repr(self.transaction4))    

    # The test_constructor method tests the constructor when called without parameters
    def test_constructorNoParameters(self):
        print("\nTesting the constructor with no parameters")
        self.assertRaises(TypeError, Transaction)
    
    # Anna
    def test_constructorInvalidBalanceAmount(self):
        print("\nTesting the constructor for an assertion error when a negative amount balance is passed in") 
        self.assertRaises(AssertionError, Transaction, "Deposit", -100.0)
    
    # Anna
    def test_constructorInvalidBalanceType(self):
        print("\nTesting the constructor for an assertion error when a non-String balance is passed in") 
        self.assertRaises(AssertionError, Transaction, "Deposit", "100.0")
    
    # Anna
    def test_constructorInvalidTType(self):
        print("\nTesting the constructor for an assertion error when a non-String transaction type is passed in") 
        self.assertRaises(AssertionError, Transaction, 100, 500.0)
    
    # Anna
    def test_constructorInvalidTTypeNonSet(self):
        print("\nTesting the constructor for an assertion error when a transaction type not in the transaction set is passed in") 
        self.assertRaises(AssertionError, Transaction, "transact", 500.0)    

    # Test the __eq__ special method 
    def test_eq(self):
        print("\nTesting the equal special method") 
        self.assertTrue(self.transaction1 == self.transaction1)  

    # Second test of the __eq__ special method    
    def test_eq_2(self):
        print("\nSecond test of the equal special method") 
        self.assertFalse(self.transaction1 == self.transaction2)  

    # Test the __ne__ special method     
    def test_ne(self):
        print("\nTesting the not equal special method ") 
        self.assertTrue(self.transaction1 != self.transaction2)

    # Second test of the __ne__ special method     
    def test_ne_2(self):
        print("\nSecond test of the not equal special method") 
        self.assertFalse(self.transaction1 != self.transaction1)    

    # Test the __add__ special method 
    def test_add(self):
        addTest = self.transaction1 + self.transaction1
        print("\nTesting the addition special method")        
        self.assertEqual(addTest, 4000)

    # Test the __sub__ special method 
    def test_sub(self):
        subTest = self.transaction1 - self.transaction2
        print("\nTesting the subtraction special method")
        self.assertEqual(subTest, 1500)   

    # Test the __sum__ special method     
    def test_sum(self):
        listTransactions = [self.transaction1, self.transaction2, self.transaction3]
        sumTest = sum(listTransactions)
        print("\nTesting the sum special method %d" % sumTest) 
        self.assertEqual(sumTest, (TestTransaction.DEPOSIT + TestTransaction.WITHDRAWL))
    
    # Anna
    def test_getDay(self):
        print("\nTesting the getDay method") 
        
        # Determines what day it is today
        now = datetime.now()
        currentDay = now.strftime("%d")        
        
        # Checks to see that the transaction is pulling the current day
        self.assertEqual(self.transaction1.getDay(), currentDay)
    
    # Anna
    def test_getMonth(self):
        print("\nTesting the getMonth method") 
        
        # Determines what month it is today
        now = datetime.now()
        currentMonth = now.strftime("%m")        
        
        # Checks to see that the transaction is pulling the current month
        self.assertEqual(self.transaction1.getMonth(), currentMonth)
    
    # Anna
    def test_getYear(self):
        print("\nTesting the getYear method") 
        
        # Determines what year it is today
        now = datetime.now()
        currentYear = now.strftime("%Y")        
        
        # Checks to see that the transaction is pulling the current year
        self.assertEqual(self.transaction1.getYear(), currentYear)
    
    # Anna
    def test_setDate(self):
        print("\nTesting the private _setDate method")
        
        # Sets the date to today
        self.transaction1._setDate()
        
        # Determines what day, month, and year it is today
        now = datetime.now()
        currentDay = now.strftime("%d")
        currentMonth = now.strftime("%m")        
        currentYear = now.strftime("%Y")        
        
        # Checks to see that the transaction is being updated to the correct
        # values
        self.assertEqual(self.transaction1.getDay(), currentDay)
        self.assertEqual(self.transaction1.getMonth(), currentMonth)
        self.assertEqual(self.transaction1.getYear(), currentYear)
    
    # Anna
    def test_getAmount(self):
        print("\nTesting the getAmount method")
        
        # Determines if the amount is what is expected
        self.assertEqual(self.transaction1.getAmount(), 2000.0)
    
    # Anna
    def test_getDate(self):
        print("\nTesting the getDate method")
        
        # Determines if the date is what is expected
        self.assertEqual(self.transaction1.getDate(), TestTransaction.currentDate)
    
    # Anna
    def test_getTNumber(self):
        print("\nTesting the getTNumber method")
        
        # Determines if the transaction numbers are what is expected
        # and that they are updating properly
        self.assertEqual(self.transaction1.getTNumber(), 100)    
        self.assertEqual(self.transaction2.getTNumber(), 101)
        self.assertEqual(self.transaction3.getTNumber(), 102)
    
    # Anna
    def test_getTType(self):
        print("\nTesting the getTType method")
        
        # Determines if the transaction types are what is expected
        # and that they are updating properly
        self.assertEqual(self.transaction1.getTType(), "deposit")    
        self.assertEqual(self.transaction2.getTType(), "withdrawal")
        self.assertEqual(self.transaction3.getTType(), "interest")
        self.assertEqual(self.transaction5.getTType(), "transfer")
    
    # Anna
    def test_getNextTNumber(self):
        print("\nTesting the getNextTNumber method")
        
        # Determines if the next transaction numbers are what are expected
        # and that they are updating properly
        # Since there have been 5 transactions created, the next transaction number
        # should be 105
        self.assertEqual(self.transaction1.getNextTNumber(), 105) 
        
        # Adds a new transaction
        newTrans = Transaction("deposit", 200.00)
        
        # Checks to ensure that the next transaction type is properly updated
        self.assertEqual(self.transaction1.getNextTNumber(), 106)
    
    # Anna
    @patch('builtins.print')
    def test_printTransaction(self, mock_print):
        print("\nTesting the printTransaction method")
        
        # Determines what the transaction string should equal
        #strCheck = "Transaction # 100, amount $2000.00, date 2024-10-11 type: deposit"
        
        # Checks to ensure that the print statement matches the String check
        #self.assertEqual(self.transaction1.printTransaction(), strCheck)
        
        # Calls the printTransaction method()
        self.transaction1.printTransaction()
        mock_print.assert_called_with("Transaction # 100, amount $2000.00, date %s type: deposit" % TestTransaction.currentDate)
    
    # Anna
    def test_strCast(self):
        print("\nTesting the __str__ method")
        
        # Determines what the transaction string should equal
        strCheck = "Transaction # 100, amount = $2000.00, date %s, type: deposit" % TestTransaction.currentDate
        
        # Checks to ensure that casting the transaction to a String type produces the correct results
        self.assertEqual(str(self.transaction1), strCheck)
    
    # Anna
    def test_repr(self):
        print("\nTesting the __repr__ method")
        
        # Determines what the transaction string should equal
        strCheck = "Transaction(tNumber = 100, amount = $2000.00, date = %s, tType = deposit)" % TestTransaction.currentDate
        
        # Checks to ensure that casting the transaction to a String type produces the correct results
        self.assertEqual(repr(self.transaction1), strCheck)     
        
if __name__ == '__main__':
    unittest.main()