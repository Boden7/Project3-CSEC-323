# Testers for the SavingsAccount class:
# @authors: Hunter Peacock 

import unittest
from savingsAccount import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    
    def setUp(self):
        # Resets the account number and client number for testing purposes
        print("\nResetting client and account numbers for testing...")
        self.accountNum = 1000
        self.clientNum = 100    

    # Test the creation of a SavingsAccount with an initial balance
    def test_initialization(self):
        # Test default initialization with zero balance
        account = SavingsAccount(self.accountNum, self.clientNum)
        self.assertEqual(account.getBalance(), 0.0)
        self.assertEqual(account.getOverdrawnCount(), 0)

        # Test initialization with a specific balance
        account2 = SavingsAccount(self.accountNum + 1, self.clientNum + 1, 500.0)
        self.assertEqual(account2.getBalance(), 500.0)

    # Test deposit method (positive amount)
    def test_deposit(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 100.0)
        
        # Deposit a valid positive amount
        success = account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 150.0)

    # Test deposit method (negative amount, should raise the assertion error)
    def test_deposit_invalid(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 100.0)
        with self.assertRaises(AssertionError):
            account.deposit(-50.0)

    # Test withdraw method (valid withdrawal)
    def test_withdraw(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 1000.0)
        
        # Withdraw a valid amount
        success = account.withdraw(200.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 800.0)

    # Test withdraw method (insufficient balance, should apply overdraft fee)
    def test_withdraw_overdraft(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 50.0)
        
        # Withdraw an amount greater than balance
        success = account.withdraw(100.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), -50.0 - account.getOverdraft())
        
        # Ensure that the overdraft count is incremented
        self.assertEqual(account.getOverdrawnCount(), 1)

    # Test withdraw method (too many overdrafts, should deny the withdrawal)
    def test_withdraw_too_many_overdrafts(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 50.0)
        account._setOverdrawnCount(3)  # Simulate too many overdrafts

        with self.assertRaises(AssertionError):
            account.withdraw(100.0)

    # Test transfer between accounts
    def test_transfer(self):
        account1 = SavingsAccount(self.accountNum, self.clientNum, 1000.0)
        account2 = SavingsAccount(self.accountNum + 1, self.clientNum + 1, 500.0)

        success = account1.transfer(200.0, account2)
        self.assertTrue(success)
        self.assertEqual(account1.getBalance(), 800.0)
        self.assertEqual(account2.getBalance(), 700.0)

    # Test interest calculation and deposit into the account
    def test_calc_interest(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 1000.0)
        
        # Assume the interest rate for savings accounts is 0.04 (4%)
        account.calcInterest()
        self.assertEqual(account.getBalance(), 1000.0 * 1.04)  # Balance should have increased by 4%

    # Test getting the overdraft fee
    def test_get_overdraft(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 100.0)
        account._setOverdrawnCount(1)
        
        overdraft_fee = account.getOverdraft()
        self.assertEqual(overdraft_fee, 20.00)  # Based on the _overdraftFee list

    def test_calculate_interest(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 100.0)
        
        # Test interest calculation and application to balance:
        print("Testing interest calculation...")
        account.calcInterest()
        expected_balance = 100.0 * (1 + 0.04)  # 4% interest applied
        self.assertAlmostEqual(account.getBalance(), expected_balance, places = 2)
    
    def test_transaction_listing(self):
        account = SavingsAccount(self.accountNum, self.clientNum)
        
        # Test printing the transaction list:
        print("Testing transaction listing...")
        account.deposit(50.0)
        account.withdraw(20.0)
        transactions = account.printTransactionList()
        self.assertNotEqual(transactions, "There are no valid transactions to display.")
    
    def test_write_transaction(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 100.0)

         # Deposit a valid positive amount
        success = account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 150.0)
        
        # Test writing a transaction to the file with encryption:
        print("Testing transaction write with encryption...")
        transaction = "test transaction"  # Dummy transaction
        account._writeTransaction(transaction)
        # Ensure no errors during the write process
    
    def test_read_transaction(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 100.0)

         # Deposit a valid positive amount
        success = account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 150.0)
        
        # Test reading and decrypting transactions from file: 
        print("Testing transaction read with decryption...")
        account._readTransactions()
        # Ensure no errors during the read process

    # Test transaction logging in the list with transaction
    def test_transaction_logging(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 1000.0)
        account.deposit(200.0)
        
        transaction_list = account._accountTransactions
        self.assertEqual(len(transaction_list), 1)
        self.assertEqual(transaction_list[0].getTType(), "deposit")
        self.assertEqual(transaction_list[0].getAmount(), 200.0)

    # Test the representation method (__repr__)
    def test_repr(self):
        account = SavingsAccount(self.accountNum, self.clientNum, 500.0)
        account.deposit(100.0)
        
        reprCheck = repr(account)
        self.assertIn("Account Number:", reprCheck)
        self.assertIn("Balance: 600.00", reprCheck)
        self.assertIn("Account Type: 'savings'", reprCheck)

if __name__ == '__main__':
    unittest.main()
