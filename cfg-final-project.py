import random
import requests

player_count = 0
computer_count = 0

for win in range(3):
    print("Round ", win+1)
# defining the random and linking the API
    def random_pokemon():
        pokemon_id = random.randint(1, 151)
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
        response = requests.get(url)
        pokemon = response.json()

    # making a dictionary of the stuff we want
        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'weight': pokemon['weight'],
            'height': pokemon['height'],
        }

    chosen_pokemon = random_pokemon()
    opponent_pokemon = random_pokemon()

    #printing the player pokemon
    def run():

        print(f"you have been given {chosen_pokemon['name']} as your pokemon")
        #drowzee hating club
    if chosen_pokemon['id'] == 96:
        print(f"{chosen_pokemon['name']} is trash...yikes")
        print("but we move")
    else:
        print(f"{chosen_pokemon['name']} is pretty cool")

    print(f"{chosen_pokemon['name']} has the ID number of {chosen_pokemon['id']}")
    print(f"{chosen_pokemon['name']} weighs {chosen_pokemon['weight']} lbs")
    print(f"{chosen_pokemon['name']} height is {chosen_pokemon['height']}")

    #asking for stat choice

    stat_choice = input("which stat would you like to use? ")

    #opposing pokemon

    chosen_stat = chosen_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]


    print(f"your opponent has been given {opponent_pokemon['name']}")
    print(f'their {stat_choice} is {opponent_stat}')


    if chosen_stat > opponent_stat:
        player_count = player_count + 1
        print("Congrats! Your pokemon trumped the computer's !! Winner winner chicken dinner!")
    elif chosen_stat < opponent_stat:
        computer_count = computer_count + 1
        print("Loser!")
    else:
        print("It's a draw!")

    print(player_count)
    print(computer_count)


#challenges = loops (while/for),
#successes = extending project, functioning code, github



