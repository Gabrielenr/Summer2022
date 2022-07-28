# CSCI 381
# Summer 2022
# Homework Chapter 7 - 7.10
# Gabriel Rubio Alvarado

"""Exercise 7.10
(Project: Two-Player, Two-Dimensional Tic-Tac-Toe) Write a script to play two-dimensional
Tic-Tac-Toe between two human players who alternate entering their moves on the same computer.
Use a 3-by-3 two-dimensional array. Each player indicates their moves by entering a pair of numbers
representing the row and column indices of the square in which they want to place their mark,
either an 'X' or an 'O'. When the first player moves, place an 'X' in the specified square.
When the second player moves, place an 'O' in the specified square.
Each move must be to an empty square. After each move, determine whether the game has
been won and whether it’s a draw. """

import random


def swap_player_turn(player):
    return 'X' if player == 'O' else 'O'


def get_random_first_player():
    return random.randint(0, 1)


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None
        n = len(self.board)
        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.chess_board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
            self.show_board()
            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)
            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break
            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break
            # swapping the turn
            player = swap_player_turn(player)
        # showing the final view of board
        print()
        self.show_board()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
