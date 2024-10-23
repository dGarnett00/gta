# locations.py

class Location:  # Define a class named Location
    def __init__(self, name, description):  # Initialize the Location class with a name and a description
        self.name = name  # Set the name of the location
        self.description = description  # Set the description of the location

    def __str__(self):  # Define a method to return a string representation of the location
        return f"{self.name}: {self.description}"  # Return the name and description of the location in a formatted string


# Define a function to get all available locations
def get_locations():  # Create a function named get_locations
    return [  # Return a list of Location objects
        Location("City Center", "The bustling heart of the city, filled with shops and people."),  # Create a Location for City Center
        Location("Park", "A peaceful park with trees and a pond."),  # Create a Location for Park
        Location("Suburbs", "A quiet neighborhood with houses and families."),  # Create a Location for Suburbs
        Location("Downtown", "The business district, busy with workers and traffic."),  # Create a Location for Downtown
        Location("Beach", "A sandy beach with waves crashing on the shore."),  # Create a Location for Beach
    ]  # End of the list of locations