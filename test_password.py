""" 
This module defines the tester for the Password class.
@author: Anna Pitt
@date: December 5th, 2024

Import the unittest module and the Password module
Test each method with at least one unit test
"""

# Import statements
import unittest
from unittest.mock import patch
from password import Password

class TestPassword(unittest.TestCase):
    # The setup method initializes a password to be used for testing purposes
    # Anna
    def setUp(self):
        # Initializes invalid passwords
        self.invalidType = 10000000
        self.invalidLengthShort = "a" * 7
        self.invalidLengthLong = "a" * 17
        self.invalidChars = "Te/st123!"
        
        # Initializes a valid password
        self.validPass = "Test123!"
    
    # Anna
    def test_ConstructorValid(self):
        print("\nTesting the constructor with a valid password")
        
        # Attempts to create a password
        testPass = Password(self.validPass)
        
        # Ensures the Password object was made
        self.assertTrue(isinstance(testPass, Password))    
    
    # Anna
    def test_ConstructorInvalidPasswordType(self):
        print("\nTesting the constructor with an invalid password type") 
        
        # Ensures the Password object with false call to password
        # throws an assertion error
        self.assertRaises(AssertionError, Password, self.invalidType)
    
    # Anna
    def test_ConstructorInvalidPasswordLengthShort(self):
        print("\nTesting the constructor with a password that is too short") 
        
        # Ensures the Password object with false call to password
        # throws an assertion error
        self.assertRaises(AssertionError, Password, self.invalidLengthShort)
    
    # Anna
    def test_ConstructorInvalidPasswordSpecialChars(self):
        print("\nTesting the constructor with a password that contains special characters") 
        
        # Ensures the Password object with false call to password
        # throws an assertion error
        self.assertRaises(AssertionError, Password, self.invalidChars)    
    
    # Anna
    def test_ConstructorInvalidPasswordLengthLong(self):
        print("\nTesting the constructor with a password that is too long") 
        
        # Ensures the Password object with false call to password
        # throws an assertion error
        self.assertRaises(AssertionError, Password, self.invalidLengthLong)

if __name__ == '__main__':
    unittest.main()
