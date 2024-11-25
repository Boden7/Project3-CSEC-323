""" 
This module defines the Name class.
@author: Hunter Peacock and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a Name
"""
class Name: 
      
    # Constructs a Name object.
    #
    #  @param first_name: The first name of the Name (String)
    #  @param last_name: The last name of the Name (String)
    #
    #  @require: first_name is a String type between 1 and 25 characters inclusive that does not contain any special characters
    #  @require: last_name is a String type between 1 and 40 characters inclusive that does not contain any special characters
    #
    #  @ensure Name object successfully created    
    def __init__(self, first_name: str, last_name: str):
        # Assert statements for preconditions
        assert isinstance(first_name, str), "The first name must be of a String type."
        assert first_name.isalpha(), "The first name must not contain any special characters."
        assert len(first_name) > 0 and len(first_name) <= 25, "The first name must be a valid length."
        assert isinstance(last_name, str), "The last name must be of a String type."
        assert last_name.isalpha(), "The last name must not contain any special characters."
        assert len(last_name) > 0 and len(last_name) <= 40, "The last name must be a valid length."
      
        self._firstName = first_name 
        self._lastName = last_name 
    
    # An accessor/getter method for the first name
    #
    # @return: The first name associated with the Bank Account (String)
    # Anna
    def getFirstName(self):
        return self._firstName
   
    # An accessor/getter method for the last name
    #
    # @return: The last name associated with the Bank Account (String)
    # Anna
    def getLastName(self):
        return self._lastName

    # A mutator/setter method for the last name
    #
    #  @param last: The last name of the Name (String)
    #
    #  @require: last is a String type between 1 and 40 characters inclusive that does not contain any special characters  
    # Anna
    def setLastName(self, last):
        # Assert statements for preconditions
        assert isinstance(last, str), "The last name must be of a String type."
        assert last.isalpha(), "The last name must not contain any special characters."
        assert len(last) > 0 and len(last) <= 40, "The last name must be a valid length."
        
        self._lastName = last 

    # A mutator/setter method for the first name
    #
    #  @param first: The first name of the Name (String)
    #
    #  @require: first is a String type between 1 and 25 characters inclusive that does not contain any special characters
    # Anna
    def setFirstName(self, first):
        # Assert statements for preconditions
        assert isinstance(first, str), "The first name must be of a String type."
        assert first.isalpha(), "The first name must not contain any special characters."
        assert len(first) > 0 and len(first) <= 25, "The first name must be a valid length."      
        
        self._firstName = first

    # Repr method for string representation of the full name
    #
    # @return: A String representation of the Name object (String)      
    # Hunter 
    def __repr__(self):
        return f"{self._firstName} {self._lastName}"