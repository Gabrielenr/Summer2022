# CSCI 381
# Summer 2022
# Homework Chapter 11 - 11.12
# Gabriel Rubio Alvarado

"""Towers of Hanoi)"""


def TowerOfHanoi(n, source, dest, aux):
    if n == 1:
        print(source, " --> ", dest)
        return
    TowerOfHanoi(n - 1, source, aux, dest)
    print(source, " --> ", dest)
    TowerOfHanoi(n - 1, aux, dest, source)


n = 3
TowerOfHanoi(n, 1, 3, 2)
