import random  # Import the random module for generating random numbers used in game events
from characters import Player, Mugger, Enemy  # Import Player, Mugger, and Enemy classes for their interactions
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
        print(f"Current Location: {self.location.name if self.location else 'Escaped from prison'}")  # Display current location
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

                # Invoke specific options for each location
                if self.location.name == "Store":
                    self.store_options()  # Store-specific actions
                elif self.location.name == "Gym":
                    self.gym_options()  # Gym-specific actions
                elif self.location.name == "Home":
                    self.home_options()  # Home-specific actions
            else:  # If the chosen index is out of bounds
                print("Invalid choice!")  # Notify the player of the invalid choice
        except ValueError:  # Handle the case where the input cannot be converted to an integer
            print("Please enter a valid number or 'exit' to quit.")  # Ask for a valid input again

    def home_options(self):  # Define a method for options available at home
        while True:  # Loop for continuous options at home
            print("\n--- Home Menu ---")
            print("1: Sleep (Gain 5 Health)")  # Option to sleep and regain health
            print("2: Missions")  # Option to view missions
            print("3: Robberies")  # Option to initiate a robbery
            print("4: Leave Home")  # Option to leave home

            choice = input("> ")  # Get player's choice at home
            
            if choice == "1":  # If the player chooses to sleep
                self.player.health += 5  # Increase player's health by 5
                print("You slept well and gained 5 health!")  # Notify the player
            elif choice == "2":  # If the player chooses to view missions
                self.missions_options()  # Call the missions options
            elif choice == "3":  # If the player chooses to initiate a robbery
                self.robbery_options()  # Call the robbery options
            elif choice == "4":  # If the player chooses to leave home
                print("You left home.")  # Notify the player
                self.travel()  # Display travel options again
                break  # Exit the home loop
            else:  # If the player's choice is invalid
                print("Invalid choice! Please select a valid option.")  # Ask for valid input

            # Display the player's status after each action
            self.display_status()  # Show updated status after an action

    def missions_options(self):  # Define available missions
        completed_missions = 0  # Track completed missions

        while True:  # Loop for continuous missions
            print("\n--- Missions Menu ---")
            # Display available missions based on completion
            if completed_missions == 0:
                print("1: Mission 1")
            if completed_missions == 1:
                print("1: Mission 1")
                print("2: Mission 2")
            if completed_missions == 2:
                print("1: Mission 1")
                print("2: Mission 2")
                print("3: Mission 3")
            if completed_missions == 3:
                print("1: Mission 1")
                print("2: Mission 2")
                print("3: Mission 3")
                print("4: Mission 4")
            if completed_missions == 4:
                print("1: Mission 1")
                print("2: Mission 2")
                print("3: Mission 3")
                print("4: Mission 4")
                print("5: Mission 5")
            if completed_missions == 5:
                print("1: Mission 1")
                print("2: Mission 2")
                print("3: Mission 3")
                print("4: Mission 4")
                print("5: Mission 5")
                print("6: Leave Missions")

            choice = input("> ")  # Get player's choice of mission
            
            if choice.isdigit() and int(choice) <= (completed_missions + 1):  # Check for valid mission selection
                if choice == "1":
                    self.mission_1()  # Call the first mission
                    completed_missions += 1  # Increment completed missions
                elif choice == "2" and completed_missions >= 1:
                    self.mission_2()  # Call the second mission
                    completed_missions += 1  # Increment completed missions
                elif choice == "3" and completed_missions >= 2:
                    self.mission_3()  # Call the third mission
                    completed_missions += 1  # Increment completed missions
                elif choice == "4" and completed_missions >= 3:
                    self.mission_4()  # Call the fourth mission
                    completed_missions += 1  # Increment completed missions
                elif choice == "5" and completed_missions >= 4:
                    self.mission_5()  # Call the fifth mission
                    completed_missions += 1  # Increment completed missions
                elif choice == "6" and completed_missions >= 5:
                    print("You left the missions.")  # Notify the player
                    break  # Exit the mission loop
                else:
                    print("You need to complete the previous missions first!")  # Notify player about mission completion prerequisites
            else:
                print("Invalid choice! Please select a valid option.")  # Ask for valid input

    def robbery_options(self):  # Define the robbery options
        while True:  # Loop to allow continuous robbery attempts
            print("\n--- Robbery Options ---")
            print("1: Attempt Robbery")  # Option to attempt a robbery
            print("2: Leave Robbery Menu")  # Option to leave the robbery menu

            choice = input("> ")  # Get the player's choice
            if choice == "1":  # If the player chooses to attempt a robbery
                self.attempt_robbery()  # Call the robbery attempt method
            elif choice == "2":  # If the player chooses to leave the robbery menu
                print("You left the robbery menu.")  # Notify the player
                break  # Exit the robbery options loop
            else:  # If the choice is invalid
                print("Invalid choice! Please select a valid option.")  # Ask for valid input

    def attempt_robbery(self):  # Define the robbery attempt logic
        outcomes = ["bank", "house", "store", "hotel", "gas station", "laundromat", "apartment", "friend", "family member"]
        target = random.choice(outcomes)  # Randomly select a target for the robbery
        print(f"You attempt to rob a {target}.")  # Notify the player of their target

        success = random.choice([True, False])  # Randomly determine if the robbery is successful

        if success:  # If the robbery is successful
            loot = random.randint(50, 150)  # Randomly generate loot
            self.player.earn_money(loot)  # Add loot to the player's money
            print(f"You successfully robbed the {target} and gained ${loot}.")  # Notify player of successful robbery
        else:  # If the robbery fails
            health_loss = random.randint(10, 50)  # Randomly determine health loss
            self.player.take_damage(health_loss)  # Apply damage to the player
            print(f"The robbery failed! You lost {health_loss} health.")  # Notify player of failure

        self.display_status()  # Show updated player status after the robbery attempt

    def fight_mutex(self, mugger):  # Define the fight with a mugger
        print(f"\n--- Fight with {mugger.name} ---")  # Introduce the fight
        while mugger.is_alive() and self.player.is_alive():  # While both the mugger and player are alive
            # Player's attack
            action = input("Do you want to (a)ttack or (l)eave? ")  # Get player action
            if action.lower() == "a":  # Player chooses to attack
                damage = random.randint(5, 15)  # Determine damage dealt by the player
                mugger.take_damage(damage)  # Apply damage to the mugger
                print(f"You dealt {damage} damage to {mugger.name}.")  # Report damage dealt
                if mugger.is_alive():  # Check if the mugger is still alive
                    mugger_damage = random.randint(5, 15)  # Determine damage dealt by the mugger
                    self.player.take_damage(mugger_damage)  # Apply damage to the player
                    print(f"{mugger.name} dealt {mugger_damage} damage to you.")  # Report damage received
            elif action.lower() == "l":  # Player chooses to leave
                print("You fled the fight.")  # Notify the player
                break
            else:
                print("Invalid action! Please choose 'a' to attack or 'l' to leave.")  # Invalid action
            
            self.display_status()  # Display updated status after each action

        if not mugger.is_alive():  # Check if the mugger has been defeated
            loot = mugger.loot()  # Loot the defeated mugger
            print(f"You defeated {mugger.name} and looted ${loot}.")  # Notify the player of victory and loot
            self.player.earn_money(20 + (20 * 4))  # Reward for defeating the mugger
        else:
            print("You ran out of health and lost the fight!")  # Notify player if they lost

    def fight_muggers(self):  # Define the sequence of fights against muggers
        for i in range(4):  # Loop for 4 muggers
            mugger = Mugger(f"Mugger {i + 1}")  # Create a new mugger
            self.fight_mutex(mugger)  # Initiate the fight sequence

    def fight_enemies(self):  # Define the sequence of fights against enemies
        enemies = [Enemy() for _ in range(4)]  # List of enemies
        for enemy in enemies:  # Loop through each enemy
            self.fight_mutex(enemy)  # Initiate the fight against the enemy

    def play(self):  # Define the main game loop where gameplay occurs
        print("Welcome to the Text-Based GTA Game!")  # Print a welcome message for the player
        while not self.game_over:  # Continue the loop until the game is over
            self.display_status()  # Display the current status of the player's character
            self.travel()  # Call the travel method to allow the player to choose a location to travel to

        print("Game Over! You couldn't survive.")  # Print a message indicating that the game has ended

if __name__ == "__main__":  # Check if the script is run directly (not imported as a module)
    game = Game()  # Create a new instance of the Game class
    game.play()  # Start the game by calling the play method that enters the main gameplay loop