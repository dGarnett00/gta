import random  # Import the random module to use for generating random events
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
                self.location = self.locations[choice]  # Update the location based on the player's choice
                print(f"You travel to {self.location.name}.")  # Inform the player of their new location
                print(self.location.description)  # Print the description of the location
                self.encounter()  # Trigger an encounter after traveling
            else:  # If the choice is invalid
                print("Invalid choice!")  # Inform the player of the invalid choice
        except ValueError:  # Handle non-integer inputs
            print("Please enter a valid number or 'exit' to quit.")  # Notify the player of invalid input

    def interact_with_prostitute(self, prostitute):  # Method for interaction with a prostitute
        print(f"\n{prostitute.name}: {prostitute.offer_services()}")  # Display services offered
        action = input("Choose an option (1, 2, or 3) or type 'exit' to quit: ")  # Get player's action choice

        if action.lower() == "exit":  # Check if the player wants to exit
            print("Thanks for playing! Goodbye!")  # Farewell message
            self.game_over = True  # Set the game over flag to True
            return

        if action == "1":  # If the player chooses to have sex
            if self.player.money >= 10:  # Check if the player has enough money
                self.player.money -= 10  # Deduct money from the player
                print(f"You have sex with {prostitute.name}. You paid $10.")  # Notify the player
            else:
                print("You don't have enough money for this service.")  # Notify if not enough money

        elif action == "2":  # If the player chooses to rob
            success = random.random() < 0.8  # 80% chance of success
            if success:
                loot = prostitute.money  # Loot the prostitute's money
                self.player.money += loot  # Add the loot to the player's total money
                prostitute.money = 0  # Set the prostitute's money to 0
                print(f"You successfully robbed {prostitute.name} and got ${loot}!")  # Notify the player
            else:
                print("You failed to rob the prostitute!")  # Notify if the robbery failed

        elif action == "3":  # If the player chooses to fight
            success = random.random() < 0.9  # 90% chance of success
            if success:
                damage = random.randint(5, 15)  # Random damage the player can deal
                prostitute.take_damage(damage)  # Inflict damage on the prostitute
                print(f"You fought {prostitute.name} and dealt {damage} damage!")  # Notify the player
                if not prostitute.is_alive():  # Check if the prostitute is defeated
                    loot = prostitute.money  # Loot money from the prostitute
                    self.player.money += loot  # Add the loot to the player's total money
                    prostitute.money = 0  # Set the prostitute's money to 0
                    print(f"You defeated {prostitute.name} and looted ${loot}!")  # Notify the player of the loot
            else:
                print("You failed to fight the prostitute!")  # Notify if the fight failed

    def encounter(self):  # Define a method for encounters that happen during travel
        print("\nYou encounter something!")  # Inform the player that an encounter occurs
        encounter_type = random.choice(["npc", "mugger", "prostitute"])  # Randomly choose between an NPC, mugger, or prostitute

        if encounter_type == "npc":  # If the encounter is with an NPC
            npc = NPC("Villager", health=50, money=10)  # Create a new NPC
            self.interact_with_npc(npc)  # Allow the player to interact with the NPC
            self.player.money += npc.money  # Add NPC's money to the player's total money
            print(f"You received ${npc.money} from the NPC.")  # Notify the player of the money received

        elif encounter_type == "mugger":  # If the encounter is with a mugger
            mugger = Mugger("Thug")  # Create a new mugger
            print(f"You encounter a mugger: {mugger.name}!")  # Notify the player about the mugger encounter
            print(f"Health: {mugger.health} | Money: ${mugger.money}")  # Print the mugger's status

            # Simulate a fight with the mugger
            while self.player.is_alive() and mugger.is_alive():
                action = input("Do you want to (1) Fight or (2) Flee? (Type 'exit' to quit) ")  # Ask the player for action
                if action.lower() == "exit":  # Check if the player wants to exit
                    print("Thanks for playing! Goodbye!")  # Farewell message
                    self.game_over = True  # Set the game over flag to True
                    return

                if action == "1":  # If the player chooses to fight
                    damage = random.randint(5, 20)  # Random damage the player can deal
                    mugger.take_damage(damage)  # Inflict damage on the mugger
                    print(f"You dealt {damage} damage to the mugger!")  # Notify the player
                    if not mugger.is_alive():  # Check if the mugger is defeated
                        loot = mugger.loot()  # Loot money from the mugger
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

        elif encounter_type == "prostitute":  # If the encounter is with a prostitute
            prostitute = Prostitute("Lola")  # Create a new prostitute
            self.interact_with_prostitute(prostitute)  # Allow the player to interact with the prostitute

    def play(self):  # Define the main game loop
        print("Welcome to the Text-Based GTA Game!")  # Print a welcome message
        while not self.game_over:  # Continue the loop until the game is over
            self.display_status()  # Display the player's current status
            self.travel()  # Call the travel method to allow the player to travel

        print("Game Over! You couldn't survive.")  # Inform the player that the game is over

if __name__ == "__main__":  # Check if the script is being run directly
    game = Game()  # Create an instance of the Game class
    game.play()  # Start the game by calling the play method