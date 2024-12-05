""" 
This module defines the Password class.
@author: Hunter Peacock and Anna Pitt
@date: December 5th, 2024

A class to represent the data elements and methods required to implement a Password
"""

import os 
import hashlib

class Password:
    # Defines the Class Constants
    PASS_MIN_LEN = 8
    PASS_MAX_LEN = 16
    bad_Chars = {"/", "\\", "<", ">", "|", ""}

    # Constructs a Password object.
    #
    #  @param password: The password associated with the Password object (String)
    #
    #  @require: password is a String type with a length between 8 and 16 (both inclusive)
    #  that does not include any special characters as defined within bad_Chars
    #
    #  @ensure Password object successfully created
    def __init__(self, password):
        # Assert statements
        assert isinstance(password, str), "The password must be a string."
        assert Password.PASS_MIN_LEN <= len(password) <= Password.PASS_MAX_LEN, "The password must be between 8 and 16 characters."
        assert _checkSyntax(password)
        
        # Creates an instance variable to store the valid password
        self._password = password

# A private helper function to check the password for prohibited characters.
#
#  @param password: The password to check for invalid characters (String)
#
#  @require: password is a String type with a length between 8 and 16 (both inclusive)
#
#  @ensure Password object successfully created  
def _checkSyntax(password):
    # Assert statements
    assert isinstance(password, str), "The password must be a string."
    assert Password.PASS_MIN_LEN <= len(password) <= Password.PASS_MAX_LEN, "The password must be between 8 and 16 characters."
    
    # Sets a boolean
    result = True
    
    # Loops through every single character within the password
    for element in password:
        # Determines the result based on the previous result and if there
        # is an invalid character within the password or not
        result = result and element not in Password.bad_Chars
        
    # Returns the result
    return result
