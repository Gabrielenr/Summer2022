# CSCI 381
# Summer 2022
# Homework Chapter 6 - 6.12
# Gabriel Rubio Alvarado

"""Exercise 6.12
(Guessing Game) Modify your solution for Exercise 5.12 to replace the lists of roles
and actors with a dictionary. This dictionary contains the actors as keys and their roles as
values. Use this dictionary to test if the players can match the right roles to the right actors
the way it was done in Exercise 5.12."""

import random

game_of_thrones = {
    'Sean Bean': 'Ned Stark',
    'Mark Addy': 'Robert Baratheon',
    'Nikolaj Coster-Waldau': 'Jaime Lannister',
    'Michelle Fairley': 'Catelyn Stark',
    'Lena Headey': 'Cersei Lannister'
}


def play_game(attempts=0):
    counter = 0
    r = ([(k, v) for k, v in game_of_thrones.items()])
    random.shuffle(r)
    for key, value in r:
        wrong_answer = True
        print(f"Which actor played {value} in Game of Thrones")
        actor = key
        if input(f"Display list of actors? [yes, no]: ").upper() == "YES":
            print(*game_of_thrones.keys(), sep=', ')
            answer = input(f"Answer: ")
            while wrong_answer:
                if answer == actor:
                    print(f'Correct')
                    counter += 1
                    attempts += 1
                    wrong_answer = False
                else:
                    answer = input(f'Try again: ')
                    attempts += 1
        else:
            answer = input(f"Answer: ")
            while wrong_answer:
                if answer == actor:
                    print(f'Correct')
                    counter += 1
                    attempts += 1
                    wrong_answer = False
                else:
                    answer = input(f'Try again: ')
                    attempts += 1

    return attempts


games_played = play_game()

print(f'The number of correct guesses is 5 out of {games_played}')