import random  # Import the random module for generating random values

class Character:  # Define a base class for characters in the game
    def __init__(self, name, health, money):  # Initialize a character with name, health, and money
        self.name = name  # Set the character's name
        self.health = health  # Set the character's health
        self.money = money  # Set the character's money

    def is_alive(self):  # Method to check if the character is alive
        return self.health > 0  # Return True if health is greater than 0, otherwise False

    def take_damage(self, amount):  # Method to reduce health when taking damage
        self.health -= amount  # Decrease health by the specified amount

    def earn_money(self, amount):  # Method to increase money
        self.money += amount  # Increase money by the specified amount

    def __str__(self):  # String representation of the character
        return f"{self.name} | Health: {self.health} | Money: ${self.money}"  # Return a formatted string


class Player(Character):  # Define a Player class that inherits from Character
    def __init__(self, name):  # Initialize the player with a name
        super().__init__(name, health=100, money=50)  # Call the parent class's initializer with default health and money
        self.muscle = 0  # Initialize muscle points

    def gain_muscle(self, amount):  # Method for the player to gain muscle
        self.muscle += amount  # Increase muscle points
        print(f"{self.name} gained {amount} muscle points!")

    def lose_muscle(self, amount):  # Method for the player to lose muscle
        self.muscle = max(0, self.muscle - amount)  # Avoid negative muscle points
        print(f"{self.name} lost {amount} muscle points!")

    def __str__(self):  # String representation including muscle points
        return f"{self.name} | Health: {self.health} | Money: ${self.money} | Muscle: {self.muscle}"  # Return formatted string with muscle


class NPC(Character):  # Define an NPC (Non-Player Character) class that inherits from Character
    def __init__(self, name, health, money):  # Initialize the NPC with name, health, and money
        super().__init__(name, health, money)  # Call the parent class's initializer
        self.dialogues = [  # List of random dialogues for the NPC
            "Hello there!",
            "What brings you here?",
            "It's a nice day, isn't it?",
            "Watch your back out there!",
            "I have some information for you."
        ]

    def interact(self):  # Method for NPC interaction
        return random.choice(self.dialogues)  # Return a random dialogue from the NPC


class Mugger(Character):  # Define a Mugger class that inherits from Character
    def __init__(self, name):  # Initialize the mugger with a name
        health = random.randint(10, 50)  # Set random health for the mugger (between 10 and 50)
        money = random.randint(5, 30)  # Set random money that the mugger has (between 5 and 30)
        super().__init__(name, health, money)  # Call the parent class's initializer

    def loot(self):  # Method to loot money from the mugger
        loot_amount = self.money  # Set loot amount to the mugger's current money
        self.money = 0  # Set the mugger's money to 0 after looting
        return loot_amount  # Return the loot amount


class Prostitute(Character):  # Define a Prostitute class that inherits from Character
    def __init__(self, name):  # Initialize the prostitute with a name
        super().__init__(name, health=30, money=20)  # Call the parent class's initializer with specific health and money

    def offer_services(self):  # Method for the prostitute's services
        return "What would you like to do? (1) Sex, (2) Rob, (3) Fight"
    










'''
# Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    player = Player("Hero")  # Create a new player character named "Hero"
    npc = NPC("Villager", health=50, money=10)  # Create a new NPC character named "Villager"
    mugger = Mugger("Thug")  # Create a new random mugger
    prostitute = Prostitute("Lola")  # Create a new prostitute

    print(player)  # Print the player's status
    print(npc)  # Print the NPC's status
    print(mugger)  # Print the mugger's status
    print(prostitute)  # Print the prostitute's status
    '''