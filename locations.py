# locations.py

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


# Define all available locations
def get_locations():
    return [
        Location("City Center", "The bustling heart of the city, filled with shops and people."),
        Location("Park", "A peaceful park with trees and a pond."),
        Location("Suburbs", "A quiet neighborhood with houses and families."),
        Location("Downtown", "The business district, busy with workers and traffic."),
        Location("Beach", "A sandy beach with waves crashing on the shore."),
    ]