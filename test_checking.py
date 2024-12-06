""" 
This module defines the tester for the Checking Account class.
@author: Brenden Shelton & Hunter Peacock
@date: November 3, 2024

Import the unittest module and the CheckingAccount module
Test each method with at least one unit test
"""

import unittest
from checkingAccount import CheckingAccount

class TestCheckingAccount(unittest.TestCase):
    
    def setUp(self):
        # Set up a CheckingAccount instance for each test
        print("\nSetting up accounts for testing...")
        self.accountNum = 1000
        self.clientNum = 100
        self.account = CheckingAccount(self.accountNum, self.clientNum, 100.0)  # Initial balance of 100.0
        self.accountNum += 1
        self.otherAccount = CheckingAccount(self.accountNum, self.clientNum, 50.0)  # Another account for transfer tests

    def test_initialization(self):
        # Test account initialization with initial balance:
        print("Testing account initialization...")
        self.assertEqual(self.account.getBalance(), 100.0)
    
    def test_deposit(self):
        # Test depositing funds into the account:
        print("Testing deposit function...")
        self.account.deposit(50.0)
        self.assertEqual(self.account.getBalance(), 150.0)
    
    def test_withdraw_within_balance(self):
        # Test withdrawing an amount within the balance: 
        print("Testing withdrawal within balance...")
        success = self.account.withdraw(30.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 70.0)
    
    def test_withdraw_exceeding_balance(self):
        # Test withdrawing an amount that exceeds the balance: 
        print("Testing withdrawal exceeding balance...")
        with self.assertRaises(AssertionError):
            self.account.withdraw(150)
        self.assertEqual(self.account.getBalance(), 100.0)  # Balance should remain unchanged
    
    def test_transfer(self):
        # Test transferring funds to another account: 
        print("Testing transfer between accounts...")
        success = self.account.transfer(20.0, self.otherAccount)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 80.0)
        self.assertEqual(self.otherAccount.getBalance(), 70.0)

    def test_calculate_interest(self):
        # Test interest calculation and application to balance: 
        print("Testing interest calculation...")
        self.account.calcInterest()
        expected_balance = 100.0 * (1 + 0.015)  # 1.5% interest applied
        self.assertAlmostEqual(self.account.getBalance(), expected_balance, places=2)
    
    def test_transaction_listing(self):
        # Test printing the transaction list: 
        print("Testing transaction listing...")
        self.account.deposit(50.0)
        self.account.withdraw(20.0)
        transactions = self.account.printTransactionList()
        self.assertNotEqual(transactions, "There are no valid transactions to display.")
    
    def test_transaction_listing_empty(self):
        # Test printing the transaction list: 
        print("Testing transaction listing...")
        transactions = self.account.printTransactionList()
        self.assertEqual(transactions, "There are no valid transactions to display.")
    
    def test_write_transaction(self):
        # Test writing a transaction to the file with encryption: 
        print("Testing transaction write with encryption...")
        transaction = Transaction('deposit', 100, 1.0)# Dummy transaction
        # Convert the dummy transaction into a string and pass it in to the write function
        transactionStr = transaction.__repr__()  
        self.account._writeTransaction(transactionStr)
        # Get the string back using readTransactions
        returnStr = self.account._readTransactions()
        # Ensure the values are equal
        self.assertEqual(returnStr, transactionStr)

    def test_get_next_transaction_number(self):
        print("Testing getting the next transaction number")
        self.assertEqual(self.account.getNextTransactionNum(), 100)
        self.account.deposit(1.0)
        self.assertEqual(self.account.getNextTransactionNum(), 101)

     # Test the representation method (__repr__)
    def test_repr(self):
        print("Testing the repr methodA")
        self.account.deposit(100.0)
        reprCheck = repr(self.account)
        self.assertIn("Account Number:", reprCheck)
        self.assertIn("Balance: 100.00", reprCheck)
        self.assertIn("Account Type: 'checking'", reprCheck)

if __name__ == "__main__":
    unittest.main()
