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
        Location("Gym", "Welcome to the gym."),  # Changed City Center to Gym
        Location("Store", "Welcome to the store."),  # Changed Park to Store
        Location("Home", "Welcome home."),  # Changed Suburbs to Home
    ]  # End of the list of locations