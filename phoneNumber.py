""" 
This module defines the PhoneNumber class.
@author: Hunter Peacock and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a Phone Number
"""
class PhoneNumber: 
    
    # Constructs a PhoneNumber object.
    #
    #  @param phoneNum: The phone number associated with the PhoneNumber object (String)
    #
    #  @require: phoneNum is a String type with a length of 10 consisting of only numeric characters. The first index cannot be equal to 0.
    #
    #  @ensure PhoneNumber object successfully created       
    def __init__(self, phoneNum: str):
        assert isinstance(phoneNum, str), "The phone number must be a string composed of integer values."
        assert phoneNum.isdigit(), "The phone number must only contain integer values."
        assert len(phoneNum) == 10, "The phone number must be ten characters in length."
        assert phoneNum[0] != '0', "The phone number cannot start with '0'."
      
        self._phoneNum = phoneNum

   # Accessor/getter method for the phone number
   #
   # @return: The phone number associated with the PhoneNumber (String)   
   # Hunter 
    def getPhoneNumber(self):
        return self._phoneNum

    # Mutator/setter method for the phone number
    #
    #  @param number: The phone number to be associated with the PhoneNumber object (String)
    #
    #  @require: phoneNum is a String type with a length of 10 consisting of only numeric characters. The first index cannot be equal to 0.
    # Hunter 
    def setPhoneNumber(self, number: str):
        # Sets a new phone number after validating it:
        # Ensures new phone number is valid
        assert isinstance(number, str), "The phone number must be a string composed of integer values."
        assert number.isdigit(), "The phone number must only contain integer values."
        assert len(number) == 10, "The phone number must be ten characters in length."
        assert number[0] != '0', "The phone number cannot start with '0'."
      
        self._phoneNum = number # ensures most current value is set (updates phone number)

    # Repr method for string representation of the PhoneNumber
    #
    # @return: A String representation of the PhoneNumber object (String)     
    def __repr__(self):
        return f"+1({self._phoneNum[0:3]}){self._phoneNum[3:6]}-{self._phoneNum[6:]}"