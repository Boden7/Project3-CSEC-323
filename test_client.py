""" 
This module defines the tester for the Client class.
@author: Anna Pitt
@date: October 6, 2024

Import the unittest module and the Client module
Test each method with at least one unit test
"""

# Import statements
import unittest
from unittest.mock import patch
from client import Client
from name import Name
from address import Address
from phoneNumber import PhoneNumber
from password import Password
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount
from bankAccount import BankAccount

class TestClient(unittest.TestCase):
    # The setup method initializes a client to be used for
    # testing purposes
    # Anna
    def setUp(self):
        # Resets the client and bank account counter for each test
        Client.clientCounter = 100
        # Initializes a valid name, address, and phone number for the client tester
        self.validName = Name("First", "Last")
        self.validAddress = Address("100 Street", "City", "VA")
        self.validPhone = PhoneNumber("8041234567")
        self.validPassword = Password("Tester123!")
        
        # Initializes two valid clients
        self.client1 = Client(self.validName, self.validAddress, self.validPhone, "checking", self.validPassword)
        self.client2 = Client(self.validName, self.validAddress, self.validPhone, "savings", self.validPassword)
        
    def test_ConstructorInvalidName(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect name type")
        
        self.assertRaises(AssertionError, Client, "First Last", self.validAddress, self.validPhone, 'checking', self.validPassword)
    
    def test_ConstructorInvalidAddress(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect address type")
        
        self.assertRaises(AssertionError, Client, self.validName, "100 Street, City, VA", self.validPhone, 'checking', self.validPassword)
    
    def test_ConstructorInvalidPhoneNumber(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect phone number type")
        
        self.assertRaises(AssertionError, Client, self.validName, self.validAddress, "8041234567", 'checking', self.validPassword)
    
    def test_ConstructorInvalidAccountType(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect account type")
        
        self.assertRaises(AssertionError, Client, self.validName, self.validAddress, self.validPhone, 'neither', self.validPassword)    
    
    def test_ConstructorSetFirstName(self):
        print("\nTesting to ensure the constructor can properly set the first name") 
        
        self.client1.setFirstName("OtherFirst")
        
        checkFirst = self.client1.getFirstName()
        
        # Ensures the Client object can properly pull out the renamed first name      
        self.assertEqual(checkFirst, "OtherFirst")
    
    def test_ConstructorSetLastName(self):
        print("\nTesting to ensure the constructor can properly set the last name")
        
        self.client1.setLastName("OtherLast")
        
        checkLast = self.client1.getLastName()
        
        # Ensures the Client object can properly pull out the renamed last name      
        self.assertEqual(checkLast, "OtherLast")
    
    def test_ConstructorSetStreet(self):
        print("\nTesting to ensure the constructor can properly set the street") 
        
        self.client1.setStreet("100 Other Street")
        
        checkStreet = self.client1.getStreet()
        
        # Ensures the Client object can properly pull out the renamed street    
        self.assertEqual(checkStreet, "100 Other Street")
    
    def test_ConstructorSetCity(self):
        print("\nTesting to ensure the constructor can properly set the city")
        
        self.client1.setCity("OtherCity")
        
        checkCity = self.client1.getCity()
        
        # Ensures the Client object can properly pull out the renamed street    
        self.assertEqual(checkCity, "OtherCity")
    
    def test_ConstructorSetState(self):
        print("\nTesting to ensure the constructor can properly set the state") 
        
        self.client1.setState("MD")
        
        checkState = self.client1.getState()
        
        # Ensures the Client object can properly pull out the changed state    
        self.assertEqual(checkState, "MD")
    
    def test_ConstructorSetPhoneNumber(self):
        print("\nTesting to ensure the constructor can properly set the phone number") 
        
        self.client1.setPhoneNumber("8049876543")
        
        checkPhone = self.client1.getPhoneNumber()
        
        # Ensures the Client object can properly pull out the changed phone number    
        self.assertEqual(checkPhone, "8049876543")    
    
    def test_ConstructorGetClientNumber(self):
        print("\nTesting to ensure the constructor can properly get the client number") 
        
        checkClientNum = self.client1.getClientNumber()
        
        # Ensures the Client object can properly pull out the client number   
        self.assertEqual(checkClientNum, 100)
    
    def test_ConstructorGetNextClientNumber(self):
        print("\nTesting to ensure the constructor can properly get the next available client number") 
        
        checkClientNum = self.client1.getNextClientNumber()
        checkClient2Num = self.client2.getNextClientNumber()
        
        # Ensures the Client objects can properly pull out the next available client number
        self.assertEqual(checkClientNum, 102)
        self.assertEqual(checkClient2Num, 102)
    
    def test_ConstructorGetClientAccounts(self):
        print("\nTesting to ensure the constructor can properly get the list of accounts") 
        
        # Receives the client accounts
        checkClientAccounts = self.client1.getClientAccounts()
        
        # Initializes the exact values of the bank account stored in client1
        checkTest = CheckingAccount(1000, self.client1.getClientNumber())
        
        # Creates the expected account list
        expected = [checkTest]
        
        # Ensures the client account list matches the expected list 
        # ** ADD PROPER CHECK HERE
        self.assertEqual(checkClientAccounts, expected)
    
    # We tried
    #def test_ConstructorReprEmpty(self):
    #    print("\nTesting to ensure the repr can correctly close the program when a client doesn't have an account") 
    #    
    #    # Ensures the Client object can properly represent the client as a string
    #    self.assertRaises(AssertionError, self.client1.__repr__())
    
    # We tried
    #def test_ConstructorRepr(self):
    #    print("\nTesting to ensure the constructor can properly list the info of a client with at least one bank account") 
    #            
    #    checkRepr = str(self.client1)
    #    self.client1.openBankAccount("checking", 0.0)

        #compareStr = (f"Client Number: 100\n"
        #              f"Name: First Last\n"
        #                        f"Phone Number: +1(804)123-4567\n"
        #                        f"Address: 100 Street, City, VA\n"
        #                        f"Bank Accounts:\n"
        #                        f"Account Number: 1000\n"
        #                        f"Balance: 0.00\n"
        #                        f"Account Type: 'checking'\n"
        #                        f"Transactions:\n"
        #                        f"There are no valid transactions to display."
        #                        )
        
        # Ensures the Client object can properly represent the client as a string
        #self.assertEqual(checkRepr, compareStr)    
    
    def test_EqualityTrue(self):
        print("\nTesting to ensure that equality works when two clients are equal") 
                
        # Ensures the Client object can properly determine equality  
        self.assertEqual(self.client1, self.client1)
    
    def test_EqualityFalse(self):
        print("\nTesting to ensure that equality works when two clients are not equal") 
                
        # Ensures the Client object can properly determine inequality   
        self.assertNotEqual(self.client1, self.client2)
    
    def test_openBankAccountInvalidAccountType(self):
        print("\nTesting to ensure that openBankAccount() throws an assertion when the account type is an invalid type") 
        
        self.assertRaises(AssertionError, self.client1.openBankAccount, 100.0, "neither")  
    
    def test_openBankAccountValidChecking(self):
        print("\nTesting to ensure that openBankAccount() works as intended with a checking account") 
        
        # Attempts to add a new bank account
        self.client1.openBankAccount('checking', 100.0)
        
        # Pulls the bank accounts to compare
        checkList = self.client1.getClientAccounts()
        
        # Creates the exact same bank accounts
        checkTest = CheckingAccount(1000, self.client1.getClientNumber())
        checkTest2 = CheckingAccount(1001, self.client1.getClientNumber())
        
        # The expected list
        expectedList = [checkTest, checkTest2]
        
        # Compares the list of bank accounts of the client with the expected list
        self.assertEqual(checkList, expectedList)
    
    def test_openBankAccountValidSavings(self):
        print("\nTesting to ensure that openBankAccount() works as intended with a savings account") 
        
        # Attempts to add a new bank account
        self.client1.openBankAccount('savings', 100.0)
        
        # Pulls the bank accounts to compare
        checkList = self.client1.getClientAccounts()
        
        # Creates the exact same bank accounts
        checkTest = CheckingAccount(1000, self.client1.getClientNumber())
        checkTest2 = SavingsAccount(1001, self.client1.getClientNumber())
        
        # The expected list
        expectedList = [checkTest, checkTest2]
        
        # Compares the list of bank accounts of the client with the expected list
        self.assertEqual(checkList, expectedList)    
    
    def test_openBankAccountValidEmptyBal(self):
        print("\nTesting to ensure that openBankAccount() works as intended when no balance is passed in") 
        
        # Attempts to add a new bank account
        self.client1.openBankAccount('checking')
        
        # Pulls the bank accounts to compare
        checkList = self.client1.getClientAccounts()
        
        # Creates the exact same bank accounts
        checkTest = CheckingAccount(1000, self.client1.getClientNumber())
        checkTest2 = CheckingAccount(1001, self.client1.getClientNumber())
        
        # The expected list
        expectedList = [checkTest, checkTest2]
        
        # Compares the list of bank accounts of the client with the expected list
        self.assertEqual(checkList, expectedList)    
    
    def test_closeBankAccountValid(self):
        print("\nTesting to ensure that closeBankAccount() works as intended")
        
        # Adds a new bank account to delete
        self.client1.openBankAccount('checking', 100.0)
        
        # Pulls out the bank account to close it
        closeAccount = self.client1._bankAccounts[1]
        
        # Attempts to close the new bank account
        self.client1.closeBankAccount(closeAccount)
        
        # Pulls out the client account list
        clientList = self.client1.getClientAccounts()
        
        # Creates the exact same bank accounts
        checkTest = CheckingAccount(1000, self.client1.getClientNumber())
        
        # The expected list
        expectedList = [checkTest]        
        
        # Checks to ensure the bank account does not exist in the client account list anymore
        self.assertEqual(clientList, expectedList)    
    
    def test_closeBankAccountInvalidAccountNumber(self):
        print("\nTesting to ensure that closeBankAccount() throws an assertion error when an invalid account number is passed in")
        
        # Attempts to close a nonexistent bank account
        self.assertRaises(AssertionError, self.client1.closeBankAccount, 1005)    

    def test_closeBankAccountOneAccount(self):
        print("\nTesting to ensure that closeBankAccount() does not allow the closing of an account if the client only has one account") 
        
        # Attempts to close a bank account when there is only one account
        self.assertRaises(AssertionError, self.client1.closeBankAccount, 1000)
    
    def test_clientAccountTransactionNum(self):
        print("\nTesting to ensure that proper client numbers, account numbers, and transaction numbers are being assigned")
        
        # Checks the client numbers of both clients to ensure they are valid and increasing by 1 each time
        self.assertEqual(self.client1.getClientNumber(), 100)
        self.assertEqual(self.client2.getClientNumber(), 101)
        
        # Creates additional accounts for each client
        self.client1.openBankAccount('savings', 100.0)
        self.client2.openBankAccount('savings', 100.0) 
        
        # Checks the account numbers of each of the two client accounts for both clients
        self.assertEqual(self.client1._bankAccounts[0].getAccountNumber(), 1000)
        self.assertEqual(self.client1._bankAccounts[1].getAccountNumber(), 1001)
        self.assertEqual(self.client2._bankAccounts[0].getAccountNumber(), 1000)
        self.assertEqual(self.client2._bankAccounts[1].getAccountNumber(), 1001)
        
        # Adds two valid transactions to each of the accounts
        self.client1._bankAccounts[0].deposit(100.0)
        self.client1._bankAccounts[0].withdraw(50.0)
        self.client1._bankAccounts[1].deposit(100.0)
        self.client1._bankAccounts[1].withdraw(50.0)   
        self.client2._bankAccounts[0].deposit(100.0)
        self.client2._bankAccounts[0].withdraw(50.0)
        self.client2._bankAccounts[1].deposit(100.0)
        self.client2._bankAccounts[1].withdraw(50.0)
        
        # Checks the transaction numbers of each of the two transactions within the client accounts for both clients
        self.assertEqual(self.client1._bankAccounts[0]._accountTransactions[0].getTNumber(), 100)
        self.assertEqual(self.client1._bankAccounts[0]._accountTransactions[1].getTNumber(), 101)
        self.assertEqual(self.client1._bankAccounts[1]._accountTransactions[0].getTNumber(), 100)
        self.assertEqual(self.client1._bankAccounts[1]._accountTransactions[1].getTNumber(), 101)
        self.assertEqual(self.client2._bankAccounts[0]._accountTransactions[0].getTNumber(), 100)
        self.assertEqual(self.client2._bankAccounts[0]._accountTransactions[1].getTNumber(), 101)
        self.assertEqual(self.client2._bankAccounts[1]._accountTransactions[0].getTNumber(), 100)
        self.assertEqual(self.client2._bankAccounts[1]._accountTransactions[1].getTNumber(), 101)
        
        # Prints out the client accounts to show visually that the numbers are valid/monotonically increasing
        print(self.client1)
        print(self.client2)

if __name__ == '__main__':
    unittest.main()
