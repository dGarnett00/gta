# game.py
import random  # Import the random module for generating random numbers used in game events
from characters import Player, NPC, Mugger, Prostitute, Enemy  # Import character classes for player and NPC interactions
from locations import get_locations  # Import a function to retrieve available locations in the game

class Game:  # Define the Game class to encapsulate the game's logic and functionality
    def __init__(self):  # Initialize a new game instance
        player_name = input("Enter your character's name: ")  # Prompt the user for their character's name
        self.player = Player(player_name)  # Create a Player object using the provided name
        self.location = None  # Initialize the player's location to None (not set)
        self.game_over = False  # Set a flag to indicate whether the game is over
        self.locations = get_locations()  # Retrieve a list of valid locations for the player to visit

    def display_status(self):  # Define a method to display the current status of the player
        print("\n--- Status ---")  # Print a header for the status display
        # Print the current location name or a default message indicating an escaped state
        print(f"Current Location: {self.location.name if self.location else 'Escaped from prison'}")
        print(f"Name: {self.player.name}")  # Display the player's character name
        print(f"Health: {self.player.health}")  # Display the player's current health points
        print(f"Money: ${self.player.money}")  # Display the money the player currently possesses
        print(f"Muscle: {self.player.muscle}")  # Display the player's muscle points, indicating strength level

    def travel(self):  # Define a method that allows the player to travel to different game locations
        print("\nWhere would you like to travel? (Type 'exit' to quit)")  # Prompt the player for a travel location

        # Loop through the available locations to display them to the player
        for idx, loc in enumerate(self.locations):  
            print(f"{idx + 1}: {loc.name}")  # Print the index and name of each location

        choice = input("> ")  # Get user input for their location choice
        if choice.lower() == "exit":  # Check if the user wants to exit the game
            print("Thanks for playing! Goodbye!")  # Print a farewell message
            self.game_over = True  # Set the game_over flag to True to end the game
            return  # Exit the method

        try:  # Try to process the user's input
            choice = int(choice) - 1  # Convert the input to an integer index (adjust for zero-based indexing)
            if 0 <= choice < len(self.locations):  # Check if the chosen index is within the valid range
                new_location = self.locations[choice]  # Get the newly chosen location

                # Check if the user is trying to travel to the same location
                if new_location == self.location:  
                    print("You are already in this location! Choose a different one.")  # Inform the user to select a different location
                    return  # Exit the method without changing the location

                self.location = new_location  # Update the player's current location
                print(f"You travel to {self.location.name}.")  # Notify the player of the new location
                print(self.location.description)  # Print the description of the newly arrived location

                # If the player arrives at the Gym, invoke gym-specific options
                if self.location.name == "Gym":
                    self.gym_options()  # Call the gym options function for actions available in the gym

                self.encounter()  # Trigger a random encounter after the player travels
            else:  # If the chosen index is out of bounds
                print("Invalid choice!")  # Notify the player of the invalid choice
        except ValueError:  # Handle the case where the input cannot be converted to an integer
            print("Please enter a valid number or 'exit' to quit.")  # Ask for a valid input again

    def gym_options(self):  # Define a method for actions available in the gym
        while True:  # Loop to allow continuous options in the gym
            print("\nWhat would you like to do?")  # Prompt the user for their choice of action within the gym
            for idx, option in enumerate(self.location.get_options()):  # Loop through available gym options for the player
                print(f"{idx + 1}: {option}")  # Print each option along with its index

            choice = input("> ")  # Get the player's choice of action in the gym
            if choice == "1":  # If the player chooses to work out
                print("You decide to work out! Your muscle increases.")  # Notify the player of their workout decision
                self.player.gain_muscle(1)  # Increase the player's muscle points by 1 using the newly defined method
            elif choice == "2":  # If the player chooses to leave the gym
                print("You chose to leave the gym.")  # Notify the player
                break  # Exit the loop, returning to the travel options
            else:  # If the player's choice is invalid
                print("Invalid choice! Please select a valid option.")  # Ask for valid input

    def interact_with_character(self, character):  # Define a method for player interaction with characters
        if isinstance(character, Prostitute):  # Check if the character is a Prostitute
            print(f"{character.name}: {character.offer_services()}")  # Display the prostitute's offer
            return  # Placeholder for future implementation of prostitute interactions

        elif isinstance(character, NPC):  # Check if the character is a non-playable character (NPC)
            print(f"\n{character.name}: {character.interact()}")  # Display the NPC's dialogue
            if random.random() < 0.1:  # 10% chance to receive a reward from the NPC
                reward = random.randint(10, 100)  # Generate a random reward amount between $10 and $100
                self.player.money += reward  # Add the reward to the player's total money
                print(f"{character.name} gave you ${reward}! What a nice surprise!")  # Notify the player of the reward

        elif isinstance(character, Mugger):  # Check if the character is a Mugger
            print(f"You encounter a mugger: {character.name}!")  # Notify the player of the mugger encounter
            self.fight(character)  # Call the fight method to handle the fight with the mugger

        elif isinstance(character, Enemy):  # Check if the character is an Enemy
            print(f"You encounter an enemy: {character.name}!")  # Notify the player of the enemy encounter
            self.fight(character)  # Call the fight method to handle the fight with the enemy
      
    def fight(self, enemy):  # Define a method to handle the fight against an enemy
        while self.player.is_alive() and enemy.is_alive():  # Loop while both the player and the enemy are alive
            print(f"\nYou encounter {enemy.name}! Health: {enemy.health}, Muscle: {self.player.muscle}")  # Notify the player about the encounter
            action = input("Choose an action: (1) Punch (2) Flee \n> ")  # Prompt the player to choose an action
            if action == "1":  # If the player chooses to punch
                # Calculate damage using player's muscle 
                player_damage = random.randint(5, 15) + self.player.muscle  # Include muscle points in damage calculation
                enemy.take_damage(player_damage)  # Inflict damage on the enemy
                print(f"You hit {enemy.name} for {player_damage} damage!")  # Notify the player of the damage dealt to the enemy

                # Check if the enemy has been defeated
                if not enemy.is_alive():  
                    loot = enemy.loot()  # Loot the defeated enemy's money
                    self.player.money += loot  # Add the loot to the player's total money
                    print(f"You defeated {enemy.name} and looted ${loot}!")  # Notify the player of their success
                    break  # Exit the fight loop after defeating the enemy

                # If enemy is still alive, it retaliates
                enemy_damage = random.randint(5, 15)  # Generate random damage value for the enemy's attack
                self.player.take_damage(enemy_damage)  # Inflict damage to the player
                print(f"{enemy.name} hit you for {enemy_damage} damage!")  # Notify the player of the damage taken
            elif action == "2":  # If the player chooses to flee
                print("You fled from the fight!")  # Notify the player of their choice to escape
                break  # Exit the fight loop
            else:  # If the player's action is invalid
                print("Invalid action! Choose 1 to Punch or 2 to Flee.")  # Prompt the player to choose a valid action

        # Check if the player has been defeated during the fight
        if not self.player.is_alive():  
            self.game_over = True  # Set the game over flag to True
            print("You were defeated!")  # Notify the player that they lost the encounter

    def encounter(self):  # Define a method to handle random encounters
        print("\nYou encounter something!")  # Inform the player that an encounter is about to occur
        encounter_type = random.choice(["npc", "mugger", "prostitute", "enemy"])  # Randomly choose an encounter type

        if encounter_type == "npc":  # If the encounter is with an NPC
            npc = NPC("Villager", health=50, money=10)  # Create an NPC instance
            self.interact_with_character(npc)  # Initiate interaction with the created NPC

        elif encounter_type == "mugger":  # If the encounter is with a mugger
            mugger = Mugger("Thug")  # Create a Mugger instance
            self.interact_with_character(mugger)  # Initiate interaction with the mugger

        elif encounter_type == "prostitute":  # If the encounter is with a prostitute
            prostitute = Prostitute("Prostitute")  # Create a Prostitute instance
            self.interact_with_character(prostitute)  # Initiate interaction with the prostitute

        elif encounter_type == "enemy":  # If the encounter is with an Enemy
            enemy = Enemy()  # Create an Enemy instance
            if not enemy.defeated:  # Only interact if this enemy hasn't been defeated
                self.interact_with_character(enemy)  # Initiate interaction with the enemy 

    def play(self):  # Define the main game loop where gameplay occurs
        print("Welcome to the Text-Based GTA Game!")  # Print a welcome message for the player
        while not self.game_over:  # Continue the loop until the game is over
            self.display_status()  # Display the current status of the player's character
            self.travel()  # Call the travel method to allow the player to choose a location to travel to

        print("Game Over! You couldn't survive.")  # Print a message indicating that the game has ended

if __name__ == "__main__":  # Check if the script is run directly (not imported as a module)
    game = Game()  # Create a new instance of the Game class
    game.play()  # Start the game by calling the play method that enters the main gameplay loop