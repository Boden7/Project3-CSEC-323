""" 
This module defines the tester for the Name class.
@author: Anna Pitt
@date: November 3, 2024

Import the unittest module and the Name module
Test each method with at least one unit test
"""

import unittest
from unittest.mock import patch
from name import Name

class TestName(unittest.TestCase):
    # Tests not done in this tester that have been tested elsewhere:
    # - Valid constructor for a Name (tested in Client tester and setUp)
    # - Call to getFirstName() (tested in Client tester)
    # - Call to getLastName() (tested in Client tester)
    # - Valid call to setFirstName() (tested in Client tester)
    # - Valid call to setLastName() (tested in Client tester)
    # - Call to repr (tested in repr in Client tester)
    
    # The setup method initializes incorrect names to be used for
    # testing purposes
    # Anna
    def setUp(self):
        # Initializes incorrect first and last names
        self.invalidType = 100
        self.invalidFirstLength = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.invalidLastLength = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.invalidChars = "!@#$%"
        self.invalidEmpty = ""
        
        # Initializes a valid name to attempt to change
        self.validName = Name("First", "Last")
    
    # Anna
    def test_ConstructorInvalidFirstNameType(self):
        print("\nTesting the constructor with an invalid first name type") 
        
        # Ensures the Name object with false call to first name
        # throws an assertion error
        self.assertRaises(AssertionError, Name, self.invalidType, "Last")    
    
    # Anna
    def test_ConstructorInvalidFirstNameBlank(self):
        print("\nTesting the constructor with a blank first name (too short)") 
        
        # Ensures the Name object with false call to first name
        # throws an assertion error
        self.assertRaises(AssertionError, Name, self.invalidEmpty, "Last")

    # Anna
    def test_ConstructorInvalidFirstNameSpecialChar(self):
        print("\nTesting the constructor with a first name with special characters") 
        
        # Ensures the Name object with false call to first name
        # throws an assertion error
        self.assertRaises(AssertionError, Name, self.invalidChars, "Last")        
    
    # Anna
    def test_ConstructorInvalidFirstNameLength(self):
        print("\nTesting the constructor with a first name that is too long") 
        
        # Ensures the Name object with false call to first name
        # throws an assertion error
        self.assertRaises(AssertionError, Name, self.invalidFirstLength, "Last")
        
    # Anna
    def test_ConstructorInvalidLastNameType(self):
        print("\nTesting the constructor with invalid last name type") 
        
        # Ensures the Name object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, Name, "First", self.invalidType)    
    
    # Anna
    def test_ConstructorInvalidLastNameBlank(self):
        print("\nTesting the constructor with blank last name (too short)") 
        
        # Ensures the Name object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, Name, "First", self.invalidEmpty)
    
    # Anna
    def test_ConstructorInvalidLastNameSpecialChar(self):
        print("\nTesting the constructor with a last name with special characters") 
        
        # Ensures the Name object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, Name, "First", self.invalidChars)         

    # Anna
    def test_ConstructorInvalidLastNameLength(self):
        print("\nTesting the constructor with a last name that is too long") 
        
        # Ensures the Name object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, Name, "First", self.invalidLastLength)
    
    # Anna
    def test_setFirstInvalidFirstNameType(self):
        print("\nTesting setFirst() with invalid type") 
        
        # Ensures the Name object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setFirstName, self.invalidType)    
    
    # Anna
    def test_setFirstInvalidFirstNameBlank(self):
        print("\nTesting setFirst() with blank input (too short)") 
        
        # Ensures the Name object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setFirstName, self.invalidEmpty)

    # Anna
    def test_setFirstInvalidFirstNameSpecialChar(self):
        print("\nTesting setFirst() with invalid special characters") 
        
        # Ensures the Name object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setFirstName, self.invalidChars)        

    # Anna
    def test_setFirstInvalidFirstNameNameLength(self):
        print("\nTesting setFirst() with a first name that is too long") 
        
        # Ensures the Name object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setFirstName, self.invalidFirstLength)
    
    # Anna
    def test_setLastInvalidLastNameType(self):
        print("\nTesting setLast() with an invalid type") 
        
        # Ensures the Name object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setLastName, self.invalidType)    
    
    # Anna
    def test_setLastInvalidLastNameBlank(self):
        print("\nTesting setLast() with a blank last name (too short)") 
        
        # Ensures the Name object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setLastName, self.invalidEmpty)

    # Anna
    def test_setLastInvalidLastNameSpecialChar(self):
        print("\nTesting setLast() with a last name with invalid characters") 
        
        # Ensures the Name object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setLastName, self.invalidChars)         

    # Anna
    def test_setLastInvalidLastNameLength(self):
        print("\nTesting setLast() with a last name that is too long") 
        
        # Ensures the Name object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.validName.setLastName, self.invalidLastLength)    

if __name__ == '__main__':
    unittest.main()