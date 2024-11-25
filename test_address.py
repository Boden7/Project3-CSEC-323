""" 
This module defines the tester for the Address class.
@author: Anna Pitt
@date: November 3, 2024

Import the unittest module and the Address module
Test each method with at least one unit test
"""

import unittest
from unittest.mock import patch
from address import Address

class TestAddress(unittest.TestCase):
    # Tests not done in this tester that have been tested elsewhere:
    # - Valid constructor for an Address (tested in Client tester and setUp)
    # - Call to getStreet() (tested in Client tester)
    # - Call to getCity() (tested in Client tester)
    # - Call to getState() (tested in Client tester)
    # - Valid call to setStreet() (tested in Client tester)
    # - Valid call to setCity() (tested in Client tester)
    # - Valid call to setState() (tested in Client tester)
    # - Call to repr (tested in repr in Client tester)
    
    # Anna
    def setUp(self):
        # Initializes incorrect streets, cities, and states
        self.invalidType = 100
        self.invalidEmpty = ""
        self.invalidStreetCityLength = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.invalidStateLength = "VAA"
        self.invalidStateAbbr = "TX"
        self.invalidCharsStreetCity = "123 Street!@"
        self.invalidCharsState = "!@"
        
        # Initializes a valid address to attempt to change
        self.validAddress = Address("Street", "City", "VA")
    
    # Anna
    def test_ConstructorInvalidStreetType(self):
        print("\nTesting the constructor with an invalid street type") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, self.invalidType, "City", "VA")
    
    # Anna
    def test_ConstructorInvalidStreetBlank(self):
        print("\nTesting the constructor with a blank street (too short)") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, self.invalidEmpty, "City", "VA")

    # Anna
    def test_ConstructorInvalidStreetSpecialChar(self):
        print("\nTesting the constructor with a street with special characters") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, self.invalidCharsStreetCity, "City", "VA")        
    
    # Anna
    def test_ConstructorInvalidStreetLength(self):
        print("\nTesting the constructor with a street that is too long") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, self.invalidStreetCityLength, "City", "VA")
    
    # Anna
    def test_ConstructorInvalidCityType(self):
        print("\nTesting the constructor with an invalid city type") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", self.invalidType, "VA")      
    
    # Anna
    def test_ConstructorInvalidCityBlank(self):
        print("\nTesting the constructor with a blank city (too short)") 
        
        # Ensures the Address object with false call to city
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", self.invalidEmpty, "VA")

    # Anna
    def test_ConstructorInvalidCitySpecialChar(self):
        print("\nTesting the constructor with a city with special characters") 
        
        # Ensures the Address object with false call to city
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", self.invalidCharsStreetCity, "VA")        
    
    # Anna
    def test_ConstructorInvalidCityLength(self):
        print("\nTesting the constructor with a city that is too long") 
        
        # Ensures the Address object with false call to city
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", self.invalidStreetCityLength, "VA")
    
    # Anna
    def test_ConstructorInvalidStateType(self):
        print("\nTesting the constructor with an invalid state type") 
        
        # Ensures the Address object with false call to state
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", "City", self.invalidType)    
    
    # Anna
    def test_ConstructorInvalidStateBlank(self):
        print("\nTesting the constructor with a blank state (too short)") 
        
        # Ensures the Address object with false call to state
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", "City", self.invalidEmpty)

    # Anna
    def test_ConstructorInvalidStateSpecialChar(self):
        print("\nTesting the constructor with a state with special characters") 
        
        # Ensures the Address object with false call to state
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", "City", self.invalidCharsState)        
    
    # Anna
    def test_ConstructorInvalidStateLength(self):
        print("\nTesting the constructor with a state that is too long") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", "City", self.invalidStateLength)
    
    # Anna
    def test_ConstructorInvalidStateAbbreviation(self):
        print("\nTesting the constructor with an invalid state abbreviation") 
        
        # Ensures the Address object with false call to street
        # throws an assertion error
        self.assertRaises(AssertionError, Address, "Street", "City", self.invalidStateAbbr)
    
    # Anna
    def test_setStreetInvalidType(self):
        print("\nTesting setStreet() with an invalid street type") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setStreet, self.invalidType)    
    
    # Anna
    def test_setStreetInvalidBlank(self):
        print("\nTesting setStreet() with a blank street (too short)") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setStreet, self.invalidEmpty)

    # Anna
    def test_setStreetInvalidSpecialChar(self):
        print("\nTesting setStreet() with a street with special characters") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setStreet, self.invalidCharsStreetCity)        
    
    # Anna
    def test_setStreetInvalidLength(self):
        print("\nTesting setStreet() with a street that is too long") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setStreet, self.invalidStreetCityLength)
    
    # Anna
    def test_setCityInvalidType(self):
        print("\nTesting setCity() with an invalid city type") 
        
        # Ensures the Address object with false call to changing city
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setCity, self.invalidType)    
    
    # Anna
    def test_setCityInvalidBlank(self):
        print("\nTesting setCity() with a blank city (too short)") 
        
        # Ensures the Address object with false call to changing city
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setCity, self.invalidEmpty)

    # Anna
    def test_setCityInvalidSpecialChar(self):
        print("\nTesting setCity() with a city with special characters") 
        
        # Ensures the Address object with false call to changing city
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setCity, self.invalidCharsStreetCity)        
    
    # Anna
    def test_setCityInvalidLength(self):
        print("\nTesting setCity() with a city that is too long") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setCity, self.invalidStreetCityLength)
    
    # Anna
    def test_setStateInvalidType(self):
        print("\nTesting setState() with an invalid state type") 
        
        # Ensures the Address object with false call to changing state
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setState, self.invalidType)    
    
    # Anna
    def test_setStateInvalidBlank(self):
        print("\nTesting setState() with a blank state (too short)") 
        
        # Ensures the Address object with false call to changing state
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setState, self.invalidEmpty)

    # Anna
    def test_setStateInvalidSpecialChar(self):
        print("\nTesting setState() with a state with special characters") 
        
        # Ensures the Address object with false call to state
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setState, self.invalidCharsState)        
    
    # Anna
    def test_setStateInvalidLength(self):
        print("\nTesting setState() with a state that is too long") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setState, self.invalidStateLength)
    
    # Anna
    def test_setStateInvalidAbbreviation(self):
        print("\nTesting setState() with an invalid state abbreviation") 
        
        # Ensures the Address object with false call to changing street
        # throws an assertion error
        self.assertRaises(AssertionError, self.validAddress.setState, self.invalidStateAbbr)    

if __name__ == '__main__':
    unittest.main()
