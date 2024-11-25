""" 
This module defines the Address class.
@author: Hunter Peacock, Boden Kahn, and Anna Pitt
@date: November 4, 2024

Class containing address information for clients
""" 
class Address:

    # Constructs an Address object.
    #
    #  @param street: The street name of the Address (String)
    #  @param city: The city name of the Address (String)
    #  @param state: The state abbreviation of the Address (String)
    #
    #  @require: street is a String type between 1 and 30 characters inclusive and must contain alphanumeric characters or spaces only
    #  @require: city is a String type between 1 and 30 characters inclusive and must only contain letters (upper or lower)
    #  @require: state is a String type that must have a length of 2, must only contain letters (upper or lower), and must be a valid state within the provided state list
    #
    #  @ensure Address object successfully created
    def __init__(self, street: str, city: str, state: str):

        assert isinstance(street, str), "The street must be of a String type."
        assert self.validStreet(street), "The street must not contain any special characters."
        assert len(street) > 0 and len(street) <= 30, "The street must be a valid length."
        
        assert isinstance(city, str), "The city must be of a String type."
        assert self.validCity(city), "The city must not contain any special characters."
        assert len(city) > 0 and len(city) <= 30, "The city must be a valid length."
        
        assert isinstance(state, str), "The state must be of a String type."
        assert state.isalpha(), "The state must not contain any special characters."
        assert len(state) == 2, "State abbreviation must be two characters in length."
        assert state in ["VA", "MD", "NJ", "PA", "DE", "NC", "WV", "DC"], "Invalid State designated."
      
        self._street = street
        self._city = city
        self._state = state 

    # Accessor/getter for the street name
    #
    #  @return: The street associated with the Address (String)
    # Hunter 
    def getStreet(self):
        return self._street

    # Accessor/getter for the city name
    #
    #  @return: The city associated with the Address (String)    
    # Hunter
    def getCity(self):
        return self._city

    # Accessor/getter for the state abbreviation
    #
    #  @return: The state abbreviation associated with the Address (String)    
    # Hunter
    def getState(self):
        return self._state

    # Mutator/setter for the street
    #
    #  @param street: The street name of the Address (String)
    #
    #  @require: street is a String type between 1 and 30 characters inclusive and must contain alphanumeric characters or spaces only   
    # Hunter
    def setStreet(self, street: str):
        assert isinstance(street, str), "The street must be of a String type."
        assert self.validStreet(street), "The street must not contain any special characters."
        assert len(street) > 0 and len(street) <= 30, "The street must be a valid length."
        self._street = street

    # Mutator/setter for the city
    #
    #  @param city: The city name of the Address (String)
    #
    #  @require: city is a String type between 1 and 30 characters inclusive and must only contain letters (upper or lower)
    # Hunter
    def setCity(self, city: str):
        assert isinstance(city, str), "The city must be of a String type."
        assert city.isalpha(), "The city must not contain any special characters."
        assert len(city) > 0 and len(city) <= 30, "The city must be a valid length."
        self._city = city

    # Mutator/setter for the state
    #
    #  @param state: The state abbreviation of the Address (String)
    #
    #  @require: state is a String type that must have a length of 2, must only contain letters (upper or lower), and must be a valid state within the provided state list    
    # Hunter 
    def setState(self, state: str):
        assert isinstance(state, str), "The state must be of a String type."
        assert state.isalpha(), "The state must not contain any special characters."
        assert len(state) == 2, "State abbreviation must be two characters in length."
        assert state in ["VA", "MD", "NJ", "PA", "DE", "NC", "WV", "DC"], "Invalid state designated."
        self._state = state

    # Check to be sure the street name doesn't have any special characters
    # Boden
    # @require every char in street is a letter, number, or space
    # @return The validity of the street name
    def validStreet(self, street: str):
        for character in street:
            if character.isalpha() or character.isdigit() or character == " ":
                pass
            else:
                return False
        return True
    
    # Check to be sure the city name doesn't have any special characters or numbers
    # Boden
    # @require every char in city is a letter, number, or space
    # @return The validity of the city name
    def validCity(self, city: str):
        for character in city:
            if character.isalpha() or character == " ":
                pass
            else:
                return False
        return True
        
    # Repr method for string representation of the full address
    #
    # @return: A String representation of the Address object (String)    
    # Hunter 
    def __repr__(self):
        return f"{self._street}, {self._city}, {self._state}"