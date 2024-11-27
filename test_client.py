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
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount
from bankAccount import BankAccount

class TestClient(unittest.TestCase):
    # The setup method initializes a client to be used for
    # testing purposes
    # Anna
    def setUp(self):
        # Resets the client and bank account counter for each test
        Client.client_counter = 100
        BankAccount._nextAccountVal = 1000
        
        # Initializes a valid name, address, and phone number for the client tester
        self.validName = Name("First", "Last")
        self.validAddress = Address("100 Street", "City", "VA")
        self.validPhone = PhoneNumber("8041234567")
        
        # Initializes two valid clients
        self.client1 = Client(self.validName, self.validAddress, self.validPhone, "checking")
        self.client2 = Client(self.validName, self.validAddress, self.validPhone, "savings")
        
    def test_ConstructorInvalidName(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect name type")
        
        self.assertRaises(AssertionError, Client, "First Last", self.validAddress, self.validPhone, 'checking')
    
    def test_ConstructorInvalidAddress(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect address type")
        
        self.assertRaises(AssertionError, Client, self.validName, "100 Street, City, VA", self.validPhone, 'checking')
    
    def test_ConstructorInvalidPhoneNumber(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect phone number type")
        
        self.assertRaises(AssertionError, Client, self.validName, self.validAddress, "8041234567", 'checking')
    
    def test_ConstructorInvalidAccountType(self):
        print("\nTesting to ensure the constructor properly throws an assertion with incorrect account type")
        
        self.assertRaises(AssertionError, Client, self.validName, self.validAddress, self.validPhone, 'neither')    
    
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
        print("\nTesting to ensure the constructor can properly get the list of accounts.")

        # Receives the client accounts
        checkClientAccounts = self.client1.getClientAccounts()

        # Retrieves the expected account number dynamically
        expected_account_number = checkClientAccounts[0].getAccountNumber()

        # Initializes the exact values of the bank account stored in client1
        expected_account = CheckingAccount(0.0)
        expected_account._accountNum = expected_account_number

        # Creates the expected account list
        expected = [expected_account]

        # Ensures the client account list matches the expected list
        self.assertEqual(checkClientAccounts, expected)
    
    #Updated Test cases -Brenden Shelton
    def test_ConstructorReprEmpty(self):
        print("\nTesting `__repr__` for a client without bank accounts.") 
        
        client_without_accounts = Client(
            Name("First", "Last"),
            Address("100 Street", "City", "VA"),
            PhoneNumber("8041234567"),  # Valid, unformatted phone number
            accountType='checking'
        )
        client_without_accounts._bankAccounts.clear()

        expected_repr = (
            f"Client Number: {client_without_accounts.getClientNumber()}\n"
            f"Name: First Last\n"
            f"Phone Number: +1(804)123-4567\n"  # This uses the __repr__ format
            f"Address: 100 Street, City, VA\n"
            f"There are no bank accounts associated with client {client_without_accounts.getClientNumber()}\n"
        )
        self.assertEqual(client_without_accounts.__repr__(), expected_repr)

    #Updated Test Cases -Brenden Shelton
    def test_ConstructorRepr(self):
        print("\nTesting `__repr__` for a client with at least one bank account.") 
        
        client_with_account = Client(
            Name("First", "Last"),
            Address("100 Street", "City", "VA"),
            PhoneNumber("8041234567"),  # Valid, unformatted phone number
            accountType='checking'
        )
        client_with_account.openBankAccount("checking", 0.0)

        expected_repr = (
            f"Client Number: {client_with_account.getClientNumber()}\n"
            f"Name: First Last\n"
            f"Phone Number: +1(804)123-4567\n"  # This uses the __repr__ format
            f"Address: 100 Street, City, VA\n"
            f"Bank Accounts: \n"
        )
        for account in client_with_account.getClientAccounts():
            expected_repr += account.__repr__() + "\n"

        self.assertEqual(client_with_account.__repr__(), expected_repr)
   
    
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
        print("\nTesting `openBankAccount()` works as intended with a checking account.")

        # Attempts to add a new bank account
        self.client1.openBankAccount('checking', 100.0)

        # Pulls the bank accounts to compare
        checkList = self.client1.getClientAccounts()

        # Retrieves dynamically assigned account numbers
        first_account_number = checkList[0].getAccountNumber()
        second_account_number = checkList[1].getAccountNumber()

        # Creates the expected accounts
        expected_account1 = CheckingAccount(0.0)
        expected_account1._accountNum = first_account_number

        expected_account2 = CheckingAccount(100.0)
        expected_account2._accountNum = second_account_number

        # The expected list
        expectedList = [expected_account1, expected_account2]

        # Compares the list of bank accounts of the client with the expected list
        self.assertEqual(checkList, expectedList)
    
    def test_openBankAccountValidSavings(self):
        print("\nTesting `openBankAccount()` works as intended with a savings account.")

        # Attempts to add a new bank account
        self.client1.openBankAccount('savings', 100.0)

        # Pulls the bank accounts to compare
        checkList = self.client1.getClientAccounts()

        # Retrieves dynamically assigned account numbers
        first_account_number = checkList[0].getAccountNumber()
        second_account_number = checkList[1].getAccountNumber()

        # Creates the expected accounts
        expected_account1 = CheckingAccount(0.0)
        expected_account1._accountNum = first_account_number

        expected_account2 = SavingsAccount(100.0)
        expected_account2._accountNum = second_account_number

        # The expected list
        expectedList = [expected_account1, expected_account2]

        # Compares the list of bank accounts of the client with the expected list
        self.assertEqual(checkList, expectedList)
    
    def test_openBankAccountValidEmptyBal(self):
        print("\nTesting `openBankAccount()` works as intended when no balance is passed in.")

        # Attempts to add a new bank account
        self.client1.openBankAccount('checking')

        # Pulls the bank accounts to compare
        checkList = self.client1.getClientAccounts()

        # Retrieves dynamically assigned account numbers
        first_account_number = checkList[0].getAccountNumber()
        second_account_number = checkList[1].getAccountNumber()

        # Creates the expected accounts
        expected_account1 = CheckingAccount(0.0)
        expected_account1._accountNum = first_account_number

        expected_account2 = CheckingAccount(0.0)
        expected_account2._accountNum = second_account_number

        # The expected list
        expectedList = [expected_account1, expected_account2]

        # Compares the list of bank accounts of the client with the expected list
        self.assertEqual(checkList, expectedList)
    
    def test_closeBankAccountValid(self):
        print("\nTesting `closeBankAccount()` works as intended.")

        # Adds a new bank account to delete
        self.client1.openBankAccount('checking', 100.0)

        # Pulls out the bank account from the client's account list
        initial_accounts = self.client1.getClientAccounts()
        account_to_close = initial_accounts[1]

        # Attempts to close the new bank account
        self.client1.closeBankAccount(account_to_close)

        # Pulls out the client account list
        clientList = self.client1.getClientAccounts()

        # Retrieves dynamically assigned account numbers
        remaining_account_number = clientList[0].getAccountNumber()

        # Creates the expected remaining account
        expected_account = CheckingAccount(0.0)
        expected_account._accountNum = remaining_account_number

        # The expected list
        expectedList = [expected_account]

        # Compares the lists
        self.assertEqual(clientList, expectedList)
    
    def test_closeBankAccountInvalidType(self):
        print("\nTesting to ensure that closeBankAccount() does not allow improper types to be passed in") 
        
        # Adds a new bank account
        self.client1.openBankAccount('checking', 100.0)        
        
        # Attempts to pass in an integer (account number) instead of a BankAccount object
        self.assertRaises(AssertionError, self.client1.closeBankAccount, 1000)    
    
    def test_closeBankAccountInvalidAccount(self):
        print("\nTesting to ensure that closeBankAccount() throws an assertion error when an account not in the user's account list is passed in")
        
        # Adds a new bank account
        self.client1.openBankAccount('checking', 100.0)
        
        # Attempts to close a bank account that doesn't exist
        self.assertRaises(AssertionError, self.client1.closeBankAccount, SavingsAccount(250.0))    

    def test_closeBankAccountOneAccount(self):
        print("\nTesting to ensure that closeBankAccount() does not allow the closing of an account if the client only has one account") 
        
        # Attempts to close a bank account when there is only one account
        self.assertRaises(AssertionError, self.client1.closeBankAccount, self.client1._bankAccounts[0])        

if __name__ == '__main__':
    unittest.main()
