# CSCI 381
# Summer 2022
# Homework Chapter 4 - 4.14
# Gabriel Rubio Alvarado

"""Exercise 4.14
(Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the
use of computers in education. Write a script to help an elementary school student learn
multiplication. Create a function that randomly generates and returns a tuple of two positive one-digit integers.
Use that function’s result in your script to prompt the user with a question, such as
How much is 6 times 7?
For a correct answer, display the message "Very good!" and ask another multiplication
question. For an incorrect answer, display the message "No. Please try again." and let
the student try the same question repeatedly until the student finally gets it right. """

import random


def generate_tuple():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    return num1, num2


def play_game(numbers):
    num1, num2 = numbers
    wrong_answer = True

    print(f'How much is {num1} times {num2}')
    user_answer = (input())

    while wrong_answer:
        if user_answer == num1 * num2:
            print("Very good!")
            wrong_answer = False
        else:
            print("No. Please try again")
            print(f'How much is {num1} times {num2}')
            user_answer = int(input())

    new_game()


def new_game():
    num_values = generate_tuple()
    play_game(num_values)


if __name__ == "__main__":
    new_game()
