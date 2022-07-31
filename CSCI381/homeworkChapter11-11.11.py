# CSCI 381
# Summer 2022
# Homework Chapter 11 - 11.11
# Gabriel Rubio Alvarado

"""(Eight Queens)"""

N = 8

chess_board = [[0] * N for _ in range(N)]


def Move_Queen(i, j):
    for k in range(0, N):
        if chess_board[i][k] == 1 or chess_board[k][j] == 1:
            return True

    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if chess_board[k][l] == 1:
                    return True
    return False


def QueensBoard(n):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not (Move_Queen(i, j))) and (chess_board[i][j] != 1):
                chess_board[i][j] = 1
                if QueensBoard(n - 1):
                    return True
                chess_board[i][j] = 0
    return False


# call to place the queens on the board
QueensBoard(N)

# display the board after placing all the queens
for i in chess_board:
    print(i)
