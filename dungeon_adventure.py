import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TODO: Return the dictionary

        user_name = input('Please enter your name to get started!\n')

        player_info = {
            'name' : user_name,
            'health' : 10,
            'inventory' : [],
            'lunch box' : []
        }

        return player_info

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary

        treasures = {
            'gold coin' : 5,
            'ruby' : 10,
            'ancient scroll' : 7,
            'emerald' : 9,
            'silver ring' : 4
        }

        return treasures
    
    def create_traps():
        """
        Creates a dictionary of traps, where each trap has a value.
        
        Returns trap dictionary
            dict: example:
                {
                    'bear claw': 5
                    'small bomb': 8
                    'big bomb': 10
                    'oil spot': 2
                    'stubbed toe': 1
                }
        """
        #TODO: Create a dictionary of trap names and integer values
        #TODO: Return the dictionary

        traps = {
            'bear claw' : 5,
            'small bomb' : 8,
            'big bomb' : 10,
            'oil spot' : 2,
            'stubbed toe' : 1
        }

        return traps
    
    def create_heals():
        """
        Creates a dictionary of healing items, where each item has a value.

        Returns healing dictionary
            dict: example:
                {
                    'apple': 2
                    'candy': 3
                    'chocolate': 4
                    'steak': 10
                }        
        """

        #TODO: Create a dictionary of healing items and integer values
        #TODO: Return the dictionary

        heals = {
            'apple' : 2,
            'candy' : 3,
            'chocolate' : 4,
            'steak' : 10
        }

        return heals


    def display_options():
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above

        # print("\nYou are currently in the hallway, what would you like to do?")

        options = {
            '0.' : "Display instructions",
            '1.' : "Search for treasure",
            '2.' : "Move to the next room",
            '3.' : "Check health and inventory",
            '4.' : "Quit the game"
        }

        for key, values in options.items():
            print(f'\n{key} {values}')
        

    def search_room(player, treasures, traps, heals):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened

        outcome = random.choice(["treasure", "trap", "heals"])

        if outcome == "treasure":
            found_treasure = random.choice(list(treasures.keys()))
            player["inventory"].append(found_treasure)

            print(f"\nYou found a {found_treasure}! It has a value of {treasures[found_treasure]}.")

        elif outcome == "heals":
            found_food = random.choice(list(heals.keys()))
            restore = heals[found_food]

            if player['health'] == 10:
                    player['lunch box'].append(found_food)
                    print(f"\nYou found a {found_food} but I don't need any food, my health is full. I'll put this in my lunch box for later!")

            else:
                old_health = player['health']
                player['health'] = min(player['health'] + restore, 10)
                actual_restore = player['health'] - old_health

                print(f'\nOh Yeah! You found a {found_food} and restored your health by {actual_restore} points!')
                print(f"\nYour health is now {player['health']}.")

        
        else:
            sprung_trap = random.choice(list(traps.keys()))
            damage = traps[sprung_trap]
            player['health'] -= damage
            player['health'] = max(player['health'], 0)

            print(f'\nOh no! You triggered a {sprung_trap} and lost {damage} health points!')

            if player['health'] > 0:
                print(f"\nYour health is now {player['health']}.")

            else:
                print('You have succumbed to your injuries...')




    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”

        print(f"\nHealth: {player['health']}")

        if player['inventory']:
            items = ", ".join(player["inventory"])
            print(f"Inventory: {items}")

        else:
            print("Your inventory is empty.")
        
        if player['lunch box']:
            snacks = ", ".join(player['lunch box'])
            print(f'Snacks: {snacks}')

        else:
            print("Your lunchbox is empty.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."
        total_value = 0

        for item in player['inventory']:
            if item in player['inventory']:
                total_value += treasures[item]

        print("\n--- Game Summary ---\n")
        
        print(f"Final health: {player['health']}")
              
        if player['inventory']:
            items = ", ".join(player['inventory'])
            print(f'Final inventory: {items}')

        else:
            print("Final inventory: You have no items.")
        
        if player['lunch box']:
            goodies = ", ".join(player['lunch box'])
            print(f'Lunch box contents: {goodies}')

        else:
            print("Final lunch box contents: You have no snacks.")

        print(f"Total treasure value: {total_value}")

        if player['health'] == 0:
            print('\nWASTED! Try Agian...')

        else:
            print('\nGame Over! Thanks for playing!')
            
    def player_instructions():
        """
        This function will be used to print a message on how the game works.

        Flow:
            - Allow the player to choose an option to display the instruction message.
        """
        # TODO: print a message to display how the game works

        print('--- How to Play ---\n')

        print(
            "- To play the game, you must select an option of 1-4.\n\n- When you enter a room, you might find treasure, a heals, or you might run into a trap.\n\n- The treasure will be added to your inventory, a heals will add a certain amount back to your health, and a trap will reduce your health by a certain amount of points.\n\n- If you run out of health before exploring all the rooms, you wil die!\n\n- You can search a room as many times as you like to find more treasure. But, BE CAUTIOUS, there might be more than one trap in that room!\n\n- Once you are done in that room, select the option to move on to the next.\n\n- To quit the game, and leave with your entire inventory, select the appropriate option."
        )

    def run_game_loop(player, treasures, traps, heals):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored

        print(f"\nWelcome, {player['name']}! Your adventure begins here...\n")

        player_instructions()


        for room in range(1, 6):
            print(f'\n--- Room {room} ---')

            while True:
                display_options()
                player_choice = input("\nEnter your choice (1-4): ").strip()

                if player_choice == '0':
                    player_instructions()

                elif player_choice == '1':
                    search_room(player, treasures, traps, heals)

                    if player['health'] <= 1:
                        end_game(player, treasures)
                        return

                elif player_choice == '2':
                    print('\nYou move cautiously into the next room...')
                    break
                
                elif player_choice == '3':
                    check_status(player)
                
                elif player_choice == '4':
                    print('\nYou have decided to leave the dungeon')
                    end_game(player, treasures)
                    return
                else:
                    print('Invalid choice: Please select 1-4.')

        print('\nYou have explored all the rooms in the dungeon!')
        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    traps = create_traps()
    heals = create_heals()

    run_game_loop(player, treasures, traps, heals)

if __name__ == "__main__":
    main()
