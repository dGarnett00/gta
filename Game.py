import random  # Import the random module for generating random values
from characters import Player, NPC, Mugger, Prostitute  # Import character classes
from locations import get_locations  # Import the function to get locations

class Game:  # Define a new class called Game
    def __init__(self):  # Define the initializer method for the Game class
        player_name = input("Enter your character's name: ")  # Prompt for the player's name
        self.player = Player(player_name)  # Create a player character with the provided name
        self.location = None  # Initialize the current location
        self.game_over = False  # Set the game over flag to False
        
        # Load the available locations
        self.locations = get_locations()  # Get the list of locations

    def display_status(self):  # Define a method to display the player's status
        print("\n--- Status ---")  # Print a header for the status display
        print(f"Current Location: {self.location.name if self.location else 'Escaped from prison'}")  # Print the current location
        print(f"Health: {self.player.health}")  # Print the player's current health
        print(f"Money: ${self.player.money}")  # Print the player's current amount of money
        print(f"Muscle: {self.player.muscle}")  # Print the player's current muscle points

    def travel(self):  # Define a method for the player to travel to different locations
        print("\nWhere would you like to travel? (Type 'exit' to quit)")  # Prompt the player for travel options

        for idx, loc in enumerate(self.locations):  # Loop through each location with its index
            print(f"{idx + 1}: {loc.name}")  # Print the index and name of each location

        choice = input("> ")  # Get the player's choice
        if choice.lower() == "exit":  # Check if the player wants to exit
            print("Thanks for playing! Goodbye!")  # Farewell message
            self.game_over = True  # Set the game over flag to True
            return

        try:
            choice = int(choice) - 1  # Convert the player's choice to an index
            if 0 <= choice < len(self.locations):  # Check if the player's choice is valid
                new_location = self.locations[choice]  # Store the new location

                if new_location == self.location:  # Check if the new location is the same as the current one
                    print("You are already in this location! Choose a different one.")  # Notify the player
                    return  # Do not proceed with traveling

                self.location = new_location  # Update the location based on the player's choice
                print(f"You travel to {self.location.name}.")  # Inform the player of their new location
                print(self.location.description)  # Print the description of the location
                self.encounter()  # Trigger an encounter after traveling
            else:  # If the choice is invalid
                print("Invalid choice!")  # Inform the player of the invalid choice
        except ValueError:  # Handle non-integer inputs
            print("Please enter a valid number or 'exit' to quit.")  # Notify the player of invalid input

    def interact_with_character(self, character):  # Method for interaction with any character
        if isinstance(character, Prostitute):  # Check if the character is a prostitute
            print(f"\n{character.name}: {character.offer_services()}")  # Display services offered
            action = input("Choose an option (1, 2, or 3) or type 'exit' to quit: ")  # Get player's action choice

            if action.lower() == "exit":  # Check if the player wants to exit
                print("Thanks for playing! Goodbye!")  # Farewell message
                self.game_over = True  # Set the game over flag to True
                return

            if action == "1":  # If the player chooses to have sex
                if self.player.money >= 10:  # Check if the player has enough money
                    self.player.money -= 10  # Deduct money from the player
                    print(f"You have sex with {character.name}. You paid $10.")  # Notify the player
                else:
                    print("You don't have enough money for this service.")  # Notify if not enough money

            elif action == "2":  # If the player chooses to rob
                success = random.random() < 0.8  # 80% chance of success
                if success:
                    loot = character.money  # Loot the prostitute's money
                    self.player.money += loot  # Add the loot to the player's total money
                    character.money = 0  # Set the prostitute's money to 0
                    print(f"You successfully robbed {character.name} and got ${loot}!")  # Notify the player
                else:
                    print("You failed to rob the prostitute!")  # Notify if the robbery failed

            elif action == "3":  # If the player chooses to fight
                success = random.random() < 0.9  # 90% chance of success
                if success:
                    damage = random.randint(5, 15)  # Random damage the player can deal
                    character.take_damage(damage)  # Inflict damage on the prostitute
                    print(f"You fought {character.name} and dealt {damage} damage!")  # Notify the player
                    if not character.is_alive():  # Check if the prostitute is defeated
                        loot = character.money  # Loot money from the prostitute
                        self.player.money += loot  # Add the loot to the player's total money
                        character.money = 0  # Set the prostitute's money to 0
                        print(f"You defeated {character.name} and looted ${loot}!")  # Notify the player of the loot
                else:
                    print("You failed to fight the prostitute!")  # Notify if the fight failed

        elif isinstance(character, NPC):  # Check if the character is an NPC
            print(f"\n{character.name}: {character.interact()}")  # Display NPC's dialogue

            # 10% chance to reward the player with money
            if random.random() < 0.1:  # 10% chance
                reward = random.randint(10, 100)  # Random amount between $10 and $100
                self.player.money += reward  # Add the reward to the player's money
                print(f"{character.name} gave you ${reward}! What a nice surprise!")  # Notify the player of the reward

        elif isinstance(character, Mugger):  # Check if the character is a Mugger
            print(f"You encounter a mugger: {character.name}!")  # Notify the player about the mugger encounter
            while self.player.is_alive() and character.is_alive():
                action = input("Do you want to (1) Fight or (2) Flee? (Type 'exit' to quit) ")  # Ask the player for action
                if action.lower() == "exit":  # Check if the player wants to exit
                    print("Thanks for playing! Goodbye!")  # Farewell message
                    self.game_over = True  # Set the game over flag to True
                    return

                if action == "1":  # If the player chooses to fight
                    damage = random.randint(5, 20)  # Random damage the player can deal
                    character.take_damage(damage)  # Inflict damage on the mugger
                    print(f"You dealt {damage} damage to the mugger!")  # Notify the player
                    if not character.is_alive():  # Check if the mugger is defeated
                        loot = character.loot()  # Loot money from the mugger
                        self.player.money += loot  # Add the loot to the player's total money
                        print(f"You defeated the mugger and looted ${loot}!")  # Notify the player of the loot
                        break  # Exit the loop if the mugger is defeated
                    # Mugger attacks back
                    mugger_damage = random.randint(5, 15)  # Random damage the mugger can deal
                    self.player.take_damage(mugger_damage)  # Inflict damage on the player
                    print(f"The mugger dealt {mugger_damage} damage to you!")  # Notify the player of the damage taken
                elif action == "2":  # If the player chooses to flee
                    print("You fled from the mugger!")  # Notify the player
                    break  # Exit the loop if the player flees
                else:
                    print("Invalid action! Choose 1 or 2.")  # Notify the player of an invalid action

            if not self.player.is_alive():  # Check if the player is defeated
                self.game_over = True  # Set the game over flag to True
                print("You were defeated by the mugger!")  # Notify the player of their defeat

    def encounter(self):  # Define a method for encounters that happen during travel
        print("\nYou encounter something!")  # Inform the player that an encounter occurs
        encounter_type = random.choice(["npc", "mugger", "prostitute"])  # Randomly choose between an NPC, mugger, or prostitute

        if encounter_type == "npc":  # If the encounter is with an NPC
            npc = NPC("Villager", health=50, money=10) 
            self.interact_with_character(npc)

        elif encounter_type == "mugger":  # If the encounter is with a mugger
            mugger = Mugger("Thug") 
            self.interact_with_character(mugger)

        elif encounter_type == "prostitute":  # If the encounter is with a prostitute
            prostitute = Prostitute("Lola") 
            self.interact_with_character(prostitute)

    # Define the main game loop
    def play(self):
        print("Welcome to the Text-Based GTA Game!")  # Print a welcome message
        while not self.game_over:  # Continue the loop until the game is over
            self.display_status()  # Display the player's current status
            self.travel()  # Call the travel method to allow the player to travel

        print("Game Over! You couldn't survive.")  # Inform the player that the game is over

if __name__ == "__main__":  # Check if the script is being run directly
    game = Game()  # Create an instance of the Game class
    game.play()  # Start the game by calling the play method