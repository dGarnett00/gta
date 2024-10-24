# locations.py

class Location:  # Define a class named Location to represent different places in the game
    def __init__(self, name, description, options):  # Constructor to initialize the attributes of a Location
        self.name = name  # Assign the name of the location (e.g., "Gym", "Store", "Home")
        self.description = description  # Assign a description that provides details about the location
        self.options = options  # Assign a list of actions/options the player can take at this location

    def __str__(self):  # Define a method to provide a string representation of the location
        return f"{self.name}: {self.description}"  # Format and return the location's name along with its description

    def get_options(self):  # Define a method to retrieve the available options for the location
        return self.options  # Return the list of options available to the player at this location


# Define a function to retrieve all available locations in the game
def get_locations():  # Create a function named get_locations to gather all location objects
    return [  # Return a list of Location objects, each representing a different place in the game
        Location("Gym", "Welcome to the gym.", ["Work Out", "Leave"]),  # Create a Gym location with its description and available options
        Location("Store", "Welcome to the store.", ["Browse", "Leave"]),  # Create a Store location with its description and available options
        Location("Home", "Welcome home.", ["Relax", "Leave"]),  # Create a Home location with its description and available options
    ]  # End of the list of locations