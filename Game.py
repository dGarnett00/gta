# game.py file
import random  # Import the random module for generating random numbers used in game events
from characters import Player  # Import the Player class for player interactions
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

                # Invoke options specific to the location the player arrived at
                if self.location.name == "Store":
                    self.store_options()  # Call the store options function for actions available in the store
                elif self.location.name == "Gym":
                    self.gym_options()  # Call the gym options for actions available in the gym
            else:  # If the chosen index is out of bounds
                print("Invalid choice!")  # Notify the player of the invalid choice
        except ValueError:  # Handle the case where the input cannot be converted to an integer
            print("Please enter a valid number or 'exit' to quit.")  # Ask for a valid input again

    def gym_options(self):  # Define a method for actions available in the gym
        while True:  # Loop to allow continuous options in the gym
            print("\n--- Gym Menu ---")
            print("1: Work Out (Gain 10 Muscle) - Free")  # Option to work out and gain muscle
            print("2: Leave Gym")  # Option to leave the gym

            choice = input("> ")  # Get the player's choice of action in the gym
            
            if choice == "1":  # If the player chooses to work out
                self.player.gain_muscle(10)  # Increase muscle points by 10
                print(f"{self.player.name} worked out and gained 10 muscle points!")  # Notify player of their action
            elif choice == "2":  # If the player chooses to leave the gym
                print("You left the gym.")  # Notify the player
                self.travel()  # Display travel options again
                break  # Exit the gym loop
            else:  # If the player's choice is invalid
                print("Invalid choice! Please select a valid option.")  # Ask for valid input

            # Display the player's status after each action
            self.display_status()  # Show updated status after an action

    def store_options(self):  # Define a method for actions available in the store
        while True:  # Loop to allow continuous options in the store
            print("\n--- Store Menu ---")
            print("1: Buy Health (Cost: $10, Gain: 10 Health)")  # Option to buy health
            print("2: Buy Steroids (Cost: $30, Gain: 20 Muscle)")  # Option to buy steroids
            print("3: Leave Store")  # Option to leave the store

            choice = input("> ")  # Get the player's choice of action in the store
            
            if choice == "1":  # If the player chooses to buy health
                if self.player.money >= 10:  # Check if the player has enough money
                    self.player.money -= 10  # Deduct cost from player's money
                    self.player.health += 10  # Increase player's health by 10
                    print("You bought health! Your health has increased by 10!")
                else:
                    print("Not enough money to buy health!")  # Notify player they don't have enough money

            elif choice == "2":  # If the player chooses to buy steroids
                if self.player.money >= 30:  # Check if the player has enough money
                    self.player.money -= 30  # Deduct cost from player's money
                    self.player.gain_muscle(20)  # Increase muscle points by 20
                    print("You bought steroids! Your muscle has increased by 20!")
                else:
                    print("Not enough money to buy steroids!")  # Notify player they don't have enough money

            elif choice == "3":  # If the player chooses to leave the store
                print("You left the store.")  # Notify the player
                self.travel()  # Display travel options again
                break  # Exit the store loop
            
            else:  # If the player's choice is invalid
                print("Invalid choice! Please select a valid option.")  # Ask for valid input

            # Display the player's status after each transaction
            self.display_status()  # Show updated status after a transaction

    def play(self):  # Define the main game loop where gameplay occurs
        print("Welcome to the Text-Based GTA Game!")  # Print a welcome message for the player
        while not self.game_over:  # Continue the loop until the game is over
            self.display_status()  # Display the current status of the player's character
            self.travel()  # Call the travel method to allow the player to choose a location to travel to

        print("Game Over! You couldn't survive.")  # Print a message indicating that the game has ended

if __name__ == "__main__":  # Check if the script is run directly (not imported as a module)
    game = Game()  # Create a new instance of the Game class
    game.play()  # Start the game by calling the play method that enters the main gameplay loop