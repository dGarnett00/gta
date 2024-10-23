''' # Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    player = Player("Hero")  # Create a new player character named "Hero"
    npc = NPC("Villager", health=50, money=10)  # Create a new NPC character named "Villager"
    mugger = Mugger("Thug")  # Create a new random mugger

    print(player)  # Print the player's status
    print(npc)  # Print the NPC's status
    print(npc.interact())  # Display the NPC's interaction
    player.converse(npc)  # Allow the player to converse with the NPC

    # Simulate an encounter with a mugger
    print(f"\nYou encounter a mugger: {mugger.name}!")  # Notify the player about the mugger encounter
    print(f"Health: {mugger.health} | Money: ${mugger.money}")  # Print the mugger's status

    # Example of a fight (this can be expanded into a method in the Game class)
    while player.is_alive() and mugger.is_alive():
        action = input("Do you want to (1) Fight or (2) Flee? ")  # Ask the player for action
        if action == "1":  # If the player chooses to fight
            damage = random.randint(5, 20)  # Random damage the player can deal
            mugger.take_damage(damage)  # Inflict damage on the mugger
            print(f"You dealt {damage} damage to the mugger!")  # Notify the player
            if not mugger.is_alive():  # Check if the mugger is defeated
                loot = mugger.loot()  # Loot money from the mugger
                print(f"You defeated the mugger and looted ${loot}!")  # Notify the player of the loot
                break  # Exit the loop if the mugger is defeated
            # Mugger attacks back
            mugger_damage = random.randint(5, 15)  # Random damage the mugger can deal
            player.take_damage(mugger_damage)  # Inflict damage on the player
            print(f"The mugger dealt {mugger_damage} damage to you!")  # Notify the player
        elif action == "2":  # If the player chooses to flee
            print("You fled from the mugger!")  # Notify the player
            break  # Exit the loop if the player flees
        else:
            print("Invalid action! Choose 1 or 2.")  # Notify the player of an invalid action

    if not player.is_alive():  # Check if the player is defeated
        print("You were defeated by the mugger!")  # Notify the player of their defeat   '''



'''
# Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    player = Player("Hero")  # Create a new player character named "Hero"
    npc = NPC("Villager", health=50, money=10)  # Create a new NPC character named "Villager"

    print(player)  # Print the player's status
    print(npc)  # Print the NPC's status
    print(npc.interact())  # Display the NPC's interaction
    '''