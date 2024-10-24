# characters.py
import random  # Import the random module to facilitate the generation of random values used throughout the game

class Character:  # Define a base class for all characters within the game
    def __init__(self, name, health, money):  # Method to initialize a character with specific attributes
        self.name = name  # Assign the character's name
        self.health = health  # Assign the character's health
        self.money = money  # Assign the amount of money the character possesses

    def is_alive(self):  # Method to check if the character is still alive
        return self.health > 0  # Return True if health is greater than 0, otherwise return False

    def take_damage(self, amount):  # Method to handle damage taken by the character
        self.health -= amount  # Reduce the character's health by the specified damage amount

    def earn_money(self, amount):  # Method for increasing the character's money
        self.money += amount  # Increase the character's money by the specified amount

    def __str__(self):  # Define the string representation of the character
        return f"{self.name} | Health: {self.health} | Money: ${self.money}"  # Return a formatted string with character attributes


class Player(Character):  # Define a Player class that inherits from the Character base class
    def __init__(self, name):  # Initialize the player with a given name
        super().__init__(name, health=100, money=50)  # Call the parent class's initializer with default values for health and money
        self.muscle = 0  # Initialize muscle points for the player

    def gain_muscle(self, amount):  # Method for the player to gain muscle points
        self.muscle += amount  # Increase the player's muscle points by the specified amount
        print(f"{self.name} gained {amount} muscle points!")  # Notify the player of their gained muscle points

    def lose_muscle(self, amount):  # Method for the player to lose muscle points
        self.muscle = max(0, self.muscle - amount)  # Decrease muscle points but prevent them from going below zero
        print(f"{self.name} lost {amount} muscle points!")  # Notify the player of their lost muscle points

    def __str__(self):  # Define the string representation of the player
        return f"{self.name} | Health: {self.health} | Money: ${self.money} | Muscle: {self.muscle}"  # Return formatted string with player's attributes


class NPC(Character):  # Define a Non-Player Character (NPC) class that inherits from Character
    def __init__(self, name, health=50, money=10):  # Initialize an NPC with a specific name, health, and money
        super().__init__(name, health, money)  # Call the parent class's initializer to set attributes
        self.dialogues = [  # Define a list of possible dialogues for the NPC
            "Hello there!",  # Dialogue options that can be randomly selected during interaction
            "What brings you here?",
            "It's a nice day, isn't it?",
            "Watch your back out there!",
            "I have some information for you."
        ]

    def interact(self):  # Method for interacting with the NPC
        return random.choice(self.dialogues)  # Return a randomly selected dialogue from the NPC's list


class Enemy(Character):  # Define an Enemy class that inherits from Character
    ENEMY_NAMES = ["Carlos", "Davonta", "Ray-Ray", "Doog"]  # List of possible enemy names
    MAX_HEALTH = 50  # Maximum health for enemies

    def __init__(self):
         # Randomly choose an enemy name
        self.health = random.randint(30, 50)  # Randomly set enemy health between 30 and 50
        self.encounter_count = 0  # Track the number of encounters with the player
        self.defeated = False  # Track if the enemy is defeated

    def interact(self):
        # Enemy dialogue based on encounter count
        dialogues = {
            "Carlos": [
                "You think you can take me on?",
                "I won't go easy on you!",
                "This is our final showdown!"
            ],
            "Davonta": [
                "Ready to lose?",
                "You think you're tough?",
                "I've had enough of you!"
            ],
            "Ray-Ray": [
                "No one beats me!",
                "You’ll regret this!",
                "You can’t escape!"
            ],
            "Doog": [
                "You’ll pay for this!",
                "I’m way stronger than you think!",
                "You don’t stand a chance!"
            ]
        }
        return dialogues[self.name][self.encounter_count % len(dialogues[self.name])]  # Select dialogue based on encounter count

    def take_damage(self, amount):
        self.health -= amount  # Decrease enemy's health by the damage amount
        if self.health < 0:  # Prevent negative health
            self.health = 0

    def is_alive(self):
        return self.health > 0  # Check if enemy is still alive

    def loot(self):
        return random.randint(5, 30)  # Define loot value when defeated


class Mugger(Character):  # Define a Mugger class which inherits from Character
    def __init__(self, name):  # Initialize the mugger with a name
        health = random.randint(10, 50)  # Assign a random health value to the mugger (between 10 and 50)
        money = random.randint(5, 30)  # Assign a random amount of money the mugger possesses (between 5 and 30)
        super().__init__(name, health, money)  # Call the parent class's initializer to set the mugger's attributes

    def loot(self):  # Method to handle looting money from the mugger
        loot_amount = self.money  # Set the loot amount to the current money the mugger has
        self.money = 0  # After looting, set the mugger's money to zero
        return loot_amount  # Return the quantity of money looted


class Prostitute(Character):  # Define a Prostitute class that inherits from Character
    def __init__(self, name):  # Initialize the prostitute with a name
        super().__init__(name, health=30, money=20)  # Call the parent class's initializer with specific values for health and money

    def offer_services(self):  # Method for the prostitute to offer services
        return "What would you like to do? (1) Sex, (2) Rob, (3) Fight"  # Return a string indicating available actions



'''


def get_locations():
    # This function simulates fetching locations
    # Replace these with your actual location objects
    return [Location("Gym", "A place to enhance your strength."), Location("Park", "A peaceful area to relax.")]


class Location:
    def __init__(self, name, description):
        self.name = name  # Location name
        self.description = description  # Description of the location

    def get_options(self):
        return ["Work out", "Leave"]  # Sample options for locations


        # Example usage (this section can be removed or commented out in production):
if __name__ == "__main__":  # Check if this script is being executed as the main program
    player = Player("Hero")  # Create a new Player character named "Hero"
    npc = NPC("Villager", health=50, money=10)  # Create a new NPC character named "Villager" with specified attributes
    mugger = Mugger("Thug")  # Create a new mugger character with a random name
    prostitute = Prostitute("Lola")  # Create a new prostitute named "Lola"

    print(player)  # Print the player's status
    print(npc)  # Print the NPC's status
    print(mugger)  # Print the mugger's status
    print(prostitute)  # Print the prostitute's status
'''