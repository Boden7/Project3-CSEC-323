""" 
This module defines the tester for the Savings Account class.
@author: Hunter Peacock
@date: November 3, 2024

Import the unittest module and the SavingAccount module
Test each method with at least one unit test
"""

import unittest
from savingsAccount import SavingsAccount

class TestSavings(unittest.TestCase):
    
    def setUp(self):
        # Resets the account number and client number for testing purposes
        print("\nResetting client and account numbers for testing...")
        self.accountNum = 1000
        self.clientNum = 100    
        self.account = SavingsAccount(self.accountNum, self.clientNum, 0.0)  # Initial balance of 0.0
        self.accountNum += 1
        self.account2 = SavingsAccount(self.accountNum, self.clientNum, 500.0)  # Another account for transfer tests

    # Test the creation of a SavingsAccount with an initial balance
    def test_initialization(self):
        # Test default initialization with zero balance
        print("Testing account initialization")
        self.assertEqual(self.account.getBalance(), 0.0)
        self.assertEqual(self.account.getOverdrawnCount(), 0)

        # Test initialization with a specific balance
        self.assertEqual(self.account2.getBalance(), 500.0)

    # Test deposit method (positive amount)
    def test_deposit(self):        
        print("Testing a valid deposit")
        # Deposit a valid positive amount
        success = self.account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 50.0)

    # Test deposit method (negative amount, should raise the assertion error)
    def test_deposit_invalid(self):
        print("Testing an invalid deposit")
        with self.assertRaises(AssertionError):
            self.account.deposit(-50.0)

    # Test withdraw method (valid withdrawal)
    def test_withdraw(self):    
        print("Testing a valid withdrawal")    
        # Withdraw a valid amount
        self.account._balance = 1000.0
        success = self.account.withdraw(200.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 800.0)

    # Test withdraw method (insufficient balance, should apply overdraft fee)
    def test_withdraw_overdraft(self):      
        print("Testing a valid withdrawal with overdraft")
        # Withdraw an amount greater than balance
        success = self.account.withdraw(50.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), -50.0 - self.account.getOverdraft())
        
        # Ensure that the overdraft count is incremented
        self.assertEqual(self.account.getOverdrawnCount(), 1)

    # Test withdraw method (too many overdrafts, should deny the withdrawal)
    def test_withdraw_too_many_overdrafts(self):
        print("Testing an invalid withdrawal because of excess overdrafts")
        self.account._setOverdrawnCount(3)  # Simulate too many overdrafts

        with self.assertRaises(AssertionError):
            self.account.withdraw(100.0)

    # Test transfer between accounts
    def test_transfer(self):
        print("Testing a valid transfer")
        self.account._balance = 1000.0
        success = self.account.transfer(200.0, self.account2)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 800.0)
        self.assertEqual(self.account2.getBalance(), 700.0)

    # Test interest calculation and deposit into the account
    def test_calc_interest(self):
        print("Testing a valid interest transaction")
        self.account._balance = 1000.0
        # Assume the interest rate for savings accounts is 0.04 (4%)
        self.account.calcInterest()
        self.assertEqual(self.account.getBalance(), 1000.0 * 1.04)  # Balance should have increased by 4%

    # Test getting the overdraft fee
    def test_get_overdraft(self):
        print("Testing the get overdraft")
        self.account._setOverdrawnCount(1)
        
        overdraft_fee = self.account.getOverdraft()
        self.assertEqual(overdraft_fee, 20.00)  # Based on the _overdraftFee list

    def test_calculate_interest(self):
        print("Testing an interest calculation")
        # Test interest calculation and application to balance:
        self.account._balance = 100.0
        print("Testing interest calculation...")
        self.account.calcInterest()
        expected_balance = 100.0 * (1 + 0.04)  # 4% interest applied
        self.assertAlmostEqual(self.account.getBalance(), expected_balance, places = 2)
    
    def test_transaction_listing(self):
        # Test printing the transaction list:
        print("Testing transaction listing...")
        self.account.deposit(50.0)
        self.account.withdraw(20.0)
        transactions = self.account.printTransactionList()
        self.assertNotEqual(transactions, "There are no valid transactions to display.")

    def test_transaction_listing_empty(self):
        # Test printing the transaction list:
        print("Testing transaction listing with an empty transaction list...")
        transactions = self.account.printTransactionList()
        self.assertEqual(transactions, "There are no valid transactions to display.")
    
    def test_write_transaction(self):
        # Deposit a valid positive amount
        print("Testing valid transaction writing")
        success = self.account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 50.0)
        
        # Test writing a transaction to the file with encryption:
        print("Testing transaction write with encryption...")
        transaction = "test transaction"  # Dummy transaction
        self.account._writeTransaction(transaction)
        # Ensure no errors during the write process
    
    def test_read_transaction(self):
        # Deposit a valid positive amount
        print("Testing reading transactions")
        success = self.account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 50.0)
        
        # Test reading and decrypting transactions from file: 
        print("Testing transaction read with decryption...")
        self.account._readTransactions()
        # Ensure no errors during the read process

    # Test transaction logging in the list with transaction
    def test_transaction_logging(self):
        print("Testing that the transaction list updates properly")
        self.account.deposit(200.0)
        transaction_list = self.account._accountTransactions
        self.assertEqual(len(transaction_list), 1)
        self.assertEqual(transaction_list[0].getTType(), "deposit")
        self.assertEqual(transaction_list[0].getAmount(), 200.0)

    # Test the representation method (__repr__)
    def test_repr(self):
        print("Testing the repr methodA")
        self.account.deposit(100.0)
        reprCheck = repr(self.account)
        self.assertIn("Account Number:", reprCheck)
        self.assertIn("Balance: 100.00", reprCheck)
        self.assertIn("Account Type: 'savings'", reprCheck)

if __name__ == '__main__':
    unittest.main()
