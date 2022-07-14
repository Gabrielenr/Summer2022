# CSCI 381
# Summer 2022
# Homework Chapter 3 - 3.14
# Gabriel Rubio Alvarado

""" Exercise 3.14
(Challenge: Approximating the Mathematical Constant ) Write a script that computes the value of π from the
following infinite series. Print a table that shows the value of π approximated by one term of this series,
by two terms, by three terms, and so on.
How many terms of this series do you have to use before you first get 3.14?
3.141? 3.1415? 3.14159? """

series_for_pi = 0
number_of_places = 0
denominator = 1
loop_counter = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
h = 0

print(f'{"Term":30}{"Value of Pi"}')
print('-' * 41)

for i in range(0, 1000000):
    if i % 2 == 0:
        series_for_pi += 4/denominator
    else:
        series_for_pi -= 4/denominator

    f = str(series_for_pi)[0:4]
    f1 = str(series_for_pi)[0:5]
    f2 = str(series_for_pi)[0:6]
    f3 = str(series_for_pi)[0:7]

    if h < 1 and f == '3.14':
        counter_1 = loop_counter
        h += 1
    elif h < 2 and f1 == '3.141':
        counter_2 = loop_counter
        h += 1
    elif h < 3 and f2 == '3.1415':
        counter_3 = loop_counter
        h += 1
    elif h < 4 and f3 == '3.14159':
        counter_4 = loop_counter
        h += 1

    print(f'{loop_counter:>4}{series_for_pi:>37}')
    loop_counter += 1
    denominator += 2

print(f'3.14 was found after the {counter_1}th iteration')
print(f'3.141 was found after the {counter_2}th iteration')
print(f'3.1415 was found after the {counter_3}th iteration')
print(f'3.14159 was found after the {counter_4}th iteration')
