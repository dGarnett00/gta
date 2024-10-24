# game.py
import random  # Import the random module, enabling the generation of random numbers used for game events
from characters import Player, NPC, Mugger, Prostitute  # Import various character classes for player and NPC interactions
from locations import get_locations  # Import a function to retrieve available locations in the game

class Game:  # Define a class named Game that encapsulates the game's functionality
    def __init__(self):  # Define the initializer method, which sets up the game when an instance of Game is created
        player_name = input("Enter your character's name: ")  # Prompt the user to enter a name for their character
        self.player = Player(player_name)  # Create a Player object with the provided name
        self.location = None  # Initialize the current location of the player to None
        self.game_over = False  # Set a flag to track if the game is over, initialized to False
        
        # Load the available locations by calling the imported function
        self.locations = get_locations()  # Retrieve a list of locations that the player can visit

    def display_status(self):  # Define a method to display the current status of the player
        print("\n--- Status ---")  # Print a section header for easy identification of the status overview
        # Print the name of the current location, defaulting to a message if no location is set
        print(f"Current Location: {self.location.name if self.location else 'Escaped from prison'}")  
        print(f"Name: {self.player.name}")  # Display the player's character name
        print(f"Health: {self.player.health}")  # Display the player's current health points
        print(f"Money: ${self.player.money}")  # Display the amount of money the player has
        print(f"Muscle: {self.player.muscle}")  # Display the player's muscle points, indicating strength level

    def travel(self):  # Define a method that allows the player to travel to different locations
        print("\nWhere would you like to travel? (Type 'exit' to quit)")  # Prompt the player to choose a travel destination

        for idx, loc in enumerate(self.locations):  # Loop through all available locations with their index
            print(f"{idx + 1}: {loc.name}")  # Print the index of each location along with its name

        choice = input("> ")  # Get user input for their choice of location
        if choice.lower() == "exit":  # Check if the user wants to exit the game
            print("Thanks for playing! Goodbye!")  # Print a farewell message
            self.game_over = True  # Set the game_over flag to True to end the game
            return  # Exit the method

        try:
            choice = int(choice) - 1  # Convert the player's input to an integer index (subtracting 1 for zero-based index)
            if 0 <= choice < len(self.locations):  # Check if the chosen index is within valid range
                new_location = self.locations[choice]  # Update the new_location with the player's choice

                if new_location == self.location:  # Check if the chosen location is the same as the current location
                    print("You are already in this location! Choose a different one.")  # Inform the player to choose a different location
                    return  # Exit the method, allowing them to make a new choice

                self.location = new_location  # Update the current location to the new location chosen by the player
                print(f"You travel to {self.location.name}.")  # Notify the player of their new location
                print(self.location.description)  # Display the description of the newly arrived location

                # If the player arrives at the Gym, present gym-specific options
                if self.location.name == "Gym":
                    self.gym_options()  # Call a method to present specific actions available in the gym

                self.encounter()  # Call a method to trigger an encounter after the player travels
            else:  # If the choice index is out of bounds
                print("Invalid choice!")  # Notify the player that their choice is invalid
        except ValueError:  # Handle the case where input cannot be converted to an integer
            print("Please enter a valid number or 'exit' to quit.")  # Ask for valid input again

    def gym_options(self):  # Define a method for gym-specific activities
        while True:  # Loop to allow continuous options in the gym
            print("\nWhat would you like to do?")  # Prompt the user for their choice of action within the gym
            for idx, option in enumerate(self.location.get_options()):  # Loop through available gym options for the player
                print(f"{idx + 1}: {option}")  # Print each option along with its corresponding index

            choice = input("> ")  # Get the player's choice of action in the gym
            if choice == "1":  # If the player chooses to work out
                print("You decide to work out! Your strength increases.")  # Notify the player of their choice
                self.player.muscle += 1  # Increase the player's muscle points by 1
                print(f"Muscle points increased to: {self.player.muscle}")  # Confirm the new muscle point total
            elif choice == "2":  # If the player chooses to leave the gym
                print("You chose to leave the gym.")  # Notify the player
                break  # Exit the loop, returning to the travel options
            else:  # In case of an invalid choice
                print("Invalid choice! Please select a valid option.")  # Prompt the player to choose a valid action

    def interact_with_character(self, character):  # Define a method for player interaction with characters
        if isinstance(character, Prostitute):  # Check if the character is a Prostitute
            print(f"\n{character.name}: {character.offer_services()}")  # Print the prostitute's name and services offered
            action = input("Choose an option (1, 2, or 3) or type 'exit' to quit: ")  # Prompt the player to choose an action

            if action.lower() == "exit":  # If the player decides to exit the game
                print("Thanks for playing! Goodbye!")  # Print a farewell message
                self.game_over = True  # End the game
                return  # Exit the method

            if action == "1":  # If the player chooses to accept the services
                if self.player.money >= 10:  # Check if the player has enough money
                    self.player.money -= 10  # Deduct $10 from the player's money
                    print(f"You have sex with {character.name}. You paid $10.")  # Notify the player of the transaction
                else:  # If the player does not have enough money
                    print("You don't have enough money for this service.")  # Notify the player

            elif action == "2":  # If the player chooses to rob the prostitute
                success = random.random() < 0.8  # Generate a random number; 80% chance of a successful robbery
                if success:  # If the robbery is successful
                    loot = character.money  # Retrieve the prostitute's money
                    self.player.money += loot  # Add the stolen money to the player's total
                    character.money = 0  # Set the prostitute's money to zero after the robbery
                    print(f"You successfully robbed {character.name} and got ${loot}!")  # Notify the player of the successful robbery
                else:  # If the robbery fails
                    print("You failed to rob the prostitute!")  # Notify the player of the failure

            elif action == "3":  # If the player chooses to fight the prostitute
                success = random.random() < 0.9  # 90% chance to successfully deal damage
                if success:  # If the fight is successful
                    damage = random.randint(5, 15)  # Calculate random damage dealt by the player
                    character.take_damage(damage)  # Inflict damage on the prostitute
                    print(f"You fought {character.name} and dealt {damage} damage!")  # Notify the player of the damage
                    if not character.is_alive():  # Check if the prostitute has been defeated
                        loot = character.money  # Loot money from the defeated character
                        self.player.money += loot  # Add the loot to the player's money
                        character.money = 0  # Set the prostitute's money to zero after looting
                        print(f"You defeated {character.name} and looted ${loot}!")  # Notify the player of their success
                else:  # If the fight fails
                    print("You failed to fight the prostitute!")  # Notify the player of the failure

        elif isinstance(character, NPC):  # Check if the character is a generic NPC
            print(f"\n{character.name}: {character.interact()}")  # Display the NPC's dialogue

            # Introduce a small chance for unexpected rewards
            if random.random() < 0.1:  # 10% chance to receive a reward
                reward = random.randint(10, 100)  # Generate a random reward amount between $10 and $100
                self.player.money += reward  # Add the reward to the player's total money
                print(f"{character.name} gave you ${reward}! What a nice surprise!")  # Notify the player of the reward

        elif isinstance(character, Mugger):  # Check if the character is a Mugger
            print(f"You encounter a mugger: {character.name}!")  # Notify the player about the mugger encounter
            while self.player.is_alive() and character.is_alive():  # Loop while both the player and the mugger are alive
                action = input("Do you want to (1) Fight or (2) Flee? (Type 'exit' to quit) ")  # Ask for the player's action
                if action.lower() == "exit":  # If the player wants to exit
                    print("Thanks for playing! Goodbye!")  # Farewell message
                    self.game_over = True  # Set the game over flag
                    return  # Exit the method

                if action == "1":  # If the player chooses to fight
                    damage = random.randint(5, 20)  # Generate a random damage value the player can deal
                    character.take_damage(damage)  # Inflict that damage on the mugger
                    print(f"You dealt {damage} damage to the mugger!")  # Notify the player of the damage dealt
                    if not character.is_alive():  # If the mugger is defeated
                        loot = character.loot()  # Loot the mugger's money
                        self.player.money += loot  # Add loot to the player's total money
                        print(f"You defeated the mugger and looted ${loot}!")  # Notify the player of their victory
                        break  # Exit the loop after defeating the mugger
                    # Mugger attacks back
                    mugger_damage = random.randint(5, 15)  # Generate random damage the mugger can deal
                    self.player.take_damage(mugger_damage)  # Inflict that damage on the player
                    print(f"The mugger dealt {mugger_damage} damage to you!")  # Notify the player of the damage taken
                elif action == "2":  # If the player chooses to flee
                    print("You fled from the mugger!")  # Notify the player of their choice and exit the loop
                    break  # Exit the encounter loop
                else:  # If the player chooses an invalid action
                    print("Invalid action! Choose 1 or 2.")  # Notify the player to select a valid action

            if not self.player.is_alive():  # If the player has been defeated in battle
                self.game_over = True  # Set the game over flag to True
                print("You were defeated by the mugger!")  # Notify the player that they lost

    def encounter(self):  # Define a method to handle random encounters during travel
        print("\nYou encounter something!")  # Inform the player that an encounter is happening
        encounter_type = random.choice(["npc", "mugger", "prostitute"])  # Randomly select an encounter type from options

        if encounter_type == "npc":  # If the encounter is with an NPC
            npc = NPC("Villager", health=50, money=10)  # Create an NPC instance with specific attributes
            self.interact_with_character(npc)  # Initiate interaction with the created NPC

        elif encounter_type == "mugger":  # If the encounter is with a mugger
            mugger = Mugger("Thug")  # Create a Mugger instance
            self.interact_with_character(mugger)  # Initiate interaction with the mugger

        elif encounter_type == "prostitute":  # If the encounter is with a prostitute
            prostitute = Prostitute("Prostitute")  # Create a Prostitute instance
            self.interact_with_character(prostitute)  # Initiate interaction with the prostitute

    def play(self):  # Define the main game loop where gameplay occurs
        print("Welcome to the Text-Based GTA Game!")  # Print a welcome message to the player
        while not self.game_over:  # Continue the loop until the game over state is set to True
            self.display_status()  # Display the current status of the player's character
            self.travel()  # Call the travel method to allow the player to choose a location to travel to

        print("Game Over! You couldn't survive.")  # Print a message indicating that the game has ended

if __name__ == "__main__":  # Check if the script is being executed directly (not imported)
    game = Game()  # Create a new instance of the Game class
    game.play()  # Start the game by calling the play method to enter the main game loop