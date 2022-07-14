# CSCI 381
# Summer 2022
# Homework Chapter 3 - 3.17
# Gabriel Rubio Alvarado

"""Exercise 3.17
(Nested Loops) Write a script that displays the following triangle patterns separately, one below the other.
Separate each pattern from the next by one blank line. Use for loops to generate the patterns.
Display all asterisks (*) with a single statement of the form print('*', end='')
which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
each line with zero or more space characters.]"""

for a in range(0, 11, +1):
    for b in range(0, a):
        print('*', end='')
    print()

for c in range(10, 0, -1):
    for d in range(1, c+1):
        print('*', end='')
    print()

for e in range(0, 10):
    for f in range(0, e):
        print(' ', end='')
    for f in range(0, 10-e):
        print('*', end='')
    print()

for g in range(0, 10, +1):
    for h in range(9-g):
        print(' ', end='')
    for h in range(0, g+1):
        print('*', end='')
    print()



