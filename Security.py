# Example of storing and retrieving Clients securely - adapted from
# https://www.askpython.com/python/examples/storing-retrieving-Clients-securely
# @author: Gurpreet Kaur / December 29, 2023
# @author: John McManus
# @date 11/08/2024
# import the required libraries
import os
import hashlib
# Example Client clas to demonstrat storing the required attributes to has passwords
class Client():
    # Define the Class Constants
    PEPPER = "SHELBY_MADE"
    PASS_MIN_LEN = 8
    PASS_MAX_LEN = 16
    bad_Chars = {"/", "\\", "<", ">", "|", ""} 
   
   
    # Client constructor
    # @parameter: password - the string passed in containing the password
    # @require: 8 <= len(password) <= 16
    # @require: password does not contain "/", "\\", "<", ">", "|"
    def __init__(self, password):
        assert isinstance(password, str), "Invalid type"
        assert Client.PASS_MIN_LEN <= len(password) <= Client.PASS_MAX_LEN, "Invalid length"
        assert _checkSyntax(password)
        self._createSecureHash(password)
   
   
   # return a string representation of the object
    def __repr__(self):
        return ("Iterations: %d, salt: %s, Algorithm: %s" % (self._iterations, \
            self._salt, self._hash_algo))
    

    # Method to securly hash the password
    # @parameter: the password to hash
    # @require: 8 <= len(password) <= 16
    # @require: password does not contain "/", "\\", "<", ">", "|"
    def _createSecureHash(self, password):
        assert isinstance(password, str), "Invalid type"
        assert Client.PASS_MIN_LEN <= len(password) <= Client.PASS_MAX_LEN, "Invalid length"
        assert _checkSyntax(password)
        self._salt = os.urandom(16)
        self._iterations = 100_000
        self._hash_algo = 'sha256'
        hash_value = hashlib.pbkdf2_hmac(self._hash_algo, \
            password.encode('utf-8') + Client.PEPPER.encode('utf-8'), self._salt, self._iterations)
        self._hash = hash_value


    # Private method to check a password against the stored hash
    # @parameter: password - the string passed in containing the password to check
    # @require: 8 <= len(password) <= 16
    # @require: password does not contain "/", "\\", "<", ">", "|"
    def _checkPassword(self, password):
        #Assertions to check password type, length, and syntax
        assert isinstance(password, str), "Invalid type"
        assert Client.PASS_MIN_LEN <= len(password) <= Client.PASS_MAX_LEN, "Invalid length"
        assert _checkSyntax(password)
        # Compute the hash from password entered
        passswordHash = hashlib.pbkdf2_hmac(self._hash_algo,\
            password.encode('utf-8') + Client.PEPPER.encode('utf-8'), self._salt, self._iterations)
        # Compare the computed hash and the stored hash and return the result
        return (passswordHash == self._hash)
    
# helper function to check the password for prohibitied characters
# @parameter: password - the string passed in containing the password
# @require: 8 <= len(password) <= 16
def _checkSyntax(password):
    assert isinstance(password, str), "Invalid type"
    assert Client.PASS_MIN_LEN <= len(password) <= Client.PASS_MAX_LEN, "Invalid length"
    result = True
    for element in password:
        result = result and element not in Client.bad_Chars
    return result
