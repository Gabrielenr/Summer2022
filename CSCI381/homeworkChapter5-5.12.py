# CSCI 381
# Summer 2022
# Homework Chapter 5 - 5.12
# Gabriel Rubio Alvarado

""" Exercise 5.12
Write a script that displays one of the main characters of the series and asks the user
which actor played the role. The programmer can choose to either display the actors’
names and let the player chose one or to not display any options at all.
After each question, the player is informed if their answer was correct. The game is
finished when the user has linked five actors to five characters correctly. At the end of the
game, the number of correct guesses is displayed on the screen."""

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
                    print(f'Counter:{counter}')
                    print(f'Attempts:{attempts}')
                    wrong_answer = False
                else:
                    answer = input(f'Try again: ')
                    attempts += 1
                    print(f'Attempts:{attempts}')
        else:
            answer = input(f"Answer: ")
            while wrong_answer:
                if answer == actor:
                    print(f'Correct')
                    counter += 1
                    attempts += 1
                    print(f'Counter:{counter}')
                    print(f'Attempts:{attempts}')
                    wrong_answer = False
                else:
                    answer = input(f'Try again: ')
                    attempts += 1
                    print(f'Attempts:{attempts}')

    return attempts


games_played = play_game()

print(f'The number of correct guesses is 5 out of {games_played}')
