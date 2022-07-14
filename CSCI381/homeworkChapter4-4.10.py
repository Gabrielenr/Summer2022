# CSCI 381
# Summer 2022
# Homework Chapter 4 - 4.10
# Gabriel Rubio Alvarado

"""Exercise 4.10
(Play the Multiplication Game) Write a script that lets the user play a multiplication game.
To begin, the game randomly selects two numbers between 1 and 10.
It displays the selected numbers and asks the player for the product of both numbers.
If the player answers correctly, they are asked if they want to play again.
This cycle is continued until the player makes a mistake or stops the game. """

import random


def play_game():
    random_num1 = random.randrange(1, 11)
    random_num2 = random.randrange(1, 11)
    print(f'What is the product of {random_num1} and {random_num2}')
    user_answer = int(input())
    if user_answer == random_num1 * random_num2:
        print(f'{user_answer} is the correct answer')
    else:
        exit(f'{user_answer} is the wrong answer.')


def play_again():
    wrong_response = True
    while wrong_response:
        response = input('Do you want to play again? [yes, no]: ')
        response = response.upper()

        if response == "YES":
            wrong_response = False
            return True
        elif response == "NO":
            wrong_response = False
            return False
        elif response != "YES" or response != "NO":
            print("Wrong input. Enter 'yes' or 'no'")


if __name__ == "__main__":
    play_game()
    while play_again():
        play_game()
    print("Thank you for playing")
