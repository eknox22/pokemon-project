import requests
import random


# Class to represent the player and store persistent stats
class Player:
    def __init__(self):
        # Introducing a new player object with initial stats
        self.wins = 0
        self.losses = 0

        # These attributes store the player's performance across multiple rounds in the game.
        # The wins and losses are initially set to 0, and they will be updated as the player progresses in the game.
        # Each player object created from this class will have its own wins and losses attributes.
        # The __init__ method is a special method that is automatically called when a new player object is created.


# Function to get information about a random Pokemon from the PokeAPI
def random_pokemon():
    player_pokemon_number = random.randint(1, 151)
    opponent_pokemon_number = player_pokemon_number

    # Keep generating a new opponent's Pokemon until it's different from the player's Pokemon
    while opponent_pokemon_number == player_pokemon_number:
        opponent_pokemon_number = random.randint(1, 151)

    player_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon_number)
    player_response = requests.get(player_url)
    player_pokemon = player_response.json()

    opponent_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_pokemon_number)
    opponent_response = requests.get(opponent_url)
    opponent_pokemon = opponent_response.json()

    # Return dictionaries containing the player's and opponent's Pokemon data
    return {
        'player': {
            'name': player_pokemon['name'],
            'id': player_pokemon['id'],
            'height': player_pokemon['height'],
            'weight': player_pokemon['weight'],
        },
        'opponent': {
            'name': opponent_pokemon['name'],
            'id': opponent_pokemon['id'],
            'height': opponent_pokemon['height'],
            'weight': opponent_pokemon['weight'],
        }
    }


# Function to display Pokemon information
def display_pokemon(pokemon, show_stats=True):
    print("Name: {}".format(pokemon['name']))
    print("ID: {}".format(pokemon['id']))

    # Display height and weight if show_stats is True
    if show_stats:
        print("Height: {} decimetres".format(pokemon['height']))
        print("Weight: {} hectograms".format(pokemon['weight']))

    print("\n")


# Main game function
def run():
    # Print a welcome message to the player
    print("Welcome to Pokemon Top Trumps!")

    # Create an instance of the Player class to track persistent stats
    player = Player()

    # Continuous loop for the game
    while True:
        # Display available game modes
        print("\nGame Modes:")
        print("1. Normal Mode")
        print("2. Difficult Mode")
        print("3. Exit")

        # Allow the player to choose a game mode
        mode_choice = input("Choose a game mode (1/2/3): ")

        # Check if the player wants to exit the game
        if mode_choice == '3':
            print("Thanks for playing! Goodbye.")
            break

        # Introducing the round counter
        rounds = 0
        # Loop for each round (best of 3 rounds)
        while rounds < 3:
            # Display the current round number
            print("\nRound {}".format(rounds + 1))

            # Generate Pokemon for the player and opponent
            pokemon_data = random_pokemon()

            player_pokemon = pokemon_data['player']
            opponent_pokemon = pokemon_data['opponent']

            # In easy mode, show Pokemon data.  In difficult mode this won't be seen.
            if mode_choice == '1':
                print("Your Pokemon:")
                display_pokemon(player_pokemon)

            # Ask the user which stat they want to use (id, height, or weight)
            valid_stats = ['id', 'height', 'weight']
            stat_to_compare = input("Which stat do you want to compare? (id/height/weight): ").lower()

            if stat_to_compare in valid_stats:
                player_stat = player_pokemon[stat_to_compare]
                opponent_stat = opponent_pokemon[stat_to_compare]

                print("Your Pokemon's {}: {}".format(stat_to_compare, player_stat))

                # Display opponent's Pokemon after player's input
                input("Press Enter to reveal the opponent's Pokemon.")
                display_pokemon(opponent_pokemon)

                # Compare the stats and determine the winner
                if player_stat > opponent_stat:
                    print("You win this round!")
                    player.wins += 1
                elif player_stat < opponent_stat:
                    print("Opponent wins this round!")
                    player.losses += 1
                else:
                    print("It's a tie!")

                rounds += 1

            else:
                print("Invalid stat. Please choose 'id', 'height', or 'weight.'")

        print("\nGame Over!")
        print("Wins: {}".format(player.wins))
        print("Losses: {}".format(player.losses))


# Run the game if the script is executed
if __name__ == "__main__":
    run()