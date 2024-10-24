# locations.py

class Location:  # Define a class named Location
    def __init__(self, name, description, options):  # Initialize the Location class with a name, description, and options
        self.name = name  # Set the name of the location
        self.description = description  # Set the description of the location
        self.options = options  # Set the options available at this location

    def __str__(self):  # Define a method to return a string representation of the location
        return f"{self.name}: {self.description}"  # Return the name and description of the location in a formatted string

    def get_options(self):  # Define a method to get available options
        return self.options  # Return the options for the location


# Define a function to get all available locations
def get_locations():  # Create a function named get_locations
    return [  # Return a list of Location objects
        Location("Gym", "Welcome to the gym.", ["Work Out", "Leave"]),  # Options for Gym
        Location("Store", "Welcome to the store.", ["Browse", "Leave"]),  # General options for Store
        Location("Home", "Welcome home.", ["Relax", "Leave"]),  # General options for Home
    ]  # End of the list of locations